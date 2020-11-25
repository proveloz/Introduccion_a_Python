def pattern_writer(n):
    j = 0
    k = n - 1
    letra=""
    espacios=""
    while j < n and k > -1:
        for t in range(n):
            if t == j or t == k:
                letra+=("x")
            else:
                espacios+=("")    
        j += 1
        k -= 1
        print(letra+espacios)
pattern_writer(5)