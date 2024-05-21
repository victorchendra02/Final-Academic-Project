def append_training_result(csv_file_name:str, string: str):
    newline = False
    with open(csv_file_name, 'r') as f1:
        f1_list = f1.readlines()
    if f1_list[-1][-1] != "\n": newline = True
    
    with open(csv_file_name, 'a') as f2:
        if newline is True:
            f2.write("\n")
    
        f2.write(string)
    