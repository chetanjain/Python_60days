today = input("Enter today;s date : ")
mood = input("How are you feeling today rate from 1 to 10 :")
thought = input("Let your thoughts flow: ")

file_name = f"journal\{today}.txt"
with open(file_name, 'w') as file:
    file.write(mood + "\n")
    file.write(thought + "\n")
