def encrypt_this(text):
    c = []
    for i in text.split():
        
        if len(i) == 1:
            c.append(str(ord(i)))
        elif len(i) == 2:
            c.append(str(ord(i[0])) + i[-1])
        else:
            c.append(str(ord(i[0])) +i[-1] + i[2:-1] + i[1])
    return ' '.join(c)

print(encrypt_this("A wise old owl lived in an oak"))