class GonderiDugumu:
    def __init__(self, gonderi_id, tarih, durum, teslim_suresi):
        self.gonderi_id = gonderi_id
        self.tarih = tarih
        self.durum = durum
        self.teslim_suresi = teslim_suresi
        self.sonraki = None


class BagliListe:
    def __init__(self):
        self.bas = None

    def sirali_gonderi_ekle(self, gonderi_id, tarih, durum, teslim_suresi):
        yeni_gonderi = GonderiDugumu(gonderi_id, tarih, durum, teslim_suresi)
        if not self.bas or self.bas.tarih > tarih:
            yeni_gonderi.sonraki = self.bas
            self.bas = yeni_gonderi
            return

        mevcut = self.bas
        while mevcut.sonraki and mevcut.sonraki.tarih <= tarih:
            mevcut = mevcut.sonraki
        yeni_gonderi.sonraki = mevcut.sonraki
        mevcut.sonraki = yeni_gonderi

    def gonderileri_goruntule(self):
        gonderiler = []
        mevcut = self.bas
        while mevcut:
            gonderiler.append({
                "gonderi_id": mevcut.gonderi_id,
                "tarih": mevcut.tarih,
                "durum": mevcut.durum,
                "teslim_suresi": mevcut.teslim_suresi
            })
            mevcut = mevcut.sonraki
        return gonderiler


class Musteri:
    def __init__(self, musteri_id, ad_soyad):
        self.musteri_id = musteri_id
        self.ad_soyad = ad_soyad
        self.gonderi_gecmisi = BagliListe()


class MusteriYoneticisi:
    def __init__(self):
        self.musteriler = {}

    def musteri_ekle(self, musteri_id, ad_soyad):
        if musteri_id in self.musteriler:
            print(f"{musteri_id} ID'li müşteri zaten mevcut.")
            return
        self.musteriler[musteri_id] = Musteri(musteri_id, ad_soyad)
        print(f"{ad_soyad} adlı müşteri başarıyla eklendi.")

    def gonderi_gecmisi_getir(self, musteri_id):
        if musteri_id not in self.musteriler:
            print(f"{musteri_id} ID'li müşteri bulunamadı.")
            return
        gonderiler = self.musteriler[musteri_id].gonderi_gecmisi.gonderileri_goruntule()
        return gonderiler

    def musteriye_gonderi_ekle(self, musteri_id, gonderi_id, tarih, durum, teslim_suresi):
        if musteri_id not in self.musteriler:
            print(f"{musteri_id} ID'li müşteri bulunamadı.")
            return
        self.musteriler[musteri_id].gonderi_gecmisi.sirali_gonderi_ekle(gonderi_id, tarih, durum, teslim_suresi)
        print(f"{gonderi_id} ID'li gönderi başarıyla eklendi.")


if __name__ == "__main__":
    yonetici = MusteriYoneticisi()

    # Yeni müşteriler ekleme
    yonetici.musteri_ekle(1, "Ayşe Yılmaz")
    yonetici.musteri_ekle(2, "Mehmet Kaya")

    # Müşteri 1'e gönderim ekleme
    yonetici.musteriye_gonderi_ekle(1, 101, "2023-12-20", "Teslim Edildi", 2)
    yonetici.musteriye_gonderi_ekle(1, 102, "2023-12-21", "Teslim Edildi", 1)
    yonetici.musteriye_gonderi_ekle(1, 103, "2023-12-19", "Teslim Edilmedi", 3)

    # Müşteri 1'in gönderim geçmişini sorgulama
    print("Ayşe Yılmaz'ın gönderim geçmişi:")
    gonderiler = yonetici.gonderi_gecmisi_getir(1)
    for gonderi in gonderiler:
        print(gonderi)

    # Müşteri 2'nin gönderim geçmişini sorgulama (Boş olmalı)
    print("\nMehmet Kaya'nın gönderim geçmişi:")
    gonderiler = yonetici.gonderi_gecmisi_getir(2)
    for gonderi in gonderiler:
        print(gonderi)
