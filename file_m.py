import parser
import method
def f(r):
    n = len(r)
    if n!=2:
        print("Невверный ввод")
    else:
        try:
            par = parser.parse_file(r[1])
            result = method.gaus(par[0], par[1], par[2])
            if (result == False): return
            print("Ответ: ", end="")
            print(*result[0])
            print(f"Количество итераций: {result[2]}")
            print(f'Норма: {result[1]}')
            print("Погрешности: ", end='')
            print(*result[-1])
        except:
            print("Неверное имя файла")