products = {}
try:
    start_prod = int(input("Cuántos productos desea agregar: "))
    for new_product in range(start_prod):
        id_prod = input("Coloque el código del producto: ")
        p_name = input("Coloque el nombre del producto: ")
        p_type = input("Coloque la categoría del producto: ")
        p_size = input("Coloque la talla del producto: ")
        real_price = False
        #Verificación de precio
        while not real_price:
            p_price = int(input("Coloque el precio del producto: "))
            if p_price <= 0:
                print("Ese no puede ser un valor para el precio")
            else:
                real_price = True

        p_stock_remaining = int(input("Cuánto de este producto hay en stock: "))
except ValueError:
    print("Eso no es un número, intente de nuevo")
    """
    Código (por ejemplo: "P001").
    Nombre del producto (ej. "Playera Deportiva").
    Categoría (ej. "Hombre", "Mujer", "Niño").
    Talla (S, M, L, XL).
    Precio unitario (mayor a Q0.00).
    Cantidad en stock (entero positivo).
    """


