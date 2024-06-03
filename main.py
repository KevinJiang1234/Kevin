score=0
# Ask the user their name and save it
name=input("What's your name?")
if name == "Mike":
    print("Gool")
    print("My name is Kevin")
print("Let's play a game")
# Greet the user and introduce the quiz
print("Welcome to this quiz.",name)
print("This quiz is about capital cities of the world.")
# Start the quiz
play = input("Do you want to play")
while play == "yes":
    # Ask the user a question   
    question = "What's the capital city of China."
    a = "Beijing"
    b = "Shanghai"
    c = "Nanjing"
    d = "Chengdu"
answer = input("{}\nA.{} B.{} C.{} D}".format(question, a, b, c, d)).lower()
if answer == "Beijing":
    print("Nice try,you are correct")
    score +=5
elif answer == "":
        print("Not sure?")
elif answer != b and answer != "b" and answer != c and answer != "c" and answer != d and answer != "d":
     print("That wasn't an option")
else:
    print("No,you are wrong")
    # Tell them the correct answer
    print("The correct answer is Beijing")
# End the quiz
print("That's the end.You got",score,"points")
print("Thank you",name)