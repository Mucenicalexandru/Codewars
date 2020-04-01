def get_middle(s):
    0 < len(s) < 1000
    if len(s) % 2 != 0:
        x = len(s)
        y = (x - 1) / 2
        return s[int(y)]
    else:
        q = len(s)
        w = int((q - 1) / 2)
        r = int((q + 1) / 2)
        string = s[w]+s[r]
        return string
