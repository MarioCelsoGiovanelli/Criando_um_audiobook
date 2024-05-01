import pyttsx3
import pdfplumber

# Inicializando a engine de NLP.
engine = pyttsx3.init()

# Lendo o arquivo PDF.
pdf = pdfplumber.open('O elefante em apuros.pdf')

# Gerando lista de páginas do livro (exceto páginas: 1, 2, 27, 28 e 29!).
paginas = pdf.pages[2:-3]

texto_livro = ''
for pagina in paginas:
    texto_livro += pagina.extract_text()


# Tratando o texto para gerar o audio.
texto_final = texto_livro.replace('.', '. ').replace(',', ', ').replace('\n', ' ')

engine.save_to_file(texto_final, 'audiobook.mp3')
engine.runAndWait()