string = 'hola'
string2 = 'aeiou'

def reverser_vocales(word):
    word = list(word)
    newlist = []
    vocales = 'aeiouy'
    for i in word:
        if i in vocales:
            newlist.append(i)
    newlist.reverse()
    j = 0
    for i in range(len(word)):
        if word[i] in vocales:
            word[i] = newlist[j]
            j += 1
    word = "".join(word)
    return word
    
print(string)
print(reverser_vocales(string))
print(string2)
print(reverser_vocales(string2))