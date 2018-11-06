def digit_sum(num):
    result = 0
    for c in str(num):
        result += int(c)
    return result

def digit_sum_nonstr(num):
    result = 0
    while num > 0:
        result += num % 10
        num = num // 10
    return result

def is_harshad(num):
    return num % digit_sum(num) == 0
    # return num % digit_sum_nonstr(num) == 0

def main():
    for i in range(1, 201):
         if is_harshad(i):
            print(i)
            
main()
