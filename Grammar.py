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

        for key in self.p:
            self.p[key].sort(key=lambda st: len(st))
            for s in self.p[key]:
                if key in s:
                    for i in range(len(self.p[key])):
                        if self.p[key] == s and i < len(self.p[key]) - 1:
                            self.p[key].pop(i)
                            self.p[key].append(s)

    # Check if a string is valid (terminal)
    def check(self, s):
        return not any(c not in self.vt for c in s)

    def generate_string(self):
        strings = []
        final_strings = []
        string = self.s
        strings.append(string)
        while len(final_strings) < 5:
            for c in string:
                if c in self.vn:
                    ind = 0
                    initial_string = string
                    string = string.replace(c, self.p[c][ind], 1)
                    if string in final_strings:
                        string = initial_string
                        ind += 1
                        string = string.replace(c, self.p[c][ind], 1)

                    if not self.check(string):
                        strings.append(string)

            if self.check(string) and string not in final_strings:
                final_strings.append(string)
                string = strings[-1]

        return final_strings
