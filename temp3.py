class Sehir:
    def __init__(self, sehir_id, sehir_adi):
        self.sehir_id = sehir_id
        self.sehir_adi = sehir_adi
        self.alt_sehirler = []

    def alt_sehir_ekle(self, alt_sehir):
        self.alt_sehirler.append(alt_sehir)

    def __str__(self):
        return f"Şehir ID: {self.sehir_id}, Adı: {self.sehir_adi}"


class TeslimatAgaci:
    def __init__(self):
        self.kok = None

    def merkez_belirle(self, sehir_id, sehir_adi):
        self.kok = Sehir(sehir_id, sehir_adi)
        print(f"{sehir_adi} teslimat merkezi olarak belirlendi.")

    def alt_sehir_ekle(self, ust_sehir_id, alt_sehir_id, alt_sehir_adi):
        ust_sehir = self._sehir_bul(self.kok, ust_sehir_id)
        if not ust_sehir:
            print(f"ID {ust_sehir_id} ile eşleşen üst şehir bulunamadı.")
            return
        yeni_alt_sehir = Sehir(alt_sehir_id, alt_sehir_adi)
        ust_sehir.alt_sehir_ekle(yeni_alt_sehir)
        print(f"{alt_sehir_adi} şehri, {ust_sehir.sehir_adi} altına eklendi.")

    def _sehir_bul(self, sehir, sehir_id):
        if not sehir:
            return None
        if sehir.sehir_id == sehir_id:
            return sehir
        for alt_sehir in sehir.alt_sehirler:
            bulunan = self._sehir_bul(alt_sehir, sehir_id)
            if bulunan:
                return bulunan
        return None

    def agaci_goster(self, sehir=None, seviye=0):
        if sehir is None:
            sehir = self.kok
        if not sehir:
            print("Teslimat ağacı boş.")
            return
        print(" " * seviye * 4 + str(sehir))
        for alt_sehir in sehir.alt_sehirler:
            self.agaci_goster(alt_sehir, seviye + 1)

    def agac_derinligi(self, sehir=None):
        if sehir is None:
            sehir = self.kok
        if not sehir.alt_sehirler:
            return 1
        return 1 + max(self.agac_derinligi(alt_sehir) for alt_sehir in sehir.alt_sehirler)


if __name__ == "__main__":
    teslimat_agaci = TeslimatAgaci()

    # Teslimat merkezi belirleme
    teslimat_agaci.merkez_belirle(1, "İstanbul")

    # Alt şehirler ekleme
    teslimat_agaci.alt_sehir_ekle(1, 2, "Şehir A")
    teslimat_agaci.alt_sehir_ekle(1, 3, "Şehir B")
    teslimat_agaci.alt_sehir_ekle(2, 4, "Şehir C")
    teslimat_agaci.alt_sehir_ekle(3, 5, "Şehir D")
    teslimat_agaci.alt_sehir_ekle(3, 6, "Şehir E")

    # Ağaç yapısını görüntüleme
    print("\nTeslimat Ağaç Yapısı:")
    teslimat_agaci.agaci_goster()

    # Ağaç derinliğini hesaplama
    print(f"\nTeslimat ağacının derinliği: {teslimat_agaci.agac_derinligi()}")
