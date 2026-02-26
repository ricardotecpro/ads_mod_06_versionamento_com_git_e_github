# Solução – Exercícios da Aula 14

Aqui você encontra as respostas sugeridas para os exercícios de GitHub Pages da Aula 14.

### 1. Ativação do Serviço
Resposta prática. A URL geralmente segue o padrão `https://seu-usuario.github.io/seu-repositorio/`.

### 2. Verificação do index.html
Se o arquivo for renomeado para `home.html`, o GitHub Pages não conseguirá encontrar o ponto de entrada padrão. O usuário receberá um erro **404 (Not Found)** ou verá apenas a listagem de arquivos (caso o README não esteja configurado como fallback).

### 3. Deploy em Tempo Real
Resposta prática. Geralmente o deploy leva entre **30 segundos a 2 minutos**, dependendo da fila de processamento do GitHub Actions.

### 4. Monitorando a "Esteira" (Actions)
O ícone **verde** indica que o processo de "Build" (construção) e "Deployment" (publicação) foi concluído com sucesso e o site foi atualizado.

### 5. Temas Automáticos (Jekyll)
O GitHub utiliza um motor chamado **Jekyll**. Ele lê o conteúdo do seu arquivo Markdown e o "injeta" dentro de um template HTML/CSS pronto. Isso permite focar apenas no conteúdo, deixando o design a cargo do gerador de site estático.
