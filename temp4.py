class GonderimStack:
    def __init__(self, kapasite=5):
        self.stack = []
        self.kapasite = kapasite

    def push(self, gonderi):
        if len(self.stack) >= self.kapasite:
            self.stack.pop(0)  # Kapasite dolarsa en eski gönderiyi çıkar
        self.stack.append(gonderi)
        print(f"Gönderi {gonderi} yığına eklendi.")

    def pop(self):
        if not self.stack:
            print("Gönderim geçmişi boş.")
            return None
        return self.stack.pop()

    def peek(self):
        if not self.stack:
            print("Gönderim geçmişi boş.")
            return None
        return self.stack[-1]

    def goruntule(self):
        if not self.stack:
            print("Gönderim geçmişi boş.")
            return []
        print("Son gönderim geçmişi:")
        return list(reversed(self.stack))


class Musteri:
    def __init__(self, musteri_id, ad_soyad):
        self.musteri_id = musteri_id
        self.ad_soyad = ad_soyad
        self.gonderim_gecmisi = GonderimStack()


if __name__ == "__main__":
    # Örnek kullanım
    musteri1 = Musteri(1, "Ayşe Yılmaz")

    # Gönderim ekleme
    musteri1.gonderim_gecmisi.push("Kargo-101")
    musteri1.gonderim_gecmisi.push("Kargo-102")
    musteri1.gonderim_gecmisi.push("Kargo-103")
    musteri1.gonderim_gecmisi.push("Kargo-104")
    musteri1.gonderim_gecmisi.push("Kargo-105")
    musteri1.gonderim_gecmisi.push("Kargo-106")  # Kapasiteyi aştığında en eski kargo çıkar

    # Gönderim geçmişini görüntüleme
    print(musteri1.gonderim_gecmisi.goruntule())

    # Son gönderimi kontrol etme
    print(f"Son gönderi: {musteri1.gonderim_gecmisi.peek()}")

    # Gönderim çıkarma
    print(f"Çıkarılan gönderi: {musteri1.gonderim_gecmisi.pop()}")

    # Tekrar görüntüleme
    print(musteri1.gonderim_gecmisi.goruntule())
