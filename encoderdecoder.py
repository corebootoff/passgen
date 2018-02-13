def XOR_cipher(string, key):
    s=''
    for i in range(len(string)):
        s += chr(ord(string[i])^ord(key[i%len(key)]))
    return s

def ooo(string,key):
    s=''
    for i in range(len(string)):
        s += chr(ord(string[i])^ord(key[i%len(key)]))
    return s

if __name__=='__main__':
    val = input('Введите строку и ключ через запятую: ').split(',')
    Xval = XOR_cipher(val[0],val[1].lstrip())
    print('%s - закодировано %s по ключу %s' % (Xval, val[0], val[1].lstrip()))

    
