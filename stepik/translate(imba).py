import string
trans={'l':'','I':'','o':'','O':'','1':'','0':''}
syms=string.ascii_letters+string.digits
st=syms.maketrans(trans)
resst=syms.translate(st)
print(syms,resst)

