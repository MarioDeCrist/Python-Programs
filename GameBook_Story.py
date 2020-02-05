# Lab 2 - Gamebook
# September 18, 2017
# Mario DeCristofaro
# MD2224
# CS-126L Sec-001

# Gamebook - Create a gamebook story that allows the user to playthrough
# end up at different endings
# Requirements - 1) There must at least be two decisions points for each path
# 2) One possible path where you have at least three or more decision points
# 3) At least one decision must have at least three consequences
# 4) At least one decision involves a numerical comparison

# Firstly, we set up the situation before asking the user for an input
# of how many times to hit your snooze button.

print("You are about ready to get up in the morning for")
print("class when your alarm rings.")
print(" ")
choice1 = int(input("How many times do you hit the snooze button:  "))

# This is our numerical choice for the user. They have four different paths
# to go down depending on the amount of times they hit the snooze button.
# We used a series of if, then statements to set the paths.
# Using a combination of If and Elif statements, we are able to send the user
# down different paths for different endings. 

# Choice1 == 0 leads to an instant gameover
if choice1 == 0:
        print(" ")
        print("No person could ever possibly wake up with only")
        print("one alarm.You sleep through class.")

# Choice1 == 1 leads to our first decision path with mutliple outcomes
elif choice1 == 1:
        print(" ")
        print("You wake up somewhat tired but begin to head to class.")
        print("However, you begin to contemplate. Should you SKIP your class.")
        choice4 = input("or GO to class: ")
# Second descision point for the first path
        if choice4 == 'SKIP':
                print(" ")
                print("What are you doing. You paid thousands of dollars for these")
                print("classes. Get your life together. Try again.")


        elif choice4 == 'GO':
                print(" ")
                print("You decide to go to class, but how should you get there.")
                choice2 = input("Do you WALK, RUN or BUS to your class?: ")
# Third decision point that can only be attained if answered the previous
# questions with the correct response
                if choice2 == 'RUN':
                    print(" ")
                    print("You made it to class but you are sweaty")
                    print("you classmates think you smell but at least your")
                    print("on time to class")

                elif choice2 == 'WALK':
                    print(" ")
                    print("You are 5 min late to class")
                    print("But you are not sweaty nor do you smell")

                elif choice2 == 'BUS':
                    print(" ")
                    print("Since you got up early, the bus is almost empty")
                    print("You made it to class on time and not sweaty")

# Choice1 == 2 leads to our second decsion path that the user will go through
# 3 different decison points depending on thier answers
elif choice1 == 2:
        print(" ")
        print("You lay in your bed think about life. This week has been long ")
        print("You begin to contemplate. Should you SKIP your class")
        choice5 = input("or GO to class: ")        

        if choice5 == 'SKIP':
                print(" ")
                print("What are you doing. You paid thousands of dollars for these")
                print("classes. Get your life together. Try again.")


        elif choice5 == 'GO':
                print(" ")
                print("You decide to go to class, but how should you get there.")
                choice3 = input("You are going to be late. Do you RUN or BUS?:")

                if choice3 == 'RUN':
                        print(" ")
                        print("You are really late and sweaty. The class and")
                        print("teacher hates you.")

                elif choice3 == 'BUS':
                        print(" ")
                        print("You get on very crowded bus and the person next to")
                        print("you is sick. You make it to class on time but you")
                        print("get the flu.")

# Choice1 >= 3 leads to another gameover path.
elif choice1 >= 3:
        print(" ")
        print("You try to make the bus because it is your only option")
        print("but you end up missing the bus as well. Class has ended")
        print("by the time that you get there. Wake up next time.")
