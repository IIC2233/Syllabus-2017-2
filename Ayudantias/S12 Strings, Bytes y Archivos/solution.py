# Ayudantía 12 - Archivos y Bytes
__author__ = 'Alejandro Kaminetzky'

# Funciones
# 1) Sumar cuatro bytes
# 2) Reemplazar dígitos
# 3) Espejar bytes


def sum_ints(corrupted_ints):
    fixed_int = sum(corrupted_ints)
    return fixed_int


def replace_digits(corrupted_int):
    replace_dict = {'1': '9', '2': '8', '3': '7', '4': '6', '5': '0'}
    temp_dict = {y: x for x, y in replace_dict.items()}
    replace_dict.update(temp_dict)

    corrupted_string = '{:0>3}'.format(str(corrupted_int))
    fixed_string = ''.join(map(lambda x: replace_dict[x], corrupted_string))
    fixed_int = int(fixed_string)
    return fixed_int


def mirror_int(corrupted_int):
    corrupted_string = str(corrupted_int)
    fixed_string = '{:0>3}'.format(corrupted_string)[::-1]
    fixed_int = int(fixed_string)
    return fixed_int


def fix_bytes(corrupted_bytes):
    fixed_bytes = bytearray()
    for i in range(0, len(corrupted_bytes), 4):
        corrupted_ints = map(lambda x: int(x), corrupted_bytes[i:i+4])
        fixed_int = mirror_int(replace_digits(sum_ints(corrupted_ints)))
        fixed_byte = bytes([fixed_int])
        fixed_bytes.extend(fixed_byte)
    return fixed_bytes


def fix_file(corrupted_file_path, fixed_file_path):
    with open(corrupted_file_path, 'rb') as corrupted_file, \
            open(fixed_file_path, 'wb') as fixed_file:
        fixed_bytes = fix_bytes(corrupted_file.read())
        fixed_file.write(fixed_bytes)


if __name__ == '__main__':
    fix_file('encoded.file', 'fixed_file.jpg')



