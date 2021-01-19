import random

ran_num = ["0", "0", "0"]
ran_num[0] = str(random.randrange(1, 9, 1))
ran_num[1] = ran_num[0]
ran_num[2] = ran_num[0]
while (ran_num[0] == ran_num[1]):
    ran_num[1] = str(random.randrange(1, 9, 1))
while (ran_num[0] == ran_num[2] or ran_num[1] == ran_num[2]):
    ran_num[2] = str(random.randrange(1, 9, 1))
 
t_count = 0 
s_count = 0 
b_count = 0 
 
print("\n")
while ( s_count < 3 ):
    num = str(input("숫자를 입력하시오"))
    
    s_count = 0
    b_count = 0
 
    for i in range(0, 3):
        for j in range(0, 3):
            if(num[i] == str(ran_num[j]) and i == j):
                s_count += 1
            elif(num[i] == str(ran_num[j]) and i != j):
                b_count += 1
    print("\n[", s_count, "] strike [", b_count, "] ball\n")
    t_count += 1
print("정답")
