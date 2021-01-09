# 17-> Çanakkale mantığı ile çalışan liste tipi

# sehirler = ["sakarya", "çanakkale"]
# plakalar = [54, 17]

# print(plakalar[sehirler.index("çanakkale")])

plakalar = { "sakarya" : 54, "çanakkale" : 17, 16 : "bursa"}

plakalar["ankara"] = 6

print(plakalar)


users = {
    "ömerdağıstanlı":{
        "age": 25,
        "email": "omer@gmail.com",
        "adress":"biga"
    },
    "yusufdağıstanlı":{
        "age": 21,
        "email": "yusuf@gmail.com",
        "adress":"biga"
    }
}

print(users["ömerdağıstanlı"])