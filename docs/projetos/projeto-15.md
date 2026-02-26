# Projeto 15 - Viajando no Tempo

---

## 🚀 Objetivo
Praticar técnicas de recuperação de arquivos e reversão de commits para nunca mais ter medo de errar.

### 📋 Passo a Passo

#### 1. A Recuperação (Restore)
1. Edite seu arquivo `sobre.txt` e apague metade do conteúdo (sem querer!).
2. Salve o arquivo.
3. No terminal, use: `git restore sobre.txt`.
4. Verifique que o conteúdo voltou ao normal!

#### 2. A Reversão (Reset Soft)
1. Faça uma pequena alteração e dê um commit com uma mensagem errada (ex: `git commit -m "asdjaslkd"`).
2. Use o comando de rebobinar:
   ```bash
   git reset --soft HEAD~1
   ```
3. O commit "sumiu", mas o arquivo continua alterado e pronto para você commitar com a mensagem correta.

#### 3. O Botão de Pânico (Reset Hard)
1. Crie um arquivo `teste_erro.txt` e faça um commit.
2. Agora, imagine que você quer deletar esse commit E o arquivo de uma só vez:
   ```bash
   git reset --hard HEAD~1
   ```

### 🏆 Conquista
Você agora domina a "borracha" do Git. Erros não são mais permanentes, são apenas lições aprendidas.
