text1 = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr\'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
text2 = "map"

def decode(text):

    txt = list(text)

    for i in range(len(txt)):
        val = ord(txt[i])+2
        if val > 97+25:
            val = val - 26
        txt[i] = chr(val)

    sol = "".join(txt)

    print sol

decode(text2)
