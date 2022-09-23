from random import *
print('\n'.join((''.join(map(str, [x for x in sample('abcdefghijklmnopqrstuvwxyzABCDEFGHJKLMNOPQRSTUVWXYZ1234567890', 15)]))) for i in range(10)))