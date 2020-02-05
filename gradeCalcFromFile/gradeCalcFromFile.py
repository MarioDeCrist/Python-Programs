# lab 8 - Grade calculator 2
# Mario DeCristofaro
# md2224
# 11-6-17
# lab section - 1


# reads grade data from a text file and exports it to a HTML file

def read_grade_data(filehandle):
    # creates dictionary to store data from the input file
    grades_dict = {}
    for line in filehandle:
        # goes through the list until all lines have been read
        score_list = []
        # creates an empty list to store the numerator of the scores
        max_list = []
        # creats an empty list to store the denominator of the scores
        line = (line.strip())
        # removes the spaces at the beginning and end of each line
        split_at_percent = line.split("%")
        # splits the string at the percent sign
        list_name = split_at_percent[0].split(" ")
        # splits the first element of new list at the space to get the
        # name of the category
        grade = split_at_percent[1].split(",")
        # separates each grade from each other and puts it into a list
        for i in range(len(grade)):
            # iterates through all the grades in the grades list
            grades_without_spaces = grade[i].strip()
            # removes all the spaces at the beginning and end of each element
            # in the grades list
            temp_score = grades_without_spaces.split("/")
            # splits the grades at /, separating the numerator and denominator
            # of the scores
            score_list.append(int(temp_score[0]))
            # adds the numerators to score list
            max_list.append(int(temp_score[1]))
            # adds the denominators to max list
        grades_dict[list_name[0]] = [list_name[1], score_list, max_list]
        # assigns the percentage, score list, and max list of each category
        # to the grade dictionary with the category name as the key
    return grades_dict


def average(score_list, max_list):
    # finds average and turns it into a decimal and returns that value
    percent = (sum(score_list) / sum(max_list))
    return percent


def letter_grade(percent):
    # determines the letter grade and returns the value
    if percent >= 0.9:
        return "A"
    elif percent >= 0.8 and percent < 0.9:
        return "B"
    elif percent >= 0.7 and percent < 0.8:
        return "C"
    elif percent >= 0.6 and percent < 0.7:
        return "D"
    else:
        return "F"


def average_weighted(score_list, max_list, weight):
    # will print the percentage and the letter grade and return the value
    # weighted
    percent = average(score_list, max_list)
    actual_percent = round((percent * 100), 0)
    # print(actual_percent, (letter_grade(percent)))
    weighted_percent = (actual_percent * weight)
    return weighted_percent


def generate_data():
    grades = open('lab8input.txt', 'r')
    # opens the input file
    grades_dict = read_grade_data(grades)
    # assigns the returned list to grades_dict

    homework_score = grades_dict["Homework"][1]
    # element 1 in the dictionary under the key, homework is the numerator
    # of the scores
    homework_max = grades_dict["Homework"][2]
    # element 2 in the dictionary is the denominator of the scores
    homework_percentage = grades_dict["Homework"][0]
    # the first element is the percentage
    homework_percentage = float(homework_percentage)/100
    # divides by 100 to get a decimal

    quiz_score = grades_dict["Quizzes"][1]
    quiz_max = grades_dict["Quizzes"][2]
    quiz_percentage = grades_dict["Quizzes"][0]
    quiz_percentage = float(quiz_percentage) / 100

    test_score = grades_dict["Tests"][1]
    test_max = grades_dict["Tests"][2]
    test_percentage = grades_dict["Tests"][0]
    test_percentage = float(test_percentage) / 100

    project_score = grades_dict["Projects"][1]
    project_max = grades_dict["Projects"][2]
    project_percentage = grades_dict["Projects"][0]
    project_percentage = float(project_percentage) / 100

    final_score = grades_dict["Final"][1]
    final_max = grades_dict["Final"][2]
    final_percentage = grades_dict["Final"][0]
    final_percentage = float(final_percentage) / 100

    # stores the data in a dictionary
    data = {}

    # prints all grades and the final score
    # print("Homework grade ")
    homework_grade = (average_weighted(homework_score, homework_max,
                                       homework_percentage))
    # print("Quiz grade ")
    quiz_grade = (average_weighted(quiz_score, quiz_max, quiz_percentage))
    # print("Test grade ")
    test_grade = (average_weighted(test_score, test_max, test_percentage))
    # print("Project grade ")
    project_grade = (average_weighted(project_score, project_max,
                                      project_percentage))
    # print("Final test grade ")
    final_test_grade = (average_weighted(final_score, final_max,
                                         final_percentage))

    # total = homework_grade + quiz_grade + test_grade + project_grade +
    # final_test_grade

    # print("Final Score: ", round(total, 0), letter_grade(total/100))

    # stores the data in a new dictionary to be used in the write_grade_report
    # function
    percent = average(homework_score, homework_max)
    homework_percent = round((percent * 100), 0)
    homework_letter = letter_grade(percent)
    data["homework"] = [homework_percentage, homework_percent,
                        homework_letter, homework_grade]

    percent = average(quiz_score, quiz_max)
    quiz_percent = round((percent * 100), 0)
    quiz_letter = letter_grade(percent)
    data["quiz"] = [quiz_percentage, quiz_percent, quiz_letter, quiz_grade]

    percent = average(test_score, test_max)
    test_percent = round((percent * 100), 0)
    test_letter = letter_grade(percent)
    data["test"] = [test_percentage, test_percent, test_letter, test_grade]

    percent = average(project_score, project_max)
    project_percent = round((percent * 100), 0)
    project_letter = letter_grade(percent)
    data["project"] = [project_percentage, project_percent,
                       project_letter, project_grade]

    percent = average(final_score, final_max)
    final_percent = round((percent * 100), 0)
    final_letter = letter_grade(percent)
    data["final"] = [final_percentage, final_percent, final_letter,
                     final_test_grade]

    return data


def write_grade_report(filehandle, data):
    # writes the data to a html file
    output = open(filehandle, "w")
    output.write("<html>\n")
    output.write("<body>\n")
    # calculates the total score
    total = data["homework"][3] + data["quiz"][3] + data["test"][3] + \
        data["project"][3] + data["final"][3]
    # rounds the total score
    total = round(total, 0)
    # finds what letter grade the total score is
    final_letter = (letter_grade(total/100))

    for key in data:
        # writes the data for each key to the html file
        category = key
        percentage = str(data[key][0])
        grade = str(data[key][1])
        letter = str(data[key][2])
        weight = str(round(data[key][3], 3))

        # formats the html file and writes the data
        output.write("<h1>" + category + " (" + percentage + ")" + "</h1>\n")
        output.write("<ul>")
        output.write("<li><b>" + "average: </b>" + grade + "</li>\n")
        output.write("<li><b>" + "letter grade: </b>" + letter + "</li>\n")
        output.write("<li><b>" + "grade contribution: </b>" + weight +
                     "</li>\n")
        output.write("</ul>\n")

    # writes the cumulative grade to the file
    output.write("<h1>" + "cumulative grade" + "</h1>\n")
    output.write("<ul>")
    output.write("<li><b>" + "average: " + str(total) + "</b></li>\n")
    output.write("<li><b>" + "letter grade: " + final_letter + "</b></li>")
    output.write("</ul>")
    output.write("</body></html>")


def main():
    data = generate_data()
    write_grade_report("output.html", data)

main()
