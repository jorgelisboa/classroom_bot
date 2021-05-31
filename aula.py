import sys
from time import sleep
from classroom import *
inp = sys.argv[1].upper()

if inp in classes:
    open_link(classes[inp])
elif inp == 'TODAY' or inp == '-T':
    print()
    classes_today()
elif inp == 'HELP' or inp == '-H':
    help_menu()
elif inp == 'AUTOMATE' or inp == '-A':
    subs = find_classes()
    c = 0
    while True:
        if c == 1:
            break
        time = datetime.now().time()
        time = str(time).split(':')
        print(time)
        ['08', '57', '29.790054']
        for i in subs:
            print('Executando')
            if time[0] == i[0] and time[1] == i[3:5] and 'INTERVALO' in i:
                print('Caiu no if')
                open_link(classes[i[25:]])
                print('Opened ' + i[25:] + ' link')
                if i == subs[-1]:
                    c = 1
                    break
                sleep(3600)
                break
else:
    print('\n' + '\t' + 'Invalid command')
    print('\n' + '\t' + 'Try class -h for help menu')