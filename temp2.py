import heapq

class Kargo:
    def __init__(self, gonderi_id, teslim_suresi, durum):
        self.gonderi_id = gonderi_id
        self.teslim_suresi = teslim_suresi
        self.durum = durum

    def __lt__(self, other):
        return self.teslim_suresi < other.teslim_suresi


class OncelikliKargoListesi:
    def __init__(self):
        self.kargo_heap = []

    def kargo_ekle(self, gonderi_id, teslim_suresi, durum):
        yeni_kargo = Kargo(gonderi_id, teslim_suresi, durum)
        heapq.heappush(self.kargo_heap, yeni_kargo)
        print(f"Kargo {gonderi_id} başarıyla eklendi.")

    def oncelikli_kargo_isle(self):
        if not self.kargo_heap:
            print("İşlenecek kargo bulunmamaktadır.")
            return None
        oncelikli_kargo = heapq.heappop(self.kargo_heap)
        print(f"Öncelikli kargo işleniyor: {oncelikli_kargo.gonderi_id}")
        return oncelikli_kargo

    def mevcut_kargolari_goruntule(self):
        print("Mevcut kargolar (teslimat süresine göre):")
        for kargo in sorted(self.kargo_heap):
            print(f"ID: {kargo.gonderi_id}, Süre: {kargo.teslim_suresi}, Durum: {kargo.durum}")


if __name__ == "__main__":
    kargo_listesi = OncelikliKargoListesi()

    # Kargo ekleme
    kargo_listesi.kargo_ekle(201, 3, "İşleme Alındı")
    kargo_listesi.kargo_ekle(202, 1, "Teslimatta")
    kargo_listesi.kargo_ekle(203, 2, "İşleme Alındı")

    # Kargoları görüntüleme
    kargo_listesi.mevcut_kargolari_goruntule()

    # Öncelikli kargo işleme
    kargo_listesi.oncelikli_kargo_isle()

    # Kargoları tekrar görüntüleme
    kargo_listesi.mevcut_kargolari_goruntule()
