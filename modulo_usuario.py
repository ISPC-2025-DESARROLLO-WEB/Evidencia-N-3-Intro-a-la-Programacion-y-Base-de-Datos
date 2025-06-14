class Usuario:
    def __init__(self, nombre, email, contraseña, rol, id_usuario=None):
        
        self.__id_usuario = id_usuario  
        self.nombre = nombre            
        self.email = email              
        self.__contraseña = contraseña  
        self.rol = rol                  

    @property
    def id_usuario(self):
        return self.__id_usuario

    def get_contraseña(self):
        return "********"  

    def set_contraseña(self, nueva_contraseña):
        self.__contraseña = nueva_contraseña

    def ver_datos(self):
        print("----------- INFORMACION PERSONAL ----------")
        return (
            f"Id_Usuario: {self.__id_usuario}\n"
            f"Nombre: {self.nombre}\n"
            f"Email: {self.email}\n"
            f"Contraseña: {self.get_contraseña()}\n"
            f"Rol: {self.rol}\n"
        )
