'''
def multiply(): #can have parameters here
    result=10.5*4
    return result
answer=multiply()  #can pass arguments  here
print(answer)
'''

#Palindrome

def is_palindrome(string):
 #   backwards=string[::-1]
  #  return backwards==string
    return string[::-1] == string

def palindrome_sentence(sentence):
    string=""
    for char in sentence:
        if char.isalnum():
            string +=char
    #return string[::-1].casefold()==string.casefold()
    return is_palindrome(string)

word=input("please enter Words:").casefold()
if is_palindrome(word):
    print(f"{word} is a plindrome")
else:
    print(f"{word} is not a plindrome")
sentence=input("please enter Sentence:")
if palindrome_sentence(sentence):
    print(f"{sentence} is a plindrome")
else:
    print(f"{sentence} is not a plindrome")



# Palindrome

