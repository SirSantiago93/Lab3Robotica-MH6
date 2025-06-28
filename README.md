# Lab3Robotica-MotomanMH6

## Comparativa entre Motoman MH6 vs ABB IRB140

La selección del robot adecuado depende de factores como la carga que puede levantar, el espacio que necesita para operar, la velocidad de sus movimientos y sus aplicaciones principales. Se presenta una comparación entre dos robots ampliamente utilizados: el **Motoman MH6** de Yaskawa y el **ABB IRB 140**. Ambos modelos son versátiles, compactos y adecuados para tareas de manipulación, ensamblaje y automatización de procesos, aunque presentan diferencias clave que pueden hacer que uno se adapte mejor a ciertas necesidades específicas.

| Característica                | **Motoman MH6**                              | **ABB IRB140**                              |
|-----------------------------|----------------------------------------------|----------------------------------------------|
| **Marca**                   | Yaskawa Motoman                              | ABB Robotics                                 |
| **Carga máxima**            | 6 kg                                         | 6 kg                                         |
| **Alcance máximo**          | 1,420 mm                                     | 810 mm                                       |
| **Grados de libertad**      | 6 ejes (movimientos similares al brazo humano) | 6 ejes (movimientos similares al brazo humano) |
| **Precisión (repetibilidad)**| ±0.08 mm                                     | ±0.03 mm                                     |
| **Peso del robot**          | Aprox. 130 kg                                | Aprox. 98 kg                                 |
| **Formas de instalación**   | Piso, pared o techo                          | Piso, pared, techo o invertido               |
| **Velocidad de movimiento** | Alta (hasta 11.5 m/s combinado)              | Media (hasta 6.5 m/s combinado)              |
| **Aplicaciones comunes**    | Soldadura, ensamblaje, paletizado, manipulación | Ensamblaje, alimentación de máquinas, embalaje, prueba de componentes |
| **Protección ambiental**    | IP54 (protección básica, IP67 en la muñeca)  | IP67 (protección completa contra polvo y agua) |
| **Controlador**             | DX100 o DX200                                | IRC5                                         |
| **Software**                | RoboDK, MotoSim, MotoPlus                    | RobotStudio, RAPID (lenguaje de programación de ABB) |
| **Condiciones de trabajo**  | 0–45 °C, humedad sin condensación            | 5–45 °C, humedad hasta 95% sin condensación  |

## Procedimiento para realizar movimientos manuales

Para iniciar el proceso, el operador debe encender el controlador del robot y esperar a que el sistema complete su arranque. Una vez activo, se debe verificar que el teach pendant esté encendido y que el robot se encuentre libre de errores o alarmas. A continuación, el operador debe asegurarse de que el robot esté configurado en **modo Teach**, lo que permitirá realizar movimientos manuales de manera segura. Este modo puede ser activado desde un selector físico en el panel de control o desde el menú del teach pendant.

El operador puede controlar manualmente el robot en dos modos principales:

- **Modo Articulado (Joint Mode)**: permite mover cada uno de los seis ejes del robot por separado. Es útil para posicionar el robot ajustando individualmente las articulaciones.
- **Modo Cartesiano (Base, World o Tool)**: permite mover el extremo del brazo (usualmente una herramienta) en direcciones lineales (X, Y, Z) o realizar rotaciones alrededor de esos ejes, según un sistema de coordenadas definido.

Para cambiar entre estos modos, se debe presionar el botón `COORD` en el teach pendant. Este botón abre un menú que permite seleccionar el sistema de coordenadas deseado:
- `JOINT` para el modo articulado,
- `BASE` o `WORLD` para coordenadas relativas a la base del robot,
- `TOOL` para coordenadas relativas a la herramienta,
- `USER` si se ha definido un sistema de coordenadas personalizado.

Una vez seleccionado el modo de movimiento adecuado, el operador puede proceder a controlar el robot manualmente.

<div align="center">
  <img src="https://github.com/user-attachments/assets/a8c2c216-be31-4a33-8a2b-cfc170b36f09" alt="image" width="400" />
</div>

En **modo articulado**, se utilizan las teclas del teach pendant correspondientes a cada eje (por ejemplo, `S`, `L`, `U`, `R`, `B`, `T`) para mover individualmente las articulaciones del robot. Cada tecla tiene asociada una dirección positiva (`+`) y negativa (`-`), lo que permite realizar giros o desplazamientos en ambos sentidos.

En **modo cartesiano**, las teclas permiten mover el extremo del brazo robótico (el efector final) de forma lineal o rotacional en el espacio:
- Para traslaciones: se usan los comandos `+X`, `-X`, `+Y`, `-Y`, `+Z`, `-Z`.
- Para rotaciones: se utilizan `+RX`, `-RX`, `+RY`, `-RY`, `+RZ`, `-RZ`.

En todos los casos, es obligatorio mantener presionado el botón de habilitación (`ENABLE`) ubicado en la parte trasera del teach pendant mientras se ejecutan los movimientos. Esto es un mecanismo de seguridad que garantiza que los movimientos solo ocurran mientras el operador tiene control activo del robot.

## Descripción de las funcionalidades de RoboDK y su comunicación con el Motoman MH6

RoboDK es una herramienta de simulación y programación offline de robots industriales que permite diseñar, validar y ejecutar trayectorias sin necesidad de usar directamente el robot físico. Es compatible con una amplia gama de marcas, incluyendo Yaskawa Motoman, lo que facilita el desarrollo y la integración de procesos automatizados como soldadura, paletizado, fresado, ensamblaje, entre otros.

### Principales funcionalidades de RoboDK

1. **Simulación 3D del entorno de trabajo**
   - Permite crear una celda robótica virtual que incluye el robot Motoman MH6, herramientas, transportadores, sensores y piezas.
   - Ayuda a visualizar y corregir trayectorias antes de transferirlas al robot real, reduciendo riesgos y tiempos de prueba.

2. **Programación offline (sin conexión directa al robot)**
   - Se pueden programar trayectorias y movimientos mediante una interfaz gráfica o mediante scripts en Python.
   - El software genera automáticamente el código nativo que el robot entiende, dependiendo del fabricante (en este caso, código INFORM para Motoman).

3. **Postprocesamiento automático**
   - RoboDK convierte los movimientos definidos en la simulación a instrucciones específicas del lenguaje del controlador Motoman (INFORM).
   - Esto permite transferir fácilmente el programa al robot real mediante archivo o conexión directa.

4. **Generación de trayectorias a partir de CAD/CAM**
   - Es posible importar archivos de modelos 3D (como STEP o STL) y generar automáticamente trayectorias para tareas como pintura, soldadura o mecanizado.

5. **Programación con Python**
   - RoboDK permite extender sus funcionalidades mediante scripts en Python, lo que habilita tareas personalizadas como lógica de control, comunicación con sensores o interacción con otros sistemas.

### Comunicación entre RoboDK y el robot Motoman

Para que RoboDK pueda ejecutar movimientos en un **robot Motoman MH6**, se utilizan dos métodos principales:

#### 1. **Transferencia por archivo**
- RoboDK genera archivos de programa en formato **.JBI** (formato INFORM de Motoman).
- Estos archivos se transfieren al controlador DX100/DX200 mediante una memoria USB o por red (FTP).
- Una vez en el controlador, el operador puede ejecutar el programa desde el teach pendant.

#### 2. **Comunicación directa (online programming)**
- También es posible establecer una conexión directa entre RoboDK y el robot a través de **Ethernet**, usando el protocolo **MotoCom SDK** o mediante API de RoboDK si está configurado.
- Esto permite enviar comandos en tiempo real, monitorear el estado del robot y hacer ajustes sin necesidad de generar archivos.

> Nota: La comunicación en tiempo real requiere que el robot tenga habilitada la opción de comunicación remota y que esté correctamente configurada la red entre el PC y el controlador.

---

### Procesos que realiza RoboDK para ejecutar movimientos

1. El usuario diseña la trayectoria en RoboDK, utilizando coordenadas cartesianas o movimientos relativos.
2. El software simula el movimiento y detecta posibles colisiones o errores de alcance.
3. Se selecciona el postprocesador adecuado (en este caso, Motoman INFORM) para generar el código del robot.
4. Se transfiere el archivo al controlador del robot.
5. Finalmente, el robot ejecuta la secuencia programada tal como fue simulada.

Esta metodología reduce el tiempo de programación en el sitio, mejora la precisión y permite realizar pruebas y optimizaciones sin detener la línea de producción.
