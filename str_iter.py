#iterate through word and print backwards
word = "hello"

def rev(word):
   fin = []
   i = len(word)

   for x in word:
      fin.append(word[i-1])  #add to list
      i -= 1

   return("".join(fin))  #join list and print


print(rev(word))