class Kargo:
    def __init__(self, kargo_id, durum, teslim_suresi):
        self.kargo_id = kargo_id
        self.durum = durum
        self.teslim_suresi = teslim_suresi

    def __repr__(self):
        return f"Kargo ID: {self.kargo_id}, Durum: {self.durum}, Teslim Süresi: {self.teslim_suresi}"


def binary_search(sorted_list, kargo_id):
    low, high = 0, len(sorted_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_list[mid].kargo_id == kargo_id:
            return sorted_list[mid]
        elif sorted_list[mid].kargo_id < kargo_id:
            low = mid + 1
        else:
            high = mid - 1
    return None


def merge_sort_by_teslim_suresi(kargo_list):
    if len(kargo_list) <= 1:
        return kargo_list

    mid = len(kargo_list) // 2
    left = merge_sort_by_teslim_suresi(kargo_list[:mid])
    right = merge_sort_by_teslim_suresi(kargo_list[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    while left and right:
        if left[0].teslim_suresi <= right[0].teslim_suresi:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left or right)
    return result


if __name__ == "__main__":
    # Örnek kargo listesi
    kargo_listesi = [
        Kargo(101, "Teslim Edildi", 2),
        Kargo(102, "Teslim Edilmedi", 5),
        Kargo(103, "Teslim Edildi", 1),
        Kargo(104, "Teslim Edilmedi", 3),
        Kargo(105, "Teslim Edildi", 4)
    ]

    # Teslim edilmiş kargoları sıralama ve binary search ile sorgulama
    teslim_edilmis_kargolar = [kargo for kargo in kargo_listesi if kargo.durum == "Teslim Edildi"]
    teslim_edilmis_kargolar.sort(key=lambda x: x.kargo_id)

    print("Teslim Edilmiş Kargolar:")
    for kargo in teslim_edilmis_kargolar:
        print(kargo)

    kargo_id = 103
    sonuc = binary_search(teslim_edilmis_kargolar, kargo_id)
    print(f"\nBinary Search ile {kargo_id} ID'li kargo: {sonuc}")

    # Teslim edilmemiş kargoları sıralama
    teslim_edilmemis_kargolar = [kargo for kargo in kargo_listesi if kargo.durum == "Teslim Edilmedi"]
    teslim_edilmemis_kargolar = merge_sort_by_teslim_suresi(teslim_edilmemis_kargolar)

    print("\nTeslim Edilmemiş Kargolar (Teslim Süresine Göre Sıralı):")
    for kargo in teslim_edilmemis_kargolar:
        print(kargo)
