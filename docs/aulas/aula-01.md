# Aula 01 – O que é controle de versão e por que usar Git

## 🎯 Objetivos de Aprendizagem
- Entender o conceito de Controle de Versão e sua importância.
- Diferenciar Git (software) de GitHub (plataforma).
- Compreender a diferença entre sistemas centralizados e distribuídos.
- Conhecer a história e a popularidade do Git no mercado de TI.

## 📚 Conteúdo

### 1. O Problema do "Versão Final.doc"
Você já trabalhou em um arquivo importante e acabou criando cópias como:
- `tcc_final.doc`
- `tcc_final_agora_vai.doc`
- `tcc_final_IMPRIMIR.doc`

Isso é **controle de versão manual** e é propenso a falhas. Você perde o histórico do que mudou, quem mudou e por que mudou.

### 2. O que é um Sistema de Controle de Versão (VCS)?
Um VCS (*Version Control System*) é um software que registra as mudanças em um ou mais arquivos ao longo do tempo. Ele permite que você:
- Reverta arquivos para um estado anterior.
- Compare mudanças ao longo do tempo.
- Veja quem modificou o que.
- Recupere arquivos perdidos.

### 3. Git: O Padrão da Indústria
O Git é um **Sistema de Controle de Versão Distribuído**.
- **Distribuído** significa que cada desenvolvedor tem uma cópia completa de todo o histórico do projeto em seu computador, não apenas a última versão.
- Foi criado por Linus Torvalds (criador do Linux) em 2005.
- É rápido, eficiente e permite trabalho offline.

### 4. Git vs GitHub
É crucial não confundir os dois:
- **Git**: É a ferramenta (software) que você instala no seu computador para gerenciar versões. Funciona localmente.
- **GitHub**: É uma plataforma na nuvem que hospeda repositórios Git. Funciona como uma rede social para desenvolvedores e facilita o trabalho em equipe.
*Analogia*: O Git é como o Microsoft Word (ferramenta), e o GitHub é como o Google Drive (onde você guarda e compartilha).

## 📽 Roteiro de Slides
- O Caos dos Arquivos Manuais (v1, v2, final)
- O que é Version Control System (VCS)?
- Benefícios: Histórico, Backup, Trabalho em Equipe
- Git: Distribuído, Rápido, Padrão de Mercado
- Git vs GitHub: Ferramenta Local vs Plataforma na Nuvem
- Glossário Inicial: Repositório, Commit (visão geral)

## 📝 Quiz
1. Qual é a principal função de um Sistema de Controle de Versão?
2. Quem criou o Git?
3. Qual a diferença fundamental entre Git e GitHub?
4. O que significa o Git ser "Distribuído"?
5. Qual problema o Git resolve?

## Gabarito
1: A
2: C
3: B
4: D
5: A

## 🛠 Exercícios
1. **Verificação Inicial**: Abra seu terminal e digite:
   ```console
   $ git --version
   git version 2.40.0.windows.1
   ```
   Se der erro, não se preocupe, instalaremos na próxima aula.
2. **Criação de Conta**: Acesse [github.com](https://github.com) e crie sua conta gratuita, caso ainda não tenha. Escolha um nome de usuário profissional.
3. **Simulação Manual**: Crie uma pasta chamada `simulacao_vcs` no seu computador. Crie um arquivo texto, faça uma alteração e salve uma cópia `v2`. Note a dificuldade de gerenciar isso manualmente.

## 🚀 Projeto da Aula
Neste curso, construiremos um **Portfólio Profissional**.
- **Passo 1**: Crie uma pasta no seu computador (Desktop ou Documentos) chamada `meu-portfolio-git`.
- **Passo 2**: Dentro dela, crie um arquivo de texto simples chamado `sobre.txt` e escreva apenas seu nome.
- **Passo 3**: Guarde essa pasta. Nas próximas aulas, vamos transformá-la em um repositório Git e subi-la para o GitHub.
