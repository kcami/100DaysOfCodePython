# Dia 5 - 100DaysOfCodeChallenge
# Average Height

student_heights = input("Input a list of student heights separeted by whitespaces: ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)
average_height = 0
for height in student_heights:
    average_height += height
average_height = round(average_height / len(student_heights))
print(f"The average height is {average_height}")