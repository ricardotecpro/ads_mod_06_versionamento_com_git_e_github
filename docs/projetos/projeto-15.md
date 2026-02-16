# Projeto da Aula 15

## 🚀 Projeto da Aula: O Salvamento

Hoje você vai ser o herói de si mesmo.

### Passo 1: O "Desastre"
1. No `portfolio-dev`, edite o `index.html`. Apague todo o conteúdo e escreva "OOPS DELETEI TUDO".
2. Salve.
3. Não commite!

### Passo 2: O Arrependimento
1. Olhe para o arquivo e perceba o erro.
2. Use `git restore index.html` (ou `git checkout -- index.html` versão antiga).
3. Abra o arquivo. A mágica aconteceu? O código original voltou?

### Passo 3: O "Desastre" Maior (Reset)
1. Crie um arquivo `lixo.txt`.
2. `git add .` e `git commit -m "Commit inútil"`.
3. Olhe o `git log`. O commit inútil está lá.
4. Execute `git reset --hard HEAD~1` (Cuidado!).
5. Olhe o `git log`. O commit sumiu.
6. Olhe a pasta. O arquivo `lixo.txt` sumiu.
   (Nota: `--hard` é destrutivo para arquivos novos não trackeados ou mudanças. Use com sabedoria).

**Parabéns!** Você aprendeu a controlar o tempo.
