from random import randrange

def eeoo():
    with open('chaplin.txt') as f:
        for line in f:
            if 'ee' in line or 'oo' in line:
                print(line)

def random_numbers():
    rand_nums = []
    for _ in range(1000):
        rand_nums.append(randrange(1000000))
    rand_nums = sorted(rand_nums)

    with open('random-numbers.txt', 'w') as f:
        for line in rand_nums:
            print(line, file=f)

def new_filename(original_name):
    i = original_name.rfind('.')
    if i != -1:
        return original_name[:i] + '_nonempty' + original_name[i:]
    else:
        return original_name + '_nonempty'

def remove_empty(filename):
    deleted_lines = 0
    with open(filename) as original_file:
        with open(new_filename(filename), 'w') as new_file:
            for line in original_file:
                if line == '' or line.isspace():
                    deleted_lines += 1
                else:
                    print(line.rstrip(), file=new_file)

    print('Deleted {} blank lines.'.format(deleted_lines))
