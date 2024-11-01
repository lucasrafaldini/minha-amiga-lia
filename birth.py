import os
import subprocess
import urllib.request
import zipfile

# Caminhos e URLs para download
MODEL_URL = "https://link_do_modelo_llama.com/llama_model.zip"  # Substitua pelo link real do modelo
MODEL_PATH = "./models/llama_model.zip"
EXTRACT_PATH = "./models/"

def download_model():
    print("🌸 Bem-vindo! A Lia está nascendo... Vamos baixar o modelo necessário.")
    
    # Verificar se a pasta existe
    if not os.path.exists(EXTRACT_PATH):
        os.makedirs(EXTRACT_PATH)
    
    # Baixar o modelo se ele ainda não existir
    if not os.path.exists(MODEL_PATH):
        print("🔄 Baixando o modelo LLaMA...")
        urllib.request.urlretrieve(MODEL_URL, MODEL_PATH)
        print("✅ Download concluído!")
    else:
        print("✅ O modelo já foi baixado anteriormente.")

def extract_model():
    print("🔄 Extraindo o modelo...")
    with zipfile.ZipFile(MODEL_PATH, 'r') as zip_ref:
        zip_ref.extractall(EXTRACT_PATH)
    print("✅ Modelo extraído com sucesso!")

def install_dependencies():
    print("🔄 Instalando dependências...")
    try:
        subprocess.check_call(["pip", "install", "-r", "requirements.txt"])
        print("✅ Dependências instaladas!")
    except subprocess.CalledProcessError:
        print("⚠️ Erro ao instalar as dependências. Verifique o arquivo requirements.txt.")

def setup_lia():
    print("🌱 Iniciando o processo de setup da Lia...")
    download_model()
    extract_model()
    install_dependencies()
    print("🌸 A Lia está pronta para te ajudar!")

if __name__ == "__main__":
    setup_lia()