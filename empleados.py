# B) Implementación del método mostrarSalarios:

class Empleado:
    def __init__(self, dni, nombre, apellido, anio_ingreso):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.anio_ingreso = anio_ingreso

    def calcular_salario(self):
        pass  # Implementar en las subclases

    def empleadoConMasClientes(empleados):
    return max(empleados, key=lambda emp: emp.clientes_captados)

    empleado_mas_clientes = empleadoConMasClientes(empleados)
    print(f"Empleado con más clientes captados: {empleado_mas_clientes.nombre} ({empleado_mas_clientes.clientes_captados} clientes)")

class EmpleadoComision(Empleado):
    def __init__(self, dni, nombre, apellido, anio_ingreso, salario_minimo, clientes_captados, monto_por_cliente):
        super().__init__(dni, nombre, apellido, anio_ingreso)
        self.salario_minimo = salario_minimo
        self.clientes_captados = clientes_captados
        self.monto_por_cliente = monto_por_cliente

    def calcular_salario(self):
        salario = self.clientes_captados * self.monto_por_cliente
        return max(salario, self.salario_minimo)

class EmpleadoSalarioFijo(Empleado):
    def __init__(self, dni, nombre, apellido, anio_ingreso, sueldo_basico, anios_en_empresa):
        super().__init__(dni, nombre, apellido, anio_ingreso)
        self.sueldo_basico = sueldo_basico
        self.anios_en_empresa = anios_en_empresa

    def calcular_salario(self):
        if self.anios_en_empresa < 2:
            return self.sueldo_basico
        elif 2 <= self.anios_en_empresa <= 5:
            return self.sueldo_basico * 1.05
        else:
            return self.sueldo_basico * 1.10

# Crear 10 empleados
empleados = [
    EmpleadoComision(30285415, "Juan", "Pérez", 2019, 100000, 10, 500),
    EmpleadoSalarioFijo(22658974, "María", "Gómez", 2018, 200000, 3),
    EmpleadoComision(33791852, "Susana", "Pérez", 2022, 100000, 25, 2750),
    EmpleadoComision(4015948, "Pedro", "Martínez", 2017, 100000, 55, 9450),
    EmpleadoComision(25164978, "Esteban", "Watson", 2015, 100000, 33, 3450),
    EmpleadoComision(234012597, "Camila", "Suárez", 2011, 100000, 70, 6850),
    EmpleadoSalarioFijo(24953167, "Estefanía", "Gimenez", 2014, 200000, 10),
    EmpleadoSalarioFijo(26001003, "Juana", "Cáceres", 2017, 200000, 7),
    EmpleadoComision(27531890, "Simón", "Velasquez", 2012, 100000, 60, 1050),
    EmpleadoComision(28679423, "Federica", "Cristaldo", 2021, 100000, 15, 3350),
]

# Mostrar salarios
for empleado in empleados:
    print(f"{empleado.nombre} {empleado.apellido}: ${empleado.calcular_salario():.2f}")
