# Reto_2_Actividad_Final
Reto_2_Actividad_Final_&lt;Cesar Lopez>
Sistema de Gestión de Vehículos y Conductores
Contexto General del Reto
La empresa Transporte Seguro S.A. necesita modelar digitalmente su operación básica.
Actualmente toda la información se maneja en papel, y desean un sistema sencillo —pero bien diseñado— que les permita gestionar:

Conductores
Vehículos (Moto, Carro y Camión)
Relaciones entre ellos
Reglas de negocio especializadas según el tipo de vehículo

El sistema debe:

Registrar conductores con datos validados (nombre, documento, licencia).
Crear distintos vehículos con atributos encapsulados.
Aplicar reglas diferenciadas según el tipo:
Moto → requiere casco obligatorio.
Carro → requiere revisión técnico-mecánica vigente.
Camión → requiere planilla de carga y máximo peso permitido.
Asignar un conductor a un vehículo (Agregación).
Iniciar una jornada de trabajo para cada vehículo (Polimorfismo).

Implementar:

Clase abstracta Vehículo
Subclases: Moto, Carro, Camión
Interfaz Movible con método mover()
Composición: Cada vehículo tiene un Motor
Agregación: Un vehículo puede existir sin conductor
