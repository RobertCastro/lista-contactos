from Mundo.Contacto import Contacto

class ListaDeContactos:
    def __init__(self):
        self.contactos = []

    def darTodosLosContactos(self):
        return [f"{contacto.darNombre()} {contacto.darApellido()}" for contacto in self.contactos]

    def buscarContactosPalabraClave(self, palabra):
        return [f"{contacto.darNombre()} {contacto.darApellido()}" for contacto in self.contactos if contacto.contienePalabraClave(palabra)]

    def buscarContacto(self, nombre, apellido):
        for contacto in self.contactos:
            if contacto.darNombre() == nombre and contacto.darApellido() == apellido:
                return contacto
        return None

    def agregarContacto(self, nombre, apellido, direccion, correo, telefonos, palabras):
        if self.buscarContacto(nombre, apellido) is None:
            nuevo_contacto = Contacto(nombre, apellido, direccion, correo)
            for telefono in telefonos:
                nuevo_contacto.agregarTelefono(telefono)
            for palabra in palabras:
                nuevo_contacto.agregarPalabra(palabra)
            self.contactos.append(nuevo_contacto)
            return True
        else:
            return False

    def eliminarContacto(self, nombre, apellido):
        contacto = self.buscarContacto(nombre, apellido)
        if contacto:
            self.contactos.remove(contacto)
            return True
        return False

    def modificarContacto(self, nombre, apellido, direccion, correo, telefonos, palabras):
        contacto = self.buscarContacto(nombre, apellido)
        if contacto:
            contacto.cambiarDireccion(direccion)
            contacto.cambiarCorreo(correo)
            contacto.telefonos = telefonos
            contacto.palabras = palabras
            return True
        return False

    def actualizarTelefonos(self, telefonos, contacto):
        if contacto in self.contactos:
            contacto.telefonos = telefonos
            return True
        return False

    def actualizarPalabras(self, palabras, contacto):
        if contacto in self.contactos:
            contacto.palabras = palabras
            return True
        return False

    def metodo1(self):
        pass

    def metodo2(self):
        pass
