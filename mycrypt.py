import codecs

def encode(s):
    if not isinstance(s,str):
        raise TypeError
    origlen = len(s)
    crypted = ""
    digitmapping = dict(zip('1234567890!"#€%&/()=','!"#€%&/()=1234567890'))
    if len(s) > 1000:
        raise IndexError
    s += 'a' * (1000-origlen);
    chars = set('öäå+')
    if any((c in chars) for c in s):
        raise ValueError
    for c in s:
        if c.isalpha():
            if c.islower():
                c=c.upper()
            # Rot13 the character for maximum security
            crypted+=codecs.encode(c,'rot13')
        elif c in digitmapping:
          crypted+=digitmapping[c]

    return crypted[0:origlen] 

def decode(c):
    decrypted = ""
    digitmapping = dict(zip('!"#€%&/()=1234567890','1234567890!"#€%&/()='))
    for a in c:
        if a.isalpha():
            if a.isupper():
                a=a.lower()
            # Rot13 the character for maximum security
            decrypted+=codecs.encode(a,'rot13')
        elif a in digitmapping:
          decrypted+=digitmapping[a]
    return decrypted

