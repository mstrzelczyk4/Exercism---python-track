def transpose(lines):
    if not lines:
        return ""
    tab = lines.split("\n")
    line_len = max([len(line) for line in tab])
    for i, line in enumerate(tab):
        tab[i] += " " * (line_len - len(tab[i]))
    output = []
    for x in range(line_len):
        temp = ""
        for y in range(len(tab)):
            temp += tab[y][x]
        output.append(temp)
    for i in range(len(output)):
        m = max(len(line.rstrip()) for line in output[i:])
        if len(output[i]) > m:
            output[i] = output[i][0:m]
    return '\n'.join(output)
