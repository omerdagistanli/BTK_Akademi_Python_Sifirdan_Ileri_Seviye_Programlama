def toplama(a,b):
    return a+b

def cikarma(a,b):
    return a-b

def carpma(a,b):
    return a*b

def bolme(a,b):
    return a/b

def islem(parameter1,parameter2,parameter3,parameter4,islem_adi):
    if islem_adi == "toplama":
        print(parameter1(2,3))
    elif islem_adi == "cikarma":
        print(parameter2(5,3))
    elif islem_adi == "carpma":
        print(parameter3(3,4))
    elif islem_adi == "bolme":
        print(parameter4(10,2))
    else:
        print("Geçersiz işlem!")

islem(toplama,cikarma,carpma,bolme, "toplama")
islem(toplama,cikarma,carpma,bolme, "cikarma")
islem(toplama,cikarma,carpma,bolme, "carpma")
islem(toplama,cikarma,carpma,bolme, "bolme")
islem(toplama,cikarma,carpma,bolme, "modalma")