"""
Script de configuração inicial do projeto Bocão Lanches
Execute: python setup.py
"""

import os
import sys
import subprocess

def run_command(command):
    """Executa um comando no terminal"""
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✓ {command}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Erro ao executar: {command}")
        print(f"  {e.stderr}")
        return False

def main():
    print("=" * 50)
    print("Configuração do Sistema Bocão Lanches")
    print("=" * 50)
    
    # Verificar se está em ambiente virtual
    if not hasattr(sys, 'real_prefix') and not (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("\n⚠ Aviso: Parece que você não está em um ambiente virtual.")
        print("Recomendamos criar e ativar um ambiente virtual antes de continuar.")
        resposta = input("Deseja continuar mesmo assim? (s/n): ")
        if resposta.lower() != 's':
            print("Encerrando...")
            return
    
    # Instalar dependências
    print("\n1. Instalando dependências...")
    if not run_command("pip install -r requirements.txt"):
        print("Erro ao instalar dependências. Verifique se o arquivo requirements.txt existe.")
        return
    
    # Criar arquivo .env se não existir
    print("\n2. Verificando arquivo .env...")
    if not os.path.exists('.env'):
        print("Criando arquivo .env...")
        with open('.env', 'w') as f:
            f.write("SECRET_KEY=django-insecure-change-this-in-production-12345\n")
            f.write("DEBUG=True\n")
            f.write("MERCADOPAGO_ACCESS_TOKEN=\n")
            f.write("INSTAGRAM_ACCESS_TOKEN=\n")
        print("✓ Arquivo .env criado. Configure as variáveis conforme necessário.")
    else:
        print("✓ Arquivo .env já existe.")
    
    # Criar diretórios necessários
    print("\n3. Criando diretórios...")
    dirs = ['static', 'media', 'media/produtos']
    for dir_name in dirs:
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
            print(f"✓ Diretório {dir_name} criado")
    
    # Executar migrações
    print("\n4. Executando migrações...")
    if not run_command("python manage.py makemigrations"):
        print("Erro ao criar migrações.")
        return
    
    if not run_command("python manage.py migrate"):
        print("Erro ao executar migrações.")
        return
    
    # Coletar arquivos estáticos
    print("\n5. Coletando arquivos estáticos...")
    run_command("python manage.py collectstatic --noinput")
    
    print("\n" + "=" * 50)
    print("Configuração concluída!")
    print("=" * 50)
    print("\nPróximos passos:")
    print("1. Crie um superusuário: python manage.py createsuperuser")
    print("2. Execute o servidor: python manage.py runserver")
    print("3. Acesse: http://127.0.0.1:8000")
    print("4. Acesse o admin: http://127.0.0.1:8000/admin")
    print("\nConfigure os dados iniciais:")
    print("- Categorias de produtos")
    print("- Ingredientes")
    print("- Produtos")

if __name__ == '__main__':
    main()
