
def encoder(data):
    di = {}
    out = ''
    i = 0
    j = 0
    while i < 15:
        
        if data[i] in di:
            if (data[i]+data[i+1]) in di:
                if (data[i]+data[i+1]+data[i+2]) in di:
                    if (data[i]+data[i+1]+data[i+2]+data[i+3]) in di:
                        out+="*"

                    else:
                        di[data[i]+data[i+1]+data[i+2]+data[i+3]]=max(di.values())+1
                        out+=str(di[data[i]+data[i+1]+data[i+2]])+str(data[i+3])
                        i+=4
                else:
                    di[data[i]+data[i+1]+data[i+2]]=max(di.values())+1
                    out+=str(di[data[i]+data[i+1]])+str(data[i+2])
                    i+=3
            else:
                di[data[i]+data[i+1]]=max(di.values())+1
                out+=str(di[data[i]])+str(data[i+1])
                i+=2
        else:
            di[data[i]]=i+1
            out+=str(j)+str(data[i])
            i+=1


        print(di)
        print(out)

        print('0A0B0C1B3A2C4C7A6')

def decoder(data):
    return

#data = 'ABAABABAABAB'
#data = 'AAAAAAAAAAAAAAA'
data = 'ABCABCABCABCABCABC'
encoder(data)
#decoder()