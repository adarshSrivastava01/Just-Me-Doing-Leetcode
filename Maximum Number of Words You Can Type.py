def canBeTypedWords(text, brokenLetters):
    brokenLettersMap = {}
    for each in brokenLetters:
        if each in brokenLettersMap:
            brokenLettersMap[each] += 1
        else:
            brokenLettersMap[each] = 1
    broken_words = 0
    found_one = False
    for each in text:
        if each in brokenLettersMap:
            found_one = True
        elif each == " ":
            if found_one == True:
                broken_words += 1
            found_one = False
    print(len(text.split()) - broken_words)


canBeTypedWords("leet code", "lt")
