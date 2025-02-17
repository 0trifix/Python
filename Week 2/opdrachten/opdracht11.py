def som_veelvouden():
    som = 0
    for i in range(1, 1000):
        if i % 3 == 0 or i % 5 == 0:
            som += i
    return som

print(som_veelvouden())
