def dot_product(vec1, vec2):
    return sum(x * y for x, y in zip(vec1, vec2))

vec1 = [1, 2, 3]
vec2 = [4, 5, 6]

print(f"Dot Product: {dot_product(vec1, vec2)}")
