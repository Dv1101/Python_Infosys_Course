def fancy_name_plate(*names):
    for name in names:
        print('#############################')
        print('##-------------------------##')
        print('##' +name.center(25,'-')+ '##')
        print('##-------------------------##')
        print('#############################')

fancy_name_plate('Dhruv')