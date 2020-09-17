import time
bar=[' ' for i in range(103)]
bar[0],bar[-2],bar[-1]='[', ']', ' 0%'

def shot_frame():
    for per in bar:
        print(per, end='')

print('starting the progress bar...')
for i in range(1,len(bar)-1):
    shot_frame()
    time.sleep(0.1)
    print('\r',end='')
    bar[i],bar[-1] = '#',f' {i}%'

print()
print('updated progress bar successfully.')
input('\nPress enter to exit.')
