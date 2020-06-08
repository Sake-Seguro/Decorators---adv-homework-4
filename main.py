

from datetime import datetime


class Logger:

    def __init__(self, path, mode='rt', encoding='utf-8'):
        self.file = open(path, mode)

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


def decorator(function_for_decoration):

    """
    Writing into a file date & time of the fucntion execution, its name and arguments

    """

    print(f"\nThis function -- {function_for_decoration} -- to be decorated\n")

    def modifying_function(*args):

        with Logger("logs.txt", 'w', encoding='utf-8') as file:
          
            start_time = datetime.now()
            file.write(f'\nThe function {function_for_decoration} was initiated at  - {start_time}.\n')
            print(f'\nThe function {function_for_decoration} was initiated at - {start_time}.\n')
            result = function_for_decoration(*args)
            arg = args
            file.write(f'\nThe following arguments {arg} were transmitted into this function -- {function_for_decoration}.\n')
            print(f'\nThe following arguments {arg} were transmitted into this function -- {function_for_decoration}.\n')
            file.write(f'\nThe function ended with the following result - {result}.\n')
            print(f'\nThe function ended with the following result - {result}.\n')
            stop_time = datetime.now()
            file.write(f'\nThe time of the function {function_for_decoration} ending - {stop_time}.\n')
            print(f'\nThe time of the function {function_for_decoration} ending - {stop_time}.\n')
            return result
    return modifying_function


def modifying_decorator(file):

    """
    Modified decorator with a required parameter - log_path

    """
    def specy_decorator(function_for_decoration):

        print(f'\nThe function to be decorated with predefined parameters is {function_for_decoration}.\n')

        def modifying_function(*args):

            nonlocal file
            with Logger(file, 'w', encoding='utf-8') as file:
                start_time = datetime.now()
                file.write(f'\nThe function {function_for_decoration} was called up at {start_time}.\n')
                print(f'\nThe function {function_for_decoration} was called up at {start_time}.\n')
                sec_result = function_for_decoration(*args)
                arg = args
                file.write(f'\nThe arguments {arg} were applied within this function {function_for_decoration}.\n')
                print(f'\nThe arguments {arg} were applied within this function {function_for_decoration}.\n')
                file.write(f'\nThe result of this operation is {sec_result}.\n')
                print(f'\nThe result of this operation is {sec_result}.\n')
                stop_time = datetime.now()
                file.write(f'\nThe function {function_for_decoration} ended its operation at {stop_time}.\n')
                print(f'\nThe function {function_for_decoration} ended its operation at {stop_time}.\n')
                return sec_result
        return modifying_function
    return specy_decorator


@decorator
def polish_notation(operation_sym, number_1, number_2):
    """
    Reminding the very Polish notation :))
    Realizing arythmetic actions

    """
    if operation_sym == '*':
        result = number_1 * number_2
    elif operation_sym == '/':
        try:
            result = number_1 / number_2
        except ZeroDivisionError:
            print(f'\nIt is impossible to divide by 0.\n')
            result = number_1
    elif operation_sym == '-':
        result = number_1 - number_2
    elif operation_sym == '+':
        result = number_1 + number_2
    return result


@modifying_decorator('logs-ver-2.txt')
def main():

    """
    Making our program work

    """
    your_input = input('Enter your Polish notation: e.g. + 2 9: ').split()

    try:
        operation_sym, number_1, number_2 = your_input
    except ValueError:
        print('\nYou entered more arguments than required. Please, try again.')
        return
    operation_sym = str(operation_sym)
    assert operation_sym in ['*', '/', '+', '-'], 'This command is not supported. Please, try again.'
    try:
        number_1 = int(number_1)
    except ValueError:
        print(f'\nThe number you entered {number_1} is not a positive integer required.')
        return
    try:
        number_2 = int(number_2)
    except ValueError:
        print(f'\nThe number you entered {number_2} is not a positive integer required.')
        return
    result = polish_notation(operation_sym, number_1, number_2)
    print('\nYour Polish notation is cited below:')
    print(f'{number_1} {operation_sym} {number_2} = {result}')


if __name__ == '__main__':

  main()


