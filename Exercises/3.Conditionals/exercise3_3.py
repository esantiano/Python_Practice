for i in range(5):
    score = input("Enter score: ")
    try:
        score_float = float(score)
    except:
        print("Bad score")
        continue
    if score_float > 0.0 and score_float < 1.0:
        grade = ''
        if score_float >= 0.9:
            grade = 'A'
        elif score_float >= 0.8:
            grade = 'B'
        elif score_float > 0.7:
            grade = 'C'
        elif score_float >= 0.6:
            grade = 'D'
        elif score_float < 0.6:
            grade = 'F'
        print(grade)
    else:
        print("Bad score")