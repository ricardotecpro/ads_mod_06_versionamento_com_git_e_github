# Aula 09 – Fluxo de trabalho com GitHub Flow

## 🎯 Objetivos de Aprendizagem
- Entender a importância de seguir um fluxo de trabalho padronizado.
- Aprender o **GitHub Flow**: um modelo simples e eficaz para projetos ágeis.
- Diferenciar GitHub Flow de Git Flow (mais complexo).
- Compreender o ciclo: Branch -> Commit -> PR -> Merge -> Deploy.

## 📚 Conteúdo

### 1. O que é um Workflow?
Um workflow (fluxo de trabalho) é um conjunto de regras que a equipe combina para evitar o caos.
Sem regras: "Vou commitar na main", "Vou criar a branch `teste-do-joao`", "Vou mergear sem PR".
Com regras: "Toda mudança precisa de branch", "A main é sagrada", "Só mergeia com aprovação".

### 2. O GitHub Flow
É o modelo recomendado pelo GitHub e usado por empresas modernas. Ele tem regras simples:
1. A branch `main` é **sempre** estável e pronta para ir ao ar (Deploy).
2. Para qualquer tarefa (nova feature ou bugfix), crie uma branch descritiva a partir da `main`.
3. Commite suas mudanças nessa branch.
4. Abra um Pull Request para discutir o código.
5. Após aprovação, faça o Merge na `main`.
6. Imediatamente após o merge, a `main` é atualizada em produção (Deploy).

### 3. GitHub Flow vs Git Flow
- **Git Flow**: Modelo antigo (2010), complexo, com branches `develop`, `release`, `hotfix`, tags... Bom para softwares "em caixa" com versões semestrais.
- **GitHub Flow**: Leve, contínuo, focado em web/SaaS e entrega rápida. É o que vamos focar.

## 📽 Roteiro de Slides
- O Caos sem Regras.
- Apresentando: GitHub Flow.
- Regra #1: A `main` é intocável e sempre funciona.
- O Ciclo de 6 Passos:
  - Create Branch.
  - Add Commits.
  - Open PR.
  - Discuss & Review.
  - Deploy (Teste).
  - Merge.
- Comparação Visual: GitHub Flow (linha reta com galhos curtos) vs Git Flow (teia de aranha complexa).

## 📝 Quiz
1. No GitHub Flow, a branch `main` deve estar em qual estado?
2. Qual a principal diferença para o Git Flow?
3. O que deve ser feito antes de qualquer mudança de código?
4. Quando o código deve ir para produção (Deploy) no GitHub Flow?
5. O que acontece com a branch de feature após o merge?

## Gabarito
1: B ("Sempre pronta para deploy")
2: A ("GitHub Flow é mais simples")
3: C ("Criar uma nova branch")
4: D ("Assim que o merge na main ocorre")
5: B ("Ela pode ser deletada")

## 🛠 Exercícios
1. **Desenhar o Fluxo**: Pegue papel e caneta. Desenhe o fluxo do GitHub Flow. (Main -> Branch -> Commits -> PR -> Merge -> Main).
2. **Simulação Completa**:
   - `git switch main` -> `git pull` (Garanta estar atualizado).
   - `git switch -c fix-typo`.
   - Corrija um erro de digitação proposital em qualquer arquivo.
   - `git push origin fix-typo`.
   - Abra o PR.
   - Merjeie.
   - Delete a branch.

## 🚀 Projeto da Aula
No `portfolio-dev`:
1. Vamos aplicar o GitHub Flow para adicionar uma seção de "Tecnologias".
2. Crie branch `feature-techs`.
3. No arquivo `sobre.txt`, adicione: "Tecnologias: Git, GitHub, Markdown".
4. Envie, abra PR, aprove.
5. **Importante**: No GitHub Flow, merges são frequentes. Não acumule trabalho de semanas. Tente mergear coisas pequenas todo dia.
