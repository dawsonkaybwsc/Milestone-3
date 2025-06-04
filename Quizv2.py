def country_quiz():
    questions = [
        {
            "question": "1. What is the longest river in the world?",
            "options": ["A. Amazon", "B. Nile", "C. Ganges", "D. Volga"],
            "answer": "B"
        },
        {
            "question": "2. What is the largest desert in the world?",
            "options": ["A. Kalahari", "B. Gobi", "C. Sahara", "D. Antarctica"],
            "answer": "D"
        },
        {
            "question": "3. Which country has the longest coast line?",
            "options": ["A. South Korea", "B. Canada", "C. Thailand", "D. Vietnam"],
            "answer": "B"
        },
        {
            "question": "4. What country has the smallest population?",
            "options": ["A. Vatican", "B. Nauru", "C. Tuvalu", "D. Palau"],
            "answer": "A"
        },
        {
            "question": "5. What is the name of the largest national park in Wales?",
            "options": ["A. Eryri", "B. Uryu", "C. Ihomi", "D. Erues"],
            "answer": "A"
        },
        {
            "question": "6. What is the name of the largest national park in Wales?",
            "options": ["A. Europe", "B. Africa", "C. Asia", "D. North America"],
            "answer": "C"
        }
    ]

    score = 0

    print(" Welcome to the Countries Quiz! \n")

    for q in questions:
        print(q["question"])
        for opt in q["options"]:
            print(opt)
        user_answer = input("Your answer (A,B,C,D): ").strip().upper()
        if user_answer == q["answer"]:
            print(" Correct!\n")
            score += 1
        else:
            print(f" Wrong! The correct answer was {q['answer']}.\n")

    print(f" You got {score} out of {len(questions)} correct!")

if __name__ == "__main__":
    country_quiz()