string = input("Enter the line")

charcount = 0
wordcount = 1
 
for i in string:
    charcount = charcount + 1
    if i == ' ':
        wordcount = wordcount + 1

print(charcount)
print(wordcount)
    

   