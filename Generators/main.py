def count_up_to(max:int):
    count = 1
    while count <= max:
        yield count # yield — это как return, но "пауза", а не "выход"
        count += 1
    
counter = count_up_to(5)
for num in counter:
    print(num)