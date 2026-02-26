# Solução – Exercícios da Aula 03

Aqui você encontra as respostas sugeridas para os exercícios de Repositórios e Commits da Aula 03.

### 1. Iniciando a Jornada
O comando para transformar a pasta em um repositório é:
```bash
git init
```

### 2. O Primeiro Commit
A sequência de comandos é:
```bash
git add index.html
git commit -m "Adiciona index.html inicial"
```

### 3. Rastreando o Estado
O comando para verificar o estado é:
```bash
git status
```
O arquivo `estilos.css` aparecerá em **Vermelho** na seção chamada **Untracked files** (Arquivos não rastreados).

### 4. Visualizando o Passado
Para ver o histórico resumido em uma única linha por commit:
```bash
git log --oneline
```

### 5. A Pasta Oculta
Se você deletar a pasta `.git`, o Git deixará de reconhecer aquela pasta como um repositório. O comando `git status` retornará um erro: `fatal: not a git repository`. Você perderá todo o histórico de versões permanentemente.
