
def countUniques(a):
    num_list = list()
    for num in a:
        if num not in num_list:
            num_list.append(num)

    return len(num_list)

def solution(a):
    min_len = 0
    for str in a:
        if min_len < len(str):
            max_len = len(str)


# def h(a) :
#     s = 0
#     while a//1 != 0 :
#         s += (a%10)**2
#         a = int(a/10)
#     return (s)
#
# a = int(input())
#
# #각 자릿수의 제곱합이 1혹은 4가 될때 까지 반복해서 구해주는 반복문
# while 1 :
#     a = h(a)
#     if a == 4 :
#         print('UNHAPPY')
#         break
#     elif a == 1 :
#         print('HAPPY')
#         break

def sol(a):
    sum = 0
    while a//1 != 0:
        sum += (a % 10)**2
        a = int(a/10)
    if sum == 1:
        return True
    else:
        return False


def happynum(n):
    num = [n]
    while n != 1 or n < pow(10, 9):
        k = 0
        for i in str(n):
            k += int(i) ** 2
        n = k
        num.append(k)
        continue
    return print(num)


def result(n):
    if happynum(n).count(n) >= 2:
        return print("Unhappy Number")
    elif happynum(n).count(n) == 1:
        return print("Happy Number")


def happyNumber(n):
    number = ",".join(str(n)).split(",")
    while 1:
        result = 0
        for i in range(0,len(number)):
            result += int(number[i])**2
        if result == 1:
            return True
        elif result == n:
            return False
        else:
            number = ",".join(str(result)).split(",")
            continue

if __name__ == "__main__":
    print(happyNumber(19))