# TODO Найдите количество книг, которое можно разместить на дискете
disk_Mb = 1.44
disk_b = 1.44 * 1024 * 1024

page = 100
line = 50
symb = 25
kod = 4
book = kod * symb * line * page

result = round(disk_b / book)

print("Количество книг, помещающихся на дискету:", result)
