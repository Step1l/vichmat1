import random
import method
def generate_random_system(n, min_val=-10, max_val=10):

    matrix = [[random.uniform(min_val, max_val) for _ in range(n)] for _ in range(n)]
    b = [random.uniform(min_val, max_val) for _ in range(n)]
    return matrix, b


def generate_diagonally_dominant_system(n, min_val=-10.0, max_val=10.0, dominance_factor=1.0):
    matrix = []
    for i in range(n):

        row = [random.uniform(min_val, max_val) for _ in range(n)]
        sum_others = sum(abs(row[j]) for j in range(n) if j != i)

        diag = sum_others + dominance_factor + random.uniform(0, 1)
        if random.choice([True, False]):
            diag = -diag
        row[i] = diag
        matrix.append(row)

    b = [random.uniform(min_val, max_val) for _ in range(n)]

    return matrix, b

def rand(r):
    n = len(r)
    if n!=2:
        print("Невверный аргумент")
    else:
        if r[1].isdigit():
            k = int(r[1])
            if k<=0:
                print("Агрумент не натуральное число")
                return
            matr,b = generate_random_system(k)
            try :
                print("Введите точность")
                eps = float(input().replace(',', '.'))
                result = method.gaus(matr, b, eps)
                if (result == False): return
                print("Ответ: ", end="")
                print(*result[0])
                print(f"Количество итераций: {result[2]}")
                print(f'Норма: {result[1]}')
                print("Погрешности: ", end='')
                print(*result[-1])
            except:
                print("Это не правильный формат числа")
        else:
            print("Аргумент не натуральное чисол")
            return


def rrand(r):
    n = len(r)
    if n!=2:
        print("Невверный аргумент")
    else:
        if r[1].isdigit():
            k = int(r[1])
            if k<=0:
                print("Агрумент не натуральное число")
                return
            matr,b = generate_diagonally_dominant_system(k)
            try :
                print("Введите точность")
                eps = float(input().replace(',', '.'))
                result = method.gaus(matr, b, eps)
                if (result == False): return
                print("Ответ: ", end="")
                print(*result[0])
                print(f"Количество итераций: {result[2]}")
                print(f'Норма: {result[1]}')
                print("Погрешности: ", end='')
                print(*result[-1])
            except:
                print("Это не правильный формат числа")
        else:
            print("Аргумент не натуральное чисол")
            return

