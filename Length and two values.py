def alternate(n, first_value, second_value):
    if n <= 0:
        return []

    result = []
    for i in range(n):
        result.append(first_value if i % 2 == 0 else second_value)

    return result