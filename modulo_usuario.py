class Usuario:
    def __init__(self, id_usuario, nombre, email, contraseña, rol): #Creación de una instancia para la clase usuario, utilizando el constructor "__init__". Datos que se deben proporcionar para crear el objeto
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.email = email #Asignar el valor del parametro email al atributo email del objeto
        self.contraseña = contraseña
        self.rol = rol

    def ver_datos(self): #Definimos el metodo Ver_datos
        print("----------- INFORMACION PERSONAL ----------")
        return (
            f"Id_Usuario: {self.id_usuario}\n"
            f"Nombre: {self.nombre}\n" 
            f"Email: {self.email}\n" 
            f"Contraseña: {self.contraseña}\n"
            f"Rol: {self.rol}\n"
            )
