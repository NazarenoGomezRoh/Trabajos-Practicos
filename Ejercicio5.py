def romano_a_decimal(num_romano):
    """
    Función que convierte un número romano en un número decimal.
    """
    valores_romanos = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    num_decimal = 0
    valor_previo = 0

    for i in range(len(num_romano)-1, -1, -1):
        valor_actual = valores_romanos[num_romano[i]]

        if valor_actual < valor_previo:
            num_decimal -= valor_actual
        else:
            num_decimal += valor_actual

        valor_previo = valor_actual

    return num_decimal


# Modificar la variable para otro resultado
num_romano = "XXVIII"
num_decimal = romano_a_decimal(num_romano)
print(
    f"El número romano {num_romano} es equivalente a {num_decimal} en decimal.")
