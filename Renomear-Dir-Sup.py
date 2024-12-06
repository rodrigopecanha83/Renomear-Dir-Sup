import os
from pathlib import Path

def renomear_arquivos(pasta):
    # Se nenhum diretório for especificado, usa o diretório atual
    pasta = Path(pasta or os.getcwd())
    
    # Obtém o nome da pasta um nível acima do diretório especificado
    nome_pasta_acima = pasta.parent.name
    
    # Lista de extensões suportadas
    extensoes_validas = {'jpg', 'jpeg', 'png', 'webp', 'heic'}
    
    contador = 1
    for arquivo in pasta.iterdir():
        if arquivo.is_file():
            # Obtém a extensão do arquivo
            extensao = arquivo.suffix.lower().lstrip('.')
            
            if extensao in extensoes_validas:
                # Novo nome do arquivo
                novo_nome = pasta / f"{nome_pasta_acima} {contador:03d}{arquivo.suffix}"
                
                # Ajusta o nome se necessário
                while novo_nome.exists():
                    contador += 1
                    novo_nome = pasta / f"{nome_pasta_acima} {contador:03d}{arquivo.suffix}"
                
                # Renomeia o arquivo
                arquivo.rename(novo_nome)
                contador += 1
    
    print("Arquivos renomeados com sucesso!")

if __name__ == "__main__":
    import sys
    # Diretório passado como argumento ou atual se não houver
    diretorio = sys.argv[1] if len(sys.argv) > 1 else None
    renomear_arquivos(diretorio)
