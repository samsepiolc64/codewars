def get_middle(s):
    if int(len(s))>2:
        if int(len(s) % 2) == 0:
            print(s[(int(len(s)/2)-1):-((int(len(s)/2)-1))])
        else:
            print(s[(int(len(s) / 2)):-((int(len(s) / 2)))])
    else:
        print (s)


word = "yo"
get_middle(word)