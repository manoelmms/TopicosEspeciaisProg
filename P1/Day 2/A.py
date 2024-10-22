def generate_all_strings(string, result, ordem, tam):
    char = 'a'
    if len(string) == tam:
        return
    for i in range(26):            
        if len(string) != 0:
            if char == string[-1]:
                continue
        s = string+char
        if len(string) == tam-1:
            result[s] = ordem
            ordem += 1
        char = chr(ord(char) + 1)
        generate_all_strings(s, result, ordem, tam)

resultado = {}
generate_all_strings('', resultado, 1, 2)
print(resultado)

