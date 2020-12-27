all_courses=[]
user="MEHMET APALAN"
check=False

def course_count():
    if len(all_courses)<3:
        count=len(all_courses)
        print(f"You have {count} courses")
        all_courses.clear()
        return "You failed in class"

def grades():
    g={"midterm":0,"final":0,"project":0}
    midterm=int(input("Midterm note: "))
    final=int(input("Final note: "))
    project=int(input("Project note: "))
    g[midterm]=midterm
    g[final]=final
    g[project]=project
    grade= midterm*0.3 + final*0.5 + project*0.2
    return grade
      
entry=3
while range(3):   
    name=input("Your name and surname: ")
    if name=="exit" or name=="Exit" or name=="EXIT":
        break
    if name.upper()==user:
        print(f"WELCOME {user}")
        for i in range(5):
            i+=1
            print("Select courses. To stop selecting, press q")
            course=input(f"Select the course {i}: ")
            if course=="q":
                print(course_count())
                break              
            all_courses.append(course)
            print("Your courses: ", all_courses)
        check=True
        break
            
    else:
        entry-=1
        if entry==0:
            print("Please try again later")
            break
            
if check==True:
    while True:
        select_course=int(input("Select a course,write its number: "))
        if select_course>len(all_courses) or select_course<1:
            print("Invalid course number, try again!")
        else:
            x=all_courses[select_course-1]
            print(f"Your selected course: {x}")
            grade=grades()
            if grade>=90:
                print(f"Your average is {grade}")
                print("AA")
            elif grade>=70:
                print(f"Your average is {grade}")
                print("BB")
            elif grade>=50:
                print(f"Your average is {grade}")
                print("CC")
            elif grade>=30:
                print(f"Your average is {grade}")
                print("DD")
            else:
                print(f"Your average is {grade}")
                print("FF")
                print("You failed in course")
       
        break
        
      
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
