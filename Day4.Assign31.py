def check_palindrome(str):
    
    #Remove pass and write your logic here
     str_len=len(str)
     counter=0
     for i in range(len(str)):
         if (str[i]==str[-i-1]):
            counter+=1
     if(counter==str_len):
         return True
     else:
         return False

status=check_palindrome("madam")
if(status):
    print("word is palindrome")
else:
    print("word is not palindrome")
