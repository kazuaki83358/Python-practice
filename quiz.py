print("ready for quiz")

list_of_question = [
    "What is the capital of Japan?",
    "Who is the founder of ChatGPT?",
    "Who is the president of USA?",
    "Who is the founder of Facebook?"
]

options = [
    {"a": "Tokyo", "b": "Osaka", "c": "Beijing", "d": "Seoul"},
    {"a": "Sam Altman", "b": "Elon Musk", "c": "Bill Gates", "d": "Larry Page"},
    {"a": "Donald Trump", "b": "Joe Biden", "c": "Barack Obama", "d": "Kamala Harris"},
    {"a": "Mark Zuckerberg", "b": "Steve Jobs", "c": "Jeff Bezos", "d": "Jack Ma"}
]

correct_answers = ["a", "a", "b", "a"]

score = 0

print("\ntype a for option a, type b for option b, type c for option c, type d for option d")

for i in range(len(list_of_question)):
    print("\n" + list_of_question[i])

    for key,value in options[i].items():
        print(f"{key} {value}")

    ans = input("Your answer: ").lower()

    if ans == correct_answers[i]:
        print("answer is correct")
        score += 1
    else:
        print(f"Wrong! Correct answer is ({correct_answers[i]}) {options[i][correct_answers[i]]}")

print(f"\nyou score is {score}")

