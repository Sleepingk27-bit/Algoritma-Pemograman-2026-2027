tugas = float(input("input nilai Tugas: "))
uts = float(input("input nilai UTS: "))
uas = float(input("input nilai UAS: "))

nilai = (0.15 * tugas) + (0.35 * uts) + (0.5 * uas)

if nilai >80:
    grade = "A"
elif nilai >70:
    grade = "B"
elif nilai >60:
    grade = "C"
elif nilai >50:
    grade = "D"
else:
    grade = "E"

if nilai >60:
    status = 'lulus'
else:
    status = 'tidak lulus'

print('Nilai Akhir: %0.2f' % nilai)
print('Grade: {}'.format(grade))
print('Status: {}'.format(status))
