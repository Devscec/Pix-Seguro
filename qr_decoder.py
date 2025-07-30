import cv2

def ler_qr_code(caminho_imagem):
    detector = cv2.QRCodeDetector()
    imagem = cv2.imread(caminho_imagem)
    dados, _, _ = detector.detectAndDecode(imagem)
    return dados
