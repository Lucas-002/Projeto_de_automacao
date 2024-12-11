# PDF Merger

#Descrição
Este projeto utiliza o módulo `PyPDF2` para combinar múltiplos arquivos PDF em um único arquivo chamado **PDF FINAL.pdf**. Ele foi projetado para buscar PDFs em um diretório específico, ordená-los alfabeticamente e mesclá-los.

# Requisitos
- Python 3.6 ou superior
- Biblioteca PyPDF2

# Instalação
Certifique-se de ter o Python instalado e depois instale a biblioteca PyPDF2 com o seguinte comando:
```bash
pip install PyPDF2
```

# Como Usar
1. Certifique-se de que o diretório `Arquivos` existe na mesma pasta do script.
2. Coloque todos os arquivos PDF que deseja combinar dentro do diretório `Arquivos`.
3. Execute o script.

# Exemplo de Execução
1. Estrutura esperada:
```
.
|-- script.py
|-- Arquivos/
    |-- documento1.pdf
    |-- documento2.pdf
    |-- documento3.pdf
```
2. Comando para execução:
```bash
python script.py
```
3. Resultado:
O script gerará um arquivo chamado **PDF FINAL.pdf** no mesmo diretório do script.

# Lógica do Código
1. Verifica se o diretório `Arquivos` existe. Caso contrário, exibe uma mensagem de erro e encerra a execução.
2. Lista e ordena os arquivos no diretório `Arquivos` em ordem alfabética.
3. Mescla todos os arquivos PDF encontrados no diretório.
4. Salva o resultado no arquivo **PDF FINAL.pdf**.

# Observações
- Apenas arquivos com a extensão `.pdf` serão processados.
- Caso não existam arquivos PDF no diretório `Arquivos`, o script gerará um arquivo PDF vazio.
- O nome dos arquivos é sensível a maiúsculas/minúsculas e deve estar correto para garantir a ordem desejada.

# Possíveis Melhorias
- Adicionar suporte para subdiretórios.
- Incluir opções para personalizar o nome do arquivo final.
- Adicionar validações para arquivos corrompidos ou PDFs inválidos.


