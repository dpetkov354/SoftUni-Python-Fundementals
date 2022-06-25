import math
total_students = int(input())
lectures_count = int(input())
additional_bonus = int(input())
attendances = []
after_bonus_score = []

if total_students > 0:
    for s in range(total_students):
        current_attendance = int(input())
        attendances.append(current_attendance)
        total_bonus = current_attendance / lectures_count * (5 + additional_bonus)
        after_bonus_score.append(total_bonus)

        max_score = max(after_bonus_score)
        max_score_index = after_bonus_score.index(max_score)
        student_with_max_score = attendances[max_score_index]

else:
    max_score = 0
    student_with_max_score = 0

print(f"Max Bonus: {math.ceil(max_score)}.\nThe student has attended {student_with_max_score} lectures.")
