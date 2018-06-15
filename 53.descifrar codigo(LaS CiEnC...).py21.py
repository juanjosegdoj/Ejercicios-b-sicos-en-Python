s = "AsL OjClU SxE AsIdCeNrEtTyOuP NjE StAsIcCfNgErIeC EhD AkL NsOdIfCgAtTyUuPaMsOdC"
for palabra in s.split(' '):
    resultado = ''
    for i in range(0,len(palabra)):
        if i % 2 == 0:
            resultado = palabra[i] + resultado
    print(resultado)
