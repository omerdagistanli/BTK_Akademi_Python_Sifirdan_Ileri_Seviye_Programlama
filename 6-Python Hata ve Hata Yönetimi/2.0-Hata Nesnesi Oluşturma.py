def check_password(psw):
    import re
    if len(psw) < 8:
        raise Exception("parola en az 7 karakter olmalıdır")
    elif not re.search("[a-z]", psw):
        raise Exception("parola küçük harf içermelidir")
    elif not re.search("[A-Z]", psw):
        raise Exception("parola büyük harf içermelidir")
    elif not re.search("[0-9]", psw):
        raise Exception("parola rakam içermelidir")
    elif re.search("\s",psw):
        raise Exception("parola boşluk içermemelidir")

password = "B234567a"

try:
    check_password(password)

except Exception as ex:
    print(ex)
else:
    print("Geçerli parola")