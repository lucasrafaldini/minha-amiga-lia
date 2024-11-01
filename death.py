import os
import shutil
import subprocess

# Caminhos do modelo e pastas de configuração
MODEL_PATH = "./models/llama_model.zip"
EXTRACT_PATH = "./models/"

def delete_model():
    # Exclui o modelo e dados
    print("🔄 Deletando o modelo e dados da Lia...")
    if os.path.exists(MODEL_PATH):
        os.remove(MODEL_PATH)
        print("✅ Arquivo do modelo excluído.")
    else:
        print("⚠️ O modelo já foi excluído anteriormente ou não encontrado.")

    # Exclui a pasta de extração do modelo
    if os.path.exists(EXTRACT_PATH):
        shutil.rmtree(EXTRACT_PATH)
        print("✅ Diretório de modelos limpo.")
    else:
        print("⚠️ Diretório de modelos não encontrado ou já excluído.")

def reinstall_model():
    # Re-executa o processo de download e setup
    print("🌱 Renascento a Lia com uma nova configuração...")
    download_model()
    extract_model()
    install_dependencies()
    print("🌸 A Lia renasceu e está pronta para um novo começo!")

def download_model():
    MODEL_URL = "https://link_do_modelo_llama.com/llama_model.zip"  # Substitua pelo link real do modelo
    print("🔄 Baixando o modelo LLaMA...")
    urllib.request.urlretrieve(MODEL_URL, MODEL_PATH)
    print("✅ Download concluído!")

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

def kill_and_renew_lia():
    print("⚠️ A Lia será dispensada agora. Todos os dados e modelos serão excluídos.")
    delete_model()
    reinstall_model()

if __name__ == "__main__":
    kill_and_renew_lia()