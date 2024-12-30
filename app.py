import requests
import json
import pandas as pd
from tabulate import tabulate
import time
from concurrent.futures import ThreadPoolExecutor
import os

# Create data directory if it doesn't exist
os.makedirs('data', exist_ok=True)

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
            return {'roll': roll_no, 'status': 200}
        return {'roll': roll_no, 'status': response.status_code}

    except Exception:
        return {'roll': roll_no, 'status': 'error'}

def generate_roll_numbers(patterns, include_detained=False, include_lateral=False):
    """Generate and test all possible roll numbers"""
    valid_rolls = []
    
    # Test rejoin/detained rolls (test all)
    if include_detained:
        detained_rolls = [f"{patterns['regular'][1]}{num:02d}" for num in range(1, 101)]
        print(f"Testing {len(detained_rolls)} detained roll numbers...")
        with ThreadPoolExecutor(max_workers=5) as executor:
            results = list(executor.map(test_roll_number, detained_rolls))
            valid_rolls.extend(result['roll'] for result in results if result['status'] == 200)
    
    # Test regular rolls (stop at first 404)
    regular_rolls = [f"{patterns['regular'][0]}{num:02d}" for num in range(1, 101)]
    print(f"Testing regular roll numbers...")
    for roll in regular_rolls:
        result = test_roll_number(roll)
        if result['status'] == 200:
            valid_rolls.append(result['roll'])
        elif result['status'] == 404:
            print(f"Stopped at {roll} after encountering a 404 error")
            break
        time.sleep(0.2)  # Small delay between requests
    
    # Test lateral entry rolls (test all)
    if include_lateral:
        lateral_rolls = [f"{patterns['lateral'][0]}{num:02d}" for num in range(1, 101)]
        print(f"Testing {len(lateral_rolls)} lateral roll numbers...")
        with ThreadPoolExecutor(max_workers=5) as executor:
            results = list(executor.map(test_roll_number, lateral_rolls))
            valid_rolls.extend(result['roll'] for result in results if result['status'] == 200)
    
    # Sort rolls to maintain rejoin -> regular -> lateral order
    def get_roll_type_order(roll):
        if '22EG' in roll:  # Rejoin/Detained
            return 0
        elif '24EG5' in roll:  # Lateral
            return 2
        return 1  # Regular
    
    valid_rolls.sort(key=get_roll_type_order)
    
    return valid_rolls

def determine_student_status(data):
    """Determine if a student is regular, detained, or lateral entry"""
    roll_no = data["student"]["rollNo"]
    batch_year = "20" + roll_no[:2]
    current_year = 2024
    
    # Check if lateral entry
    if "509" in roll_no or "512" in roll_no:
        return "Lateral"
        
    # Get all exam attempts chronologically
    all_attempts = []
    for sem in data["results"]:
        for subject in sem["subjectsResults"]:
            for grade in subject["subjectGrades"]:
                all_attempts.append({
                    'sem': sem["semNo"],
                    'date': grade["monthYear"],
                    'passed': grade["passed"]
                })
    
    # Sort attempts by date
    all_attempts.sort(key=lambda x: x['date'])
    
    # Check for out-of-sequence attempts or multiple attempts in same subject
    expected_year = int(batch_year)
    for attempt in all_attempts:
        attempt_year = int(attempt['date'].split()[-1])
        if attempt_year - expected_year > 2:  # More than expected gap
            return "Rejoin"
            
    # If student is from 2022 batch and still has first/second year subjects in 2024
    if batch_year == "2022" and current_year == 2024:
        for attempt in all_attempts:
            if attempt['date'].endswith("2024") and attempt['sem'] <= 2:
                return "Rejoin"
    
    return "Regular"

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
        
        # Check if student has all requested semesters
        available_sems = {sem["semNo"] for sem in data["results"]}
        missing_sems = set(selected_sems) - available_sems
        if missing_sems:
            print(f"Skipping {roll_no}: Missing semesters {missing_sems}")
            return None
        
        student_info = data["student"]
        student_name = student_info["fullName"]
        
        # Determine student status
        status = determine_student_status(data)
        
        # Add batch year from roll number
        batch_year = "20" + roll_no[:2]
        
        student_result_detailed = {
            "Roll No": roll_no,
            "Name": student_info["fullName"],
            "Batch": batch_year,
            "Entry Type": status
        }
        
        student_result_simple = student_result_detailed.copy()
        
        # Process each semester's subjects
        for semester in data["results"]:
            if semester["semNo"] not in selected_sems:
                continue
            
            if not semester["subjectsResults"]:
                continue
                
            for subject in semester["subjectsResults"]:
                subject_info = subject["subject"]
                grade_info = subject["consideredGrade"]
                subject_name = subject_info['name']
                
                # For detailed CSV (with grades)
                student_result_detailed[f"{subject_name}"] = subject_name
                student_result_detailed[f"{subject_name} Grade"] = grade_info['grade']
                student_result_detailed[f"{subject_name} Result"] = 'Pass' if grade_info['passed'] else 'Fail'
                
                # For simple CSV (only pass/fail)
                student_result_simple[subject_name] = 'Pass' if grade_info['passed'] else 'Fail'
        
        if len(student_result_detailed) > 4:  # If subjects were added
            return {
                'detailed': student_result_detailed,
                'simple': student_result_simple
            }
        return None

    except Exception as e:
        print(f"Error processing {roll_no}: {str(e)}")
        return None

def get_manual_roll_numbers(include_custom=False):
    """Get roll numbers manually from user input"""
    roll_numbers = []
    
    # Get rejoin roll numbers
    print("\nEnter rejoin roll numbers (comma-separated or one per line, press Enter twice to finish):")
    while True:
        rolls = input().strip()
        if not rolls:
            break
        # Split by comma and clean each roll number
        roll_list = [r.strip() for r in rolls.split(',') if r.strip()]
        roll_numbers.extend(roll_list)
    
    # Get lateral entry roll numbers
    print("\nEnter lateral entry roll numbers (comma-separated or one per line, press Enter twice to finish):")
    while True:
        rolls = input().strip()
        if not rolls:
            break
        # Split by comma and clean each roll number
        roll_list = [r.strip() for r in rolls.split(',') if r.strip()]
        roll_numbers.extend(roll_list)
    
    # Get custom roll numbers
    if include_custom:
        print("\nEnter any other roll numbers (comma-separated or one per line, press Enter twice to finish):")
        while True:
            rolls = input().strip()
            if not rolls:
                break
            # Split by comma and clean each roll number
            roll_list = [r.strip() for r in rolls.split(',') if r.strip()]
            roll_numbers.extend(roll_list)
    
    return roll_numbers

def main():
    print("Available Sections:")
    for section in SECTION_PATTERNS.keys():
        print(f"Section {section}")
    
    section = input("\nEnter section (e.g., CS-A, IT-B): ")
    if section not in SECTION_PATTERNS:
        print("Invalid section!")
        return
    
    # Ask for mode
    print("\nChoose mode:")
    print("1. Automated (Check all possible roll numbers)")
    print("2. Manual (Input specific roll numbers)")
    mode = input("Enter mode (1/2): ").strip()
    
    include_detained = input("Include detained students? (y/n): ").lower() == 'y'
    include_lateral = input("Include lateral entry students? (y/n): ").lower() == 'y'
    include_custom = input("Include any other roll numbers? (y/n): ").lower() == 'y'
    
    if mode == "1":
        # Automated mode
        roll_numbers = generate_roll_numbers(
            SECTION_PATTERNS[section],
            include_detained,
            include_lateral
        )
    else:
        # Manual mode
        manual_rolls = get_manual_roll_numbers(include_custom) if (include_detained or include_lateral or include_custom) else []
        
        # Generate regular roll numbers (1-80)
        regular_prefix = SECTION_PATTERNS[section]['regular'][0]  # Current batch prefix
        regular_rolls = [f"{regular_prefix}{num:02d}" for num in range(1, 81)]
        
        # Combine and sort roll numbers
        roll_numbers = manual_rolls + regular_rolls
        
        # Sort rolls to maintain rejoin -> regular -> lateral -> custom order
        def get_roll_type_order(roll):
            if '22EG' in roll:  # Rejoin/Detained
                return 0
            elif '24EG5' in roll:  # Lateral
                return 2
            elif roll.startswith('23EG'):  # Regular
                return 1
            return 3  # Custom/Other
        
        roll_numbers.sort(key=get_roll_type_order)
    
    if not roll_numbers:
        print("No valid roll numbers found!")
        return
    
    print(f"\nFound {len(roll_numbers)} roll numbers")
    print("Roll numbers:", roll_numbers)
    
    print("\nEnter semester numbers to fetch (comma-separated)")
    print("Example: 1,2,3")
    sems_input = input("Semesters: ")
    selected_sems = [int(sem.strip()) for sem in sems_input.split(",")]
    
    detailed_results = []
    simple_results = []
    total_rolls = len(roll_numbers)
    
    print(f"\nFetching results for {total_rolls} students...")
    for i, roll_no in enumerate(roll_numbers, 1):
        print(f"Processing {roll_no} ({i}/{total_rolls})...")
        result = get_student_results(roll_no, selected_sems)
        if result and isinstance(result, dict) and 'detailed' in result and 'simple' in result:
            detailed_results.append(result['detailed'])
            simple_results.append(result['simple'])
        time.sleep(1)  # Add delay to avoid overwhelming the server
    
    if detailed_results and simple_results:
        # Convert to DataFrames
        df_detailed = pd.DataFrame(detailed_results)
        df_simple = pd.DataFrame(simple_results)
        
        # Sort DataFrames by Entry Type in desired order
        entry_type_order = {'Rejoin': 0, 'Regular': 1, 'Lateral': 2}
        for df in [df_detailed, df_simple]:
            df['EntryTypeOrder'] = df['Entry Type'].map(entry_type_order)
            df.sort_values(['EntryTypeOrder', 'Roll No'], inplace=True)
            df.drop('EntryTypeOrder', axis=1, inplace=True)
        
        # Create base filename
        sem_str = '-'.join(map(str, selected_sems))
        types = []
        if include_detained:
            types.append("rejoin")
        if include_lateral:
            types.append("lateral")
        type_str = "_with_" + "_".join(types) if types else ""
        base_filename = f"{section}_sem{sem_str}{type_str}"
        
        # Save detailed CSV
        detailed_filepath = os.path.join('data', f"{base_filename}_detailed.csv")
        df_detailed.to_csv(detailed_filepath, index=False)
        
        # Save simple CSV
        simple_filepath = os.path.join('data', f"{base_filename}_simple.csv")
        df_simple.to_csv(simple_filepath, index=False)
        
        print(f"\nResults exported to:")
        print(f"Detailed results: {detailed_filepath}")
        print(f"Simple results: {simple_filepath}")
        
        # Display summary
        print("\nSummary:")
        print(f"Total students processed: {total_rolls}")
        print(f"Total unique students: {len(df_detailed)}")
        
        # Display batch-wise and entry-type summary
        batch_summary = df_detailed.groupby(['Batch', 'Entry Type'])['Roll No'].nunique().sort_index()
        print("\nBatch-wise Summary:")
        print(batch_summary)
        
        # Display entry-type summary
        entry_summary = df_detailed.groupby('Entry Type')['Roll No'].nunique()
        print("\nEntry Type Summary:")
        for entry_type in ['Rejoin', 'Regular', 'Lateral']:
            if entry_type in entry_summary:
                print(f"{entry_type}: {entry_summary[entry_type]} students")
    else:
        print("No results were fetched!")

if __name__ == "__main__":
    main()
