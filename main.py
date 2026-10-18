import cv2
import pandas as pd  

# Caminho do video
cap = cv2.VideoCapture(r"INSIRA O CAMINHO AQUI")

fps = cap.get(cv2.CAP_PROP_FPS)

dados = []

frame_count = 0  

print("Processando o video...")

while cap.isOpened():
    ret, frame = cap.read()
    
    if not ret:
        break

    t = frame_count / fps

    #Converte para tons de cinza e aplica o Threshold
    cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    limiar_escuridao = 60
    _, mascara = cv2.threshold(cinza, limiar_escuridao, 255, cv2.THRESH_BINARY_INV)

    #Encontra a massa
    contornos, _ = cv2.findContours(mascara, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contornos) > 0:
        maior_contorno = max(contornos, key=cv2.contourArea)
        M = cv2.moments(maior_contorno)
        
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])

            dados.append({'x': cx, 'y': cy, 't': t})

            cv2.circle(frame, (cx, cy), 10, (0, 255, 0), -1)

    #Exibe o rastreamento ao vivo
    cv2.namedWindow("Rastreamento do Pendulo", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Rastreamento do Pendulo", 800, 600)
    cv2.imshow("Rastreamento do Pendulo", frame)

    # Incrementa o número do frame
    frame_count += 1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# CRIAÇÃO DA TABELA
# Converte a lista para um DataFrame do Pandas
df = pd.DataFrame(dados)

# Exibe as primeiras linhas da tabela no terminal
print("\n--- Primeiras linhas da Tabela (x, y, t) ---")
print(df.head())

# Salva a tabela em um arquivo CSV na mesma pasta
df.to_csv("dados_pendulo.csv", index=False)
print("\nTabela salva com sucesso no arquivo 'dados_pendulo.csv'!")
