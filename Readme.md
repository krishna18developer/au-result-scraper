# AU Result Scraper

## Prepare the environment

### Windows
Use Powershell
```
python3 -m venv venv
venv/Scripts/Activate
```

### MacOS / Linux

```
python3 -m venv venv
./venv/Scripts/activate
```

## Install The Packages

```
pip install -r requirements.txt
```

## Using The Script

```
python app.py
```

## Additional Details

Sample Response Format from server

```json
{
    "student": {
        "fullName": "BEESU DURGA PRASAD",
        "rollNo": "23EG109A08",
        "institutionId": 1
    },
    "course": {
        "id": 1,
        "institutionId": 1,
        "courseName": "B TECH",
        "program": "BACHELOR OF TECHNOLOGY",
        "displayName": "Bachelor of Technology",
        "refCode": null,
        "duration": 4,
        "level": "UNDER GRADUATE",
        "schoolType": "ENGINEERING"
    },
    "program": {
        "id": 36,
        "courseId": 1,
        "branchCode": "CSE(CS)",
        "branchName": "COMPUTER SCIENCE AND ENGINEERING (CYBER SECURITY)",
        "branchDisplay": "COMPUTER SCIENCE AND ENGINEERING (CYBER SECURITY)",
        "refCode": "Computer Science and Engineering (Cyber Security)C",
        "programOrder": null,
        "departmentId": "64a45d4e234e56399d9c646d"
    },
    "showMarks": false,
    "cgpa": "9.46",
    "results": [
        {
            "semNo": 1,
            "blocked": false,
            "sgpa": "9.49",
            "cgpa": "9.49",
            "subjectsResults": [
                {
                    "subject": {
                        "id": 6848,
                        "name": "Mathematics-I",
                        "subjectCode": "A51001",
                        "credits": "4.00",
                        "refCode": "M-I",
                        "hasInternal": true,
                        "intMax": 50,
                        "hasExternal": true,
                        "extMax": 50,
                        "isSatisfactoryCourse": false,
                        "isSatisfactoryWithExternal": false,
                        "isAuditCourse": false,
                        "isGradedCourse": true
                    },
                    "consideredGrade": {
                        "id": 4004157,
                        "monthYear": "JANUARY 2024",
                        "examType": "R",
                        "batch": "2023 - 2024",
                        "subjectId": 6848,
                        "passed": true,
                        "isAbsent": false,
                        "isMalPracticed": false,
                        "credits": "4.00",
                        "grade": "A+",
                        "gradePoints": 9,
                        "satisfactory": null
                    },
                    "subjectGrades": [
                        {
                            "id": 4004157,
                            "monthYear": "JANUARY 2024",
                            "examType": "R",
                            "batch": "2023 - 2024",
                            "subjectId": 6848,
                            "passed": true,
                            "isAbsent": false,
                            "isMalPracticed": false,
                            "credits": "4.00",
                            "grade": "A+",
                            "gradePoints": 9,
                            "satisfactory": null
                        }
                    ]
                },
                {
                    "subject": {
                        "id": 6850,
                        "name": "Applied Physics",
                        "subjectCode": "A51006",
                        "credits": "4.00",
                        "refCode": "AP-I",
                        "hasInternal": true,
                        "intMax": 50,
                        "hasExternal": true,
                        "extMax": 50,
                        "isSatisfactoryCourse": false,
                        "isSatisfactoryWithExternal": false,
                        "isAuditCourse": false,
                        "isGradedCourse": true
                    },
                    "consideredGrade": {
                        "id": 4004159,
                        "monthYear": "JANUARY 2024",
                        "examType": "R",
                        "batch": "2023 - 2024",
                        "subjectId": 6850,
                        "passed": true,
                        "isAbsent": false,
                        "isMalPracticed": false,
                        "credits": "4.00",
                        "grade": "O",
                        "gradePoints": 10,
                        "satisfactory": null
                    },
                    "subjectGrades": [
                        {
                            "id": 4004159,
                            "monthYear": "JANUARY 2024",
                            "examType": "R",
                            "batch": "2023 - 2024",
                            "subjectId": 6850,
                            "passed": true,
                            "isAbsent": false,
                            "isMalPracticed": false,
                            "credits": "4.00",
                            "grade": "O",
                            "gradePoints": 10,
                            "satisfactory": null
                        }
                    ]
                },
                {
                    "subject": {
                        "id": 6851,
                        "name": "Programming for Problem Solving-I",
                        "subjectCode": "A51004",
                        "credits": "2.00",
                        "refCode": "PPS-I",
                        "hasInternal": true,
                        "intMax": 50,
                        "hasExternal": true,
                        "extMax": 50,
                        "isSatisfactoryCourse": false,
                        "isSatisfactoryWithExternal": false,
                        "isAuditCourse": false,
                        "isGradedCourse": true
                    },
                    "consideredGrade": {
                        "id": 4004158,
                        "monthYear": "JANUARY 2024",
                        "examType": "R",
                        "batch": "2023 - 2024",
                        "subjectId": 6851,
                        "passed": true,
                        "isAbsent": false,
                        "isMalPracticed": false,
                        "credits": "2.00",
                        "grade": "A+",
                        "gradePoints": 9,
                        "satisfactory": null
                    },
                    "subjectGrades": [
                        {
                            "id": 4004158,
                            "monthYear": "JANUARY 2024",
                            "examType": "R",
                            "batch": "2023 - 2024",
                            "subjectId": 6851,
                            "passed": true,
                            "isAbsent": false,
                            "isMalPracticed": false,
                            "credits": "2.00",
                            "grade": "A+",
                            "gradePoints": 9,
                            "satisfactory": null
                        }
                    ]
                },
                {
                    "subject": {
                        "id": 6853,
                        "name": "Basic Electrical Engineering",
                        "subjectCode": "A51007",
                        "credits": "3.00",
                        "refCode": "BEE",
                        "hasInternal": true,
                        "intMax": 50,
                        "hasExternal": true,
                        "extMax": 50,
                        "isSatisfactoryCourse": false,
                        "isSatisfactoryWithExternal": false,
                        "isAuditCourse": false,
                        "isGradedCourse": true
                    },
                    "consideredGrade": {
                        "id": 4004160,
                        "monthYear": "JANUARY 2024",
                        "examType": "R",
                        "batch": "2023 - 2024",
                        "subjectId": 6853,
                        "passed": true,
                        "isAbsent": false,
                        "isMalPracticed": false,
                        "credits": "3.00",
                        "grade": "O",
                        "gradePoints": 10,
                        "satisfactory": null
                    },
                    "subjectGrades": [
                        {
                            "id": 4004160,
                            "monthYear": "JANUARY 2024",
                            "examType": "R",
                            "batch": "2023 - 2024",
                            "subjectId": 6853,
                            "passed": true,
                            "isAbsent": false,
                            "isMalPracticed": false,
                            "credits": "3.00",
                            "grade": "O",
                            "gradePoints": 10,
                            "satisfactory": null
                        }
                    ]
                },
                {
                    "subject": {
                        "id": 6854,
                        "name": "Applied Physics Lab",
                        "subjectCode": "A51232",
                        "credits": "1.50",
                        "refCode": "AP Lab",
                        "hasInternal": true,
                        "intMax": 50,
                        "hasExternal": true,
                        "extMax": 50,
                        "isSatisfactoryCourse": false,
                        "isSatisfactoryWithExternal": false,
                        "isAuditCourse": false,
                        "isGradedCourse": true
                    },
                    "consideredGrade": {
                        "id": 4004161,
                        "monthYear": "JANUARY 2024",
                        "examType": "R",
                        "batch": "2023 - 2024",
                        "subjectId": 6854,
                        "passed": true,
                        "isAbsent": false,
                        "isMalPracticed": false,
                        "credits": "1.50",
                        "grade": "O",
                        "gradePoints": 10,
                        "satisfactory": null
                    },
                    "subjectGrades": [
                        {
                            "id": 4004161,
                            "monthYear": "JANUARY 2024",
                            "examType": "R",
                            "batch": "2023 - 2024",
                            "subjectId": 6854,
                            "passed": true,
                            "isAbsent": false,
                            "isMalPracticed": false,
                            "credits": "1.50",
                            "grade": "O",
                            "gradePoints": 10,
                            "satisfactory": null
                        }
                    ]
                },
                {
                    "subject": {
                        "id": 6856,
                        "name": "Programming for Problem Solving-I Lab",
                        "subjectCode": "A51233",
                        "credits": "1.50",
                        "refCode": "PPS-I Lab",
                        "hasInternal": true,
                        "intMax": 50,
                        "hasExternal": true,
                        "extMax": 50,
                        "isSatisfactoryCourse": false,
                        "isSatisfactoryWithExternal": false,
                        "isAuditCourse": false,
                        "isGradedCourse": true
                    },
                    "consideredGrade": {
                        "id": 4004162,
                        "monthYear": "JANUARY 2024",
                        "examType": "R",
                        "batch": "2023 - 2024",
                        "subjectId": 6856,
                        "passed": true,
                        "isAbsent": false,
                        "isMalPracticed": false,
                        "credits": "1.50",
                        "grade": "A+",
                        "gradePoints": 9,
                        "satisfactory": null
                    },
                    "subjectGrades": [
                        {
                            "id": 4004162,
                            "monthYear": "JANUARY 2024",
                            "examType": "R",
                            "batch": "2023 - 2024",
                            "subjectId": 6856,
                            "passed": true,
                            "isAbsent": false,
                            "isMalPracticed": false,
                            "credits": "1.50",
                            "grade": "A+",
                            "gradePoints": 9,
                            "satisfactory": null
                        }
                    ]
                },
                {
                    "subject": {
                        "id": 6857,
                        "name": "Basic Electrical Engineering Lab",
                        "subjectCode": "A51234",
                        "credits": "1.00",
                        "refCode": "BEE Lab",
                        "hasInternal": true,
                        "intMax": 50,
                        "hasExternal": true,
                        "extMax": 50,
                        "isSatisfactoryCourse": false,
                        "isSatisfactoryWithExternal": false,
                        "isAuditCourse": false,
                        "isGradedCourse": true
                    },
                    "consideredGrade": {
                        "id": 4004163,
                        "monthYear": "JANUARY 2024",
                        "examType": "R",
                        "batch": "2023 - 2024",
                        "subjectId": 6857,
                        "passed": true,
                        "isAbsent": false,
                        "isMalPracticed": false,
                        "credits": "1.00",
                        "grade": "O",
                        "gradePoints": 10,
                        "satisfactory": null
                    },
                    "subjectGrades": [
                        {
                            "id": 4004163,
                            "monthYear": "JANUARY 2024",
                            "examType": "R",
                            "batch": "2023 - 2024",
                            "subjectId": 6857,
                            "passed": true,
                            "isAbsent": false,
                            "isMalPracticed": false,
                            "credits": "1.00",
                            "grade": "O",
                            "gradePoints": 10,
                            "satisfactory": null
                        }
                    ]
                },
                {
                    "subject": {
                        "id": 6859,
                        "name": "Engineering Workshop",
                        "subjectCode": "A51235",
                        "credits": "1.50",
                        "refCode": "EWS Lab",
                        "hasInternal": true,
                        "intMax": 50,
                        "hasExternal": true,
                        "extMax": 50,
                        "isSatisfactoryCourse": false,
                        "isSatisfactoryWithExternal": false,
                        "isAuditCourse": false,
                        "isGradedCourse": true
                    },
                    "consideredGrade": {
                        "id": 4004164,
                        "monthYear": "JANUARY 2024",
                        "examType": "R",
                        "batch": "2023 - 2024",
                        "subjectId": 6859,
                        "passed": true,
                        "isAbsent": false,
                        "isMalPracticed": false,
                        "credits": "1.50",
                        "grade": "A+",
                        "gradePoints": 9,
                        "satisfactory": null
                    },
                    "subjectGrades": [
                        {
                            "id": 4004164,
                            "monthYear": "JANUARY 2024",
                            "examType": "R",
                            "batch": "2023 - 2024",
                            "subjectId": 6859,
                            "passed": true,
                            "isAbsent": false,
                            "isMalPracticed": false,
                            "credits": "1.50",
                            "grade": "A+",
                            "gradePoints": 9,
                            "satisfactory": null
                        }
                    ]
                },
                {
                    "subject": {
                        "id": 6860,
                        "name": "English Communications Skills Lab",
                        "subjectCode": "A51236",
                        "credits": "1.00",
                        "refCode": "ECS Lab",
                        "hasInternal": true,
                        "intMax": 50,
                        "hasExternal": true,
                        "extMax": 50,
                        "isSatisfactoryCourse": false,
                        "isSatisfactoryWithExternal": false,
                        "isAuditCourse": false,
                        "isGradedCourse": true
                    },
                    "consideredGrade": {
                        "id": 4004165,
                        "monthYear": "JANUARY 2024",
                        "examType": "R",
                        "batch": "2023 - 2024",
                        "subjectId": 6860,
                        "passed": true,
                        "isAbsent": false,
                        "isMalPracticed": false,
                        "credits": "1.00",
                        "grade": "A+",
                        "gradePoints": 9,
                        "satisfactory": null
                    },
                    "subjectGrades": [
                        {
                            "id": 4004165,
                            "monthYear": "JANUARY 2024",
                            "examType": "R",
                            "batch": "2023 - 2024",
                            "subjectId": 6860,
                            "passed": true,
                            "isAbsent": false,
                            "isMalPracticed": false,
                            "credits": "1.00",
                            "grade": "A+",
                            "gradePoints": 9,
                            "satisfactory": null
                        }
                    ]
                }
            ]
        },
        {
            "semNo": 2,
            "blocked": false,
            "sgpa": "9.59",
            "cgpa": "9.54",
            "subjectsResults": [
                {
                    "subject": {
                        "id": 7404,
                        "name": "Mathematics–II",
                        "subjectCode": "A52001",
                        "credits": "4.00",
                        "refCode": "M 2",
                        "hasInternal": true,
                        "intMax": 50,
                        "hasExternal": true,
                        "extMax": 50,
                        "isSatisfactoryCourse": false,
                        "isSatisfactoryWithExternal": false,
                        "isAuditCourse": false,
                        "isGradedCourse": true
                    },
                    "consideredGrade": {
                        "id": 5145085,
                        "monthYear": "MAY 2024",
                        "examType": "R",
                        "batch": "2023 - 2024",
                        "subjectId": 7404,
                        "passed": true,
                        "isAbsent": false,
                        "isMalPracticed": false,
                        "credits": "4.00",
                        "grade": "O",
                        "gradePoints": 10,
                        "satisfactory": null
                    },
                    "subjectGrades": [
                        {
                            "id": 5145085,
                            "monthYear": "MAY 2024",
                            "examType": "R",
                            "batch": "2023 - 2024",
                            "subjectId": 7404,
                            "passed": true,
                            "isAbsent": false,
                            "isMalPracticed": false,
                            "credits": "4.00",
                            "grade": "O",
                            "gradePoints": 10,
                            "satisfactory": null
                        }
                    ]
                },
                {
                    "subject": {
                        "id": 7405,
                        "name": "English",
                        "subjectCode": "A52008",
                        "credits": "2.00",
                        "refCode": "ENG",
                        "hasInternal": true,
                        "intMax": 50,
                        "hasExternal": true,
                        "extMax": 50,
                        "isSatisfactoryCourse": false,
                        "isSatisfactoryWithExternal": false,
                        "isAuditCourse": false,
                        "isGradedCourse": true
                    },
                    "consideredGrade": {
                        "id": 5145087,
                        "monthYear": "MAY 2024",
                        "examType": "R",
                        "batch": "2023 - 2024",
                        "subjectId": 7405,
                        "passed": true,
                        "isAbsent": false,
                        "isMalPracticed": false,
                        "credits": "2.00",
                        "grade": "A+",
                        "gradePoints": 9,
                        "satisfactory": null
                    },
                    "subjectGrades": [
                        {
                            "id": 5145087,
                            "monthYear": "MAY 2024",
                            "examType": "R",
                            "batch": "2023 - 2024",
                            "subjectId": 7405,
                            "passed": true,
                            "isAbsent": false,
                            "isMalPracticed": false,
                            "credits": "2.00",
                            "grade": "A+",
                            "gradePoints": 9,
                            "satisfactory": null
                        }
                    ]
                },
                {
                    "subject": {
                        "id": 7406,
                        "name": "Engineering Chemistry",
                        "subjectCode": "A52009",
                        "credits": "4.00",
                        "refCode": "EC",
                        "hasInternal": true,
                        "intMax": 50,
                        "hasExternal": true,
                        "extMax": 50,
                        "isSatisfactoryCourse": false,
                        "isSatisfactoryWithExternal": false,
                        "isAuditCourse": false,
                        "isGradedCourse": true
                    },
                    "consideredGrade": {
                        "id": 5145088,
                        "monthYear": "MAY 2024",
                        "examType": "R",
                        "batch": "2023 - 2024",
                        "subjectId": 7406,
                        "passed": true,
                        "isAbsent": false,
                        "isMalPracticed": false,
                        "credits": "4.00",
                        "grade": "O",
                        "gradePoints": 10,
                        "satisfactory": null
                    },
                    "subjectGrades": [
                        {
                            "id": 5145088,
                            "monthYear": "MAY 2024",
                            "examType": "R",
                            "batch": "2023 - 2024",
                            "subjectId": 7406,
                            "passed": true,
                            "isAbsent": false,
                            "isMalPracticed": false,
                            "credits": "4.00",
                            "grade": "O",
                            "gradePoints": 10,
                            "satisfactory": null
                        }
                    ]
                },
                {
                    "subject": {
                        "id": 7407,
                        "name": "Programming for Problem Solving-II",
                        "subjectCode": "A52003",
                        "credits": "2.00",
                        "refCode": "PPS 2",
                        "hasInternal": true,
                        "intMax": 50,
                        "hasExternal": true,
                        "extMax": 50,
                        "isSatisfactoryCourse": false,
                        "isSatisfactoryWithExternal": false,
                        "isAuditCourse": false,
                        "isGradedCourse": true
                    },
                    "consideredGrade": {
                        "id": 5145086,
                        "monthYear": "MAY 2024",
                        "examType": "R",
                        "batch": "2023 - 2024",
                        "subjectId": 7407,
                        "passed": true,
                        "isAbsent": false,
                        "isMalPracticed": false,
                        "credits": "2.00",
                        "grade": "A+",
                        "gradePoints": 9,
                        "satisfactory": null
                    },
                    "subjectGrades": [
                        {
                            "id": 5145086,
                            "monthYear": "MAY 2024",
                            "examType": "R",
                            "batch": "2023 - 2024",
                            "subjectId": 7407,
                            "passed": true,
                            "isAbsent": false,
                            "isMalPracticed": false,
                            "credits": "2.00",
                            "grade": "A+",
                            "gradePoints": 9,
                            "satisfactory": null
                        }
                    ]
                },
                {
                    "subject": {
                        "id": 7408,
                        "name": "Engineering Graphics Lab",
                        "subjectCode": "A52229",
                        "credits": "2.50",
                        "refCode": "EG LAB",
                        "hasInternal": true,
                        "intMax": 50,
                        "hasExternal": true,
                        "extMax": 50,
                        "isSatisfactoryCourse": false,
                        "isSatisfactoryWithExternal": false,
                        "isAuditCourse": false,
                        "isGradedCourse": true
                    },
                    "consideredGrade": {
                        "id": 5145089,
                        "monthYear": "MAY 2024",
                        "examType": "R",
                        "batch": "2023 - 2024",
                        "subjectId": 7408,
                        "passed": true,
                        "isAbsent": false,
                        "isMalPracticed": false,
                        "credits": "2.50",
                        "grade": "A+",
                        "gradePoints": 9,
                        "satisfactory": null
                    },
                    "subjectGrades": [
                        {
                            "id": 5145089,
                            "monthYear": "MAY 2024",
                            "examType": "R",
                            "batch": "2023 - 2024",
                            "subjectId": 7408,
                            "passed": true,
                            "isAbsent": false,
                            "isMalPracticed": false,
                            "credits": "2.50",
                            "grade": "A+",
                            "gradePoints": 9,
                            "satisfactory": null
                        }
                    ]
                },
                {
                    "subject": {
                        "id": 7409,
                        "name": "English Language Skills Lab",
                        "subjectCode": "A52230",
                        "credits": "1.00",
                        "refCode": "ELS LAB",
                        "hasInternal": true,
                        "intMax": 50,
                        "hasExternal": true,
                        "extMax": 50,
                        "isSatisfactoryCourse": false,
                        "isSatisfactoryWithExternal": false,
                        "isAuditCourse": false,
                        "isGradedCourse": true
                    },
                    "consideredGrade": {
                        "id": 5145090,
                        "monthYear": "MAY 2024",
                        "examType": "R",
                        "batch": "2023 - 2024",
                        "subjectId": 7409,
                        "passed": true,
                        "isAbsent": false,
                        "isMalPracticed": false,
                        "credits": "1.00",
                        "grade": "A+",
                        "gradePoints": 9,
                        "satisfactory": null
                    },
                    "subjectGrades": [
                        {
                            "id": 5145090,
                            "monthYear": "MAY 2024",
                            "examType": "R",
                            "batch": "2023 - 2024",
                            "subjectId": 7409,
                            "passed": true,
                            "isAbsent": false,
                            "isMalPracticed": false,
                            "credits": "1.00",
                            "grade": "A+",
                            "gradePoints": 9,
                            "satisfactory": null
                        }
                    ]
                },
                {
                    "subject": {
                        "id": 7410,
                        "name": "Engineering Chemistry Lab",
                        "subjectCode": "A52231",
                        "credits": "1.50",
                        "refCode": "EC LAB",
                        "hasInternal": true,
                        "intMax": 50,
                        "hasExternal": true,
                        "extMax": 50,
                        "isSatisfactoryCourse": false,
                        "isSatisfactoryWithExternal": false,
                        "isAuditCourse": false,
                        "isGradedCourse": true
                    },
                    "consideredGrade": {
                        "id": 5145091,
                        "monthYear": "MAY 2024",
                        "examType": "R",
                        "batch": "2023 - 2024",
                        "subjectId": 7410,
                        "passed": true,
                        "isAbsent": false,
                        "isMalPracticed": false,
                        "credits": "1.50",
                        "grade": "O",
                        "gradePoints": 10,
                        "satisfactory": null
                    },
                    "subjectGrades": [
                        {
                            "id": 5145091,
                            "monthYear": "MAY 2024",
                            "examType": "R",
                            "batch": "2023 - 2024",
                            "subjectId": 7410,
                            "passed": true,
                            "isAbsent": false,
                            "isMalPracticed": false,
                            "credits": "1.50",
                            "grade": "O",
                            "gradePoints": 10,
                            "satisfactory": null
                        }
                    ]
                },
                {
                    "subject": {
                        "id": 7411,
                        "name": "Programming for Problem Solving – II Lab",
                        "subjectCode": "A52232",
                        "credits": "1.50",
                        "refCode": "PPS LAB 2",
                        "hasInternal": true,
                        "intMax": 50,
                        "hasExternal": true,
                        "extMax": 50,
                        "isSatisfactoryCourse": false,
                        "isSatisfactoryWithExternal": false,
                        "isAuditCourse": false,
                        "isGradedCourse": true
                    },
                    "consideredGrade": {
                        "id": 5145092,
                        "monthYear": "MAY 2024",
                        "examType": "R",
                        "batch": "2023 - 2024",
                        "subjectId": 7411,
                        "passed": true,
                        "isAbsent": false,
                        "isMalPracticed": false,
                        "credits": "1.50",
                        "grade": "O",
                        "gradePoints": 10,
                        "satisfactory": null
                    },
                    "subjectGrades": [
                        {
                            "id": 5145092,
                            "monthYear": "MAY 2024",
                            "examType": "R",
                            "batch": "2023 - 2024",
                            "subjectId": 7411,
                            "passed": true,
                            "isAbsent": false,
                            "isMalPracticed": false,
                            "credits": "1.50",
                            "grade": "O",
                            "gradePoints": 10,
                            "satisfactory": null
                        }
                    ]
                }
            ]
        },
        {
            "semNo": 3,
            "blocked": false,
            "sgpa": "9.60",
            "cgpa": "9.56",
            "subjectsResults": [
                {
                    "subject": {
                        "id": 7959,
                        "name": "Digital Logic Design",
                        "subjectCode": "A53024",
                        "credits": "3.00",
                        "refCode": "DLD",
                        "hasInternal": true,
                        "intMax": 50,
                        "hasExternal": true,
                        "extMax": 50,
                        "isSatisfactoryCourse": false,
                        "isSatisfactoryWithExternal": false,
                        "isAuditCourse": false,
                        "isGradedCourse": true
                    },
                    "consideredGrade": {
                        "id": 5196083,
                        "monthYear": "OCTOBER 2024",
                        "examType": "R",
                        "batch": "2023 - 2024",
                        "subjectId": 7959,
                        "passed": true,
                        "isAbsent": false,
                        "isMalPracticed": false,
                        "credits": "3.00",
                        "grade": "O",
                        "gradePoints": 10,
                        "satisfactory": null
                    },
                    "subjectGrades": [
                        {
                            "id": 5196083,
                            "monthYear": "OCTOBER 2024",
                            "examType": "R",
                            "batch": "2023 - 2024",
                            "subjectId": 7959,
                            "passed": true,
                            "isAbsent": false,
                            "isMalPracticed": false,
                            "credits": "3.00",
                            "grade": "O",
                            "gradePoints": 10,
                            "satisfactory": null
                        }
                    ]
                },
                {
                    "subject": {
                        "id": 7960,
                        "name": "Data Structures",
                        "subjectCode": "A53025",
                        "credits": "3.00",
                        "refCode": "DS",
                        "hasInternal": true,
                        "intMax": 50,
                        "hasExternal": true,
                        "extMax": 50,
                        "isSatisfactoryCourse": false,
                        "isSatisfactoryWithExternal": false,
                        "isAuditCourse": false,
                        "isGradedCourse": true
                    },
                    "consideredGrade": {
                        "id": 5196084,
                        "monthYear": "OCTOBER 2024",
                        "examType": "R",
                        "batch": "2023 - 2024",
                        "subjectId": 7960,
                        "passed": true,
                        "isAbsent": false,
                        "isMalPracticed": false,
                        "credits": "3.00",
                        "grade": "O",
                        "gradePoints": 10,
                        "satisfactory": null
                    },
                    "subjectGrades": [
                        {
                            "id": 5196084,
                            "monthYear": "OCTOBER 2024",
                            "examType": "R",
                            "batch": "2023 - 2024",
                            "subjectId": 7960,
                            "passed": true,
                            "isAbsent": false,
                            "isMalPracticed": false,
                            "credits": "3.00",
                            "grade": "O",
                            "gradePoints": 10,
                            "satisfactory": null
                        }
                    ]
                },
                {
                    "subject": {
                        "id": 7961,
                        "name": "Introduction to Python Programming",
                        "subjectCode": "A53038",
                        "credits": "2.00",
                        "refCode": "IPP",
                        "hasInternal": true,
                        "intMax": 50,
                        "hasExternal": true,
                        "extMax": 50,
                        "isSatisfactoryCourse": false,
                        "isSatisfactoryWithExternal": false,
                        "isAuditCourse": false,
                        "isGradedCourse": true
                    },
                    "consideredGrade": {
                        "id": 5196087,
                        "monthYear": "OCTOBER 2024",
                        "examType": "R",
                        "batch": "2023 - 2024",
                        "subjectId": 7961,
                        "passed": true,
                        "isAbsent": false,
                        "isMalPracticed": false,
                        "credits": "2.00",
                        "grade": "A+",
                        "gradePoints": 9,
                        "satisfactory": null
                    },
                    "subjectGrades": [
                        {
                            "id": 5196087,
                            "monthYear": "OCTOBER 2024",
                            "examType": "R",
                            "batch": "2023 - 2024",
                            "subjectId": 7961,
                            "passed": true,
                            "isAbsent": false,
                            "isMalPracticed": false,
                            "credits": "2.00",
                            "grade": "A+",
                            "gradePoints": 9,
                            "satisfactory": null
                        }
                    ]
                },
                {
                    "subject": {
                        "id": 7962,
                        "name": "Discrete Mathematics",
                        "subjectCode": "A53027",
                        "credits": "3.00",
                        "refCode": "DM",
                        "hasInternal": true,
                        "intMax": 50,
                        "hasExternal": true,
                        "extMax": 50,
                        "isSatisfactoryCourse": false,
                        "isSatisfactoryWithExternal": false,
                        "isAuditCourse": false,
                        "isGradedCourse": true
                    },
                    "consideredGrade": {
                        "id": 5196085,
                        "monthYear": "OCTOBER 2024",
                        "examType": "R",
                        "batch": "2023 - 2024",
                        "subjectId": 7962,
                        "passed": true,
                        "isAbsent": false,
                        "isMalPracticed": false,
                        "credits": "3.00",
                        "grade": "A",
                        "gradePoints": 8,
                        "satisfactory": null
                    },
                    "subjectGrades": [
                        {
                            "id": 5196085,
                            "monthYear": "OCTOBER 2024",
                            "examType": "R",
                            "batch": "2023 - 2024",
                            "subjectId": 7962,
                            "passed": true,
                            "isAbsent": false,
                            "isMalPracticed": false,
                            "credits": "3.00",
                            "grade": "A",
                            "gradePoints": 8,
                            "satisfactory": null
                        }
                    ]
                },
                {
                    "subject": {
                        "id": 7963,
                        "name": "Probability and Statistics",
                        "subjectCode": "A53030",
                        "credits": "3.00",
                        "refCode": "PS",
                        "hasInternal": true,
                        "intMax": 50,
                        "hasExternal": true,
                        "extMax": 50,
                        "isSatisfactoryCourse": false,
                        "isSatisfactoryWithExternal": false,
                        "isAuditCourse": false,
                        "isGradedCourse": true
                    },
                    "consideredGrade": {
                        "id": 5196086,
                        "monthYear": "OCTOBER 2024",
                        "examType": "R",
                        "batch": "2023 - 2024",
                        "subjectId": 7963,
                        "passed": true,
                        "isAbsent": false,
                        "isMalPracticed": false,
                        "credits": "3.00",
                        "grade": "O",
                        "gradePoints": 10,
                        "satisfactory": null
                    },
                    "subjectGrades": [
                        {
                            "id": 5196086,
                            "monthYear": "OCTOBER 2024",
                            "examType": "R",
                            "batch": "2023 - 2024",
                            "subjectId": 7963,
                            "passed": true,
                            "isAbsent": false,
                            "isMalPracticed": false,
                            "credits": "3.00",
                            "grade": "O",
                            "gradePoints": 10,
                            "satisfactory": null
                        }
                    ]
                },
                {
                    "subject": {
                        "id": 7964,
                        "name": "Python Programming Lab",
                        "subjectCode": "A53221",
                        "credits": "1.50",
                        "refCode": "PP LAB",
                        "hasInternal": true,
                        "intMax": 50,
                        "hasExternal": true,
                        "extMax": 50,
                        "isSatisfactoryCourse": false,
                        "isSatisfactoryWithExternal": false,
                        "isAuditCourse": false,
                        "isGradedCourse": true
                    },
                    "consideredGrade": {
                        "id": 5196088,
                        "monthYear": "OCTOBER 2024",
                        "examType": "R",
                        "batch": "2023 - 2024",
                        "subjectId": 7964,
                        "passed": true,
                        "isAbsent": false,
                        "isMalPracticed": false,
                        "credits": "1.50",
                        "grade": "O",
                        "gradePoints": 10,
                        "satisfactory": null
                    },
                    "subjectGrades": [
                        {
                            "id": 5196088,
                            "monthYear": "OCTOBER 2024",
                            "examType": "R",
                            "batch": "2023 - 2024",
                            "subjectId": 7964,
                            "passed": true,
                            "isAbsent": false,
                            "isMalPracticed": false,
                            "credits": "1.50",
                            "grade": "O",
                            "gradePoints": 10,
                            "satisfactory": null
                        }
                    ]
                },
                {
                    "subject": {
                        "id": 7965,
                        "name": "Data Structures Lab",
                        "subjectCode": "A53222",
                        "credits": "1.50",
                        "refCode": "DS LAB",
                        "hasInternal": true,
                        "intMax": 50,
                        "hasExternal": true,
                        "extMax": 50,
                        "isSatisfactoryCourse": false,
                        "isSatisfactoryWithExternal": false,
                        "isAuditCourse": false,
                        "isGradedCourse": true
                    },
                    "consideredGrade": {
                        "id": 5196089,
                        "monthYear": "OCTOBER 2024",
                        "examType": "R",
                        "batch": "2023 - 2024",
                        "subjectId": 7965,
                        "passed": true,
                        "isAbsent": false,
                        "isMalPracticed": false,
                        "credits": "1.50",
                        "grade": "O",
                        "gradePoints": 10,
                        "satisfactory": null
                    },
                    "subjectGrades": [
                        {
                            "id": 5196089,
                            "monthYear": "OCTOBER 2024",
                            "examType": "R",
                            "batch": "2023 - 2024",
                            "subjectId": 7965,
                            "passed": true,
                            "isAbsent": false,
                            "isMalPracticed": false,
                            "credits": "1.50",
                            "grade": "O",
                            "gradePoints": 10,
                            "satisfactory": null
                        }
                    ]
                },
                {
                    "subject": {
                        "id": 7966,
                        "name": "Design Thinking Lab",
                        "subjectCode": "A53224",
                        "credits": "1.00",
                        "refCode": "DT LAB",
                        "hasInternal": true,
                        "intMax": 50,
                        "hasExternal": true,
                        "extMax": 50,
                        "isSatisfactoryCourse": false,
                        "isSatisfactoryWithExternal": false,
                        "isAuditCourse": false,
                        "isGradedCourse": true
                    },
                    "consideredGrade": {
                        "id": 5196091,
                        "monthYear": "OCTOBER 2024",
                        "examType": "R",
                        "batch": "2023 - 2024",
                        "subjectId": 7966,
                        "passed": true,
                        "isAbsent": false,
                        "isMalPracticed": false,
                        "credits": "1.00",
                        "grade": "O",
                        "gradePoints": 10,
                        "satisfactory": null
                    },
                    "subjectGrades": [
                        {
                            "id": 5196091,
                            "monthYear": "OCTOBER 2024",
                            "examType": "R",
                            "batch": "2023 - 2024",
                            "subjectId": 7966,
                            "passed": true,
                            "isAbsent": false,
                            "isMalPracticed": false,
                            "credits": "1.00",
                            "grade": "O",
                            "gradePoints": 10,
                            "satisfactory": null
                        }
                    ]
                },
                {
                    "subject": {
                        "id": 7967,
                        "name": "Linux Programming Lab",
                        "subjectCode": "A53223",
                        "credits": "2.00",
                        "refCode": "LP LAB",
                        "hasInternal": true,
                        "intMax": 50,
                        "hasExternal": true,
                        "extMax": 50,
                        "isSatisfactoryCourse": false,
                        "isSatisfactoryWithExternal": false,
                        "isAuditCourse": false,
                        "isGradedCourse": true
                    },
                    "consideredGrade": {
                        "id": 5196090,
                        "monthYear": "OCTOBER 2024",
                        "examType": "R",
                        "batch": "2023 - 2024",
                        "subjectId": 7967,
                        "passed": true,
                        "isAbsent": false,
                        "isMalPracticed": false,
                        "credits": "2.00",
                        "grade": "O",
                        "gradePoints": 10,
                        "satisfactory": null
                    },
                    "subjectGrades": [
                        {
                            "id": 5196090,
                            "monthYear": "OCTOBER 2024",
                            "examType": "R",
                            "batch": "2023 - 2024",
                            "subjectId": 7967,
                            "passed": true,
                            "isAbsent": false,
                            "isMalPracticed": false,
                            "credits": "2.00",
                            "grade": "O",
                            "gradePoints": 10,
                            "satisfactory": null
                        }
                    ]
                },
                {
                    "subject": {
                        "id": 7968,
                        "name": "Environmental Studies",
                        "subjectCode": "A53007",
                        "credits": "0.00",
                        "refCode": "ES",
                        "hasInternal": false,
                        "intMax": null,
                        "hasExternal": false,
                        "extMax": null,
                        "isSatisfactoryCourse": true,
                        "isSatisfactoryWithExternal": false,
                        "isAuditCourse": false,
                        "isGradedCourse": true
                    },
                    "consideredGrade": {
                        "id": 5196082,
                        "monthYear": "OCTOBER 2024",
                        "examType": "R",
                        "batch": "2023 - 2024",
                        "subjectId": 7968,
                        "passed": true,
                        "isAbsent": false,
                        "isMalPracticed": false,
                        "credits": "0.00",
                        "grade": null,
                        "gradePoints": null,
                        "satisfactory": true
                    },
                    "subjectGrades": [
                        {
                            "id": 5196082,
                            "monthYear": "OCTOBER 2024",
                            "examType": "R",
                            "batch": "2023 - 2024",
                            "subjectId": 7968,
                            "passed": true,
                            "isAbsent": false,
                            "isMalPracticed": false,
                            "credits": "0.00",
                            "grade": null,
                            "gradePoints": null,
                            "satisfactory": true
                        }
                    ]
                }
            ]
        },
        {
            "semNo": 4,
            "blocked": false,
            "sgpa": "9.15",
            "cgpa": "9.46",
            "subjectsResults": [
                {
                    "subject": {
                        "id": 8305,
                        "name": "Computer Organization",
                        "subjectCode": "A54040",
                        "credits": "3.00",
                        "refCode": "CO",
                        "hasInternal": true,
                        "intMax": 50,
                        "hasExternal": true,
                        "extMax": 50,
                        "isSatisfactoryCourse": false,
                        "isSatisfactoryWithExternal": false,
                        "isAuditCourse": false,
                        "isGradedCourse": true
                    },
                    "consideredGrade": {
                        "id": 6080032,
                        "monthYear": "APRIL 2025",
                        "examType": "R",
                        "batch": "2023 - 2024",
                        "subjectId": 8305,
                        "passed": true,
                        "isAbsent": false,
                        "isMalPracticed": false,
                        "credits": "3.00",
                        "grade": "A+",
                        "gradePoints": 9,
                        "satisfactory": null
                    },
                    "subjectGrades": [
                        {
                            "id": 6080032,
                            "monthYear": "APRIL 2025",
                            "examType": "R",
                            "batch": "2023 - 2024",
                            "subjectId": 8305,
                            "passed": true,
                            "isAbsent": false,
                            "isMalPracticed": false,
                            "credits": "3.00",
                            "grade": "A+",
                            "gradePoints": 9,
                            "satisfactory": null
                        }
                    ]
                },
                {
                    "subject": {
                        "id": 8308,
                        "name": "Computer Networks",
                        "subjectCode": "A54039",
                        "credits": "3.00",
                        "refCode": "CN",
                        "hasInternal": true,
                        "intMax": 50,
                        "hasExternal": true,
                        "extMax": 50,
                        "isSatisfactoryCourse": false,
                        "isSatisfactoryWithExternal": false,
                        "isAuditCourse": false,
                        "isGradedCourse": true
                    },
                    "consideredGrade": {
                        "id": 6080033,
                        "monthYear": "APRIL 2025",
                        "examType": "R",
                        "batch": "2023 - 2024",
                        "subjectId": 8308,
                        "passed": true,
                        "isAbsent": false,
                        "isMalPracticed": false,
                        "credits": "3.00",
                        "grade": "A+",
                        "gradePoints": 9,
                        "satisfactory": null
                    },
                    "subjectGrades": [
                        {
                            "id": 6080033,
                            "monthYear": "APRIL 2025",
                            "examType": "R",
                            "batch": "2023 - 2024",
                            "subjectId": 8308,
                            "passed": true,
                            "isAbsent": false,
                            "isMalPracticed": false,
                            "credits": "3.00",
                            "grade": "A+",
                            "gradePoints": 9,
                            "satisfactory": null
                        }
                    ]
                },
                {
                    "subject": {
                        "id": 8312,
                        "name": "Data Base Management Systems",
                        "subjectCode": "A54027",
                        "credits": "3.00",
                        "refCode": "DBMS",
                        "hasInternal": true,
                        "intMax": 50,
                        "hasExternal": true,
                        "extMax": 50,
                        "isSatisfactoryCourse": false,
                        "isSatisfactoryWithExternal": false,
                        "isAuditCourse": false,
                        "isGradedCourse": true
                    },
                    "consideredGrade": {
                        "id": 6080034,
                        "monthYear": "APRIL 2025",
                        "examType": "R",
                        "batch": "2023 - 2024",
                        "subjectId": 8312,
                        "passed": true,
                        "isAbsent": false,
                        "isMalPracticed": false,
                        "credits": "3.00",
                        "grade": "A+",
                        "gradePoints": 9,
                        "satisfactory": null
                    },
                    "subjectGrades": [
                        {
                            "id": 6080034,
                            "monthYear": "APRIL 2025",
                            "examType": "R",
                            "batch": "2023 - 2024",
                            "subjectId": 8312,
                            "passed": true,
                            "isAbsent": false,
                            "isMalPracticed": false,
                            "credits": "3.00",
                            "grade": "A+",
                            "gradePoints": 9,
                            "satisfactory": null
                        }
                    ]
                },
                {
                    "subject": {
                        "id": 8315,
                        "name": "Object Oriented Programming",
                        "subjectCode": "A54043",
                        "credits": "3.00",
                        "refCode": "OOP",
                        "hasInternal": true,
                        "intMax": 50,
                        "hasExternal": true,
                        "extMax": 50,
                        "isSatisfactoryCourse": false,
                        "isSatisfactoryWithExternal": false,
                        "isAuditCourse": false,
                        "isGradedCourse": true
                    },
                    "consideredGrade": {
                        "id": 6080035,
                        "monthYear": "APRIL 2025",
                        "examType": "R",
                        "batch": "2023 - 2024",
                        "subjectId": 8315,
                        "passed": true,
                        "isAbsent": false,
                        "isMalPracticed": false,
                        "credits": "3.00",
                        "grade": "A+",
                        "gradePoints": 9,
                        "satisfactory": null
                    },
                    "subjectGrades": [
                        {
                            "id": 6080035,
                            "monthYear": "APRIL 2025",
                            "examType": "R",
                            "batch": "2023 - 2024",
                            "subjectId": 8315,
                            "passed": true,
                            "isAbsent": false,
                            "isMalPracticed": false,
                            "credits": "3.00",
                            "grade": "A+",
                            "gradePoints": 9,
                            "satisfactory": null
                        }
                    ]
                },
                {
                    "subject": {
                        "id": 8317,
                        "name": "Design and Analysis of Algorithms",
                        "subjectCode": "A54026",
                        "credits": "4.00",
                        "refCode": "DAA",
                        "hasInternal": true,
                        "intMax": 50,
                        "hasExternal": true,
                        "extMax": 50,
                        "isSatisfactoryCourse": false,
                        "isSatisfactoryWithExternal": false,
                        "isAuditCourse": false,
                        "isGradedCourse": true
                    },
                    "consideredGrade": {
                        "id": 6080036,
                        "monthYear": "APRIL 2025",
                        "examType": "R",
                        "batch": "2023 - 2024",
                        "subjectId": 8317,
                        "passed": true,
                        "isAbsent": false,
                        "isMalPracticed": false,
                        "credits": "4.00",
                        "grade": "A+",
                        "gradePoints": 9,
                        "satisfactory": null
                    },
                    "subjectGrades": [
                        {
                            "id": 6080036,
                            "monthYear": "APRIL 2025",
                            "examType": "R",
                            "batch": "2023 - 2024",
                            "subjectId": 8317,
                            "passed": true,
                            "isAbsent": false,
                            "isMalPracticed": false,
                            "credits": "4.00",
                            "grade": "A+",
                            "gradePoints": 9,
                            "satisfactory": null
                        }
                    ]
                },
                {
                    "subject": {
                        "id": 8320,
                        "name": "Data Base Management Systems Lab",
                        "subjectCode": "A54288",
                        "credits": "1.50",
                        "refCode": "DBMS LAB",
                        "hasInternal": true,
                        "intMax": 50,
                        "hasExternal": true,
                        "extMax": 50,
                        "isSatisfactoryCourse": false,
                        "isSatisfactoryWithExternal": false,
                        "isAuditCourse": false,
                        "isGradedCourse": true
                    },
                    "consideredGrade": {
                        "id": 6080037,
                        "monthYear": "APRIL 2025",
                        "examType": "R",
                        "batch": "2023 - 2024",
                        "subjectId": 8320,
                        "passed": true,
                        "isAbsent": false,
                        "isMalPracticed": false,
                        "credits": "1.50",
                        "grade": "O",
                        "gradePoints": 10,
                        "satisfactory": null
                    },
                    "subjectGrades": [
                        {
                            "id": 6080037,
                            "monthYear": "APRIL 2025",
                            "examType": "R",
                            "batch": "2023 - 2024",
                            "subjectId": 8320,
                            "passed": true,
                            "isAbsent": false,
                            "isMalPracticed": false,
                            "credits": "1.50",
                            "grade": "O",
                            "gradePoints": 10,
                            "satisfactory": null
                        }
                    ]
                },
                {
                    "subject": {
                        "id": 8322,
                        "name": "Java Programming Lab",
                        "subjectCode": "A54227",
                        "credits": "1.50",
                        "refCode": "JP Lab",
                        "hasInternal": true,
                        "intMax": 50,
                        "hasExternal": true,
                        "extMax": 50,
                        "isSatisfactoryCourse": false,
                        "isSatisfactoryWithExternal": false,
                        "isAuditCourse": false,
                        "isGradedCourse": true
                    },
                    "consideredGrade": {
                        "id": 6080038,
                        "monthYear": "APRIL 2025",
                        "examType": "R",
                        "batch": "2023 - 2024",
                        "subjectId": 8322,
                        "passed": true,
                        "isAbsent": false,
                        "isMalPracticed": false,
                        "credits": "1.50",
                        "grade": "O",
                        "gradePoints": 10,
                        "satisfactory": null
                    },
                    "subjectGrades": [
                        {
                            "id": 6080038,
                            "monthYear": "APRIL 2025",
                            "examType": "R",
                            "batch": "2023 - 2024",
                            "subjectId": 8322,
                            "passed": true,
                            "isAbsent": false,
                            "isMalPracticed": false,
                            "credits": "1.50",
                            "grade": "O",
                            "gradePoints": 10,
                            "satisfactory": null
                        }
                    ]
                },
                {
                    "subject": {
                        "id": 8324,
                        "name": "Soft Skills for Success Lab",
                        "subjectCode": "A54226",
                        "credits": "1.00",
                        "refCode": "SSS LAB",
                        "hasInternal": true,
                        "intMax": 50,
                        "hasExternal": true,
                        "extMax": 50,
                        "isSatisfactoryCourse": false,
                        "isSatisfactoryWithExternal": false,
                        "isAuditCourse": false,
                        "isGradedCourse": true
                    },
                    "consideredGrade": {
                        "id": 6080039,
                        "monthYear": "APRIL 2025",
                        "examType": "R",
                        "batch": "2023 - 2024",
                        "subjectId": 8324,
                        "passed": true,
                        "isAbsent": false,
                        "isMalPracticed": false,
                        "credits": "1.00",
                        "grade": "A+",
                        "gradePoints": 9,
                        "satisfactory": null
                    },
                    "subjectGrades": [
                        {
                            "id": 6080039,
                            "monthYear": "APRIL 2025",
                            "examType": "R",
                            "batch": "2023 - 2024",
                            "subjectId": 8324,
                            "passed": true,
                            "isAbsent": false,
                            "isMalPracticed": false,
                            "credits": "1.00",
                            "grade": "A+",
                            "gradePoints": 9,
                            "satisfactory": null
                        }
                    ]
                },
                {
                    "subject": {
                        "id": 8326,
                        "name": "Gender Sensitization",
                        "subjectCode": "A54022",
                        "credits": "0.00",
                        "refCode": "GS",
                        "hasInternal": true,
                        "intMax": 100,
                        "hasExternal": false,
                        "extMax": null,
                        "isSatisfactoryCourse": true,
                        "isSatisfactoryWithExternal": false,
                        "isAuditCourse": false,
                        "isGradedCourse": true
                    },
                    "consideredGrade": {
                        "id": 6080040,
                        "monthYear": "APRIL 2025",
                        "examType": "R",
                        "batch": "2023 - 2024",
                        "subjectId": 8326,
                        "passed": true,
                        "isAbsent": false,
                        "isMalPracticed": false,
                        "credits": "0.00",
                        "grade": null,
                        "gradePoints": null,
                        "satisfactory": true
                    },
                    "subjectGrades": [
                        {
                            "id": 6080040,
                            "monthYear": "APRIL 2025",
                            "examType": "R",
                            "batch": "2023 - 2024",
                            "subjectId": 8326,
                            "passed": true,
                            "isAbsent": false,
                            "isMalPracticed": false,
                            "credits": "0.00",
                            "grade": null,
                            "gradePoints": null,
                            "satisfactory": true
                        }
                    ]
                }
            ]
        }
    ]
}
```