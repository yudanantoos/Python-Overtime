import datetime


def fungsi (a:int, b:int, c:int) -> str:
    if (type(a) == int
        and type(b) == int
        and type(c) == int):
        d = datetime.date(a, b, c)
        s = '%d-%m-%Y'
        return d.strftime(s)
    return 0

print(fungsi('2025',1,1))