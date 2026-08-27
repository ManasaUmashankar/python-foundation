# Quiz Game
# Python Foundation - Project 09

def run_quiz():
    questions = [
        {
            "question": "What does CPU stand for?",
            "options": ["A. Central Processing Unit",
                        "B. Computer Personal Unit",
                        "C. Central Program Utility",
                        "D. Control Processing Unit"],
            "answer": "A"
        },
        {
            "question": "Which language is used to create this program?",
            "options": ["A. Java",
                        "B. C++",
                        "C. Python",
                        "D. HTML"],
            "answer": "C"
        },
        {
            "question": "Which command is used to list files in Linux?",
            "options": ["A. cd",
                        "B. ls",
                        "C. pwd",
                        "D. mkdir"],
            "answer": "B"
        },
        {
            "question": "Which protocol is commonly used for secure remote access?",
            "options": ["A. FTP",
                        "B. HTTP",
                        "C. SSH",
                        "D. SMTP"],
            "answer": "C"
        },
        {
            "question": "How many bits are in an IPv4 address?",
            "options": ["A. 16",
                        "B. 32",
                        "C. 64",
                        "D. 128"],
            "answer": "B"
        }
    ]

    score = 0

    print("\n🧠 CYBERSECURITY BASICS QUIZ")
    print("-----------------------------")

    for number, question in enumerate(questions, start=1):
        print(f"\nQuestion {number}: {question['question']}")

        for option in question["options"]:
            print(option)

        user_answer = input("Your answer: ").upper()

        if user_answer == question["answer"]:
            print("Correct! ✅")
            score += 1
        else:
            print(f"Wrong! ❌ Correct answer: {question['answer']}")

    print("\n🎯 QUIZ COMPLETE!")
    print(f"Your score: {score}/{len(questions)}")

    percentage = (score / len(questions)) * 100
    print(f"Percentage: {percentage:.0f}%")

    if percentage == 100:
        print("Excellent! 🔥")
    elif percentage >= 60:
        print("Good job! 👍")
    else:
        print("Keep practicing! 💪")


run_quiz()
