# Exercícios da Aula 05

## 🛠 Exercícios

1. **Provocando um Conflito (Sandbox)**:
   - Crie uma pasta `treino-conflito`, inicie o git.
   - Crie `lista.txt` com: "Arroz, Feijão". Commite.
   - Crie branch `lista-nova`. Mude "Feijão" para "Feijão Preto". Commite.
   - Volte para `main`. Mude "Feijão" para "Feijão Carioca". Commite.
   - Merge `lista-nova`.
   - **Resultado**: CONFLITO!

2. **Resolvendo o Conflito**:
   - Abra `lista.txt`.
   - Você verá os marcadores.
   - Edite para ficar: "Arroz, Feijão Preto e Carioca" (ou escolha um).
   - Apague os símbolos `<<<`, `===`, `>>>`.
   - Salve.

3. **Finalizando**:
   - Rode `git status`. Ele dirá "both modified".
   - Rode `git add lista.txt`.
   - Rode `git commit`.
   - Rode `git log` para ver o merge registrado.

## Dica
Existem ferramentas visuais (no VS Code, GitKraken) que ajudam a resolver conflitos com cliques, mas aprender a fazer "na mão" é essencial para entender o processo.
