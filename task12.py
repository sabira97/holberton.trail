class Kitab:
    def __init__(self, ad, muellif):
        self.ad = ad
        self.muellif = muellif
        self.goturulub = False

class Kitabxana:
    def __init__(self):
        self.kitablar = []

    def kitab_elave_et(self, kitab):
        self.kitablar.append(kitab)

    def butun_kitablar(self):
        for k in self.kitablar:
            status = "Goturulub" if k.goturulub else "Movcuddur"
            print(f"{k.ad} - {k.muellif} [{status}]")

    def kitab_gotur(self, ad):
        for k in self.kitablar:
            if k.ad == ad and not k.goturulub:
                k.goturulub = True
                print(f"{ad} goturuldu.")
                return
            print("Kitab tapilmadi ve ya goturulub.")

k1 = Kitab("Aktirisa", "Xez Paltolu Maddonna")
k2 = Kitab("Cinayet ve Ceza", "Qurur ve Qerez")

lib = Kitabxana()
lib.kitab_elave_et(k1)
lib.kitab_elave_et(k2)

lib.butun_kitablar()
lib.kitab_gotur("Cinayet ve Ceza")
lib.butun_kitablar()
    