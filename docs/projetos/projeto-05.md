# Projeto 05 - Dominando Conflitos

---

## 🚀 Objetivo
Perder o medo de conflitos de merge através de uma simulação controlada e resolução manual.

### 📋 Passo a Passo

#### 1. Criando a Divergência
1. Crie uma branch chamada `ajuste-texto`: `git switch -c ajuste-texto`.
2. Edite `sobre.txt`. Mude seu cargo para: "Desenvolvedor em Formação".
3. Commite: `git commit -am "style: altera cargo na branch"` (o `-a` faz o add e commit juntos).

#### 2. O Conflito na Branch Principal
1. Volte para a `main`: `git switch main`.
2. Edite o MESMO `sobre.txt`. Mude o cargo para: "Futuro Especialista em Git".
3. Commite: `git commit -am "style: altera cargo na main"`.

#### 3. O Impacto
Tente unir as versões:
```bash
git merge ajuste-texto
```
*Você receberá o erro: `CONFLICT (content): Merge conflict in sobre.txt`.*

#### 4. A Resolução Manual
1. Abra o arquivo no VS Code. Ele estará cheio de marcadores (`<<<<`, `====`, `>>>>`).
2. Apague o que não deseja e remova os marcadores. Deixe apenas o texto limpo.
3. No terminal:
   ```bash
   git add sobre.txt
   git commit
   ```

### 🏆 Conquista
Você resolveu seu primeiro conflito! O Git agora tem um histórico unificado com a sua decisão final.
