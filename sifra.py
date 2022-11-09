def sifra(string:str,key:str)->str:
    y = 0
    nr = ""
    for i in string:
        a = y % len(key)
        x = ((ord(i)-97+ord(key[a])-97)%26)+97
        y += 1
        nr += chr(x)
    return nr
print(sifra("ahojsvet","kvet"))
