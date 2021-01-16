m = float(input('Digite uma medida em metros: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print('\033[4;1;37m{}\033[mm equivale a:'.format(m))
print('\033[4;31m{:.2f}\033[mkm'.format(km))
print('\033[4;32m{:.2f}\033[mhm'.format(hm))
print('\033[4;33m{:.2f}\033[mdam'.format(dam))
print('\033[4;34m{:.2f}\033[mdm'.format(dm))
print('\033[4;35m{:.2f}\033[mcm'.format(cm))
print('\033[4;36m{:.2f}\033[mmm'.format(mm))
