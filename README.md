![Badge Concluido](http://img.shields.io/static/v1?label=STATUS&message=%20CONCLUIDO&color=GREEN&style=for-the-badge)

# :musical_note: Criando um áudiobook

Esse projeto desenvolve uma aplicação de processamento de linguagem natural (NLP), um áudiobook a partir de uma história de um livro infantil, que está em formato PDF, utilizando o Python.

O processamento de linguagem natural é um ramo da inteligência artificial que mescla aprendizado de máquina (machine learning) com linguística.

O machine learning é o subconjunto da inteligência artificial, que se concentra na construção de sistemas que aprendem, ou melhoram o desempenho, com base nos dados que consomem.


#### Pyttsx3 é responsável pela sintetização de voz do áudiobook. A voz que vai ser usada por padrão será do mesmo idioma da configuração do sistema operacional.

Para trocar o idioma da voz, primeiro vamos instanciar um objeto do **pyttsx3**. Começamos armazenando em uma variável:

````python
engine = pyttsx3.init()
````

Com o método **setProperty()** temos várias configurações que podemos fazer, sendo uma deles alterar a voz que será usada no audiobook. Usamos como parâmetro o idioma que queremos que seja produzido.

````python
engine.setProperty(“voice”, “brazil”)
````
Obs: Brasil com **z**

Usando o método **say()** e passamos como parâmetro o que for produzido como áudio.

````python
engine.say(‘Meu nome é Mario’)
````

Só o método **say()** não temos nada como retorno, porque ele armazena como se fosse uma fila, usamos o método **runAndWait()** para produzir os textos como áudio.

````python
engine.say(‘Meu nome é Mario’)
engine.say(‘Eu sou de São Paulo’)
engine.say(‘Eu estou estudando Python’)

````
````python
engine.runAndWait()
````

Para gerar um arquivo de voz em formato mp3, utilizamos o método **save_to_file()** e passamos como parâmetro o nome do arquivo. Esse arquivo só é gerado após a execução com o método **runAndWait**.

````python
engine.say(‘Meu nome é Mario’, ’teste.mp3’)
````
````python
engine.runAndWait()
````

Para gerar um audiobook usando o texto de um arquivo pdf, devemos extrair o texto do arquivo, usando o método **pdfplumber.open()**, como parâmetro o nome do arquivo pdf e armazenado em uma variável.

````python
pdf = pdfplumber.open(‘O nome do arquivo.pdf’)
````



## 📁 Como utilizar o código:
O arquivo **script.py** pode ser usado em um terminal
````python
python script.py
````

:movie_camera:

<img src=".\Animação01.gif" alt="Código funcionando" width="600px" heidth="400px">



## :bookmark_tabs: Arquivo Requirements:
É um arquivo de texto formato **.txt**. Neste arquivo está especificado todos os pacotes e bibliotecas que são utilizados no projeto; isso ajuda como garantia que, se o projeto for usado por outro desenvolvedor, não ocorram erros ou problemas causados por alguma atualização na versão do pacote ou descontinuidade na linguagem Python.

Para instalar, entre no terminal **Ctrl + ‘** e instale o requirements para usar todos os pacotes na mesma versão que foi utilizada no projeto. 

````python
pip install -r requirements.txt
````

:film_projector:

<img src=".\Animação02.gif" alt="Instalando Requirements" width="600px" heidth="400px">




## :computer: Técnicas e Tecnologias utilizadas:

 - Técnica de slicing

 - Manipulação de strings

- Estrutura de repetição **for**
    
    - **Python**

   - **Jupter Notebook**

## :books: Bibliotecas usadas:

- pdfplumber

 - pyttsx3

## :electric_plug: Como instalar:

 - pip install pdfplumber

 - import pdfplumber

- pip install pyttsx3

 - import pyttsx3



