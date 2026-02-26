# Solução – Exercícios da Aula 07

Aqui você encontra as respostas sugeridas para os exercícios de Repositórios Remotos da Aula 07.

### 1. A Prática do Clone
O comando utilizado é:
```bash
git clone URL_DO_REPOSITORIO
```

### 2. Verificando o Vínculo
O comando é:
```bash
git remote -v
```
O termo **"origin"** é o nome (apelido) padrão dado ao servidor remoto principal do seu projeto.

### 3. Segurança com .gitignore
O Git ignorará o arquivo. Caso você tente forçar a adição via linha de comando, ele retornará uma mensagem avisando que o arquivo coincide com um padrão do seu `.gitignore`.

### 4. Conexão Remota
O comando para vincular um repositório local a um remoto é:
```bash
git remote add origin https://github.com/usuario/projeto.git
```

### 5. Ignorando por Padrão
A regra com caractere curinga no `.gitignore` é:
```text
*.log
```
Isso fará com que o Git ignore arquivos como `erro.log`, `sistema.log` ou `debug.log`.
