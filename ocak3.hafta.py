for i in range(1,101):
    print(i)

print("-----------------------------------------------------------")

for cift in range(2,101,2):
    print(cift)


print("------------------------------------------------------------------")

user_number = int(input("Faktöriyelini bulmak istediğiniz sayıyı giriniz: "))
def fak(f):
    if f == 0 or f == 1:
        return 1
    else:
        return f * fak(f - 1)
    
f = user_number
print(f"{f} bu sayının faktöriyeli: {fak(f)}")

print("---------------------------------------------------------------------")

def asal(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

for num in range(1,101):
    if asal(num):
        print(num, end=" ")