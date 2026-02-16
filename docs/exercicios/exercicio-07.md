# Exercícios da Aula 07

## 🛠 Exercícios

1. **A Prática do Clone**:
   - Saia da pasta do seu projeto (`cd ..`).
   - Clone um repositório público qualquer, por exemplo, o guia de markdown:
     `git clone https://github.com/adam-p/markdown-here.git`
   - Entre na pasta criada.
   - Dê um `git log` e veja que você tem todo o histórico do projeto de outra pessoa!

2. **O Arquivo .gitignore**:
   - No seu repo de teste (`teste-local`):
   - Crie um arquivo chamado `segredo.txt`.
   - Crie um arquivo chamado `.gitignore`.
   - Dentro do `.gitignore` escreva: `segredo.txt`.
   - Tente dar `git add segredo.txt`.
   - O Git vai ignorar/reclamar. Isso prova que funcionou.

3. **Verificando Remotes**:
   - Digite `git remote -v`.
   - Você verá os endereços de `fetch` (onde baixa) e `push` (para onde envia).

## Atenção com Senhas
Nunca suba arquivos com senhas reais para o GitHub Público. Se acontecer, considere a senha comprometida e mude-a imediatamente no serviço original.
