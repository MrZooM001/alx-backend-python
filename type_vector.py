Vector = list[float]

def scale(scaler: float, vector: Vector) -> Vector:
    return [scaler * num for num in vector]

new_vector = scale(2.0, [1.0, -4.2, 5.4])
print(new_vector)
