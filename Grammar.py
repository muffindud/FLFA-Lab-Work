def min_len_index(arr):
    m = 0
    for i in range(len(arr)):
        if len(arr[i]) < len(arr[m]):
            m = i
    return m


class Grammar:
    vn = []
    vt = []
    p = {}
    s = ''

    def __init__(self, vn, vt, p, s):
        self.vn = vn
        self.vt = vt
        self.p = p
        self.s = s

    # Check if a string is valid (terminal)
    def check(self, s):
        return not any(c not in self.vt for c in s)

    def generate_string(self):
        passes = 0
        strings = []
        final_strings = []
        string = self.s
        strings.append(string)
        while len(final_strings) < 5 and passes <= 100:
            passes += 1 # Prevent infinite loop



            if self.check(string) and string not in final_strings:
                final_strings.append(string)
                string = strings[-1]

        return final_strings, strings
