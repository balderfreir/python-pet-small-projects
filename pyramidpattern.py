def pyramid_pattern(char='*', n=7):
    for i in range(n):
        print(' ' * (n - i) + char * (i * 2 + 1))

def pyramid_pattern_v2(char='*', n=7):
    for i in range(n):
        print(' ' * (n - i) + (char + ' ') * (i + 1))

pyramid_pattern()
pyramid_pattern_v2()
