# cihazlar arasında ortak bir veri taşıma objesidir

import json
person_string = '{"name":"Ali", "languages":["python","C#"]}'

# Json string to Dictionary

# result = json.loads(person_string)
# name = result["name"]
# lang = result["languages"]
# print(name)
# print(lang)
# print(result)

# Dosyadan okuma ile json kullanımı

# with open("json_test",encoding="utf-8") as f:
#     data = json.load(f)
#     print(data["name"])

# Dictionary to Json string

# person_dict = {
#     "name" : "Ali-veli",
#     "lang" : ["C#","python"]
# }
# # result = json.dumps(person_dict)
# # print(result)
#
# # Dosyaya yazma ile json kullanımı
#
# with open("json_test","w") as f:
#     json.dump(person_dict, f)
#

sonuc = json.loads(person_string)
result = json.dumps(sonuc, indent=4, sort_keys=True)
print(result)
