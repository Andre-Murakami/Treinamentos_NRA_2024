import cv2

def main():
    # Inicializa a captura de vídeo da webcam
    cap = cv2.VideoCapture(0)  # 0 para a primeira webcam conectada, 1 para a segunda, e assim por diante

    if not cap.isOpened():
        print("Erro ao acessar a câmera. Verifique se está conectada.")
        return

    # Captura o primeiro frame para usar como referência
    ret, frame_anterior = cap.read()

    # Inicializa as coordenadas do retângulo
    x, y, w, h = 0, 0, 0, 0

    while True:
        # Captura o próximo frame
        ret, frame_atual = cap.read()

        if not ret:
            print("Erro ao capturar o frame.")
            break

        # Converte os frames para escala de cinza
        gray_anterior = cv2.cvtColor(frame_anterior, cv2.COLOR_BGR2GRAY)
        gray_atual = cv2.cvtColor(frame_atual, cv2.COLOR_BGR2GRAY)

        # Calcula a diferença absoluta entre os frames
        diferenca = cv2.absdiff(gray_anterior, gray_atual)

        # Aplica um limiar para segmentar regiões de movimento
        _, thresh = cv2.threshold(diferenca, 30, 255, cv2.THRESH_BINARY)

        # Encontra contornos de regiões de movimento
        contornos, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Atualiza as coordenadas do retângulo para acompanhar o maior contorno encontrado
        for contorno in contornos:
            if cv2.contourArea(contorno) > 1000:  # Apenas considera contornos maiores que 1000 pixels
                (x, y, w, h) = cv2.boundingRect(contorno)

        # Desenha o retângulo ao redor da área de movimento detectada
        cv2.rectangle(frame_atual, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Mostra o frame atual com o retângulo de movimento detectado
        cv2.imshow('Detecção de Movimento', frame_atual)

        # Atualiza o frame anterior para o próximo loop
        frame_anterior = frame_atual.copy()

        # Espera pela tecla 'q' para sair do loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Libera o objeto de captura e fecha todas as janelas abertas
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
