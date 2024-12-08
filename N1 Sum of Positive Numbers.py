# Challenge:
#  Create a function that takes a list of numbers and returns the sum of all positive number

def sum_of_all_positives(nums):
    positive_sum = 0

    for num in nums:
        if num > 0:
            positive_sum += num
        
    print(positive_sum)

sum_of_all_positives([1, -4, 7, 12])

# პირველ რიგში ვქმნით ცვლადს სადაც შევიახავთ ყველა დადებით რიცხვს, შემდეგ ვუვლით ფორ ლუპით სიის ყველა ელემენტს და ვნახულობთ ის დადებითია თუ არა if-ის გამოყენებით და თუ მეტია ნულზე მაშინ დაემატოს დადებითი რიცხვი მთლიანი რიცხვების ჯამს.