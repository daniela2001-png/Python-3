#You are a student and you are trying to organize your subjects and grades using Python 
last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]
subjects = ["physics", "calculus", "poetry",
"history"]
subjects.append('computer science');
subjects.append('visual arts');
grades = [98, 97, 85, 88] 
grades.append(100);
grades.append(93);
gradebook = list(zip(subjects, grades));
print(gradebook)
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook);
