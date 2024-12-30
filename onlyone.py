import requests
import json
from tabulate import tabulate

def get_student_results(roll_no):
    # API endpoint
    url = f"https://api.campx.in/exams/student-results/external"
    
    # Parameters
    params = {
        "examType": "general",
        "rollNo": roll_no
    }
    
    # Updated headers based on the cURL request
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.9",
        "Origin": "https://aupulse.campx.in",  # Changed from results.campx.in
        "Referer": "https://aupulse.campx.in/",  # Changed from results.campx.in
        "sec-ch-ua": '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "x-api-version": "2",  # Added this important header
        "x-institution-code": "aupulse",  # Added this important header
        "x-tenant-id": "aupulse"  # Changed from srkrec to aupulse
    }

    try:
        # Make the request with a session to handle cookies
        session = requests.Session()
        
        # Set the cookie from the cURL request
        cookies = {
            "_clck": "1qn1ema|2|fm8|0|1492"
        }
        session.cookies.update(cookies)
        
        # Make the main request
        response = session.get(url, params=params, headers=headers)
        
        if response.status_code == 422:
            print("Error: Unable to get tenant details. This might be because:")
            print("1. The roll number format is incorrect")
            print("2. The institution code or tenant ID might be incorrect")
            print(f"Response content: {response.text}")
            return
            
        response.raise_for_status()
        
        # Parse the JSON response
        data = response.json()
        
        # Extract and display student info
        student = data["student"]
        print(f"\nStudent Name: {student['fullName']}")
        print(f"Roll Number: {student['rollNo']}\n")
        
        # Process results semester-wise
        for semester in data["results"]:
            sem_no = semester["semNo"]
            print(f"\nSemester {sem_no} Results:")
            print("-" * 80)
            
            # Prepare results table
            results_table = []
            for subject in semester["subjectsResults"]:
                subject_info = subject["subject"]
                grade_info = subject["consideredGrade"]
                
                results_table.append([
                    subject_info["subjectCode"],
                    subject_info["name"],
                    subject_info["credits"],
                    grade_info["grade"],
                    grade_info["gradePoints"],
                    "Pass" if grade_info["passed"] else "Fail"
                ])
            
            # Display results in tabular format
            table_headers = ["Subject Code", "Subject Name", "Credits", "Grade", "Grade Points", "Status"]
            print(tabulate(results_table, headers=table_headers, tablefmt="grid"))
            
            # Display SGPA if available
            if semester["sgpa"]:
                print(f"\nSGPA: {semester['sgpa']}")
            if semester["cgpa"]:
                print(f"CGPA: {semester['cgpa']}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching results: {e}")
        print(f"Response content: {response.text if 'response' in locals() else 'No response'}")
    except json.JSONDecodeError:
        print("Error parsing response data")
        print(f"Response content: {response.text if 'response' in locals() else 'No response'}")
    except KeyError as e:
        print(f"Error accessing data: {e}")
        print(f"Available keys: {data.keys() if 'data' in locals() else 'No data'}")

if __name__ == "__main__":
    roll_no = input("Enter your roll number: ")
    get_student_results(roll_no)