def tes(nomor):
    def tes_anak(nomor):
        if nomor >= 100:
            return 100
        return nomor * tes(nomor + 1)
    return tes_anak(nomor)

print(tes(1))