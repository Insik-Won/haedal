num = int(input("다이아몬드의 반지름을 입력하세요: "))

for i in range(1, num + 1):
    print(' ' * (num - i) + '*' * (i * 2 - 1))

for i in range(1, num):
    print(' ' * i + '*' * ((num - i) * 2 - 1))
