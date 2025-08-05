# Ana sinif: Insan
class Insan:
    def __init__(self, ad, yas):
        self.ad = ad
        self.yas = yas

    def melumat_goster(self):
        print(f"Ad: {self.ad}, Yas: {self.yas}")

 # Isci sinifi - Insan sinifinden irsiyyet alir
class Isci(Insan):
    def __init__(self, ad, yas, emek_haqqi):
        super().__init__(ad, yas) #Ana sinifin konstruktorunu cagiririq
        self.__emek_haqqi = emek_haqqi #Mehdudlasdirma - gizli atribut

 # Emek haqqini almaq ucun getter metodu 
    def get_emek_haqqi(self):
        return self.__emek_haqqi

# Emek haqqini teyinetmek ucun setter metodu
    def set_emek_haqqi(self, yeni_haqq):
        if yeni_haqq > 0:
            self.__emek_haqqi = yeni_haqq
        else:
            print("Emek haqqi menfi ola bilmez!")

# Faizle emek haqqini artiran metod (Polymorphism ucun esas metod)
    def faizle_artir(self, faiz):
        if faiz > 0:
            yeni_haqq = self.__emek_haqqi * (1 + faiz/100)
            self.set_emek_haqqi(yeni_haqq)
        else:
            print("Faiz musbet olmalidir!")

# Emek haqqini goster metod
    def emek_haqqini_goster(self):
        print(f"{self.ad} adli iscinin emek haqqi: {self.__emek_haqqi:.2f} AZN")

# Irsi sinif - Menecer, Isci sinifinden miras alir ve metodlari ferqlendirir (Polymorphism)
class Menecer(Isci):
    def __init__(self, ad, yas, emek_haqqi, bonus_faizi):
        super().__init__(ad, yas, emek_haqqi)
        self.bonus_faizi = bonus_faizi

# Faizle emek haqqini artirma metodu (override)
    def faizle_artir(self, faiz):
    #Menecerlere elave bonus faiz elave olunur
        toplam_faiz = faiz + self.bonus_faizi
        super().faizle_artir(toplam_faiz)
        print(f"Menecer {self.ad}-in emek haqqi bonusla artirildi ({toplam_faiz}%).")

# Istifade numunesi:
isci1 = Isci("Aynur", 20, 2005)
isci1.melumat_goster()
isci1.emek_haqqini_goster()

isci1.faizle_artir(10) # 10% artir
isci1.emek_haqqini_goster()

menecer1 = Menecer("Sehane", 19, 2006, 5) # 5% bonus
menecer1.melumat_goster()
menecer1.emek_haqqini_goster()
 
menecer1.faizle_artir(10) # 10% + 5% bonus
menecer1.emek_haqqini_goster() 



     