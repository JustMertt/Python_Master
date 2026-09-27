kuladi="ismail"
kulsifre="ismail1234"

while True:
    inkuladi=input("ad: ")
    inkulsifre=input("sifre: ")
    if kuladi == inkuladi and kulsifre == inkulsifre:
        print("Giriş başarılı")
        break
    elif kuladi == inkuladi and kulsifre != inkulsifre:
        print("şifre yanlış başa döndürülüyorsunuz")
    elif kuladi != inkuladi and kulsifre == inkulsifre:
        print("kullanıcı adı yanlış")
    elif kuladi != inkuladi and kulsifre != inkulsifre:
        print("hem kullanıcı adı hemde şifre yanlış")

