import math
# A program  olvasson be a konzolról egy valós számot! A program számítsa ki a szám abszolút értékét, és írja ki az eredményeket a konzolra! A számításhoz a math.fabs használd!

szam = float(input("Kérem adjon meg egy valós számot!"))
eredmeny = math.fabs(szam)
print("|"+str(szam)+"|="+str(eredmeny))
