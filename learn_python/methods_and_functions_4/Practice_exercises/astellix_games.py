def print_big(letter):
    patterns = {1:'  *  ',2:' * * ',3:'*   *',4:'*****',5:'**** ',6:'   * ',7:' *   ',8:'*   * ',9:'*    '}
    alphabet = {'A':[1,2,4,3,3],'B':[5,3,5,3,5],'C':[4,9,9,9,4],'D':[5,3,3,3,5],'E':[4,9,4,9,4]}
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])
print_big('e')

print('')
for i in range(1,10,2):
    print(('*'*i).center(20))

print('')
for i in range(1,10,2):
    print('*'*i)

print('')
for i in range(1,10,2):
    print('{:>12}'.format('*'*i))

