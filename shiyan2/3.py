def get_count(sentence):
    #l = len(sentence)
    count = 0
    for letters in sentence:
        if letters == "a":
            count+=1
        if letters == "e":
            count+=1
        if letters == "i":
            count+=1
        if letters == "o":
            count+=1
        if letters == "u":
            count+=1
    return count
get_count("y")