class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

# Define your questions here
questions = [
    Question("What is the capital of France?\n(a) London\n(b) Paris\n(c) Rome\n", "b"),
    Question("Who wrote 'Romeo and Juliet'?\n(a) William Shakespeare\n(b) Jane Austen\n(c) Charles Dickens\n", "a"),
    Question("What is the powerhouse of the cell?\n(a) Nucleus\n(b) Mitochondria\n(c) Ribosome\n", "b")
]

def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer.lower() == question.answer.lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
    print("You got", score, "out of", len(questions), "questions correct.")
    return score

def main():
    print("Welcome to the Quiz Game!")
    player_name = input("Please enter your name: ")
    print(f"Hello, {player_name}! Let's start the quiz.\n")

    total_score = run_quiz(questions)
    print(f"\nWell done, {player_name}! Your total score is {total_score} out of {len(questions)}.")

if __name__ == "__main__":
    main()
 