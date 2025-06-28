from robodk.robolink import *    # API para comunicarte con RoboDK
from robodk.robomath import *    # Funciones matemáticas
import math

#------------------------------------------------
# 1) Conexión a RoboDK e inicialización
#------------------------------------------------
RDK = Robolink()

# Elegir un robot (si hay varios, aparece un popup)
robot = RDK.ItemUserPick("Selecciona un robot", ITEM_TYPE_ROBOT)
#if not robot.Valid():
#    raise Exception("No se ha seleccionado un robot válido.")

# Conectar al robot físico
#if not robot.Connect():
#    raise Exception("No se pudo conectar al robot. Verifica que esté en modo remoto y que la configuración sea correcta.")

# Confirmar conexión
#if not robot.ConnectedState():
#    raise Exception("El robot no está conectado correctamente. Revisa la conexión.")

#print("Robot conectado correctamente.")

#------------------------------------------------
# Moviendo el robot a Home
#------------------------------------------------
frame_name = "Frame_Home"
frame = RDK.Item(frame_name, ITEM_TYPE_FRAME)
if not frame.Valid():
    raise Exception(f'No se encontró el Frame "{frame_name}" en la estación.')
robot.setPoseFrame(frame)

# Ajustes de velocidad y blending
robot.setSpeed(300)   # mm/s - Ajusta según necesites
robot.setRounding(5)  # blending (radio de curvatura)

robot.MoveJ(transl(0, 0, 0))

#------------------------------------------------
# 2) Cargar el Frame (ya existente) donde quieres dibujar
#    Ajusta el nombre si tu Frame se llama diferente
#------------------------------------------------
frame_name = "Frame_from_Target1"
frame = RDK.Item(frame_name, ITEM_TYPE_FRAME)
if not frame.Valid():
    raise Exception(f'No se encontró el Frame "{frame_name}" en la estación.')

# Asignamos este frame al robot
robot.setPoseFrame(frame)
# Usamos la herramienta activa
robot.setPoseTool(robot.PoseTool())

# Ajustes de velocidad y blending
robot.setSpeed(300)   # mm/s - Ajusta según necesites
robot.setRounding(5)  # blending (radio de curvatura)

#------------------------------------------------
# 3) Parámetros de la figura (corazón)
#------------------------------------------------
num_points = 720       # Cuántos puntos muestreamos (mayor = más suave)
A = 60               # Amplitud2k
z_surface = 0          # Z=0 en el plano del frame
z_safe = -50            # Altura segura para aproximarse y salir

x_offset = 100      #Se mueve para poder ampliar la figura
y_offset = 0
#------------------------------------------------
# 4) Movimiento al centro en altura segura
# Se calcula donde se va a graficar para así llegar a esa posición 
#------------------------------------------------
theta = 0
theta_rot = -3*math.pi/2
r = A * (math.sin(theta_rot) * math.sqrt(abs(math.cos(theta_rot))) / (math.sin(theta_rot) + 1.4) - 2 * math.sin(theta_rot) + 2)
x = r * math.cos(theta) + x_offset
y = r * math.sin(theta) + y_offset

# El centro de la rosa (r=0) corresponde a x=0, y=0
robot.MoveJ(transl(x, y, z_surface + z_safe))

# Bajamos a la "superficie" (Z=0)
robot.MoveL(transl(x, y, z_surface))

#------------------------------------------------
# 5) Dibujar el corazón
#    r = A * sin(k*theta)
#    x = r*cos(theta), y = r*sin(theta)
#------------------------------------------------
# Recorremos theta de 0 a 2*pi (una vuelta completa)
full_turn = 2*math.pi

for i in range(1, num_points+1):
    # Fracción entre 0 y 1
    t = i / num_points
    # Ángulo actual
    theta = full_turn * t
    theta_rot = theta - 3*math.pi/2 #Se necesita para voltear la figura

    # Calculamos r
    r = A * (math.sin(theta_rot) * math.sqrt(abs(math.cos(theta_rot))) / (math.sin(theta_rot) + 1.4) - 2 * math.sin(theta_rot) + 2)

    # Convertimos a coordenadas Cartesianas X, Y
    x = r * math.cos(theta) + x_offset
    y = r * math.sin(theta) + y_offset

    # Movemos linealmente (MoveL) en el plano del Frame
    robot.MoveL(transl(x, y, z_surface))

# Al terminar, subimos de nuevo para no chocar
robot.MoveL(transl(x, y, z_surface + z_safe))

#------------------------------------------------
# Moviendo el robot a Home
#------------------------------------------------
frame_name = "Frame_Home"
frame = RDK.Item(frame_name, ITEM_TYPE_FRAME)
if not frame.Valid():
    raise Exception(f'No se encontró el Frame "{frame_name}" en la estación.')
robot.setPoseFrame(frame)

# Ajustes de velocidad y blending
robot.setSpeed(300)   # mm/s - Ajusta según necesites
robot.setRounding(5)  # blending (radio de curvatura)

robot.MoveJ(transl(0, 0, 0))

print(f"¡Figura (corazón) completada en el frame '{frame_name}'!")
