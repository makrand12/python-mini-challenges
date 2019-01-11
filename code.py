# --------------
#Code starts here

#Function to check for palindrome
def palindrome_check(num):
  num=str(num)
  return (num[::-1]==num)

print(palindrome_check(123))

#Function to find the smallest palindrome
def palindrome(num):
    while(1):
        num=num+1
        if palindrome_check(num):
            return num
print(palindrome(123))
        
#Code ends here        


# --------------
#Code starts here

#Function to find anagram of one word in another

def a_scramble(str_1,str_2):
    result=True
    for i in (str_2.lower()):
        if i not in (str_1.lower()):
            result=False
            break
        str_1=str_1.replace(i,'',1) #Removing the letters from str_1 that are already checked
    
    return (result)
a_scramble("ticket","chat")

#Code ends here


# --------------
#Code starts here
def check_fib(num):
    num1 = 1
    num2 = 1
    while True:
        if num2 <= num:
            if num2 == num:
                return True
            else:
                tempnum = num2
                num2 += num1
                num1 = tempnum
        else:
            return False

check_fib(145)



# --------------
#Code starts here

#Function to compress string
def compress(word):
    word=word.lower()
    mist=[]
    l=0
    while(l<len(word)):
        m=word[l]
        j=0
        while(l<len(word) and word[l]==m):
                 j=j+1
                 l=l+1    

        mist.append(m)
        mist.append(str(j))
    
    return ''.join(mist)

#Code ends here


# --------------
#Code starts here
def k_distinct(string,k):
    a = set(string.lower())
    print(a)
    if len(a) == k:
        return True
    else:
        return False
k_distinct('banana',4)


