import os
import glob
import platform
import shutil

diretorios_linux = ["/etc", "/var", "/home", "/root", "/srv"]
diretorios_windows = ["C:\\Windows\\System32", "C:\\Users"]

if platform.system() == 'Windows':
    diretorios = diretorios_windows
else:
    diretorios = diretorios_linux

os.makedirs('arquivos_copiados', exist_ok=True)

def extrair_informacoes(diretorio):
    informacoes = []
    for root, dirs, files in os.walk(diretorio):
        for file in files:
            if file.endswith('.log') or file.endswith('.txt'):
                try:
                    caminho = os.path.join(root, file)
                
                    shutil.copy2(caminho, 'arquivos_copiados')
                    informacoes.append(caminho)
                except OSError as e:
                    print(f"Erro: {e}")
    return informacoes

with open('resultados.txt', 'w') as f:
    for diretorio in diretorios:
        informacoes = extrair_informacoes(diretorio)
        f.write(f"Informações do diretório {diretorio}:\n")
        for caminho in informacoes:
            f.write(f"Arquivo: {caminho} copiado para 'arquivos_copiados'\n")
        f.write("\n")
