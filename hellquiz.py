import time

def ask_question(question, correct_answer):
    user_answer = input(question + " ")
    if user_answer.lower() == correct_answer.lower():
        return True
    else:
        print("Incorrect")
        return False

questions = [
    ("What is the capital of France?", "Paris"),
    ("Which planet is known as the Red Planet?", "Mars"),
    ("What's the largest mammal?", "Blue Whale"),
    ("In which year did World War I begin?", "1914"),
    ("Who painted the Mona Lisa?", "Leonardo da Vinci"),
    ("What's the symbol for the chemical element oxygen?", "O"),
    ("How many continents are there?", "7"),
    ("Which gas do plants absorb from the atmosphere?", "Carbon dioxide"),
    ("What's the largest organ in the human body?", "Skin"),
    ("What's the tallest mountain in the world?", "Mount Everest")
]

start_time = time.time()
score = 0

for question, answer in questions:
    if ask_question(question, answer):
        score += 1

end_time = time.time()
time_taken = end_time - start_time

print("Quiz completed! You got", score, "out of", len(questions), "questions correct.")
print("Time taken:", round(time_taken, 2), "seconds")
print("Correct:", score)
print("Incorrect:", len(questions) - score)
