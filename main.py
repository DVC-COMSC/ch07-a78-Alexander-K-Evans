
words = input('Enter the list: ').split()

are = ['a', 'r', 'e']
idxlst = []

for i in range(len(words)):
    flagA = False
    flagR = False
    FlagE = False
    if 'a' in words[i]:
        flagA = True
    if 'r' in words[i]:
        flagR = True
    if 'e' in words[i]:
        flagE = True

    if flagA and flagR and flagE:
        idxlst.append(words[i])      

# print the words that has 'a', 'r', 'e' in sequence

print (idxlst)