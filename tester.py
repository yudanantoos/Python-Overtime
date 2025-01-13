class Tes:

    def __init__(self,nama):
        self.nama = nama

    @classmethod
    def ui(cls):
        nm = 'Vian'
        c = cls(nm)
        print(c.nama)

t = Tes("Aku")
print(t.nama)
Tes.ui()