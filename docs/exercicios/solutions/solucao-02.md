# Solução – Exercícios da Aula 02

Aqui você encontra as respostas sugeridas para os exercícios de configuração da Aula 02.

### 1. Instalação do Git
Confirmação visual. Se o "Git Bash" abrir no seu Windows, a instalação foi um sucesso.

### 2. Configurando sua Identidade
Os comandos são:
```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu@email.com"
```

### 3. Validação de Configurações
O comando utilizado para listar todas as configurações é:
```bash
git config --list
```
**Alternativa**: Você também pode usar `git config user.name` para ver apenas o nome configurado.

### 4. Configuração do Editor Padrão
Para configurar o VS Code como editor padrão do Git, o comando é:
```bash
git config --global core.editor "code --wait"
```

### 5. Localizando o Arquivo de Configuração
- **No Windows**: O arquivo `.gitconfig` geralmente está em `C:\Users\SEU-USUARIO\.gitconfig`.
- **No Linux/macOS**: O arquivo está em `~/.gitconfig` (na raiz da sua pasta pessoal).
