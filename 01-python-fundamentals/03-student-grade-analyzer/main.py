students = []

def add_student() :
    while True :
            name = input("Enter student Name:").capitalize()
            if not name : 
                print("Name cannot be empty!")
                continue
            try:
                age = int(input("Enter age student:"))
                if age <= 0 : 
                    print("!Invalid Age")
                    continue
            except ValueError :
                print("Invalid Value!")
                continue

            subjectes = []
            grades = []
            credit_hours = []

            while True :
                try:
                    sub = input("Enter name subject: ").capitalize().strip()
                    if sub == "" :
                        break
                    else:
                        subjectes.append(sub)                
                        print("Press Enter to exit")
                except ValueError :
                    print("Invalid Value!")
                    continue 

            while True :
                grad = input("Enter grades:").strip()
                if grad == "" :
                    break
                else:
                    print("Press 'Enter' Space to exit") 
                    try:
                        grad = float(grad)

                        if not 0 <= grad <= 100 :
                            print("Grad must be between 0 and 100! ")
                            continue
                        grades.append(grad)
                    except ValueError :
                        print("Invalid Value!")
                        continue

            while True : 
                ch = input("How many Credit Hours: ").strip()

                if ch == "" :
                    break
                else:
                    try:
                        ch = int(ch)
                        credit_hours.append(ch)
                        print("Press 'Enter' to exit ")
                    except:
                        print("Invalid Value")
                        continue

            student = {
                "Name" : name ,
                "Age" : age ,
                "Subjectes" : subjectes ,
                "Grades" : grades ,
                "Credit_hours" : credit_hours
            }
            students.append(student)
            break

def student_Analytics(students) :

    name = students["Name"]
    credits_houres = students["Credit_hours"]
    grad = students["Grades"]
    if len(grad) == 0 :
        print(f"{name} is not has grades")
        return
    if len(grad) != len(credits_houres) :
        print("Grades and credites do not match!")
        return    
    def range_grad():
        range_grad = max(grad) - min(grad)
        return range_grad
    
    def max_and_min_grad() :
        max_grad = max(grad)
        min_grad = min(grad)
        return max_grad , min_grad
    
    def average_grad():
        average = sum(grad) / len(grad)
        return average
    
    def display_total_pass() :
        total_pass = 0
        total_falid = 0 
        for i in grad :
            if i < 50 :
                total_falid += 1 
            else:
                total_pass += 1 
        return total_pass
    
    def diplay_gpa() :
        if not credits_houres : 
            print("Credit hours are required to calculate GPA.")
            return
        # Grade point
        grad_points = []

        for i in grad :
                
            if 90 <= i <= 100 :
                grad_point = 4
            elif 85 <= i < 89 :
                grad_point = 3.7
            elif 80 <= i < 84 :
                grad_point = 3.3
            elif 75 <= i < 79 :
                grad_point = 3
            elif 70<= i < 74 :
                grad_point = 2.7
            elif 65 <= i < 69 :
                grad_point = 2
            else:
                grad_point = 0
            grad_points.append(grad_point)            

            total_points = 0 

        for point , credit in zip(grad_points , credits_houres) :
            total_points += point * credit

        gpa = total_points / sum(credits_houres)
        return gpa 
    
    while True :
        try:
            cho = int(input("""Enter what you want need:
            1- Range
            2-Max grad and min grad 
            3-Average
            4-total pass and total faild
            5- GPA 
            0- to home page 
            """))
        except ValueError :
            print("Invlaid Value.")
            continue

        match cho :
            case 1 :
                print(f"Range:{range_grad()}")
            case 2 :
                print(f"Max grad and min grad: {max_and_min_grad()}")
            case 3 :
                print(f"Average:{average_grad()}")
            case 4 : 
                print(f"Total pass : {display_total_pass()} \n total falid : {len(grad) - display_total_pass()} ")
            case 5 :
                print(f"Gpa:{diplay_gpa()}")
            case 0 :
                print("le'ts go to home page")
                break

def  search_student(students) : 
    search_name = input("Enter student name: ").strip().title()
    if not search_name : 
        print("Name cannot be empity")
        return
    for student in students :
        if student["Name"].title() == search_name : 
            student_Analytics(student)
            return
    print("student not foud")

while True :
    try:
        choice = int(input("""Enter what you want do 
        1-Add Students
        2-student Analytics by name 
        0-exit
    :"""))

    except ValueError:
        print("Invlaid Value.")
        continue

    match choice :
        case 1 :
            add_student()
        case 2 : 
            search_student(students)
        case 0:
            print("Good bay.")
            break


