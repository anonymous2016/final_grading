import os
import subprocess
rt = '/home/mmcpartlon/student_assignments/final'
dirs = os.listdir(rt)
for student in dirs:
    pth = os.path.join(rt,student,'grades.txt')
    rm_pth = os.path.join(rt,student,'programming_grades.txt')
    if os.path.isdir(os.path.join(rt,student)):
        subprocess.call('rm '+rm_pth,shell=True)
        with open(pth,'w+') as f:
            