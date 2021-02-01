##
## TODO 
## fix box
##

name = raw_input('Enter file: ')
handle = open(name)

counts = dict() 
for line in handle:
    word = line.split() 
    for word in words:
        counts(word) = counts.get(word, 0) + 1


bigncount = None
bigword = None
for word, count in counts.items(): 
    if bigcount is None or count > bigncount:
        bigword = word
        bigcount = count
        
print(bigword, bigcount)

