# Challenge:
#  Write a function to check if two strings are anagrams (contain the same characters in the same frequency).

# Test Cases:
# assert are_anagrams("listen", "silent") == True
# assert are_anagrams("hello", "world") == False
# assert are_anagrams("triangle", "integral") == True

from collections import Counter

def are_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    print(Counter(str1) == Counter(str2))

are_anagrams("listen", "silent")

#Counter ითვლის სიმბოლოებს ან ელემენტებს, მაქამდე რამე გამოტოვებულ ადგილს ვცვლი და ვაერთებ ერთ სიტყვად აი მაგალითად HELLO WORLD  რო ეწეროს გახდება helloworld ორივე სტრინზე და შემდეგ ვპრინტავთ