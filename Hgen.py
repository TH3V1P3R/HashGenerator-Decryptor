from hasher import h
retry = "y"
while retry == "y":
    pswd = str(input("\nenter your password : "))

    while pswd == "":
        pswd = str(input("enter a valid password: "))
        
    h_type = ''
    hash_list = [ 'blake2b', 'whirlpool', 'MD5', 'MD5-SHA1', 'md5', 'SHA224', 'sha3_256', 'sha3_512', 'blake2b512', 'MDC2', 'RIPEMD160', 'md5-sha1', 'shake_128', 'blake2s', 'SHA512',        'BLAKE2s256', 'shake_256', 'sha3_384', 'MD4', 'sha224', 'blake2s256', 'sha3_224', 'mdc2', 'SHA256', 'sha1', 'sha256', 'ripemd160', 'SHA384', 'BLAKE2b512', 'sha384', 'SHA1', 'md4', 'sha512']
    while h_type == "" or h_type not in hash_list:
        if h_type == 'h' or h_type == 'H' or h_type =='help':
            print("""valid hashes are: {'blake2b', 'whirlpool', 'MD5', 'MD5-SHA1', 'md5', 'SHA224', 'sha3_256', 'sha3_512', 'blake2b512', 'MDC2', 'RIPEMD160', 'md5-sha1', 'shake_128', 'blake2s', 'SHA512', 'BLAKE2s256', 'shake_256', 'sha3_384', 'MD4', 'sha224', 'blake2s256', 'sha3_224', 'mdc2', 'SHA256', 'sha1', 'sha256', 'ripemd160', 'SHA384', 'BLAKE2b512', 'sha384', 'SHA1', 'md4', 'sha512'}""")
        h_type = str(input("enter a valid hash type('h'/'H'/'help' to see valid hashes): "))
    ha = h()
    print("your hash >>>",ha.hashin(pswd,h_type))
    retry = input("\nprees 'y' to use again: ")
input("press enter to exit...")
