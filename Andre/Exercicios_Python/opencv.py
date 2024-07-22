import cv2

def detectar_rosto(frame, casc_path):
    # Carrega o classificador Haar para detecção de rosto
    face_cascade = cv2.CascadeClassifier(casc_path)

    # Converte o frame para escala de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detecta rostos no frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Desenha retângulos ao redor dos rostos detectados
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    return frame

def main():
    # Inicializa a captura de vídeo da webcam
    cap = cv2.VideoCapture(0)  # 0 para a primeira webcam conectada, 1 para a segunda, e assim por diante

    if not cap.isOpened():
        print("Erro ao acessar a câmera. Verifique se está conectada.")
        return
    
    # Caminho para o classificador Haar de detecção de rosto
    casc_path = 'haarcascade_frontalface_default.xml'  # Substitua com o caminho para o seu arquivo XML

    while True:
        # Captura frame a frame
        ret, frame = cap.read()
        
        if not ret:
            print("Erro ao capturar o frame.")
            break
        
        # Detecta rostos no frame
        frame = detectar_rosto(frame, casc_path)
        
        # Mostra o frame capturado em uma janela
        cv2.imshow('Detecção de Rosto', frame)
        
        # Espera pela tecla 'q' para sair do loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Libera o objeto de captura e fecha todas as janelas abertas
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
