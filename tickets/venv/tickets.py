def tickets(people):
    kasa = {25:0,50:0,100:0}
    for i in range(len(people)):
        if people[i] == 25:
            kasa[25] += 1
            trans = 'YES'
        elif people[i] == 50:
            if kasa[25] > 0:
                kasa[25] -= 1
                kasa[50] += 1
                trans = 'YES'
            else:
                trans = 'NO'
                break
        elif people[i] == 100:
            if kasa[50] > 0 and kasa[25] > 0:
                kasa[50] -= 1
                kasa[25] -= 1
                kasa[100] += 1
                trans = 'YES'
            elif kasa[25] >= 3:
                kasa[25] -= 3
                kasa[100] += 1
                trans = 'YES'
            else:
                trans = 'NO'
                break




    print(kasa)
    print(trans)













#kolejka = [25,100]
kolejka = [25, 25, 25, 100]

tickets(kolejka)
