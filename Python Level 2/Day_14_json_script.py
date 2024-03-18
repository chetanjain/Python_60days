import json

with open("Day_14_json_data.json", "r") as file:
    content = file.read()

data = json.loads(content)

# print(data)
score = 0
for question in data:
    print(question['question_text'])
    for i, options in enumerate(question['alternatives']):
        print(i + 1, options)

    answer = int(input("Enter your correct option : "))
    question["user_choice"] = answer
    if question["user_choice"] == question['correct_answer']:
        score = score + 1

for question in data:
    message = f"your answer: {question['user_choice']} , "\
              f"Correct answer: {question['correct_answer']}"
    print(message)

# print(data)
print(score, "/", len(data))
