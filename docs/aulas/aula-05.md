# Aula 05 – Resolução de Conflitos

## 🎯 Objetivos de Aprendizagem
- Entender o que é um conflito de merge (Merge Conflict).
- Identificar quando e por que conflitos acontecem.
- Aprender a ler os marcadores de conflito (`<<<<<<<`, `=======`, `>>>>>>>`).
- Resolver conflitos manualmente e finalizar o merge.

## 📚 Conteúdo

### 1. O que é um Conflito?
O Git é muito inteligente. Se duas pessoas alterarem arquivos diferentes, ou até partes diferentes do MESMO arquivo, ele consegue unir (merge) tudo sozinho.
Porém, se duas pessoas alterarem a **mesma linha** de formas diferentes, o Git entra em pânico: "Qual das duas versões eu devo manter?". Isso é um conflito.

### 2. Identificando um Conflito
Quando você tenta fazer um `git merge` e dá conflito, o Git avisa:
`CONFLICT (content): Merge conflict in arquivo.txt`.
O `git status` mostrará o arquivo como `both modified`.

### 3. Anatomia de um Conflito
Dentro do arquivo, o Git adiciona marcadores especiais:
```text
<<<<<<< HEAD
Texto da minha branch atual (ex: main)
=======
Texto da branch que estou tentando unir (ex: feature)
>>>>>>> feature
```
Sua missão é:
1. Apagar as linhas `<<<<`, `====`, `>>>>`.
2. Decidir qual texto fica (ou reescrever um novo texto que combine os dois).
3. Salvar.

### 4. Finalizando
Depois de editar e salvar:
1. `git add arquivo.txt` (Isso diz ao Git: "Resolvi!").
2. `git commit` (Sem mensagem, ele abrirá um editor com uma mensagem padrão de merge, basta salvar e sair).

## 📽 Roteiro de Slides
- O Pesadelo do Desenvolvedor Iniciante: A tela `CONFLICT`.
- Por que acontece? (Mexer na mesma linha ao mesmo tempo).
- O que o Git faz? (Ele PAUSA o merge e pede ajuda).
- Os Símbolos Mágicos:
  - `<<<<<<<` (O que eu tenho).
  - `=======` (Divisória).
  - `>>>>>>>` (O que está chegando).
- O Passo a Passo da Resolução: Editar -> Add -> Commit.
- Dica de Ouro: Comunique-se com sua equipe para evitar isso!

## 📝 Quiz
1. Quando ocorre um conflito de merge?
2. Como o Git resolve conflitos automaticamente na mesma linha?
3. O que significam as linhas entre `<<<<<<<` e `=======`?
4. Qual comando usamos para marcar um arquivo como "resolvido"?
5. O que devemos fazer com os marcadores de conflito (`<<<<`, `====`, `>>>>`)?

## Gabarito
1: B
2: D
3: A
4: C
5: A

## 🛠 Exercícios
1. **Prepare o Terreno**: Crie um repo novo `conflito-sandbox`. Crie `texto.txt` com "Linha 1: Original" e commite.
2. **Branch A**: Crie branch `modificacao-a`. Mude para ela. Mude o texto para "Linha 1: Modificação A". Commite.
3. **Branch B**: Volte para a `main`. Mude o arquivo para "Linha 1: Modificação B". Commite.
4. **O Caos**: Tente fazer `git merge modificacao-a`. Veja o conflito acontecer!
5. **A Solução**: Abra o arquivo, escolha qual frase manter, apague os marcadores, salve, faça `git add` e `git commit`.

## 🚀 Projeto da Aula
No `meu-portfolio-git`:
1. Crie uma branch `conflito-proposital`.
2. Mude o título no `sobre.txt`. Commite.
3. Volte para a `main`.
4. Mude o MESMO título no `sobre.txt` para algo diferente. Commite.
5. Tente mergear.
6. **Resolva o conflito** escolhendo o melhor título e finalizando o merge. Parabéns, você é um pacificador de código!
