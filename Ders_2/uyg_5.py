sayi=int(input("Hangi sayıya kadar: "))
toplamcift=0
toplamtek=0
for i in range(sayi):
    if i %2 == 0:
        toplamcift += i
    if i %2 == 1:
        toplamtek += i


print(f"tek sayıların toplamı: {toplamtek}")
print(f"cift sayıların toplamı: {toplamcift}")