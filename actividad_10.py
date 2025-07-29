products = {}
try:
    start_prod = int(input("Cuántos productos desea agregar: "))
    for new_product in range(start_prod):
        product_validation = False
        #Validación de ID
        while not product_validation:
            id_prod = input("Coloque el código del producto: ")
            if id_prod in products:
                print("Ese código ya existe...")
            else:
                product_validation = True
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

        positive_int = False
        #Validación de entero positivo
        while not positive_int:
            p_stock_remaining = int(input("Cuánto de este producto hay en stock: "))
            if p_stock_remaining <= 0:
                print("Eso no es un número válido")
            else:
                positive_int = True

        products[id_prod] = {
            "nombre":p_name,
            "category": p_type,
            "talla": p_size,
            "precio": p_price,
            "stock": p_stock_remaining
        }

    print("Estos son los productos registrados: ")
    for id, item in products.items():
        print(f"Código: {id}\nNombre: {item["nombre"]}\nCategoría: {item["category"]}\n"
              f"Talla: {item["talla"]}\nPrecio: Q.{item["precio"]}\nCantidad en inventario: {item["stock"]}\n")




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


