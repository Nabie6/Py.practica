"""
card_num=(input("ведите номер карты: "))
i=16
b="*"

if len(card_num)==i and card_num.isdigit():
    print(b*12 +card_num[-4:])
else:
    print("Invalid card number")

"""
words = ["banana", "apple", "cherry", "grape"] 
letter = "a"
for x in words:
    if x.count(letter)>=2:
     print(x)
    else:
        print("no word fouded")