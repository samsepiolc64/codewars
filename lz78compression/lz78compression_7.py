def encoder(data):
    di = {}
    out = ''
    l = list(data)
    data_len = len(l)
    i, j, k =  0, 1 ,0
    while i < data_len:
        if not l[k] in di:
            di[l[k]] = j
            if len(l[k]) > 1:
                out += str(di[l[k][:-1]]) + l[0][len(l[k])-1]
            else:
                out += '0' + l[k]
            del(l[k])
            j += 1
        else:
            try:
                l[k] = l[k] + l[k+1]
                del (l[k + 1])
            except:
                out += str(di[l[k]])
        i += 1
    return out


def decoder(data):
    di = {}
    out = ''
    out2 = ''
    l = list(data)
    data_len = len(l)
    i, j = 0 ,1
    while i < data_len:
        if l[i] == '0':
            di[l[i+1]] = j
            j += 1
        else:
            try:
                if l[i + 1].isdigit():
                    k = int(l[i] + l[i + 1])
                    di[list(di.keys())[k - 1] + l[i + 2]] = j
                    i += 1
                    j += 1
                else:
                    di[list(di.keys())[int(l[i]) - 1] + l[i + 1]] = j
                    j += 1
            except:
                try:
                    out2 += list(di.keys())[int(l[i])-1]
                except:
                    pass
        i += 2
    out = ''.join(di.keys())+out2
    return out

data = 'ABCDDEFGABCDEDBBDEAAEDAEDCDABC' #0A0B0C0D4E0F0G1B3D0E4B2D10A1E4A10D9A2C


#data = 'ABBCBCABABCAABCAABBCAA'               #0A0B2C3A2A4A6B6
#data = 'AAAAAAAAAAAAAAA'                       #0A1A2A3A4A
#data = 'ABCABCABCABCABCABC'                    #0A0B0C1B3A2C4C7A6
#data = 'ABCDDEFGABCDEDBBDEAAEDAEDCDABC'        #0A0B0C0D4E0F0G1B3D0E4B2D10A1E4A10D9A2C

#data = 'ABAABABAABAB'
#data = 'AAAAAAAAAAAAAAA'
#data = 'ABCABCABCABCABCABC'
#data = 'ABBCBCABABCAABCAABBCAAA'
#data = 'ABAABABAABABBAB'
compressed = encoder(data)
decompressed = decoder(compressed )
#decoder()