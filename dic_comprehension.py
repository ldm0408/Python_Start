students = ['태연', '성진', '민호', '유진', '동민']
for number, name in enumerate(students):
    print('{}번 {}이다'.format(number, name))


student_dict = {"{}번".format(number + 1): name for number, name in enumerate(students)}
print(student_dict)

scores = ['80','90','78','100','86']

for x,y in zip(students, scores):
    print(x,y)

scores_dict = {student : score for student, score in zip(students,scores)}
print(scores_dict)

