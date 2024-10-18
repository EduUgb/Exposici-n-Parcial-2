import cv2

# Inicializar la captura de video 
video = cv2.VideoCapture(0)

# Leer el primer frame para seleccionar el ROI
ok, frame = video.read()

# Seleccionar el ROI (área a rastrear)
bbox = cv2.selectROI("Selecciona el objeto", frame, False)
cv2.destroyWindow("Selecciona el objeto")  # Cerrar la ventana del selector de ROI

# Inicializar el tracker 
tracker = cv2.TrackerCSRT_create()

# Iniciar el tracker con el primer frame y el ROI seleccionado
ok = tracker.init(frame, bbox)

# Loop para leer frames y realizar el seguimiento
while True:
    # Leer un nuevo frame
    ok, frame = video.read()
    
    if not ok:
        print("Error: No se puede leer el frame")
        break
        
    # Actualizar el tracker con el nuevo frame
    ok, bbox = tracker.update(frame)

    if ok:
        # Si el seguimiento es exitoso, dibujar el rectángulo alrededor del objeto
        p1 = (int(bbox[0]), int(bbox[1]))
        p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        cv2.rectangle(frame, p1, p2, (0, 255, 0), 2, 1)


    # Mostrar el frame con el seguimiento
    cv2.imshow("Tracking", frame)


    # Verificar si se ha cerrado la ventana (getWindowProperty)
    if cv2.getWindowProperty("Tracking", cv2.WND_PROP_VISIBLE) < 1:
        break

    k = cv2.waitKey(1) & 0xff 
    if k == 27:  # ESC
        break


video.release()
cv2.destroyAllWindows()
