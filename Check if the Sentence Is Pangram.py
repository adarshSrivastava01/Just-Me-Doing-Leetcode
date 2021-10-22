def checkIfPangram(sentence):
    count_array = [0 for _ in range(26)]
    for each in sentence:
        count_array[ord(each)-97] += 1
    for each in count_array:
        if each == 0:
            return False
    return True


print(checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))
