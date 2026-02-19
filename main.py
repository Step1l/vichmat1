import method
import rand
import file_m
import slau_key
def pull():
    stroc = ''
    print("Команды:")
    print('slau [n(1-20)] - посчитать систему вручным вводом')
    print('file [filename] - из файла в формате матрицы(на каждой строке строка матрицы элементы через пробел, вектор b , точность, все блоки разделены пустой строчкой)')
    print("random [n] - сгенерировать матрицу и вектор b")
    print("rrandom [n] сгенерировать матрицу с диагональным преобладанием")
    while stroc!="exit":
        stroc = input("$")
        r = stroc.split()
        n = len(r)
        if r[0]=="slau":
            slau_key.slau_key(r)
        elif r[0]=="file":
            file_m.f(r)
        elif  r[0] =="random":
            rand.rand(r)
        elif r[0] =="rrandom":
            rand.rrand(r)
        elif r[0] =="help":
            print("Команды:")
            print('slau [n(1-20)] - посчитать систему вручным вводом')
            print(
                'file [filename] - из файла в формате матрицы(на каждой строке строка матрицы элементы через пробел, вектор b , точность, все блоки разделены пустой строчкой)')
            print("random [n] - сгенерировать матрицу и вектор b")
            print("rrandom [n] сгенерировать матрицу с диагональным преобладанием")

        elif r[0]=="exit":
            continue
        else:
            print("Неверная команда")


pull()


