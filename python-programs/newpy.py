def functest():
    hc = ['A','K','J','Q']
    lc = [2,3,4,5,6,7,8,9,10]
    lc.extend(hc)
    import random
    randomize = random.choices(lc,k=2)
    return randomize

print(sum(functest()))