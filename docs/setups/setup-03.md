# Configuração do Ambiente (macOS)

Este guia mostra como instalar e configurar o **Git** no macOS utilizando o terminal ou instaladores oficiais.

---

## 1. Instalando o Git

Existem três formas principais de ter o Git no seu Mac:

### Opção A: Via Homebrew (Recomendado)

Se você já usa o [Homebrew](https://brew.sh), basta rodar:

```bash
brew install git
```

### Opção B: Via Xcode Command Line Tools

O macOS costuma vir com um "atalho" para o Git. Tente rodar o comando abaixo no Terminal:

```bash
git --version
```

Se não estiver instalado, o macOS abrirá uma janela perguntando se você deseja instalar as "Ferramentas de Linha de Comando do Xcode". Clique em **Instalar**.

### Opção C: Instalador Binário

Baixe o instalador oficial (`.dmg`) em: [git-scm.com/download/mac](https://git-scm.com/download/mac).

---

## 2. Verificando a Instalação

Abra o Terminal e digite:

```bash
git --version
```

**Saída esperada:**
```
git version 2.x.x
```

---

## 3. Configuração de Identidade (Obrigatória)

Configurar sua autoria é o passo mais importante para seus commits aparecerem corretamente no GitHub.

Execute no terminal:

```bash
git config --global user.name "Seu Nome Completo"
git config --global user.email "seu.email@exemplo.com"
```

> **Dica**: Use o e-mail da sua conta do GitHub para que seu gráfico de contribuições seja contabilizado.

---

## 4. Configurando Chave SSH (Opcional)

Para facilitar o envio de código (Push) sem digitar senha:

1. Gere a chave:
   ```bash
   ssh-keygen -t ed25519 -C "seu.email@exemplo.com"
   ```
2. Adicione ao agente:
   ```bash
   eval "$(ssh-agent -s)"
   ssh-add --apple-use-keychain ~/.ssh/id_ed25519
   ```
3. Copie para o GitHub:
   ```bash
   pbcopy < ~/.ssh/id_ed25519.pub
   ```
4. Cole em **Settings > SSH and GPG keys** no seu perfil do GitHub.

---

## ✅ Pronto!

Seu ambiente macOS está configurado e pronto para o curso! 🍎

**Próximos passos:**
- Vá para a [Aula 01](../aulas/aula-01.md)
- Inicie seu projeto de portfólio!
