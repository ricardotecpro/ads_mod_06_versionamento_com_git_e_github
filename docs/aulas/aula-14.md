# Aula 14 – GitHub Pages e Portfólio

## 🎯 Objetivos de Aprendizagem
- Entender o que é o recurso **GitHub Pages**.
- Transformar um repositório de código em um site publicado na internet.
- Compreender as limitações (apenas sites estáticos).
- Publicar seu portfólio para o mundo.

## 📚 Conteúdo

### 1. Seu Código na Web
Até agora, seu portfólio é apenas uma pasta de arquivos.
O **GitHub Pages** é um serviço de hospedagem gratutita que pega seus arquivos HTML, CSS e JS e os publica em um endereço como `seu-usuario.github.io/seu-projeto`.

### 2. O que é "Estático"?
O Pages serve sites estáticos.
- **Funciona**: HTML, CSS, JavaScript, Imagens, React (buildados), Vue, Angular.
- **Não Funciona**: PHP, Python (Django/Flask), Node.js (backend), Banco de Dados (MySQL).
Para portfólios, blogs e documentações, ele é perfeito.

### 3. Configuração
Basta ir em **Settings > Pages**.
Em "Build and deployment", escolha "Deploy from a branch".
Selecione a branch `main` e a pasta `/ (root)`.
Clique em Save.

### 4. O Arquivo index.html
Para que o site funcione, a primeira página DEVE se chamar `index.html`. Se não existir, o GitHub mostrará o README (se configurado) ou um erro 404.

---

## 📦 Limites do GitHub Pages (GitHub)

* **Tamanho máximo do repositório:** 1 GB
* **Tamanho recomendado do site publicado:** até 1 GB
* **Tamanho máximo por arquivo:** 100 MB
* **Limite de build (GitHub Pages build):** 10 builds por hora
* **Largura de banda:** não é oficialmente especificada, mas uso excessivo pode gerar bloqueio temporário

---

### 💡 Observações importantes

* Ideal para **sites estáticos** (HTML, CSS, JS).
* Não suporta backend (PHP, Node.js, banco de dados etc.).
* Perfeito para:

  * Portfólios
  * Landing pages
  * Documentação
  * Projetos front-end

---

## 📽 Roteiro de Slides
- O sonho do site próprio (Grátis!).
- Diferença entre Repositório (Código) e Site (Produto Final).
- Limitações: Sem Backend (PHP, SQL).
- O passo a passo da ativação.
- O endereço mágico: `username.github.io`.
- Personalização: Temas automáticos (Jekyll).

## 📝 Quiz
1. O GitHub Pages é um serviço gratuito?
2. Posso hospedar um site feito em PHP com banco de dados MySQL no GitHub Pages?
3. Qual é o nome obrigatório do arquivo principal para que a página inicial carregue?
4. Em qual menu do repositório ativamos o GitHub Pages?
5. Quanto tempo demora para o site ir ao ar após o push?

## Gabarito
1: A ("Sim, para repos públicos e privados selecionados")
2: B ("Não, ele só aceita conteúdo estático")
3: C ("index.html")
4: D ("Settings > Pages")
5: B ("Alguns segundos ou poucos minutos")

## 🛠 Exercícios
1. **Hello World**: Crie um arquivo `index.html` básico no seu repo de teste, com `<h1>Olá Mundo</h1>`.
2. **Ativação**: Vá nas configurações desse repo e ative o Pages.
3. **Acesso**: Aguarde a bolinha ficar verde na aba "Actions" ou recarregue a página de configurações para ver o link. Clique e veja seu site no ar!

## 🚀 Projeto da Aula
Vamos transformar o `portfolio-dev` em um site de verdade.

1. **Delete** o arquivo `sobre.txt` (se ainda existir). O `README.md` vamos manter.
2. **Crie** um arquivo `index.html` na raiz do projeto.
3. Cole este código (ou faça o seu melhor):
   ```html
   <!DOCTYPE html>
   <html>
   <head>
       <title>Portfólio Dev</title>
       <style>
           body { font-family: sans-serif; text-align: center; padding: 50px; }
           h1 { color: #2c3e50; }
           p { color: #7f8c8d; }
       </style>
   </head>
   <body>
       <h1>Olá, eu sou [Seu Nome]</h1>
       <p>Desenvolvedor apaixonado por Git e GitHub.</p>
       <a href="https://github.com/seu-usuario">Meu GitHub</a>
   </body>
   </html>
   ```
4. Commite e Push (`feat: adiciona site do portfólio`).
5. Vá no GitHub, Settings > Pages, Ative na `main`.
6. Aguarde alguns instantes e acesse o link gerado.
7. **Parabéns!** Você tem um site profissional. Mande o link para seus amigos!
