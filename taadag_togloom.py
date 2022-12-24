import random

sanasan_too = random.randint(0, 100)
print('bi neg too sanasan, ta 0-100 hurtel too oruulna uu, tand 5 bolomj baigaa')
bolomj = 0
ami = 7
while bolomj <= ami:
    taavar = int(input('tanii oruulah too '))
    if taavar == sanasan_too:
        print ('congrats! you won')
        break
    if taavar < sanasan_too:
        print('baga bna ih too oruulna uu')
    else:
        print('ih bna baga too oruulna uu')
    bolomj = bolomj + 1
    print('tand', ami - bolomj, 'bolomj uldlee')
if bolomj > ami:
    print('togloom duuslaa, you lost')

 