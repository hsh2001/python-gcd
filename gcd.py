
# gcd(a, b) = gcd(b, r)
# r = a를 b로 나눈 나머지

def gcd(a, b):
    if b == 0:
        return a

    r = a % b

    return gcd(b, r)

first, second = input('두 수를 입력해주세요.').split(' ')

first = int(first)
second = int(second)

print(gcd(first, second))