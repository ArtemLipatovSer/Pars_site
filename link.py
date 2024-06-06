
def load_link(name):
    part_one = ''.join(name.split(' |')[:-1])
    part_one = part_one[2:]
    part_one = part_one.replace(' ', '%20')

    part_two = '/%E2%98%85%20'

    part_three = name[2:]
    part_three = part_three.replace('|', '%7C')
    part_three = part_three.replace(' ', '%20')
    part_three = part_three.replace('(', '%28')
    part_three = part_three.replace(')', '%29')

    result = 'https://market.csgo.com/ru/Knife/' + part_one + part_two + part_three
    return result

