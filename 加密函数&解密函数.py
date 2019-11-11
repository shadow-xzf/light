#加密函数
def encryption(s):
    d = {}
    for c in (65,97):
        for i in range(26):
            d[chr(i+c)] = chr((i+5) % 26 + c)
    print("".join([d.get(c,c) for c in s]))

#解密函数
def decryption(n):
    d = {}
    for c in (65,97):
        for i in range(26):
            d[chr(i+c)] = chr((i-5) % 26 + c)
    print("".join([d.get(c,c) for c in n]))

s =input("请输入需要加密的信息：")
n =input("请输入需要解密的信息：")
encryption(s)
decryption(n)
    
