students = ['태연', '성진', '민호', '유진', '동민']

student_dict = {"{}번".format(number + 1): name for number, name enumerate(students)}
print(student_dict)
