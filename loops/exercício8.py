def primo(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
 
for i in range(1, 51):
    if primo(i):
        print(i)