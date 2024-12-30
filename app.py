import requests
import json
import pandas as pd
from tabulate import tabulate
import time
from concurrent.futures import ThreadPoolExecutor

# Define section patterns with batch years and entry types
SECTION_PATTERNS = {
    'CS-A': {
        'regular': ['23EG109A', '22EG109A'],  # Current and detained
        'lateral': ['24EG509A']  # Lateral entry
    },
    'CS-B': {
        'regular': ['23EG109B', '22EG109B'],
        'lateral': ['24EG509B']
    },
    'IT-A': {
        'regular': ['23EG112A', '22EG112A'],
        'lateral': ['24EG512A']
    },
    'IT-B': {
        'regular': ['23EG112B', '22EG112B'],
        'lateral': ['24EG512B']
    },
    'IT-C': {
        'regular': ['23EG112C', '22EG112C'],
        'lateral': ['24EG512C']
    },
    'IT-D': {
        'regular': ['23EG112D', '22EG112D'],
        'lateral': ['24EG512D']
    },
    'IT-E': {
        'regular': ['23EG112E', '22EG112E'],
        'lateral': ['24EG512E']
    },
    'IT-F': {
        'regular': ['23EG112F', '22EG112F'],
        'lateral': ['24EG512F']
    }
}

def test_roll_number(roll_no):
    """Test if a roll number exists by making a request"""
    url = "https://api.campx.in/exams/student-results/external"
    
    params = {
        "examType": "general",
        "rollNo": roll_no
    }
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.9",
        "Origin": "https://aupulse.campx.in",
        "Referer": "https://aupulse.campx.in/",
        "sec-ch-ua": '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "x-api-version": "2",
        "x-institution-code": "aupulse",
        "x-tenant-id": "aupulse"
    }

    try:
        session = requests.Session()
        cookies = {
            "_clck": "1qn1ema|2|fm8|0|1492"
        }
        session.cookies.update(cookies)
        
        response = session.get(url, params=params, headers=headers)
        
        if response.status_code == 200:
            return roll_no
        return None

    except Exception:
        return None

def generate_roll_numbers(patterns, include_detained=False, include_lateral=False):
    """Generate and test all possible roll numbers"""
    possible_rolls = []
    
    # Order: rejoin (detained) -> regular -> lateral
    if include_detained:
        possible_rolls.extend([f"{patterns['regular'][1]}{num:02d}" for num in range(1, 101)])  # Detained/Rejoin
    
    possible_rolls.extend([f"{patterns['regular'][0]}{num:02d}" for num in range(1, 101)])  # Regular
    
    if include_lateral:
        possible_rolls.extend([f"{patterns['lateral'][0]}{num:02d}" for num in range(1, 101)])  # Lateral
    
    print(f"Testing {len(possible_rolls)} possible roll numbers...")
    
    # Use ThreadPoolExecutor to test roll numbers concurrently
    with ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(test_roll_number, possible_rolls))
    
    # Filter out None values while maintaining order
    valid_rolls = [roll for roll in results if roll is not None]
    
    # Sort rolls to maintain rejoin -> regular -> lateral order
    def get_roll_type_order(roll):
        if '22EG' in roll:  # Rejoin/Detained
            return 0
        elif '24EG5' in roll:  # Lateral
            return 2
        return 1  # Regular
    
    valid_rolls.sort(key=get_roll_type_order)
    
    return valid_rolls

def get_student_results(roll_no, selected_sems):
    """Fetch results for a single student"""
    url = "https://api.campx.in/exams/student-results/external"
    
    params = {
        "examType": "general",
        "rollNo": roll_no
    }
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.9",
        "Origin": "https://aupulse.campx.in",
        "Referer": "https://aupulse.campx.in/",
        "sec-ch-ua": '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "x-api-version": "2",
        "x-institution-code": "aupulse",
        "x-tenant-id": "aupulse"
    }

    try:
        session = requests.Session()
        cookies = {
            "_clck": "1qn1ema|2|fm8|0|1492"
        }
        session.cookies.update(cookies)
        
        response = session.get(url, params=params, headers=headers)
        
        if response.status_code == 422:
            print(f"Error fetching results for {roll_no}: {response.text}")
            return None
            
        response.raise_for_status()
        data = response.json()
        
        student_results = []
        student_info = data["student"]
        student_name = student_info["fullName"]
        
        # Update entry type determination to include rejoin
        if "22EG" in roll_no:
            entry_type = "Rejoin"
        elif "509" in roll_no or "512" in roll_no:
            entry_type = "Lateral"
        else:
            entry_type = "Regular"
        
        # Add batch year from roll number
        batch_year = "20" + roll_no[:2]
        
        for semester in data["results"]:
            if semester["semNo"] not in selected_sems:
                continue
                
            for subject in semester["subjectsResults"]:
                subject_info = subject["subject"]
                grade_info = subject["consideredGrade"]
                
                result = {
                    "Roll No": roll_no,
                    "Name": student_name,
                    "Batch": batch_year,
                    "Entry Type": entry_type,
                    "Semester": semester["semNo"],
                    "Subject Code": subject_info["subjectCode"],
                    "Subject Name": subject_info["name"],
                    "Credits": subject_info["credits"],
                    "Grade": grade_info["grade"],
                    "Grade Points": grade_info["gradePoints"],
                    "Status": "Pass" if grade_info["passed"] else "Fail"
                }
                student_results.append(result)
        
        return student_results

    except Exception as e:
        print(f"Error processing {roll_no}: {str(e)}")
        return None

def main():
    print("Available Sections:")
    for section in SECTION_PATTERNS.keys():
        print(f"Section {section}")
    
    section = input("\nEnter section (e.g., CS-A, IT-B): ")
    if section not in SECTION_PATTERNS:
        print("Invalid section!")
        return
    
    include_detained = input("Include detained students? (y/n): ").lower() == 'y'
    include_lateral = input("Include lateral entry students? (y/n): ").lower() == 'y'
    
    print("\nEnter semester numbers to fetch (comma-separated)")
    print("Example: 1,2,3")
    sems_input = input("Semesters: ")
    selected_sems = [int(sem.strip()) for sem in sems_input.split(",")]
    
    # Generate and test all possible roll numbers
    roll_numbers = generate_roll_numbers(
        SECTION_PATTERNS[section],
        include_detained,
        include_lateral
    )
    
    if not roll_numbers:
        print("No valid roll numbers found!")
        return
    
    print(f"\nFound {len(roll_numbers)} valid roll numbers")
    print("Roll numbers found:", roll_numbers)
    
    proceed = input("\nProceed with fetching results? (y/n): ").lower() == 'y'
    if not proceed:
        return
    
    all_results = []
    total_rolls = len(roll_numbers)
    
    print(f"\nFetching results for {total_rolls} students...")
    for i, roll_no in enumerate(roll_numbers, 1):
        print(f"Processing {roll_no} ({i}/{total_rolls})...")
        results = get_student_results(roll_no, selected_sems)
        if results:
            all_results.extend(results)
        time.sleep(1)  # Add delay to avoid overwhelming the server
    
    if all_results:
        # Convert to DataFrame
        df = pd.DataFrame(all_results)
        
        # Sort DataFrame by Entry Type in desired order
        entry_type_order = {'Rejoin': 0, 'Regular': 1, 'Lateral': 2}
        df['EntryTypeOrder'] = df['Entry Type'].map(entry_type_order)
        df = df.sort_values(['EntryTypeOrder', 'Roll No'])
        df = df.drop('EntryTypeOrder', axis=1)
        
        # Create filename
        types = []
        if include_detained:
            types.append("rejoin")
        if include_lateral:
            types.append("lateral")
        type_str = "_with_" + "_".join(types) if types else ""
        
        filename = f"section_{section}{type_str}_sem_{'-'.join(map(str, selected_sems))}_results.csv"
        df.to_csv(filename, index=False)
        print(f"\nResults exported to {filename}")
        
        # Display summary
        print("\nSummary:")
        print(f"Total students processed: {total_rolls}")
        print(f"Total records exported: {len(all_results)}")
        
        # Display batch-wise and entry-type summary
        batch_summary = df.groupby(['Batch', 'Entry Type'])['Roll No'].nunique().sort_index()
        print("\nBatch-wise Summary:")
        print(batch_summary)
        
        # Display entry-type summary
        entry_summary = df.groupby('Entry Type')['Roll No'].nunique()
        print("\nEntry Type Summary:")
        for entry_type in ['Rejoin', 'Regular', 'Lateral']:
            if entry_type in entry_summary:
                print(f"{entry_type}: {entry_summary[entry_type]} students")
    else:
        print("No results were fetched!")

if __name__ == "__main__":
    main()
