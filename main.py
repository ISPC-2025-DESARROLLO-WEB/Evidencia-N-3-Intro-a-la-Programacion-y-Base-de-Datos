from modulo_sistema_usuarios import Sistema_De_Usuarios

sistema = Sistema_De_Usuarios()

def menu_principal():
    while True:
        print("----------- MENU PRINCIPAL ----------")
        print("[1] Registrar Usuario.") 
        print("[2] Iniciar Sesion.")
        print("[3] Salir del Menu Principal.")
        opcion = input("Seleccione una de las opciones: ")

        match opcion:
            case "1":
                 ingresar_id_usuario = int(input("Ingrese su Id_Usuario: "))
                 ingresar_nombre = input("Ingrese su Nombre: ")
                 ingresar_email = input("Ingrese su email: ")
                 ingresar_contraseña = input("Ingrese una contraseña: ")
                 ingresar_rol = input("Ingrese su rol: ")
                 print(sistema.registrar_usuario(ingresar_id_usuario, ingresar_nombre, ingresar_email, ingresar_contraseña, ingresar_rol)) #llama al metodo registrar_usuario del objeto sistema para intentar crear el usuario con los datos ingresados

            case "2":
                 ingresar_email = input("Ingrese su email: ")
                 ingresar_contraseña = input("Ingrese una contraseña: ")
                 usuario = sistema.iniciar_sesion(ingresar_email, ingresar_contraseña)
                 if usuario:
                    sistema.menu_interno(usuario)
            
            case "3":
                 print("Usted Salio del Menu Prinicipal.")
                 break
            
            case _:
                print("ERROR!! Usted ingreso una opcion no valida.")

menu_principal()



