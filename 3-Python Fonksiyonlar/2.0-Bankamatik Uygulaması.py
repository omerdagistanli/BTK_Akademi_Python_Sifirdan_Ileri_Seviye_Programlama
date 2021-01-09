# Bankamatik Uygulaması

accountA = {
    "ad": "Ömer DAĞISTANLI",
    "hesapNo": "12314",
    "bakiye": 3000,
    "ekHesap": 2000
}
accountB = {
    "ad": "Yusuf DAĞ",
    "hesapNo": "12324",
    "bakiye": "2000",
    "ekHesap": 1000
}
def paraCek(hesap, miktar):
    print("Merhaba", hesap["ad"])

    if(hesap["bakiye"] >= miktar):
        hesap["bakiye"] -= miktar
        print("Paranızı alabilirsiniz",hesap["bakiye"])

    else:
        toplam = hesap["bakiye"] + hesap["ekHesap"]

        if (toplam >= miktar):
            ekHesapKullanimi = input("Ek hesap kullanılsın mı ? (e/h):")

            if(ekHesapKullanimi == "e"):
                hesap["bakiye"] -= miktar
                print("Paranızı alabilirsiniz")
            else:
                print(hesap["hesapNo"],"nolu hesabınızda",hesap["bakiye"],"bulunmaktadır.")
        else:
            print("Üzgünüz bakiye yetersiz!")

paraCek(accountA, 5000)
paraCek(accountA, 1000)
