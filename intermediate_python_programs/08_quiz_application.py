questions = [
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. function", "B. def", "C. define", "D. fun"],
        "answer": "B",
    },
    {
        "question": "Which data type stores key-value pairs?",
        "options": ["A. List", "B. Tuple", "C. Dictionary", "D. Set"],
        "answer": "C",
    },
    {
        "question": "Which method adds an item to the end of a list?",
        "options": ["A. append()", "B. add()", "C. insert_end()", "D. push()"],
        "answer": "A",
    },
    {
        "question": "Which keyword handles exceptions in Python?",
        "options": ["A. check", "B. error", "C. catch", "D. except"],
        "answer": "D",
    },
    {
        "question": "Which module helps generate random numbers?",
        "options": ["A. math", "B. random", "C. numbers", "D. choice"],
        "answer": "B",
    },
    {
        "question": "What does len([10, 20, 30]) return?",
        "options": ["A. 2", "B. 10", "C. 3", "D. 30"],
        "answer": "C",
    },
    {
        "question": "Which file mode is used to append content?",
        "options": ["A. r", "B. w", "C. x", "D. a"],
        "answer": "D",
    },
    {
        "question": "Which data structure does not allow duplicate elements?",
        "options": ["A. List", "B. Set", "C. Tuple", "D. String"],
        "answer": "B",
    },
]


def run_quiz(question_list):
    score = 0
    total_questions = len(question_list)

    print("=" * 45)
    print("             PYTHON QUIZ")
    print("=" * 45)
    print(f"Total questions: {total_questions}")
    print("Enter A, B, C, or D to answer.")

    for number, question in enumerate(question_list, start=1):
        print(f"\nQuestion {number}/{total_questions}")
        print(question["question"])

        for option in question["options"]:
            print(option)

        while True:
            answer = input("Your answer: ").strip().upper()

            if answer in ("A", "B", "C", "D"):
                break

            print("Invalid choice! Enter A, B, C, or D.")

        if answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! Correct answer: {question['answer']}")

    return score


def display_result(score, total):
    percentage = (score / total * 100) if total else 0

    print("\n" + "=" * 45)
    print("              QUIZ RESULTS")
    print("=" * 45)
    print(f"Correct answers: {score}/{total}")
    print(f"Incorrect answers: {total - score}")
    print(f"Final percentage: {percentage:.2f}%")

    if percentage >= 80:
        print("Performance: Excellent!")
    elif percentage >= 60:
        print("Performance: Good job!")
    elif percentage >= 40:
        print("Performance: Keep practising!")
    else:
        print("Performance: Review the concepts and try again!")

    print("=" * 45)


def main():
    score = run_quiz(questions)
    display_result(score, len(questions))


if __name__ == "__main__":
    main()