salary=float(input("your salary: "))
rating=0
if salary>=50000 :
    rating=float(input("your credit ranking: "))
    if rating>700:
     print("Кредит одобрен с низким процентом")
    else:
     print("Кредит одобрен. Но с высоким процентом")

elif salary<50000 :
    rating=float(input("your credit ranking: "))
    if rating>700:
     print("Кредит одобрен с жестким процентом")
    else:
     print("Кредит отклонен. Зп маленькая и рейтинг низкий.")
else :
  print("Error")

