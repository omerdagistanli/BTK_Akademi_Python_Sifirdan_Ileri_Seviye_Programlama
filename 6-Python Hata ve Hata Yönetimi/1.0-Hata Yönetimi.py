# error handling => hata yönetimi

while True:

    try:
        x = int(input("x:"))
        y = int(input("y:"))
        print(x/y)

    # except (ZeroDivisionError, ValueError) as e:
    #     print(print("yanlış değer girdiniz\n",e))

    except Exception as ex:
        print("yanlış değer girdiniz\n",ex)

    else:
        break

    # dosya kapatma vs işlemler için kullanılır
    finally:                            
        print("Try-except sonlandı.")