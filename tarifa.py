class Tarifa:
    def __init__(self) -> None:
        self.hora_normal = 0  # Tarifa por hora normal
        self.hora_extra = 0   # Tarifa por hora extra

    def set_hora_normal(self, tarifa_hora_normal):
        self.hora_normal = tarifa_hora_normal

    def get_hora_normal(self):
        return self.hora_normal

    def set_hora_extra(self, tarifa_hora_extra):
        self.hora_extra = tarifa_hora_extra

    def get_hora_extra(self):
        return self.hora_extra

# Ejemplo de uso
tarifa = Tarifa()
tarifa.set_hora_normal(5.0)
tarifa.set_hora_extra(7.0)

print("Tarifa por hora normal:", tarifa.get_hora_normal())
print("Tarifa por hora extra:", tarifa.get_hora_extra())
