year = int(input("Введіть рік"))
if year>=1000000:
    print(year,"рік не відповідає умові")
elif year<=1900:
    print(year,"рік не відповідає умові")
elif year%400 == 0:
    print(year,"високосний рік")
else:
    print(year,"не високосний рік")
