class Usuario:
    def __init__(self, id_usuario, nombre, email, contraseña, rol):
        # Atributos con acceso protegido (convención: _nombre)
        self._id_usuario = id_usuario
        self._nombre = nombre
        self._email = email
        self._contraseña = contraseña
        self._rol = rol

    # Método getter para ver los datos del usuario
    def ver_datos(self):
        print("----------- INFORMACIÓN PERSONAL ----------")
        return (
            f"Id Usuario: {self._id_usuario}\n"
            f"Nombre: {self._nombre}\n" 
            f"Email: {self._email}\n" 
            f"Contraseña: {self._contraseña}\n"
            f"Rol: {self._rol}\n"
        )

   
    