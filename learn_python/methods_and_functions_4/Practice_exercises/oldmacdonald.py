#OLD MACDONALD

#Write a function that capitalizes the first and fourth letters of a name
#Example
#old_macdonald('macdonald') --> MacDonald
#.capitalize() capitalize the first letter of a string
def old_macdonald(name):
    if len(name)>3:
        return name[:3].capitalize() + name[3:].capitalize()
    else:
        return 'Name is too short'

print(old_macdonald('macdonald'))

#Another way
def old_mac(name):
    first_letter=name[0]
    in_between=name[1:3]
    fourth_letter=name[3]
    rest=name[4:]
    return first_letter.upper()+in_between+fourth_letter.upper()+rest
print(old_mac('macdonald'))