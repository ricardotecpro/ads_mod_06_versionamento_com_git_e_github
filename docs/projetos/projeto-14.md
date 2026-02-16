# Projeto da Aula 14

## 🚀 Projeto da Aula: Publicando

Seu site já deve estar no ar. Vamos melhorá-lo.

### Passo 1: Melhorando o HTML
Adicione uma foto sua.
1. Salve uma foto `perfil.jpg` na pasta do projeto.
2. Adicione `<img src="perfil.jpg" width="150" style="border-radius: 50%;">` antes do `<h1>` no `index.html`.
3. `git add .`, `git commit -m "feat: adiciona foto"`, `git push`.

### Passo 2: O Badge de Deploy
1. Vá na aba "Actions".
2. Clique no último workflow de "pages-build-deployment" que deu sucesso.
3. Procure por "Create status badge" (...) ou vá no README e adicione manualmente.
4. Adicione isso ao seu README:
   `![GitHub Pages](https://github.com/SEU-USUARIO/portfolio-dev/actions/workflows/pages/pages-build-deployment/badge.svg)`
   (Ajuste o link conforme necessário, ou pegue a sintaxe correta na aba Actions > Três pontinhos > Create status badge).

Agora quem visitar seu repo saberá que o site está "Passing" (No ar).
