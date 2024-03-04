import random

def quiz_game(questions):
    score = 0
    random.shuffle(questions)
    for x,(question, options, answer) in enumerate(questions,1):
        print(f'{x}) {question}')
        random.shuffle(options)
        for i, option in enumerate(options,1):
            print(f"   {i}. {option}")

        while True:
            user_answer = input("Enter your answer (1, 2, 3, or 4) : ")
            if user_answer.isdigit() and 1 <= int(user_answer) <= 4:
                user_answer = int(user_answer)
                break
            else:
                print("Invalid input. Please enter a number between 1 and 4.")

        if options[user_answer-1] == answer:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
        if len(questions) > x:
            quit = input("'Yes or y ' Quit the game / Any key to continue :").lower()
            if quit == "yes" or quit == "y":
                print(f"You got {score} out of {len(questions)} questions correct.")
                exit()
    print(f"You got {score} out of {len(questions)} questions correct.")

questions = [
    ("Who is known as the 'Master Blaster' in cricket?",
     ["Sachin Tendulkar", "Virat Kohli", "Ricky Ponting", "Brian Lara"],
     "Sachin Tendulkar"),

    ("Which country won the ICC Cricket World Cup in 2023?",
     ["England", "Australia", "India", "New Zealand"],
     "Australia"),

    ("Which team won IPL 2023?",
     ["Chennai Super Kings", "Mumbai Indians", "Royal Challengers Bangalore", "Kolkata Knight Riders"],
     "Chennai Super Kings"),

    ("What does LBW stand for in cricket?",
     ["Leg Before Wicket", "Long Boundary Wide", "Last Ball Wicket", "Leg Break Wicket"],
     "Leg Before Wicket"),

    ("Who is the leading run-scorer in Test cricket?",
     ["Sachin Tendulkar", "Ricky Ponting", "Steve Smith", "Jacques Kallis"],
     "Sachin Tendulkar"),

    ("Which bowler has taken the most wickets in international cricket?",
     ["Muttiah Muralitharan", "Shane Warne", "Anil Kumble", "James Anderson"],
     "Muttiah Muralitharan")
]

quiz_game(questions)
