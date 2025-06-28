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

A continuación, se describe el procedimiento para ejecutar movimientos manuales en el robot Motoman MH6, incluyendo cómo cambiar entre modos de operación (articulaciones y cartesiano), y cómo realizar desplazamientos y rotaciones en los ejes X, Y y Z. Este proceso se realiza a través del teach pendant del robot, bajo supervisión y con las debidas precauciones de seguridad.

### 1. Encendido del robot y preparación

Para iniciar el proceso, el operador debe encender el controlador del robot (DX100 o DX200, según el modelo) y esperar a que el sistema complete su arranque. Una vez activo, se debe verificar que el teach pendant esté encendido y que el robot se encuentre libre de errores o alarmas.

A continuación, el operador debe asegurarse de que el robot esté configurado en **modo Teach**, lo que permitirá realizar movimientos manuales de manera segura. Este modo puede ser activado desde un selector físico en el panel de control o desde el menú del teach pendant.

### 2. Selección del modo de movimiento

El operador puede controlar manualmente el robot en dos modos principales:

- **Modo Articulado (Joint Mode)**: permite mover cada uno de los seis ejes del robot por separado. Es útil para posicionar el robot ajustando individualmente las articulaciones.
- **Modo Cartesiano (Base, World o Tool)**: permite mover el extremo del brazo (usualmente una herramienta) en direcciones lineales (X, Y, Z) o realizar rotaciones alrededor de esos ejes, según un sistema de coordenadas definido.

Para cambiar entre estos modos, se debe presionar el botón `COORD` en el teach pendant. Este botón abre un menú que permite seleccionar el sistema de coordenadas deseado:
- `JOINT` para el modo articulado,
- `BASE` o `WORLD` para coordenadas relativas a la base del robot,
- `TOOL` para coordenadas relativas a la herramienta,
- `USER` si se ha definido un sistema de coordenadas personalizado.

### 3. Realización de movimientos manuales

Una vez seleccionado el modo de movimiento adecuado, el operador puede proceder a controlar el robot manualmente.

En **modo articulado**, se utilizan las teclas del teach pendant correspondientes a cada eje (por ejemplo, `S`, `L`, `U`, `R`, `B`, `T`) para mover individualmente las articulaciones del robot. Cada tecla tiene asociada una dirección positiva (`+`) y negativa (`-`), lo que permite realizar giros o desplazamientos en ambos sentidos.

En **modo cartesiano**, las teclas permiten mover el extremo del brazo robótico (el efector final) de forma lineal o rotacional en el espacio:
- Para traslaciones: se usan los comandos `+X`, `-X`, `+Y`, `-Y`, `+Z`, `-Z`.
- Para rotaciones: se utilizan `+RX`, `-RX`, `+RY`, `-RY`, `+RZ`, `-RZ`.

En todos los casos, es obligatorio mantener presionado el botón de habilitación (`ENABLE`) ubicado en la parte trasera del teach pendant mientras se ejecutan los movimientos. Esto es un mecanismo de seguridad que garantiza que los movimientos solo ocurran mientras el operador tiene control activo del robot.
