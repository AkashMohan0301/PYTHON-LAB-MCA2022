#9-Create a string from input string where first and last word exchanged ??
word = input("Enter the string")
word_new = word[-1]+word[1:-2]+word[0]
print(word)
print(word_new)
