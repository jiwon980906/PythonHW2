import random
select = random.randint(1, 100)
i = 0
while True:
    i += 1
    userAnswer = int(input("숫자를 입력하시오"))
    if userAnswer > select:
        print("DOWN")
    elif userAnswer < select:
        print("UP")
    else:
        print("RIGHT")
        break