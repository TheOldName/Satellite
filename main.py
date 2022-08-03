# SATELLITE 0.3.0

import math
from colorama import Fore, Style

# lists
coefficients = []
pre_root_list = []
root_list = []
sqr_eq_coefficients_list = []
final_roots = []

# equation_power
equation_power = int(input(Fore.LIGHTGREEN_EX + Style.DIM + 'Введите степень уравнения: '))

# variables
root = 1
eq = 0
transfer = 0
transfer_1 = 0
transfer_2 = 0
D = 0
xpf_1 = 0
xpf_2 = 0
display_1 = 0
display_2 = 0
output_indicator = 0

# coefficients input
print("Введите коэффициенты:")
for i in range(equation_power + 1):
    coefficients.append(int(input()))

# calculating divisors
for i in range(20):
    if coefficients[-1] % root == 0:
        pre_root_list.append(root)
    if i % 2 == 0:
        root -= i + 2
        root = round(root, 1)
    if i % 2 == 1:
        root += i + 2
        root = round(root, 1)

# calculating divisors-roots
for e in range(len(pre_root_list)):
    for i in range(equation_power + 1):
        eq += coefficients[-i - 1] * (math.pow(pre_root_list[e], i))
    if eq == 0:
        root_list.append(pre_root_list[e])
    eq = 0

for i in range(len(root_list)):
    final_roots.append(root_list[i])

# solving type checking
if len(root_list) + 1 == equation_power:

    # calculating last root (in case if there are one less divisors-roots than all roots)
    for i in range(len(root_list)):
        if coefficients[1] > 0:
            if i == 0:
                transfer_2 = -abs(coefficients[1]) / coefficients[0] - root_list[i]
                display_1 = transfer_2
            else:
                transfer_2 -= root_list[i]
                display_1 = transfer_2
        if coefficients[1] < 0:
            if i == 0:
                transfer_2 = abs(coefficients[1]) / coefficients[0] - root_list[i]
                display_1 = transfer_2
            else:
                transfer_2 -= root_list[i]
                display_1 = transfer_2
        if coefficients[1] == 0:
            transfer_2 -= root_list[i]
            display_1 = transfer_2

    final_roots.append(transfer_2)

    # setting output indicator
    output_indicator = 0

else:

    # checking if equation square or not
    if equation_power >= 3:
        # solving cubic or more power equation
        sqr_eq_coefficients_list.append(1)
        for i in range(len(root_list)):
            if i == 0:
                if coefficients[1] / coefficients[0] < 0:
                    transfer = abs(coefficients[1] / coefficients[0])
                    display_1 = transfer
                if coefficients[1] / coefficients[0] > 0:
                    transfer = -abs(coefficients[1] / coefficients[0])
                    display_1 = transfer
            transfer -= root_list[i]

        sqr_eq_coefficients_list.append(transfer - transfer * 2)

        if equation_power % 2 == 0:
            for i in range(len(root_list)):
                if i == 0:
                    transfer_1 = coefficients[-1] / coefficients[0]
                    display_2 = transfer_1
                transfer_1 /= root_list[i]

        if equation_power % 2 != 0:
            for i in range(len(root_list)):
                if i == 0:
                    if coefficients[-1] / coefficients[0] < 0:
                        transfer_1 = abs(coefficients[-1] / coefficients[0])
                        display_2 = transfer_1
                    if coefficients[-1] / coefficients[0] > 0:
                        transfer_1 = -abs(coefficients[-1] / coefficients[0])
                        display_2 = transfer_1
                transfer_1 /= root_list[i]

        sqr_eq_coefficients_list.append(transfer_1)
        output_indicator = 2

    else:

        # square equation case
        for i in range(len(coefficients)):
            sqr_eq_coefficients_list.append(coefficients[i])
        output_indicator = 1

    # calculating D and two square roots
    D = math.pow(sqr_eq_coefficients_list[1], 2) - 4 * sqr_eq_coefficients_list[0] * sqr_eq_coefficients_list[2]
    if D >= 0:
        if sqr_eq_coefficients_list[1] > 0:
            xpf_1 = (-abs(sqr_eq_coefficients_list[1]) + math.sqrt(D)) / (2 * sqr_eq_coefficients_list[0])
            xpf_2 = (-abs(sqr_eq_coefficients_list[1]) - math.sqrt(D)) / (2 * sqr_eq_coefficients_list[0])
        if sqr_eq_coefficients_list[1] < 0:
            xpf_1 = (abs(sqr_eq_coefficients_list[1]) + math.sqrt(D)) / (2 * sqr_eq_coefficients_list[0])
            xpf_2 = (abs(sqr_eq_coefficients_list[1]) - math.sqrt(D)) / (2 * sqr_eq_coefficients_list[0])
        if sqr_eq_coefficients_list[1] == 0:
            xpf_1 = 0 + math.sqrt(D) / (2 * sqr_eq_coefficients_list[0])
            xpf_2 = 0 - math.sqrt(D) / (2 * sqr_eq_coefficients_list[0])

        final_roots.append(round(xpf_1, 2))
        final_roots.append(round(xpf_2, 2))

# output
print('')

# main equation printing
for i in range(equation_power + 1):
    if i != equation_power:
        if coefficients[i + 1] > 0 and i != equation_power - 1:
            print(Fore.RED + str(abs(coefficients[i])) + 'x' + str(equation_power - i), end=Fore.LIGHTWHITE_EX + ' + ')
        if coefficients[i + 1] < 0 and i != equation_power - 1:
            print(Fore.RED + str(abs(coefficients[i])) + 'x' + str(equation_power - i), end=Fore.LIGHTWHITE_EX + ' - ')
        if coefficients[i + 1] > 0 and i == equation_power - 1:
            print(Fore.RED + str(abs(coefficients[i])) + 'x' + str(equation_power - i), end='')
        if coefficients[i + 1] < 0 and i == equation_power - 1:
            print(Fore.RED + str(abs(coefficients[i])) + 'x' + str(equation_power - i), end='')
        if coefficients[i + 1] == 0 and i == equation_power - 1:
            print(Fore.RED + str(abs(coefficients[i])) + 'x' + str(equation_power - i), end=Fore.LIGHTWHITE_EX + ' + ')
        if coefficients[i + 1] == 0 and i != equation_power - 1:
            print(Fore.RED + str(abs(coefficients[i])) + 'x' + str(equation_power - i), end=Fore.LIGHTWHITE_EX + ' + ')

    if i == equation_power:
        if coefficients[i] > 0:
            print(Fore.LIGHTWHITE_EX + ' + ' + Fore.RED + str(abs(coefficients[i])), end='')
        if coefficients[i] < 0:
            print(Fore.LIGHTWHITE_EX + ' - ' + Fore.RED + str(abs(coefficients[i])), end='')

print(Fore.LIGHTWHITE_EX + ' = ' + Fore.RED + '0')
print('')

# case of cubic or more power equation (including "simple" type)
if output_indicator == 0 or output_indicator == 2:
    print(Fore.LIGHTGREEN_EX + Style.DIM + "Делители свободного члена, являющиеся корнями: ", end='')
    for i in range(len(root_list)):
        if i != len(root_list) - 1:
            print(Fore.LIGHTWHITE_EX + str(round(root_list[i], 2)), ',', end='')
        if i == len(root_list) - 1:
            print(Fore.LIGHTWHITE_EX + str(round(root_list[i], 2)), end='')

    print('')
    print('')

    for i in range(equation_power):
        if i != equation_power - 1:
            print(Fore.BLUE + 'x' + str(i + 1), end=Fore.LIGHTWHITE_EX + ' + ')
        if i == equation_power - 1:
            print(Fore.BLUE + 'x' + str(i + 1), end='')

    if coefficients[1] > 0:
        print(Fore.LIGHTWHITE_EX + ' = ' + Fore.BLUE + str(-abs(coefficients[1]) / coefficients[0]))
    if coefficients[1] < 0:
        print(Fore.LIGHTWHITE_EX + ' = ' + Fore.BLUE + str(abs(coefficients[1]) / coefficients[0]))
    if coefficients[1] == 0:
        print(Fore.LIGHTWHITE_EX + ' = ' + Fore.BLUE + '0')

    # case of "simple" equation
    if output_indicator == 0:
        print('')
        print(Fore.RED + 'x' + str(equation_power) + Fore.LIGHTWHITE_EX + ' = ' + Fore.RED + str(transfer_2))
        print('')
    # case of cubic or more power equation
    if output_indicator == 2:
        for i in range(equation_power):
            if i != equation_power - 1:
                print(Fore.BLUE + 'x' + str(i + 1), end=Fore.LIGHTWHITE_EX + ' * ')
            if i == equation_power - 1:
                print(Fore.BLUE + 'x' + str(i + 1), end='')
        print(Fore.LIGHTWHITE_EX + ' = ' + Fore.BLUE + str(display_2))

        print('')
        for i in range(len(sqr_eq_coefficients_list)):
            if i != len(sqr_eq_coefficients_list) - 1:
                if sqr_eq_coefficients_list[i + 1] > 0 and i != len(sqr_eq_coefficients_list) - 1:
                    print(Fore.RED + str(abs(sqr_eq_coefficients_list[i])) + 'x' +
                          str(len(sqr_eq_coefficients_list) - i - 1), end=Fore.LIGHTWHITE_EX + ' + ')
                if sqr_eq_coefficients_list[i + 1] < 0 and i != len(sqr_eq_coefficients_list) - 1:
                    print(Fore.RED + str(abs(sqr_eq_coefficients_list[i])) + 'x' +
                          str(len(sqr_eq_coefficients_list) - i - 1), end=Fore.LIGHTWHITE_EX + ' - ')
                if sqr_eq_coefficients_list[i + 1] > 0 and i == len(sqr_eq_coefficients_list) - 1:
                    print(Fore.RED + str(abs(sqr_eq_coefficients_list[i])) + 'x' +
                          str(len(sqr_eq_coefficients_list) - i - 1), end='')
                if sqr_eq_coefficients_list[i + 1] < 0 and i == len(sqr_eq_coefficients_list) - 1:
                    print(Fore.RED + str(abs(sqr_eq_coefficients_list[i])) + 'x' +
                          str(len(sqr_eq_coefficients_list) - i - 1), end='')
                if sqr_eq_coefficients_list[i + 1] == 0 and i == len(sqr_eq_coefficients_list) - 1:
                    print(Fore.RED + str(abs(sqr_eq_coefficients_list[i])) + 'x' +
                          str(len(sqr_eq_coefficients_list) - i - 1),
                          end=Fore.LIGHTWHITE_EX + ' + ')
                if sqr_eq_coefficients_list[i + 1] == 0 and i != len(sqr_eq_coefficients_list) - 1:
                    print(Fore.RED + str(abs(sqr_eq_coefficients_list[i])) + 'x' +
                          str(len(sqr_eq_coefficients_list) - i - 1),
                          end=Fore.LIGHTWHITE_EX + ' + ')
            if i == len(sqr_eq_coefficients_list) - 1:
                if sqr_eq_coefficients_list[i] > 0:
                    print(Fore.RED + str(abs(sqr_eq_coefficients_list[i])), end='')
                if sqr_eq_coefficients_list[i] < 0:
                    print(Fore.RED + str(abs(sqr_eq_coefficients_list[i])), end='')
        print(Fore.LIGHTWHITE_EX + ' = ' + Fore.RED + '0')
        print('')

# case of cubic or more power equation or square equation
if output_indicator == 1 or output_indicator == 2:
    print(Fore.LIGHTYELLOW_EX + 'D' + Fore.LIGHTWHITE_EX + ' = ', Fore.LIGHTYELLOW_EX + str(D))
    print(Fore.LIGHTBLUE_EX + 'x1' + Fore.LIGHTWHITE_EX + ' = ', Fore.LIGHTBLUE_EX + str(xpf_1))
    print(Fore.LIGHTRED_EX + 'x2' + Fore.LIGHTWHITE_EX + ' = ', Fore.LIGHTRED_EX + str(xpf_2))
    print('')

# answer
print(Fore.LIGHTGREEN_EX + Style.DIM + 'Ответ: ' + Fore.LIGHTWHITE_EX, end='')
answer = set(final_roots)
print(*answer, sep=', ')
