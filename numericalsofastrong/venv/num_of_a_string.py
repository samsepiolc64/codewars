def numericals(s):
    di = {}
    for i in range(len(s)):
        if s[i] in di:
            di[s[i]] += 1
        else:
            di[s[i]]=1
    print(di)






word = "Hello"
numericals(word)

