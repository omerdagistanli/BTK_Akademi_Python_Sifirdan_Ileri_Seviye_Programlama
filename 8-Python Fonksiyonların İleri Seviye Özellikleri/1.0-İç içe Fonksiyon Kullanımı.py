# encapsulation

# dış fonksiyon çalışırken iç fonksiyonda değişiklik olmuyor(çağrılmadığı sürece)
def out(num1):
    def inn(num):
        return num + 2

    num2 = inn(10)
    print(num1,num2)

out(5)