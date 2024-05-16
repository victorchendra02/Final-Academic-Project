def load_pkl(name: str):
    import pickle
    if len(name) == 0:
        raise ValueError("Filename cannot be empty")

    with open(name, 'rb') as file:
        return pickle.load(file)
    
def discretize(value):
    if 0 <= value <= 3:
        return "Easy"
    elif 3 < value <= 6:
        return "Medium"
    elif 6 < value <= 8:
        return "Hard"
    else:
        return "Very Hard"

def get_current_datetime():
    import datetime
    return datetime.datetime.now()

def get_current_date():
    from datetime import datetime
    return datetime.now().date()

# print(get_current_date().strftime('%Y%m%d'))