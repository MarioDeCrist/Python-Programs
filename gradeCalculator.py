# Mario DeCristofaro
# md2224
# 10/2/17
# Section 1
# Lab 4

# program that generates grades based on weights, from different arrays


# main function recursing many function created below
def main():
    hwmax = [40, 40, 40, 40, 40, 5]
    hwearned = [39, 40, 29, 40, 0, 5]
    qmax = [10, 10, 10, 10, 10, 10, 10]
    qearned = [10, 10, 9, 2, 10, 10, 10]
    tmax = [300, 300, 300]
    tearned = [293, 284, 300]
    hweight = .2
    qweight = .2
    tweight = .6
    quizpercent = average_list(qearned, qmax)
    hwpercent = average_list(hwearned, hwmax)
    tpercent = average_list(tearned, tmax)
    home_work_letter_grade = letter_grade(hwpercent)
    quiz_letter_grade = letter_grade(quizpercent)
    test_letter_grade = letter_grade(tpercent)
    hweightedgrade = weighted_grade(hwearned, hwmax, hweight)
    qzweightedgrade = weighted_grade(qearned, qmax, qweight)
    tweightedgrade = weighted_grade(tearned, tmax, tweight)
    finalgrade = hweightedgrade + qzweightedgrade + tweightedgrade
    finaletter = letter_grade(finalgrade)
    # prints the end product of all the functions
    print(" Final HW grade ", hwpercent, home_work_letter_grade)
    print(" Final Quiz grade ", quizpercent, home_work_letter_grade)
    print(" Final Test grade ", tpercent, test_letter_grade)


def average_list(score_list, max_list):
    # creates a averaging function
    scoresum = sum(score_list)
    maxsum = sum(max_list)
    grade = round(scoresum / maxsum, 2)
    grade = (grade * 100)
    return grade
    print(grade)
# creates a grading functino
# and prints the resulting grade


def letter_grade(percent):
    if percent >= 90:
        return percent, " A"
    elif percent >= 80 and percent <= 90:
        return percent, " B"
    elif percent >= 70 and percent <= 80:
        return percent, " C"
    elif percent >= 60 and percent <= 70:
        return percent, " D"
    elif percent >= 50 and percent <= 60:
        return percent, " F"


def weighted_grade(score_list, max_list, weight):
    average_list = round(sum(score_list) / sum(max_list), 2)
    weighted_grade = ((average_list * 100 // 1) * weight) // 1
    return weighted_grade
    #  calculates the weights of grades and sets accoridingly
main()
