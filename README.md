# Parcial_1_Progra
Parcial 1 Bloque 1, python

Integrantes:
Franklin Aldahir Portillo Flores. 
Codigo de estudiante:
SMSS011624.

Preguntas y Respuestas
1. ¿Qué ventajas tiene en comparación con poner todo el código en un solo archivo o utilizar módulos?
Dividir el proyecto en módulos ofrece varias ventajas:
Organización y claridad: cada archivo tiene una responsabilidad específica, lo que facilita la lectura y comprensión del código.
Mantenibilidad: es más sencillo localizar y modificar una parte del programa sin afectar al resto.
Reutilización: las clases y métodos pueden ser usados en otros proyectos o ampliaciones futuras sin tener que reescribir el código.
Colaboración: permite que varias personas trabajen al mismo tiempo en diferentes archivos sin generar tantos conflictos en el repositorio.
En cambio, si todo estuviera en un solo archivo, sería más difícil de leer, de depurar y de mantener a largo plazo.

2. ¿Cómo aplicaron la Programación Orientada a Objetos en su solución? Describan el papel de las clases creadas.
Aplicamos la POO usando clases e herencia para representar los aparatos eléctricos:
Clase base AparatoElectrico: contiene atributos comunes como nombre, potencia, horas de uso y tarifa, además de métodos para calcular consumo y costo.
Subclases (Refrigerador, Televisor, AireAcondicionado, Iluminacion): heredan de AparatoElectrico y permiten diferenciar los distintos tipos de aparatos.
Clase SistemaConsumo: funciona como un gestor que almacena todos los aparatos, muestra la lista de registros y calcula el consumo y costo total.
De esta forma, cada clase tiene un rol definido y se aplica la herencia para evitar repetir código.

3. ¿De qué manera el uso de GitHub facilitó el trabajo colaborativo en equipo? Den un ejemplo concreto.
El uso de GitHub facilitó el trabajo en equipo porque permitió:
Tener un repositorio centralizado donde se guarda el código actualizado.
Crear ramas (branches) para que cada integrante trabaje en su parte sin afectar lo que hace el otro.
Usar commits y mensajes descriptivos para llevar un historial de cambios.
Hacer pull requests y revisiones antes de integrar el código final.
Ejemplo concreto: mientras un integrante trabajaba en las clases de modelos/, el otro podía avanzar en el archivo gestor.py o en el main.py. Luego, ambos subieron sus cambios y se fusionaron en la rama principal sin sobrescribir el trabajo del otro.


# Parcial 1 - Programación

## 1. Requisitos previos

* Python 3.8 o superior instalado en el sistema.
* Clonar o descargar este repositorio.

Clonación con Git:

```bash
git clone https://github.com/dornens/Parcial_1_Progra.git
```

## 2. Estructura del proyecto

El proyecto está organizado de la siguiente forma:

```
Parcial_1_Progra/
│── main.py                  # Programa principal
│
├── modelos/                 # Clases de los aparatos
│   ├── refrigerador.py
│   ├── televisor.py
│   ├── aire_acondicionado.py
│   ├── iluminacion.py
│
├── sistema/                 # Lógica de gestión
│   └── gestor.py
```

## 3. Ejecución del programa

Desde la carpeta principal, ejecutar:

```bash
python main.py
```

## 4. Menú principal

El programa muestra el siguiente menú:

```
Seleccione un aparato eléctrico:
1. Refrigerador
2. Televisor
3. Aire Acondicionado
4. Iluminación
5. Ver listado de aparatos
0. Salir
```

## 5. Opciones del menú

* **1. Refrigerador**

* **2. Televisor**

* **3. Aire Acondicionado**

* **4. Iluminación**

  * Para cada opción, el sistema solicitará:

    * Potencia en watts
    * Horas de uso diario
    * Costo por kWh en dólares
  * Se registrará el aparato con su consumo calculado.

* **5. Ver listado de aparatos**

  * Muestra todos los aparatos registrados y su consumo.
  * Presenta también un resumen del consumo y costo total.

* **0. Salir**

  * Finaliza el programa mostrando un reporte de los aparatos ingresados.

## 6. Validaciones

* No se permiten valores negativos.
* Si se ingresa texto en lugar de un número, se pedirá reintentar.
* Se recomienda no ingresar más de 24 horas como uso diario.

## 7. Ejemplo de uso

```
Seleccione un aparato eléctrico:
1. Refrigerador
2. Televisor
3. Aire Acondicionado
4. Iluminación
5. Ver listado de aparatos
0. Salir
Ingrese su opción: 2
Ingrese potencia en watts: 150
Ingrese horas de uso diario: 5
Ingrese costo por kWh en $: 0.20
Televisor agregado con éxito
```

