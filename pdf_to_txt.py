from PyPDF2 import PdfReader

pdf_file_path = 'E:\\llm\\chat_gpt\\data\\auto_da_compadecida.pdf'
txt_file_path = 'E:\\llm\\chat_gpt\\data\\auto_da_compadecida.txt'

# Criar um arquivo de texto para escrever o texto extraído
with open(txt_file_path, 'w', encoding='utf-8') as txt_file:
    # Criar um leitor de PDF
    reader = PdfReader(pdf_file_path)
    
    # Iterar sobre todas as páginas do PDF
    for page_num in range(len(reader.pages)):
        # Obter a página atual
        page = reader.pages[page_num]
        
        # Extrair o texto da página e escrevê-lo no arquivo de texto
        text = page.extract_text()
        txt_file.write(text)
        txt_file.write("\n")  # Adicionar uma quebra de linha entre as páginas

# Print a confirmation message
print('O texto foi salvo no arquivo "auto_da_compadecida.txt".')
