import PyPDF2
import os

margem = PyPDF2.PdfMerger()

# Verificar se o diretório 'Arquivos' existe
diretorio_arquivos = 'Arquivos'
if not os.path.exists(diretorio_arquivos):
    print(f'O diretório {diretorio_arquivos} não existe.')
    exit()

# Lista de arquivos ordenada alfabeticamente
lista_arquivos = sorted(os.listdir(diretorio_arquivos))
print(lista_arquivos)

for Arquivo in lista_arquivos:
    if Arquivo.endswith('.pdf'):
        arquivo_path = os.path.join(diretorio_arquivos, Arquivo)
        margem.append(arquivo_path)

# Salvando o PDF final
margem.write('PDF FINAL.pdf')
margem.close()
