def calculate_score(word_list):
    count = 0
    for x in word_list:
        x_length = len(x.strip())
        if(x_length < 3):
            continue
        else:
            count = count + (x_length - 2)
    return count