
from operations.calculation import ambil_data

a = ambil_data()
print("Sebelum sortir:", a)
b = list(a)
b.sort()

a = {i : a.get(i) for i in b}

c = list(a.values())
