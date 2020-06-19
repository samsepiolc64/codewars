def hex_string(hex_string):
    t= tuple(int(hex_string[i:i + 2], 16) for i in (1, 3, 5))
    r = ('r','g','b')
    rgb = dict(zip(r,t))
    return rgb

hex = "#FF9933"

print(hex_string(hex))