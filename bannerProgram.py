# Lab 6
# Mario DeCristofaro
# md2224
# 10-16-17
# Section 1

'''We defined a main function where we could store our user input and
run our function'''

# program prints a banner a word you input and print it either horizontally or vertically

def main():
    word = (input("Enter a word: ")).upper()
    word = str(word)
    orientation = input("Enter vertical or horizontal (v/h): ")
    orientation = str(orientation)
    print_banner(word, orientation)

'''We defined the function that would actually create our word art.
We saved how each letter would be printed out in a dictionary.
We wrote code for how we would tell if the art needed to be oriented'''


def print_banner(word, orientation):
    letters = {"A": ["  #  ",
                     " # # ",
                     " ### ",
                     " # # ",
                     " # # "],
               "B": ["#####",
                     "#   #",
                     "#### ",
                     "#   #",
                     "#####"],
               "C": ["#####",
                     "#    ",
                     "#    ",
                     "#    ",
                     "#####"],
               "D": ["#### ",
                     "#   #",
                     "#   #",
                     "#   #",
                     "#### "],
               "E": ["#####",
                     "#    ",
                     "#### ",
                     "#    ",
                     "#####"],
               "F": ["#####",
                     "#    ",
                     "###  ",
                     "#    ",
                     "#    "],
               "G": ["#####",
                     "#    ",
                     "#  ##",
                     "#   #",
                     "#####"],
               "H": ["#   #",
                     "#   #",
                     "#####",
                     "#   #",
                     "#   #"],
               "I": ["#####",
                     "  #  ",
                     "  #  ",
                     "  #  ",
                     "#####"],
               "J": ["#####",
                     "  #  ",
                     "  #  ",
                     "# #  ",
                     "###  "],
               "K": ["#   #",
                     "#  # ",
                     "# #  ",
                     "#  # ",
                     "#   #"],
               "L": ["#    ",
                     "#    ",
                     "#    ",
                     "#    ",
                     "#####"],
               "M": ["#   #",
                     "## ##",
                     "# # #",
                     "#   #",
                     "#   #"],
               "N": ["#   #",
                     "##  #",
                     "# # #",
                     "#  ##",
                     "#   #"],
               "O": ["#####",
                     "#    ",
                     "#    ",
                     "#    ",
                     "#####"],
               "P": ["#####",
                     "#   #",
                     "#####",
                     "#    ",
                     "#    "],
               "Q": ["#####",
                     "#   #",
                     "#   #",
                     "#####",
                     "    #"],
               "R": ["#####",
                     "#   #",
                     "#### ",
                     "#  # ",
                     "#   #"],
               "S": ["#####",
                     "#    ",
                     "#####",
                     "    #",
                     "#####"],
               "T": ["#####",
                     "  #  ",
                     "  #  ",
                     "  #  ",
                     "  #  "],
               "U": ["#   #",
                     "#   #",
                     "#   #",
                     "#   #",
                     "#####"],
               "V": ["#   #",
                     "#   #",
                     "#   #",
                     " # # ",
                     "  #  "],
               "W": ["#   #",
                     "#   #",
                     "# # #",
                     "## ##",
                     "#   #"],
               "X": ["#   #",
                     " # # ",
                     "  #  ",
                     " # # ",
                     "#   #"],
               "Y": ["#   #",
                     " # # ",
                     "  #  ",
                     "  #  ",
                     "  #  "],
               "Z": ["#####",
                     "   # ",
                     "  #  ",
                     " #   ",
                     "#####"]}
    if orientation == "h":
        for i in range(5):
            for letter in word:
                print(letters[letter][i], end=" ")
            print()
    else:
        for letter in word:
            for i in range(5):
                print(letters[letter][i])
            print()
# We then ran our main function to execute.
main()
