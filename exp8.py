i = 0
def Monkey_go_box(x, y):
    global i
    i += 1
    print('Step:', i, 'Monkey goes from', x, 'to', y)

def Monkey_move_box(x, y):
    global i
    i += 1
    print('Step:', i, 'Monkey moves the box from', x, 'to', y)

def Monkey_on_box():
    global i
    i += 1
    print('Step:', i, 'Monkey climbs onto the box')

def Monkey_get_banana():
    global i
    i += 1
    print('Step:', i, 'Monkey gets the banana')

codeIn = input("Enter locations (monkey, banana, box): ")
codeInList = codeIn.split()

monkey = codeInList[0]
banana = codeInList[1]
box = codeInList[2]

print('The steps are as follows:')

Monkey_go_box(monkey, box)
Monkey_move_box(box, banana)
Monkey_on_box()
Monkey_get_banana()