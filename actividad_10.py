products = {}
key = True
print("-------Bienvenido al program de boutique-------")
while key:
    ops = input("\nSeleccione una opción:\n1. Agregar productos\n2. Ver productos\n3. Buscar producto\n4. Total de inventario\n5. Productos por categoría\n6. Salir")
    match ops:
        case "1":
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
            except ValueError:
                print("Eso no es un número, intente de nuevo")
        case "2":
            #Display de productos registrados
            print("Estos son los productos registrados: ")
            for id, item in products.items():
                print(f"Código: {id}\nNombre: {item["nombre"]}\nCategoría: {item["category"]}\n"
                      f"Talla: {item["talla"]}\nPrecio: Q.{item["precio"]}\nCantidad en inventario: {item["stock"]}\n")
        case "3":
            #Búsqueda
            searched = input("Coloque el código del producto que busca: ")
            if searched in products:
                print(f"Nombre: {products[searched]["nombre"]}\nCategoría: {products[searched]["category"]}\n"
                      f"Talla: {products[searched]["talla"]}\nPrecio: Q.{products[searched]["precio"]}\nCantidad en inventario: {products[searched]["stock"]}\n")
            else:
                print("Es producto no existe...")
        case "4":
            total = 0
            for id, valuex in products.items():
                total += valuex["precio"]*valuex["stock"]
            print("El total del inventario en este momento es de: {}".format(total))
        case "5":
            pass
        case "6":
            print("Gracias por usar el programa")
            key = False







