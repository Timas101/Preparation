def f(x):
    return all(x % d for d in range(2, int(x**0.5)+1))

# Найдем количество подходящих значений A
count = sum(f(a) for a in range(1, 11_111+1))

print(count)