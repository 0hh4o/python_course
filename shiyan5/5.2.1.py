def spin_words(sentence):
    words = sentence.split(' ')
    rsentence = []
    for word in words:
        if len(word) >= 5:
            rword = word[::-1]
            rsentence.append(rword)
        else:
            rsentence.append(word)
    print(rsentence)
    return (' '.join(rsentence))
print(spin_words('Hey fellow warriors'))