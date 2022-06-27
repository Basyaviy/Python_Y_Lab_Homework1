def int32_to_ip(a):
    binary = bin(a)[2:]

    # в случае необходимости дописать нули в начало строки
    while len(binary) < 32:
        binary = '0' + binary

    step = 8
    ip = ""
    for i in range(0, 32, step):
        ip += str(int(binary[i:i + step], 2)) + "."
    return ip[:-1]


ints = [2154959208, 2149583361, 32, 0]
for int32 in ints:
    print(int32_to_ip(int32))

assert int32_to_ip(2154959208) == "128.114.17.104"
assert int32_to_ip(0) == "0.0.0.0"
assert int32_to_ip(32) == "0.0.0.32"
assert int32_to_ip(2149583361) == "128.32.10.1"