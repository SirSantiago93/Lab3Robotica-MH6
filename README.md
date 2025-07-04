# Lab3Robotica-MotomanMH6

## Integrantes:
- Isabella Mendoza Cáceres
- Andrés Santiago Cañón Porras

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


## Descripción de las configuraciones home1 y home2 del Motoman MH6

El robot Motoman MH6 tiene dos posiciones predefinidas de “home” o inicio, que son utilizadas como referencia para programación, calibración o recuperación. Cada una define un conjunto específico de valores para las seis articulaciones del robot (ejes S, L, U, R, B y T). Las posiciones típicas son las siguientes:

### Home 1 (posición recogida)

<div align="center">
<table>
  <tr>
    <td>

<!-- Tabla de articulaciones -->
<b>Configuración Home 1 Teórica</b>  
<table>
  <tr><th>Articulación</th><th>Valor</th></tr>
  <tr><td>S (J1)</td><td>0°</td></tr>
  <tr><td>L (J2)</td><td>+90°</td></tr>
  <tr><td>U (J3)</td><td>–90°</td></tr>
  <tr><td>R (J4)</td><td>0°</td></tr>
  <tr><td>B (J5)</td><td>0°</td></tr>
  <tr><td>T (J6)</td><td>0°</td></tr>
</table>

</td>
<td>

<!-- Imagen -->
<b>Posición Home 1 Real</b>  
<img src="https://github.com/user-attachments/assets/2749bf67-a303-4964-bd96-9485ca865b09" alt="Home 2 Image" width="450"/>

</td>
</tr>
</table>
</div>

**Descripción:**  
El brazo del robot se encuentra replegado hacia su base, ocupando un espacio más compacto. Según los valores mostrados en el teach pendant, la configuración real usada como Home 1 en el robot es diferente de  +90° / -90° . Esto puede deberse a ajustes hechos en la programación por el integrador para evitar singularidades, colisiones o por razones prácticas del layout. Se tiene que esta posición es útil para almacenamiento, transporte o mantenimiento del robot sin riesgo de colisiones.

<div align="center">
  <img src="https://github.com/user-attachments/assets/c269c4f7-9070-4549-8950-ec07ebfd28c5" alt="image" width="400" />
</div>

### Home 2 (posición extendida)

<div align="center">
<table>
  <tr>
    <td>

<!-- Tabla de articulaciones -->
<b>Configuración Home 2 Teórica</b>  
<table>
  <tr><th>Articulación</th><th>Valor</th></tr>
  <tr><td>S (J1)</td><td>0°</td></tr>
  <tr><td>L (J2)</td><td>0°</td></tr>
  <tr><td>U (J3)</td><td>0°</td></tr>
  <tr><td>R (J4)</td><td>0°</td></tr>
  <tr><td>B (J5)</td><td>0°</td></tr>
  <tr><td>T (J6)</td><td>0°</td></tr>
</table>

</td>
<td>

<!-- Imagen -->
<b>Posición Home 2 Real</b>  
<img src="https://github.com/user-attachments/assets/a13d11d1-1290-4309-8679-8591749c1133" alt="Home 2 Image" width="450"/>

</td>
</tr>
</table>
</div>

**Descripción:**  
El robot se encuentra completamente extendido hacia el frente. Esta configuración no es exactamente la teórica Home 2 estándar, en su lugar se observa una posición casi centralizada, pero con leves desviaciones en los ejes L, U, B y T. Lo anterior se puede deber para evitar pequeñas oscilaciones, tolerancias mecánicas o ajustar a una posición de descanso natural del brazo así como evitar errores por desfase en sensores. Esta configuración es simétrica y neutral, ideal para iniciar tareas con visibilidad total del espacio de trabajo y sin interferencias.

<div align="center">
  <img src="https://github.com/user-attachments/assets/0bcc3907-70be-4900-9db4-06915641d8c1" alt="image" width="400" />
</div>

La elección entre Home 1 y Home 2 depende del objetivo. **Home 1** es más adecuado para arranques seguros, ahorro de espacio y transporte o mantenimiento. Mientras que **Home 2** es más adecuado para programación de trayectorias, calibrar posiciones, recuperar errores y comprobar colisiones o límites de movimiento.


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


## Niveles de Velocidad en Movimiento Manual - Motoman MH6

Cuando el operador mueve el robot manualmente (modo **JOG**), se utilizan *niveles de velocidad predeterminados* para controlar cuán rápido se moverán las articulaciones o el TCP (Tool Center Point).

Estos niveles permiten:
- Aumentar o reducir la precisión del movimiento.
- Prevenir movimientos peligrosos durante programación o ajustes.
- Ajustar la velocidad según la tarea: posicionamiento fino o desplazamiento largo.

### Niveles de velocidad disponibles

Los niveles pueden variar ligeramente según el modelo de controlador, pero normalmente son:

| Nivel | Descripción              | Velocidad aprox. (puede variar) |
|-------|--------------------------|----------------------------------|
| **1** | Muy lento / ajuste fino  | ~1% – 5%                         |
| **2** | Lento                    | ~10% – 20%                       |
| **3** | Medio                    | ~30% – 50%                       |
| **4** | Rápido                   | ~75%                             |
| **5** | Máximo                   | 100%                             |

El robot Motoman MH6 tiene la capacidad de operar a diferentes niveles de velocidad, permitiendo ajustar su rendimiento según las necesidades específicas de la tarea. Se puede modificar la velocidad de cada eje individualmente, variando entre un 1% y un 200% de la velocidad nominal. La velocidad no solo depende del nivel seleccionado, sino también del tipo de movimiento (ejes individuales, coordenadas cartesianas, etc.) y de la carga. Se puede cambiar el nivel de velocidad directamente desde el **teach pendant**, siguiendo estos pasos:

1. Estar en **modo JOG** (presionar el botón "JOG").
2. Presionar el botón físico o virtual con el ícono de **velocidad** (`%`) o la etiqueta `STEP`.
3. Usar las teclas de **flecha arriba/abajo** o los **botones de selección de velocidad** en pantalla para subir o bajar el nivel.
4. El cambio se aplica de inmediato y afecta todos los movimientos manuales.

<div align="center">
  <img src="https://github.com/user-attachments/assets/49c7d332-4a73-4a5e-b025-ce7f0b7797e9" alt="image" width="400" />
</div>

Se reconoce en qué valor de velocidad se encuentra debido a que en la parte superior lateral derecho del teach pendant, se muestra el **ícono o campo de velocidad actual**, normalmente con un número (ej: `STEP 3`, `SPEED 50%`, etc.).


## Descripción de las funcionalidades de RoboDK y su comunicación con el Motoman MH6

RoboDK es una herramienta de simulación y programación offline de robots industriales que permite diseñar, validar y ejecutar trayectorias sin necesidad de usar directamente el robot físico. Es compatible con una amplia gama de marcas, incluyendo Yaskawa Motoman, lo que facilita el desarrollo y la integración de procesos automatizados como soldadura, paletizado, fresado, ensamblaje, entre otros.

<div align="center">
  <img src="https://github.com/user-attachments/assets/4ff61186-27d5-4bc1-8910-ca415c36cf9f" alt="image" width="400" />
</div>

Dentro de las principales funcionalidades de RoboDK se encuentran:

1. **Simulación 3D del entorno de trabajo**
   - Permite crear una celda robótica virtual que incluye el robot Motoman MH6, herramientas, transportadores, sensores y piezas.
   - Ayuda a visualizar y corregir trayectorias antes de transferirlas al robot real, reduciendo riesgos y tiempos de prueba.

2. **Programación offline (sin conexión directa al robot)**
   - Se pueden programar trayectorias y movimientos mediante una interfaz gráfica o mediante scripts en Python.
   - El software genera automáticamente el código nativo que el robot entiende, dependiendo del fabricante (en este caso, código INFORM para Motoman).

3. **Postprocesamiento automático**
   - RoboDK convierte los movimientos definidos en la simulación a instrucciones específicas del lenguaje del controlador Motoman (INFORM). Esto permite transferir fácilmente el programa al robot real mediante archivo o conexión directa.

4. **Generación de trayectorias a partir de CAD/CAM**
   - Es posible importar archivos de modelos 3D (como STEP o STL) y generar automáticamente trayectorias para tareas como pintura, soldadura o mecanizado.

5. **Programación con Python**
   - RoboDK permite extender sus funcionalidades mediante scripts en Python, lo que habilita tareas personalizadas como lógica de control, comunicación con sensores o interacción con otros sistemas.

RoboDK puede comunicarse con el robot **Motoman MH6** principalmente de dos maneras. La primera es mediante **transferencia por archivo**, donde el software genera programas en formato **.JBI**, correspondiente al lenguaje **INFORM** de Motoman. Estos archivos pueden ser transferidos al controlador del robot (**DX100** o **DX200**) usando una memoria USB o a través de red mediante **FTP**. Una vez en el controlador, el operador puede ejecutar el programa directamente desde el teach pendant.

La segunda opción es la **comunicación directa o en línea**, que permite establecer una conexión en tiempo real entre RoboDK y el robot a través de **Ethernet**, utilizando el protocolo **MotoCom SDK** o mediante la **API de RoboDK**, si está correctamente configurada. Esta modalidad facilita el envío de comandos instantáneos, la supervisión del estado del robot y la modificación de movimientos sin necesidad de generar archivos intermedios.

> Nota: La comunicación en tiempo real requiere que el robot tenga habilitada la opción de comunicación remota y que esté correctamente configurada la red entre el PC y el controlador.

RoboDK realiza los siguientes procesos para ejecutar movimientos:

1. El usuario diseña la trayectoria en RoboDK, utilizando coordenadas cartesianas o movimientos relativos.
2. El software simula el movimiento y detecta posibles colisiones o errores de alcance.
3. Se selecciona el postprocesador adecuado (en este caso, Motoman INFORM) para generar el código del robot.
4. Se transfiere el archivo al controlador del robot.
5. Finalmente, el robot ejecuta la secuencia programada tal como fue simulada.

Esta metodología no solo facilita la interoperabilidad, sino que tambiente reduce el tiempo de programación en el sitio, mejora la precisión y permite realizar pruebas y optimizaciones sin detener la línea de producción.


## Comparativa entre RoboDK y RobotStudio

A continuación, se presenta una comparativa entre RoboDK y RobotStudio, destacando sus principales características, ventajas, limitaciones y aplicaciones. Esta comparación permite entender en qué contextos es más conveniente utilizar cada herramienta según las necesidades del usuario o del entorno industrial.

| **Criterio**               | **RoboDK**                                                                                 | **RobotStudio**                                                                              |
|---------------------------|---------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| **Compatibilidad**         | Multimarca (Motoman, ABB, KUKA, FANUC, UR, etc.)                                           | Exclusivo para robots ABB                                                                   |
| **Lenguaje de programación** | Python (externo) y lenguaje propio interno simplificado                                     | RAPID (lenguaje oficial de ABB)                                                             |
| **Facilidad de uso**       | Interfaz intuitiva, curva de aprendizaje baja                                              | Requiere conocimientos técnicos y dominio de RAPID                                          |
| **Precisión de simulación**| Alta (depende del postprocesador y configuración)                                          | Muy alta (emulación exacta del controlador IRC5)                                            |
| **Importación CAD/CAM**    | Soporte directo para archivos STEP, STL, DXF, G-code                                       | Soporte CAD limitado, más enfocado en programación RAPID                                    |
| **Programación offline**   | Sí                                                                                         | Sí                                                                                          |
| **Programación en tiempo real** | Sí, mediante conexión Ethernet o MotoCom (según marca y configuración)                   | Sí, con conexión directa al robot ABB                                                       |
| **Postprocesadores**       | Personalizables por marca y modelo                                                         | Nativo, exclusivo para ABB                                                                  |
| **Aplicaciones típicas**   | Simulación con robots diversos, automatización educativa, generación desde CAD, tareas generales | Simulación avanzada con robots ABB, configuración de celdas ABB, pruebas virtuales de ciclos |
| **Ventajas**               | - Soporte para múltiples marcas<br>- Integración con Python<br>- Fácil de usar             | - Emulación real del robot<br>- Precisión total<br>- Herramientas avanzadas para ABB        |
| **Limitaciones**           | - Menor precisión si no se ajustan los parámetros correctamente<br>- No emula controladores reales | - Solo funciona con robots ABB<br>- Requiere formación técnica especializada                |

En retrospectiva RoboDK es una opción versátil y accesible para entornos mixtos o educativos, mientras que RobotStudio ofrece un entorno profesional altamente preciso para la simulación y programación exclusiva de robots ABB. La elección dependerá del fabricante del robot y del nivel de fidelidad requerido en la simulación.

## Video de la práctica
[![Alt text](https://img.youtube.com/vi/eSCXMVGORic/0.jpg)](https://www.youtube.com/watch?v=eSCXMVGORic)
