# Fungsi untuk menhitung nilai akhir dan grade nilai
def nilai_akhir(tugas, uts, uas):
    na = 0.25 * tugas + 0.35 * uts + 0.4 * uas
    return na

nilai_A = nilai_akhir(80,85,90)
nilai_B = nilai_akhir(75,70,80)

print("nilai_A",nilai_A)
print("nilai_B",nilai_B)

def htg_grade(tugas, uts, uas):
    na = nilai_akhir(tugas, uts, uas)
    grade = "E"
    if na >= 85:
        grade = "A"
    elif na >= 70:
        grade = "B"
    elif na >= 55:
        grade = "C"
    elif na >= 40:
        grade = "D"
    
    return grade

grade_upin = htg_grade (80, 85, 90)
grade_ipin = htg_grade (75, 70, 80)

print("grade nilai A adalah", grade_upin)
print("grade nilai B adalah", grade_ipin)