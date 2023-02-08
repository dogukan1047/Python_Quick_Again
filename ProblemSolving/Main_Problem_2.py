#ilk 10.000 asal sayının kaç tanesi 3 ile başlar 7 ile biter ?

prime_list=list()

prime_list.append(2)

sayi=3

while True:
    prime=True
    for i in range(2,sayi):
        if sayi % i==0:
            prime=False
            break

    if prime:
        prime_list.append(sayi)
        if len(prime_list) ==100:
            break
    sayi+=1
prime_list2=list()

for number in prime_list:
    if number % 10 ==7:
        newNUmber=str(number)
        if newNUmber.startswith('3'):
            prime_list2.append(number)


print(prime_list2)


## 3 basamaklı sayıların  kaç tanesi rakamlarının küpelerinin toplamına eşittir


count=0
myList=list()
for k in range(100,1000):

    birlerBasamağı= k %10
    onlarBasamağı=(k // 10)%10
    yuzlerBasamağı=int((k // 10)/10)

    birlerBasamağı=(birlerBasamağı**3)
    onlarBasamağı=(onlarBasamağı**3)
    yuzlerBasamağı=(yuzlerBasamağı**3)

    result=birlerBasamağı+onlarBasamağı+yuzlerBasamağı

    if result == k:
        count+=1
        myList.append(k)
print(count,myList)


