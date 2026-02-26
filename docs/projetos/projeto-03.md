# Projeto 03 - O Primeiro Commit

---

## 🚀 Objetivo
Transformar sua pasta comum em um repositório oficial e realizar o primeiro salvamento histórico.

### 📋 Passo a Passo

#### 1. Inicialização
Abra o Git Bash na pasta do seu portfólio e execute:
```bash
git init
```
*Observe que uma pasta oculta `.git` será criada.*

#### 2. Ciclo de Salvamento (Snapshot)

1. **Verifique o estado**:
   ```bash
   git status
   ```
   *O arquivo `sobre.txt` aparecerá em vermelho (Untracked).*

2. **Prepare para o commit**:
   ```bash
   git add sobre.txt
   ```

3. **Grave a versão**:
   ```bash
   git commit -m "feat: cria arquivo inicial sobre mim"
   ```

#### 3. Auditoria do Histórico
Para confirmar que seu nome e a mensagem foram gravados, use:
```bash
git log
```

### 🏆 Conquista
Seu projeto agora tem uma "âncora" no tempo. Você pode mudar o arquivo e, se errar, terá como voltar para este exato momento!
