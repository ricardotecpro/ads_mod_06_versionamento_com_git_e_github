# Projeto 09 - Implementando o GitHub Flow

---

## 🚀 Objetivo
Simular um dia de trabalho real seguindo o fluxo ágil usado pelas maiores empresas de tecnologia.

### 📋 Passo a Passo

#### 1. Sincronização Matinal
Antes de qualquer código, garanta que sua base está atualizada:
```bash
git switch main
git pull origin main
```

#### 2. Criação da Feature
Você recebeu a tarefa de adicionar suas **Hard Skills** (Tecnologias) no portfólio.
```bash
git switch -c feat-tecnologias
```

#### 3. Desenvolvimento Atômico
1. Abra o arquivo `sobre.txt`.
2. Adicione uma seção: `### 🛠 Tecnologias: HTML, CSS, Git, GitHub`.
3. Salve e grave localmente:
   ```bash
   git add .
   git commit -m "feat: adiciona lista de tecnologias principais"
   ```

#### 4. Publicação e Revisão
1. Envie a branch para o servidor: `git push -u origin feat-tecnologias`.
2. No GitHub, abra o **Pull Request**.
3. Realize o **Merge** após revisar os arquivos.

#### 5. Limpeza de Terreno
Volte ao terminal e limpe a branch que já foi integrada:
```bash
git switch main
git pull origin main
git branch -d feat-tecnologias
```

### 🏆 Conquista
Sua `main` está atualizada e seu repositório está limpo. Você completou o ciclo de vida standard do GitHub Flow.
