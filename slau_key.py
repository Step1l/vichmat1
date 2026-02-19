import method
def slau_key(r):
    n = len(r)
    if n != 2:
        print("Inccorect input")
        return
    if r[1].isdigit():
        n = int(r[1])
        if n <= 0 or n > 20:
            print("Incorrect deg")
            return
        print("enter rows of the matrix slau")
        matr = []
        for i in range(n):
            str = input().split()
            if len(str) != n:
                print("Incorrect input")
                break
            try:
                str_i = [float(k) for k in str]
                matr.append(str_i)
            except:
                print("Incorrect input")
                break

        else:
            print("print right column of the augmented matrix")
            try:
                b = input().split()
                b_i = [int(l) for l in b]

            except:
                print("Incorrect input")
                return

            print("print Accuracy")
            try:
                acc = float(input().replace(',', '.'))
            except:
                print("Inccorect input")
                return

            result= method.gaus(matr, b_i, acc)
            if (result==False): return
            print("Ответ: " ,end ="")
            print(*result[0])
            print(f"Количество итераций: {result[2]}")
            print(f'Норма: {result[1]}')
            print("Погрешности: ", end='')
            print(*result[-1])

        return

    else:
        print("Incorrect input")
        return