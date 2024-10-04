from random import shuffle,sample
import string
n,m=int(input()),int(input())
trans={'l':'','I':'','o':'','O':'','1':'','0':''}
def cleaning(st,dic):
    return st.translate(st.maketrans(dic))
lows,ups,nums=cleaning(string.ascii_lowercase,trans),cleaning(string.ascii_uppercase,trans),cleaning(string.digits,trans)
alls=lows+ups+nums
if m==3:
    for i in range(n):
        res=sample(lows,1)+sample(ups,1)+sample(nums,1)
        shuffle(res)
        print(''.join(res))
else:
    for i in range(n):
        res=sample(lows,1)+sample(ups,1)+sample(nums,1)+sample(alls,m-3)
        shuffle(res)
        print(''.join(res))