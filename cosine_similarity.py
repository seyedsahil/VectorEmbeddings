import math


def vector_magnitude(vector: list[float]) -> float:
    return math.sqrt(sum([value ** 2 for value in vector]))


def vector_dot_product(vector1: list[float], vector2: list[float]) -> float:
    return sum(value1 * value2 for value1, value2 in zip(vector1, vector2))


def cosine_similarity(vector1: list[float], vector2: list[float]) -> float:
    if len(vector1) != len(vector2):
        raise ValueError("Vectors should be of same length")

    return vector_dot_product(vector1, vector2) / (vector_magnitude(vector1) * vector_magnitude(vector2))

def main():
    vector_a = [1, 2, 3]
    vector_b = [4, 5, 6]
    print(f'cosine_similarity({vector_a}, {vector_b}) = {cosine_similarity(vector_a, vector_b)}')

main()