questions = [
    ["Who is Shah Rukh Khan?", "WWE Wrestler", "Actor", "Astronaut", "Plumber",2],
    ["What is the capital of France?", "Rome", "Paris", "London", "Berlin", 2],
    ["What Planet is known as Red Planet?", "Earth", "Jupiter", "Mars", "Venus", 3],
    ["What is the largest mammal?", "Elephant", "Blue Whale", "Giraffe", "Shark", 2],
    ["Who wrote 'Romeo and Juliet'?", "Charles Dickens", "William Shakespeare", "Jane Austen", "Homer", 2],
    ["What is the square root of 64?", "6", "8", "10", "12", 2],
    ["Which country is known as the Land of the Rising Sun?", "China", "Japan", "South Korea", "India", 2],
    ["Who painted the Mona Lisa?", "Vincent van Gogh", "Pablo picasso", "Leonardo da Vinci", "Claude Monet", 3],
    ["What is the fastest land animal?", "Cheetah", "Lion", "Elephant", "Horse", 1],
    ["Which ocean is the largest?", "Atlantic ocean", "Indian ocean", "Arctic ocean", "Pacific ocean", 4],
]

prizes = [100000, 320000, 400000, 450000, 500000, 1000000, 2000000, 3000000, 4000000, 5000000]
sum = 0
i = 0

for question in questions:
    
    print(question[0])
    print(f"1. {question[1]}")
    print(f"2. {question[2]}")
    print(f"3. {question[3]}")
    print(f"4. {question[4]}")

    #Check weather the answer is correct or not
    a = int(input("Enter Your answer: "))
    if (question[5]==a):
        print(f"\nYou won {prizes[i]} for the correct Answer")
    else:
        print(f"Incorrect, the correct answer was {question[5]}")
        print("Better luck next time!")
        break

    sum += prizes[i]
    print(f"You total amount till now is {sum}\n")
    i +=1