import os
import subprocess
rt = '/home/mmcpartlon/student_assignments/final'
test_pth = os.path.join(rt,'final-zhaijunjay','test.py')
ds_pth = os.path.join(rt,'final-zhaijunjay','datastructures')
dg_pth = os.path.join(rt,'final-zhaijunjay','DataGenerator.py')
dirs = os.listdir(rt)
for student in dirs:
    student_test_pth = os.path.join(rt,student,'programming_test.py')
    student_pth = os.path.join(rt, student)
    #rm_pth = os.path.join(rt,student,'programming_grades.txt')
    if os.path.isdir(os.path.join(rt,student)):

        #subprocess.call('rm '+rm_pth,shell=True)
        subprocess.call('cp '+test_pth+' '+student_test_pth,shell=True)
        subprocess.call('cp ' + dg_pth + ' ' + student_pth, shell=True)
        subprocess.call('cp -r ' + ds_pth + ' ' + student_pth, shell=True)

        print('cp '+test_pth+' '+student_test_pth)
        print('cp ' + dg_pth + ' ' + student_pth)
        print('cp -r ' + ds_pth + ' ' + student_pth)
