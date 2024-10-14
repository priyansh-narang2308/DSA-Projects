'''Students grade checker 
This project aims to develop a program that can calculate and display students’ grades based on their scores in various subjects. It can use a hash table to store and retrieve grades efficiently, and stores data as key-value pairs where students’ name or IDs is the ‘key’ and their grades are the ‘value.’ You can also implement functions to add or delete grades from the table. 

Learning outcomes:

Learn fundamental concepts of data structures and algorithms related to data manipulation and basic arithmetic calculations
Use of hash tables to store students’ information and grades
Understanding of searching and sorting algorithms to organize or search students’ data based on specific criteria like student ID, total score, etc.
Knowledge of file input/output operations, error handling techniques, and designing user interface
What it takes to execute this project:

Use a data structure like an array or linked list to store student records (name, grades).
Implement functions to add, remove, and update student records.
Use sorting algorithms (e.g., merge sort, quick sort) to sort student records by name or grade.
Implement search algorithms (e.g., binary search, linear search) to find specific student records.
Calculate and store aggregate statistics like class average and highest/lowest grades.
Consider using a hash table or tree for efficient student lookup.
Implement grade calculation algorithms based on course policies (e.g., weighted averages).
Provide a user interface for managing student records and displaying grade reports.
Handle file I/O for storing and loading student data persistently'''

import pickle

class StudentGradeChecker:
    def __init__(self):
        self.records={}
        
    def add_student(self,student_id,name,grades):
        total=sum(grades)/len(grades)
        self.records[student_id]={"name": name, "grades" : grades, "total" : total}
        print("Student: " , name , "added succesfully!!")

    def remove_student(self,student_id):
        if student_id in self.records:
            del self.records[student_id]
            print("Student with the ID: " , student_id , "removed successfully!!")
        else:
            print("Student ID not found")
            
    def update_grades(self,student_id,new_grades):
        if student_id in self.records:
            self.records[student_id]["grades"]=new_grades
            self.records[student_id]["total"]=sum(new_grades)/len(new_grades)
            print("Grades updated for student id : " , student_id , "!!")
        else:
            print("Student ID not found")
            
    def display_student(self,student_id):
        if student_id in self.records:
            student=self.records[student_id]
            print("ID: " , student_id ,"|" , "Name: " , student["name"] , "|"  "Grades: " , student["grade"] , "Total: " , student["total"] )
        
        else:
            print("Student ID not found")
            
    def class_average(self):
        if self.records:
            total=sum(student["total"]for student in self.records.values()) / len(self.records)
            print("Class Average: " , total)
        else:
            print("No students to calc avaergae.")
            
    def highest_lowest(self):
        if self.records:
            highest=max(self.records.items() ,key=lambda item: item[1]["total"])
            lowest=min(self.records.items() ,key=lambda item: item[1]["total"])
            print(f"Highest Grade: {highest[1]['name']} - {highest[1]['total']:.2f}")
            print(f"Lowest Grade: {lowest[1]['name']} - {lowest[1]['total']:.2f}")
        else:
            print("No students available!")
            
    def sort_by_name(self):
        sorted_records=sorted(self.records.items() ,key=lambda item:item[1]['name'])
        for student_id, student in sorted_records:
            self.display_student(student_id)
        
    def sort_by_grade(self):
        sorted_records=sorted(self.records.items(),key=lambda item:item[1]["total"],reverse=True)
        for student_id, student in sorted_records:
            self.display_student(student_id)
            
    def search_by_id(self,student_id):
        self.display_student(student_id)
        
    def save_to_file(self,filename):
        #it saves current records to file.
        with open(filename,'wb') as file:
            pickle.dump(self.records,file)
            print("Records saved to : " ,filename)
    
    def load_from_file(self,filename):
        try:
            with open(filename, 'rb') as file:
                self.records = pickle.load(file)
                print(f"Records loaded from {filename}.")
        except FileNotFoundError:
            print("File not found!")
        except Exception as e:
            print(f"Error loading file: {e}")



def main():
    checker=StudentGradeChecker()
    
    while True:
        print("\n---STUDENT GRADE CHECKER---")
        print("1. Add student")
        print("2. Remove student")
        print("3. Update grades")
        print("4. Display student details")
        print("5. Class average")
        print("6. Highest and Lowest grades")
        print("7. Sort by name")
        print("8. Sort by grades")
        print("9. Search by student ID")
        print("10. Save to file")
        print("11. Load from file")
        print("12. Exit")
        
        choice=input("Choose an option: ")
        
        if choice=="1":
            student_id=input("Enter student ID: ")
            name = input("Enter student name: ")
            grades = list(map(float, input("Enter grades (space-separated): ").split()))
            checker.add_student(student_id, name, grades)
        
        elif choice == "2":
            student_id = input("Enter student ID to remove: ")
            checker.remove_student(student_id)

        elif choice == "3":
            student_id = input("Enter student ID to update: ")
            new_grades = list(map(float, input("Enter new grades (space-separated): ").split()))
            checker.update_grades(student_id, new_grades)

        elif choice == "4":
            student_id = input("Enter student ID for display: ")
            checker.display_student(student_id)

        elif choice == "5":
            checker.class_average()

        elif choice == "6":
            checker.highest_lowest()

        elif choice == "7":
            checker.sort_by_name()

        elif choice == "8":
            checker.sort_by_grade()

        elif choice == "9":
            student_id = input("Enter student ID to search: ")
            checker.search_by_id(student_id)

        elif choice == "10":
            filename = input("Enter filename to save: ")
            checker.save_to_file(filename)

        elif choice == "11":
            filename = input("Enter filename to load: ")
            checker.load_from_file(filename)

        elif choice == "12":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
