
# my_str = "hello world"
# vowels="aeiouAEIOU"

# final = [each for each in my_str if each in vowels]
# print(len(final))
# print(final)

palindrome =input("Enter String :")
for i in range(0, int(len(palindrome)/2)):
        if palindrome[i] != palindrome[len(palindrome)-i-1]:
            print("NO")

        else:
              print("YES")


        
            
    