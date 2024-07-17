def drop_consecutive(s: str) -> str:
    while True:
        new_s = []
        i = 0
        while i < len(s):
            count = 1
            while i + 1 < len(s) and s[i] == s[i + 1]:
                count += 1
                i += 1
            if count < 3:
                new_s.append(s[i])
            i += 1
        new_s = ''.join(new_s)
        if new_s == s:
            break
        s = new_s
    return s


def replace_consecutive(s: str) -> str:
    while True:
        new_s = []
        i = 0
        while i < len(s):
            count = 1
            while i + 1 < len(s) and s[i] == s[i + 1]:
                count += 1
                i += 1
            if count >= 3:
                new_s.append(chr(ord(s[i]) - 1))
            else:
                new_s.append(s[i])
            i += 1
        new_s = ''.join(new_s)
        if new_s == s:
            break
        s = new_s
    return s


# Testing the functions
input_str1 = "aabcccbbad"
input_str2 = "abcccbad"

print("Stage 1 Output for '{}': {}".format(input_str1, drop_consecutive(input_str1)))
print("Stage 2 Output for '{}': {}".format(input_str2, replace_consecutive(input_str2)))