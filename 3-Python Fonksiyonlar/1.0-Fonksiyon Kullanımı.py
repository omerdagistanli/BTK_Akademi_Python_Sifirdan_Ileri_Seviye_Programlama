def emeklilikYasSorgulama(sorgulanicakYas):
    if(sorgulanicakYas > 65):
        print("Zaten emekli oldunuz")
    else:
        kaldi = 65 - sorgulanicakYas
        print("Emekliliğe",kaldi,"sene kaldı.")

yas = input("Lütfen yaşınızı girin:")

emeklilikYasSorgulama(int(yas))