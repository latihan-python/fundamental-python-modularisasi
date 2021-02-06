"""
menghitung luas segitiga
luas segitiga = (alas * tinggi) / 2
"""

alas = 10
tinggi = 6
luas_segitiga = (alas * tinggi) / 2
print(f"alas = {alas} dan tinggi = {tinggi}, maka luas segitiga = {luas_segitiga}")


def hitung_luas_segitiga(alas, tinggi):
    luas_segitiga = (alas * tinggi) / 2
    return luas_segitiga

print('\nhitung luas segitiga dengan fungsi')
print(f"luas segitiga = {hitung_luas_segitiga(100, 2)}")
