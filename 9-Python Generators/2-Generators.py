# kullanılan eleman listede saklanmıcaksa yani o an kullanılıyorsak ve sonradan o elemanla işimiz yoksa anlık
# olarak kullanıp bellekten sileriz

# Generators mantığı budur (bellekte yer tutmayan iteratorler(yineleyiciler)

def cube():
    for i in range(5):
        yield i ** 3

for i in cube():
    print(i)


# alternatif

generator = (i**3 for i in range(5))
print(generator)