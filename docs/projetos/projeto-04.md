# Projeto 04 - Isolamento com Branches

---

## 🚀 Objetivo
Aprender a trabalhar em funcionalidades novas sem colocar a versão principal em risco.

### 📋 Passo a Passo

#### 1. Criando a Nova Linha do Tempo
No terminal do seu portfólio:
```bash
git switch -c feat-contato
```
*Este comando cria a branch e já muda você para ela.*

#### 2. Adicionando Funcionalidade
1. Crie o arquivo `contato.txt`.
2. Escreva seu e-mail ou LinkedIn.
3. Salve, prepare e commite:
   ```bash
   git add contato.txt
   git commit -m "feat: adiciona informações de contato"
   ```

#### 3. O Teste do Desaparecimento
1. Volte para a branch principal:
   ```bash
   git switch main
   ```
   *(Ou `master`, dependendo da sua configuração).*
2. **Olhe sua pasta**: O arquivo `contato.txt` desapareceu! Ele existe apenas no "multiverso" da branch `feat-contato`.

#### 4. A Fusão (Merge)
Agora, traga a novidade para a versão oficial:
```bash
git merge feat-contato
```

### 🏆 Conquista
O arquivo reapareceu na branch principal. Você acaba de realizar um fluxo de trabalho profissional de isolamento.
