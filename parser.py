import sys

def parse_file(filename):

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Ошибка: файл '{filename}' не найден.")
        sys.exit(1)
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        sys.exit(1)

    stripped_lines = [line.rstrip('\n\r') for line in lines]


    blocks = []
    current_block = []
    for line in stripped_lines:
        if line.strip() == '':

            if current_block:
                blocks.append(current_block)
                current_block = []
        else:
            current_block.append(line)
    if current_block:
        blocks.append(current_block)


    if len(blocks) != 3:
        print(f"Ошибка: ожидалось 3 блока (матрица, вектор b, eps), получено {len(blocks)}.")
        sys.exit(1)

    matrix_lines = blocks[0]
    if not matrix_lines:
        print("Ошибка: блок матрицы пуст.")
        sys.exit(1)

    n = len(matrix_lines)
    matrix = []
    for i, line in enumerate(matrix_lines):
        parts = line.strip().split()

        if len(parts) != n:
            print(f"Ошибка в матрице, строка {i+1}: ожидалось {n} элементов, получено {len(parts)}.")
            sys.exit(1)
        try:
            row = [float(x) for x in parts]
        except ValueError:
            print(f"Ошибка в матрице, строка {i+1}: элемент не является числом.")
            sys.exit(1)
        matrix.append(row)

    # ----- Парсим второй блок: вектор b -----
    b_lines = blocks[1]
    if len(b_lines) != 1:
        print(f"Ошибка: блок вектора b должен содержать одну строку, получено {len(b_lines)}.")
        sys.exit(1)

    b_parts = b_lines[0].strip().split()
    if len(b_parts) != n:
        print(f"Ошибка: размер вектора b ({len(b_parts)}) не совпадает с размером матрицы ({n}).")
        sys.exit(1)

    try:
        b = [float(x) for x in b_parts]
    except ValueError:
        print("Ошибка: вектор b содержит нечисловые значения.")
        sys.exit(1)


    eps_lines = blocks[2]
    if len(eps_lines) != 1:
        print(f"Ошибка: блок eps должен содержать одну строку, получено {len(eps_lines)}.")
        sys.exit(1)

    eps_str = eps_lines[0].strip().replace(',', '.')
    try:
        eps = float(eps_str)
    except ValueError:
        print("Ошибка: eps должно быть числом с плавающей точкой.")
        sys.exit(1)

    return matrix, b, eps


