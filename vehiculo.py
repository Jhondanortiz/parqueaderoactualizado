class Vehiculo:
    def __init__(self, placa, marca, modelo) -> None:
        self.placa = placa
        self.marca = marca
        self.modelo = modelo

    # Setter para la placa del vehículo
    def set_placa(self, placa):
        self.placa = placa

    # Getter para la placa del vehículo
    def get_placa(self):
        return self.placa

    # Setter para la marca del vehículo
    def set_marca(self, marca):
        self.marca = marca

    # Getter para la marca del vehículo
    def get_marca(self):
        return self.marca

    # Setter para el modelo del vehículo
    def set_modelo(self, modelo):
        self.modelo = modelo

    # Getter para el modelo del vehículo
    def get_modelo(self):
        return self.modelo

# Ejemplo de uso
mi_vehiculo = Vehiculo("ABC123", "Toyota", "Camry")
mi_vehiculo.set_placa("XYZ789")
mi_vehiculo.set_marca("Honda")
mi_vehiculo.set_modelo("Civic")

print("Placa del vehículo:", mi_vehiculo.get_placa())
print("Marca del vehículo:", mi_vehiculo.get_marca())
print("Modelo del vehículo:", mi_vehiculo.get_modelo())
