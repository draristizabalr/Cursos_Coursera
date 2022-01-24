#%%
while True:    
    fname = input('Enter name file: ')
    try:
        fhand = open(fname)
        break
    except:
        print('Error. File name does not exist')

count = 0;snum = 0
for line in fhand:
    nline = line.rstrip()
    if nline.startswith('X-DSPAM-Confidence:'):
        snum += float(nline[19:])
        count += 1
ave = snum/count
print('Average spam confidence:',ave)