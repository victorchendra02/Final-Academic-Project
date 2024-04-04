def discretize(value):
    if 0 <= value <= 3:
        return "Easy"
    elif 3 < value <= 6:
        return "Medium"
    elif 6 < value <= 8:
        return "Hard"
    else:
        return "Very Hard"
