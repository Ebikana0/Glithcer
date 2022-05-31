Cryptimageof = bytearray(b"")
CryptimageHacked = bytearray(b"")
Cryptimage = bytearray(b"")
CryptimageFirst = bytearray(b"")
CryptimageLast = bytearray(b"")
#Edit this your self
OFFSET = 0x40D
ENDPOS = 0x30ED
ENDLIKE = 0x30EE
LENG = 0x2CE1

MOVEVALUE = 0x01

fucked = 0
passed = 0

with open("BASE.png",'rb') as x:
    print(x)
    for xb in x:
        Cryptimage += xb
        print(xb)
    print("got iamge" + str(len(Cryptimage)))
for x in range(LENG):
    print("load" + str(OFFSET + x))
    Cryptimageof.append(Cryptimage[OFFSET + x])
for x in Cryptimageof:
    print(hex(x))
for x in range(OFFSET):
    CryptimageFirst.append(Cryptimage[x])
print(str(len(Cryptimage) - 0x30ED))
for x in range((len(Cryptimage) - ENDLIKE)):
    CryptimageLast.append(Cryptimage[ENDLIKE + x])
for x in Cryptimageof:
    if x + MOVEVALUE < 256:
        print(x + MOVEVALUE)
        passed += 1
        CryptimageHacked.append(x + MOVEVALUE)
    else:
        print("FUCK" + str(x + MOVEVALUE))
        CryptimageHacked.append(0x00)
        fucked += 1
print("FAILD" + str(fucked) + "||||||PASSED" + str(passed))
with open("GLITCH.png",'wb') as x:
    x.write(CryptimageFirst + CryptimageHacked + CryptimageLast)
print("OK")
"""
with open("FUCK YOU2.png",'wb') as x:
    cryptimage +=
"""
