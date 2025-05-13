N = int(input("請輸入正整數 N: "))

for a in range(1, N + 1):
    for b in range(a + 1, N + 1):
        for c in range(b + 1, N + 1):
            if a * a + b * b == c * c:
                if a + b + c <= N:
                    print(f"{a} {b} {c}")