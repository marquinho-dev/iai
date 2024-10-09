#!/usr/bin/python3.12

from pathlib import Path
import argparse
import subprocess

def create_desktop_entry(desk_file, content, message):
    """Cria o arquivo .desktop."""
    with open(desk_file, 'w', encoding='utf-8') as file:
        print(f'Criando arquivo em {desk_file}...')
        try:
            file.write(content)
        except Exception as e:
            print(f'Erro ao criar o arquivo: {e}')
            raise
        else:
            print(message)

def main():
    # Inicializa o parser de argumentos
    parser = argparse.ArgumentParser(description="Este script cria um atalho para um arquivo .AppImage.")
    
    # Define os argumentos
    parser.add_argument(
        '-l', '--location',
        type=str,
        required=True,
        help="Caminho completo para seu arquivo .AppImage (ex: /caminho/para/seu/arquivo.AppImage)."
    )
    
    parser.add_argument(
        '-d', '--destination',
        type=str,
        default='/opt',
        help='Caminho onde o arquivo AppImage será movido. O padrão é "/opt".'
    )
    
    parser.add_argument(
        '-i', '--icon',
        type=str,
        required=True,
        help='Caminho completo para o ícone do aplicativo (ex: /caminho/para/seu/icon.png).'
    )
    
    parser.add_argument(
        '-c', '--categories',
        type=str,
        default='Utility',
        help='Define a categoria do aplicativo. O padrão é "Utility".'
    )
    
    # Analisa os argumentos fornecidos
    args = parser.parse_args()
    
    # Variáveis principais
    app_location = Path(args.location)  # Localização do aplicativo AppImage
    app_name = app_location.name  # Captura apenas o nome do AppImage
    desktop_entry_path = Path('/usr/share/applications')  # Onde será gerado o arquivo .desktop
    destination = Path(args.destination)  # Destino da cópia do arquivo AppImage
    icon_file = Path(args.icon)  # Ícone escolhido pelo usuário

    # Verificações iniciais
    if app_location.suffix != ".AppImage":
        print('Erro: O arquivo informado não é um arquivo .AppImage.')
        exit(1)

    if not app_location.exists():
        print(f'Erro: Arquivo {app_location} não encontrado.')
        exit(1)

    if not icon_file.exists():
        print(f'Erro: Ícone {icon_file} não encontrado.')
        exit(1)

    # Verifica se o diretório de destino existe
    if not destination.is_dir():
        print("O caminho informado não existe.")
        answer = input('Deseja criar esse diretório? (sim/não): ')
        if answer.lower() in ['sim', 'yes']:
            destination.mkdir(parents=True, exist_ok=True)
            print(f'Diretório {destination} criado.')
        else:
            print('Saindo...')
            exit(0)

    # Prepara o nome do aplicativo para o arquivo .desktop
    app_name = app_name.replace('-', '_').replace(' ', '_')
    app_name = ''.join(char for char in app_name if not char.isnumeric())  # Remove números
    app_name = app_name.replace('AppImage', '').replace('.', '') + app_location.suffix  # Adiciona a extensão

    app_destination = destination / Path(app_name)
    desktop_file_name = app_name.replace('.AppImage', '') + '.desktop'  # Nome do arquivo .desktop
    desktop_file_destination = desktop_entry_path / desktop_file_name

    # Cria o diretório de destino para o .desktop, se necessário
    desktop_entry_path.mkdir(parents=True, exist_ok=True)

    # Verifica se o arquivo .desktop já existe
    if Path(desktop_file_destination).exists():
        print(f'Erro: O arquivo {desktop_file_name} já existe.')
        exit(1)

    # Cria o conteúdo do arquivo .desktop
    file_content = f"""[Desktop Entry]
Name={app_name.replace('.AppImage', '').replace('_', ' ').rstrip()}
Exec={app_destination}
Icon={icon_file}
Type=Application
Categories={args.categories};"""

    # Executa o comando 'cp' para copiar o arquivo AppImage
    print(f'Copiando {app_location} para {app_destination}...')
    command = subprocess.run(
        ['cp', str(app_location), str(app_destination)],
        stderr=subprocess.PIPE,  # Captura a saída de erro
        text=True  # Converte a saída de bytes para string automaticamente
    )

    # Verifica o código de retorno da cópia
    if command.returncode == 0:
        print('Cópia concluída com sucesso!')
        message = f"Entrada de menu criada com sucesso em {desktop_file_destination}."
        create_desktop_entry(desktop_file_destination, file_content, message)
    else:
        print('Erro ao tentar copiar o arquivo:')
        print(command.stderr)
        exit(1)

if __name__ == "__main__":
    main()
