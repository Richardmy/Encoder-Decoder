def key_dict_func():

    key_dict = {}

    with open('C:\\Users\\Richard\\source\\repos\\PythonApplication1\\PythonApplication1\\key.txt') as key_f:
        for line in key_f:
            (i, key, val) = line.split()
            key_dict[key] = val
    return key_dict


def key2_dict_func():

    key2_dict = {}

    with open('C:\\Users\\Richard\\source\\repos\\PythonApplication1\\PythonApplication1\\key2.txt') as key2_f:
        for line in key2_f:
            (key, val) = line.split()
            key2_dict[key] = val
    return key2_dict


def parsing_func():

        a = 0
        m = ''
        for char in message:
            m += message[a]
            a += 1
        m = m.replace(' ', '*')
        return m


def message_to_morse(m):

    key_dict = key_dict_func()
    m = m.upper()

    key_dict_keys = list(key_dict.keys())
    key_dict_values = list(key_dict.values())

    # print(key_dict_keys, '\n', key_dict_values, key_dict_values[0])

    for char in m:
        a = 0
        for key in key_dict_keys:
            if char == key:
                m = m.replace(char, key_dict_values[a] + ',')
                m = m.replace(',*', '*')
            a += 1
    return m


def morse_to_binary(b):

    key_dict = key2_dict_func()

    key_dict_keys = list(key_dict.keys())
    key_dict_values = list(key_dict.values())

    # print(key_dict_keys, '\n', key_dict_values, key_dict_values[0])

    for char in b:
        a = 0
        for key in key_dict_keys:
            if char == key:
                b = b.replace(char, key_dict_values[a])
            a += 1
    return b


message = input("Enter message here: ")

print(morse_to_binary(message_to_morse(parsing_func())))




