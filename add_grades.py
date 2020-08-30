import os
import subprocess

grade_str = "Problem 1 (leafy) : /10\n\n" \
            "Problem 2 (Mancala) : /10\n\n" \
            "part (a) : /5\n\n" \
            "part (b) : /1\n\n" \
            "part (c) : /4\n\n" \
            "Problem 3 (MAX-SAT) : /10 \n\n" \
            "part (a) I : /2 \n\n" \
            "part (a) II : /2\n\n" \
            "part (b) : /1\n\n" \
            "part (c) : /5 \n\n" \
            "Problem 4 (BSTs) : /10\n\n" \
            "part (a) : /3\n\n" \
            "part (b) : /3\n\n" \
            "part (c) : /4\n\n" \
            "Problem 5 (Comp-Geo) : /10\n\n" \
            "part (a) : /2\n\n" \
            "part (b) : /4\n\n" \
            "part (c) : /4\n\n" \
            "Problem 6 (Dijkstra : /16\n\n" \
            "Programming : /8\n\n" \
            "Theory : /8\n\n"
rt = '/home/mmcpartlon/student_assignments/final'
dirs = os.listdir(rt)
for student in dirs:
    pth = os.path.join(rt,student,'grades.txt')
    rm_pth = os.path.join(rt,student,'programming_grades.txt')
    if os.path.isdir(os.path.join(rt,student)):
        subprocess.call('rm '+rm_pth,shell=True)
        with open(pth,'w+') as f:
            f.write(grade_str)