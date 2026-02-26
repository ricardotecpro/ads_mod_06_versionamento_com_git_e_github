# Projeto 11 - A Arte do Commit Profissional

---

## 🚀 Objetivo
Aplicar o padrão **Conventional Commits** e entender a importância de mensagens claras para a manutenção do software.

### 📋 Passo a Passo

#### 1. Identificando a Melhoria
Escolha uma pequena alteração estética no seu portfólio (ex: corrigir um erro de digitação ou mudar a ordem de uma lista).

#### 2. Commit Semântico
Realize a alteração e, ao fazer o commit, use rigorosamente o prefixo correto:
- Se for erro de digitação: `fix: corrige typo no arquivo sobre.txt`
- Se for nova informação: `feat: adiciona formação acadêmica`
- Se for apenas visual: `style: melhora indentação do texto`

#### 3. Multi-Commits (Atomicidade)
Tente realizar duas melhorias separadas e faça **dois commits distintos**, um para cada ideia.
```bash
git add arquivo1.txt
git commit -m "docs: atualiza bio"

git add arquivo2.txt
git commit -m "feat: adiciona link de rede social"
```

#### 4. O Histórico Perfeito
Verifique o resultado com:
```bash
git log --oneline
```

### 🏆 Conquista
Seu histórico agora é uma lista de tarefas compreensível por qualquer pessoa (ou robô!) no mundo.
