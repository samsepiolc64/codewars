
class Human:
    pass
class Man(Human):
    pass
class Woman(Human):
    pass



def God():
    paradise = []
    Eve = Woman()
    Adam = Man()
    paradise.append(Adam)
    paradise.append(Eve)
    return paradise


paradise = God()

print(paradise[0])