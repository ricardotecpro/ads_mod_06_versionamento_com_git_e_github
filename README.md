# Git e GitHub

Domine o controle de versão do zero ao avançado e colabore profissionalmente!

## 🎯 Sobre o Curso

Este curso oferece uma trilha completa de aprendizado em Git e GitHub, desde a instalação básica até fluxos de trabalho avançados e colaboração em equipe.

### ✨ Destaques

- ✅ **Aulas Práticas** - Conteúdo focado no terminal e usabilidade
- ✅ **Slides Interativos** - Apresentações modernas com Reveal.js
- ✅ **Quizzes e Exercícios** - Fixação imediata de conteúdo
- ✅ **Projetos para Portfólio** - Construa sua presença no GitHub
- ✅ **Mentoria Visual** - Diagramas Mermaid explicativos

## 🚀 Começando

### Pré-requisitos

- Git instalado
- Conta no GitHub
- Python 3.11+ (para rodar o site localmente)
- Poetry (para gerenciar dependências do site)

### Instalação

```bash
# Clonar repositório
git clone https://github.com/ricardotecpro/ads_mod_06_versionamento_com_git_e_github.git
cd ads_mod_06_versionamento_com_git_e_github

# Instalar dependências (MkDocs e plugins)
poetry install
```

## 📚 Comandos Disponíveis

### Com Taskipy

```bash
# Servidor local
poetry run task serve

# Build do site
poetry run task build

# Gerar slides e quizzes
poetry run task slides
poetry run task quizzes

# Executar testes
poetry run task test
```

## 📁 Estrutura do Projeto

```
ads_mod_06_versionamento_com_git_e_github/
├── docs/                      # Conteúdo do curso
│   ├── aulas/                # Lições detalhadas
│   ├── exercicios/           # Listas de fixação
│   ├── quizzes/              # Quizzes interativos
│   ├── projetos/             # Projetos práticos
│   ├── slides/               # Slides (Reveal.js)
│   └── index.md              # Homepage
├── hooks/                     # Hooks customizados MkDocs
├── .github/workflows/         # CI/CD
├── pyproject.toml            # Poetry + Taskipy
├── mkdocs.yml                # Configuração MkDocs
└── scripts/                   # Scripts de automação
```

## 🎨 Tecnologias

### Ferramentas do Curso
- **Git** - Controle de versão distribuído
- **GitHub** - Plataforma de colaboração e hospedagem
- **Markdown** - Escrita de documentação

### Infraestrutura do Site
- **MkDocs** + **Material for MkDocs**
- **Reveal.js** - Para os slides
- **Poetry** - Automação e dependências
- **Pytest** - Links e build check

## 🧪 Testes

```bash
# Executar testes de links e build
poetry run task test
```

## 🚀 Deploy

O curso é publicado automaticamente no GitHub Pages via GitHub Actions.

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir Issues ou Pull Requests.

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👤 Autor

**Ricardo**

- GitHub: [@ricardotecpro](https://github.com/ricardotecpro)
- LinkedIn: [ricardotecpro](https://linkedin.com/in/ricardotecpro)

---

⭐ Se este curso te ajudou, considere dar uma estrela no repositório!
