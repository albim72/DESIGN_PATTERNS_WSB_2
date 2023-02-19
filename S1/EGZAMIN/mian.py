from homework import Homework
from exam import Exam
from grade import ExamD


print("__________HOMEWORK___________")
st1 = Homework()
st1.grade = 96
print(st1.grade)
assert st1.grade == 96

print("__________EXAM___________")

st2 = Exam()
st2.writing_grade = 90
st2.math_grade = 76

print(st2.writing_grade)
print(st2.math_grade)

print("__________EXAMD___________")

st3_1 = ExamD()
st3_1.math_grade = 34
st3_1.writing_grade = 23

print(f"pierwsze podejście: {st3_1.math_grade}")
print(f"pierwsze podejście: {st3_1.writing_grade}")

st3_2 = ExamD()
st3_2.math_grade = 60
st3_2.writing_grade = 75

print(f"drugie podejście: {st3_2.math_grade}")
print(f"drugie podejście: {st3_2.writing_grade}")

print("ponowne wyśwetlenie podejścia 1:")

print(f"pierwsze podejście: {st3_1.math_grade}")
print(f"pierwsze podejście: {st3_1.writing_grade}")
