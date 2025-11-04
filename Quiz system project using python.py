questions = {
    1:{
        "tech":"Python",
        "question":"What is Python?",
        "options": {
            "A":"general-purpose",
            "B":"high-level",
            "C":"Interpreted&Dynamically-typed",
            "D":"All of the above"
        },
        "answer": "D"
    },
    2: {
       "tech":"MySQL",
       "question":"Which MySQL statement is used to select data from a databse?",
       "options":{
           "A":"SELECT",
           "B":"EXTRACT",
           "C":"GET",
           "D":"OPEN"
           },
       "answer":"A"
    },
    3: {
        "tech": "Python",
        "question": "Which keyword is used for function in Python?",
        "options": {
            "A": "fun",
            "B": "define",
            "C": "def",
            "D": "function"
        },
        "answer": "C"
    }
}

user_scores = []
admin_id = "Diya"
admin_password = "Diya@1234"
qn_no = 4

while True:
    print('*'*15,'QUIZ SYSTEM','*'*15)
    print("1. Admin Login")
    print("2. User Login")
    print("3. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        id_input = input("Enter Admin ID: ")
        pass_input = input("Enter Admin Password: ")

        if id_input == admin_id and pass_input == admin_password:
            while True:
                print("\n--- ADMIN PANEL ---")
                print("1. Add Question")
                print("2. Modify Question")
                print("3. Delete Question")
                print("4. View All Questions")
                print("5. View All User Details")
                print("6. Logout")
                admin_choice = input("Enter choice: ")

                if admin_choice == "1":
                    tech = input("Enter technology: ")
                    ques = input("Enter question: ")
                    optA = input("Option A: ")
                    optB = input("Option B: ")
                    optC = input("Option C: ")
                    optD = input("Option D: ")
                    correct = input("Correct Option (A/B/C/D): ").upper()
                    questions[qn_no] = {
                        "tech": tech,
                        "question": ques,
                        "options": {
                            "A": optA,
                            "B": optB,
                            "C": optC,
                            "D": optD
                        },
                        "answer": correct
                    }
                    print("Question added with Q.No:", qn_no)
                    qn_no += 1

                elif admin_choice == "2":
                    qn = int(input("Enter Q.No to modify: "))
                    if qn in questions:
                        questions[qn]["question"] = input("New question: ")
                        questions[qn]["options"]["A"] = input("New Option A: ")
                        questions[qn]["options"]["B"] = input("New Option B: ")
                        questions[qn]["options"]["C"] = input("New Option C: ")
                        questions[qn]["options"]["D"] = input("New Option D: ")
                        questions[qn]["answer"] = input("New Correct Option: ").upper()
                        print("Question Modified")
                    else:
                        print("Invalid Question Number")

                elif admin_choice == "3":
                    qn = int(input("Enter Q.No to delete: "))
                    if qn in questions:
                        del questions[qn]
                        print("Question Deleted")
                    else:
                        print("Invalid Question Number")

                elif admin_choice == "4":
                    for qn in questions:
                        q = questions[qn]
                        print(f"\nQ.No {qn} [{q['tech']}]")
                        print("Q:", q["question"])
                        for opt in q["options"]:
                            print(f"{opt}) {q['options'][opt]}")
                        print("Answer:", q["answer"])

                elif admin_choice == "5":
                    print("\n--- USER DETAILS ---")
                    for user in user_scores:
                        print(user)

                elif admin_choice == "6":
                    break
                else:
                    print("Invalid choice")

        else:
            print("Wrong Admin credentials!")

    elif choice == "2":
        name = input("Enter Name: ")
        mobile = input("Enter Mobile No: ")
        tech = input("Select Technology (Python/MySQL): ")
        score = 0

        from datetime import datetime
        start_time = datetime.now()

        print("\n--- QUIZ START ---")
        for qn in questions:
            q = questions[qn]
            if q["tech"].lower() == tech.lower():
                print("\nQ:", q["question"])
                for opt in q["options"]:
                    print(f"{opt}) {q['options'][opt]}")
                user_ans = input("Your Answer (A/B/C/D): ").upper()
                if user_ans == q["answer"]:
                    score += 1

        end_time = datetime.now()
        duration = str(end_time - start_time).split('.')[0]
        print("Quiz Finished. Score:", score)

        user_scores.append({
            "name": name,
            "mobile": mobile,
            "score": score,
            "time": duration
        })

        while True:
            print("\n1. View Top 3 Scores")
            print("2. Logout")
            opt = input("Enter choice: ")
            if opt == "1":
                sorted_scores = sorted(user_scores, key=lambda x: x["score"], reverse=True)
                print("\n--- TOP 3 SCORES ---")
                for idx, u in enumerate(sorted_scores[:3], 1):
                    print(f"{idx}. {u['name']} - {u['score']} pts in {u['time']}")
            elif opt == "2":
                break
            else:
                print("Invalid choice")

    elif choice == "3":
        break
    else:
        print("Invalid choice")
