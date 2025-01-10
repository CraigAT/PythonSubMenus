
### Submenus.py

'''
Menus and Options

A series of menus and options as individual functions.
The functions are named using the menu or menus (in order) they came from as a prefix, 
and the option selected as the suffix, this should keep them unique and identifiable.

'''

def main_menu():
    menu_choice = ""
    while menu_choice.upper() != "X":
        print()
        print(f'Main Menu')
        print(f'=========')
        print(f'1. Sub Menu 1')
        print(f'2. Sub Menu 2')
        print(f'3. Option 3')
        print(f'X. Exit')
        print()
        menu_choice = input('Your Choice:')
        print()
        if len(menu_choice) >= 1:
            match menu_choice:
                case '1': 
                    m_sub_menu_1()
                case '2': 
                    m_sub_menu_2()
                case '3':
                    m_option_3()

def m_option_3():
    print('Main Menu - Option 3')


def m_sub_menu_1():
    menu_choice = ""
    while menu_choice.upper() != "X":
        print()
        print(f'Sub Menu 1')
        print(f'==========')
        print(f'1. Sub Sub Menu 1')
        print(f'2. Option 2')
        print(f'3. Option 3')
        print(f'X. Exit')
        print()
        menu_choice = input('Your Choice:')
        print()
        if len(menu_choice) >= 1:
            match menu_choice:
                case '1': 
                    m1_sub_menu_1()
                case '2': 
                    m1_option_2()
                case '3':
                    m1_option_3()

def m1_option_2():
    print('Sub Menu 1 - Option 2')

def m1_option_3():
    print('Sub Menu 1 - Option 3')


def m_sub_menu_2():
    menu_choice = ""
    while menu_choice.upper() != "X":
        print()
        print(f'Sub Menu 2')
        print(f'==========')
        print(f'1. Option 1')
        print(f'2. Option 2')
        print(f'X. Exit')
        print()
        menu_choice = input('Your Choice:')
        print()
        if len(menu_choice) >= 1:
            match menu_choice:
                case '1': 
                    m2_option_1()
                case '2': 
                    m2_option_2()

def m2_option_1():
    print('Sub Menu 2 - Option 1')

def m2_option_2():
    print('Sub Menu 2 - Option 2')


def m1_sub_menu_1():
    menu_choice = ""
    while menu_choice.upper() != "X":
        print()
        print(f'Sub Sub Menu 1')
        print(f'==============')
        print(f'1. Option 1')
        print(f'2. Option 2')
        print(f'X. Exit')
        print()
        menu_choice = input('Your Choice:')
        print()
        if len(menu_choice) >= 1:
            match menu_choice:
                case '1': 
                    m11_option_1()
                case '2': 
                    m11_option_2()

def m11_option_1():
    print('Sub Sub Menu 1 - Option 1')

def m11_option_2():
    print('Sub Sub Menu 1 - Option 2')



## The main program starts here.
main_menu()
