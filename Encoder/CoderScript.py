def key_dict_func(path):

    key_dict = {}

    with open(path) as key_f:
        for line in key_f:
            (key, val) = line.split()
            key_dict[key] = val
    return key_dict



def parsing_func():

        a = 0
        m = ''
        for char in message:
            m += message[a]
            a += 1
        m = m.replace(' ', '*')
        return m


def message_to_morse(m):

    key_dict = key_dict_func('C:\\Users\\Richard\\source\\repos\\Encoder-Decoder\\Encoder\\key.txt')
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

    key_dict = key_dict_func('C:\\Users\\Richard\\source\\repos\\Encoder-Decoder\\Encoder\\key2.txt')

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


def write_to_file(encoded_message):

    enc_txt = open('encoded_text.txt', 'w')
    enc_txt.write(encoded_message)


message = input("Enter message here: ")


print(morse_to_binary(message_to_morse(parsing_func())))
write_to_file(morse_to_binary(message_to_morse(parsing_func())))



