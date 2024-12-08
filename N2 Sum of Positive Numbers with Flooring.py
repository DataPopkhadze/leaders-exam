# Challenge:
#  Create a function that takes a list of numbers, including fractions, and returns the sum of all positive numbers, floored to the nearest integer.

import math

def sum_of_positive_numbers(nums):
    positive_sum = 0

    for num in nums:
        if num > 0:
            positive_sum += num
        
    floored_sum = math.floor(positive_sum)
    
    print(floored_sum)

sum_of_positive_numbers([-1.5, 2.7, -3.3, 4.8])

# პირველ რიგში ვქმნით ცვლადს სადაც შევიახავთ ყველა დადებით რიცხვს, შემდეგ ვუვლით ფორ ლუპით სიის ყველა ელემენტს და ვნახულობთ ის დადებითია თუ არა if-ის გამოყენებით და თუ მეტია ნულზე მაშინ დაემატოს დადებითი რიცხვი მთლიანი რიცხვების ჯამს. შემდეგ მას ვამრგვალებთ MATH.FLOOR ის გამოყენებით და ვპრინტავთ დამრგვალებულ ჯამს.