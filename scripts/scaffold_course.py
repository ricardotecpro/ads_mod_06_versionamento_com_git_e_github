import os
from pathlib import Path

# --- Configuration ---
SYLLABUS = [
    # Módulo 1 – Conceitos Básicos
    {"id": 1, "module": "Módulo 1 – Conceitos Básicos", "title": "Introdução ao Controle de Versão"},
    {"id": 2, "module": "Módulo 1 – Conceitos Básicos", "title": "Instalação e Configuração Inicial"},
    {"id": 3, "module": "Módulo 1 – Conceitos Básicos", "title": "Configuração de Identidade e Editores"},
    
    # Módulo 2 – Trabalhando Localmente
    {"id": 4, "module": "Módulo 2 – Trabalhando Localmente", "title": "Criando Repositórios e o comando init"},
    {"id": 5, "module": "Módulo 2 – Trabalhando Localmente", "title": "O Ciclo de Vida dos Arquivos (add/commit)"},
    {"id": 6, "module": "Módulo 2 – Trabalhando Localmente", "title": "Visualizando o Histórico (git log)"},
    
    # Módulo 3 – Operações Intermediárias
    {"id": 7, "module": "Módulo 3 – Operações Intermediárias", "title": "Desfazendo Alterações (checkout/reset/revert)"},
    {"id": 8, "module": "Módulo 3 – Operações Intermediárias", "title": ".gitignore – Ignorando Arquivos Corretamente"},
    
    # Módulo 4 – Branches e Organização
    {"id": 9, "module": "Módulo 4 – Branches e Organização", "title": "Trabalhando com Branches e o comando branch"},
    {"id": 10, "module": "Módulo 4 – Branches e Organização", "title": "Integrando Alterações (merge)"},
    {"id": 11, "module": "Módulo 4 – Branches e Organização", "title": "Resolvendo Conflitos de Merge"},
    
    # Módulo 5 – Git Remoto e GitHub
    {"id": 12, "module": "Módulo 5 – Git Remoto e GitHub", "title": "Trabalhando com Repositórios Remotos"},
    {"id": 13, "module": "Módulo 5 – Git Remoto e GitHub", "title": "GitHub – Introdução e Pull Requests"},
    {"id": 14, "module": "Módulo 5 – Git Remoto e GitHub", "title": "Colaboração em Equipe (fork/clone)"},
    
    # Módulo 6 – Fluxos Avançados
    {"id": 15, "module": "Módulo 6 – Fluxos Avançados", "title": "Fluxos de Trabalho (Git Flow vs GitHub Flow)"},
    {"id": 16, "module": "Módulo 6 – Fluxos Avançados", "title": "Boas Práticas e Convenções de Commit"},
]

DIRS = [
    "docs/slides",
    "docs/quizzes",
    "docs/exercicios",
    "docs/projetos",
    "docs/assets/images"
]

# --- Templates ---

TEMPLATE_AULA = """# {title}

## Objetivos da Aula
- [ ] Compreender ...
- [ ] Aplicar ...

## Conteúdo

### Introdução
O comando abaixo mostra como iniciar...

```bash
# Exemplo de comando Git
git init
```

```termynal-exec
git status
# On branch main
# nothing to commit
```

!!! tip "Dica Importante"
    Este é um bloco de dica.

!!! failure "Erro Comum"
    Cuidado com conflitos de merge!

## Em Prática
Vamos praticar o conceito aprendendo...

## Resumo
Nesta aula aprendemos sobre...

---
## 🎯 Próximos Passos

<div class="grid cards" markdown>

-   :material-presentation: **Acessar Slides**
    -   [Ver Slides da Aula](slides/{id:02d}-slides.md)

-   :material-school: **Quiz**
    -   [Responder Quiz](quizzes/quiz-{id:02d}.md)

-   :material-dumbbell: **Exercícios**
    -   [Lista de Exercícios](exercicios/exercicios-{id:02d}.md)

-   :material-rocket: **Projeto**
    -   [Mini Projeto](projetos/projeto-{id:02d}.md)

</div>
"""

TEMPLATE_SLIDE = """---
theme: material
---

# {title}
## Aula {id:02d}

---

## Objetivos
- Objetivo 1
- Objetivo 2

---

## Tópico 1
Conteúdo do tópico...

---

## Exemplo de Código

```bash
git commit -m "feat: add new feature"
```

---

## Resumo
- Ponto chave 1
- Ponto chave 2

---

<!-- _class: lead -->
# Próxima Aula: ...
"""

TEMPLATE_QUIZ = """# Quiz {id:02d}: {title}

**Teste seus conhecimentos.**

    ```bash
    git init
    ```
    - (x) Inicia um novo repositório
    - ( ) Deleta o repositório
    - ( ) Instala o Git

2. Git é o mesmo que GitHub?
    - ( ) Sim
    - (x) Não
"""

TEMPLATE_EXERCICIO = """# Exercícios Aula {id:02d}

## Nível: Fácil
1. Crie um programa que...

## Nível: Médio
2. Faça uma função que...

## Nível: Difícil
3. Implemente um algoritmo que...
"""

TEMPLATE_PROJETO = """# Projeto Aula {id:02d}

## Descrição
Desenvolva uma ferramenta que...

## Requisitos
- [ ] Usar variáveis
- [ ] Usar input

## Desafio
Tente adicionar uma funcionalidade extra de...
"""

TEMPLATE_INDEX = """# Bem-vindo ao Curso de Git e GitHub

## O Curso
Este curso foi desenhado para te levar do zero ao profissional.

## Estrutura
- 15 Módulos práticos
- Exercícios e Projetos a cada aula
- Slides e Quizzes interativos

<div class="grid cards" markdown>

-   :material-rocket: **Começar Agora**
    -   [Ir para Aula 01](aulas/aula-01.md)

</div>
"""

# --- Execution ---

def create_files():
    # 1. Ensure Directories
    for d in DIRS:
        Path(d).mkdir(parents=True, exist_ok=True)
    
    # 2. Create Index if missing
    if not Path("docs/index.md").exists():
        Path("docs/index.md").write_text(TEMPLATE_INDEX, encoding="utf-8")
        print("Created index.md")

    # 3. Generate Content
    for lesson in SYLLABUS:
        lid = lesson["id"]
        title = lesson["title"]
        
        # Paths
        p_aula = Path(f"docs/aulas/aula-{lid:02d}.md")
        p_slide = Path(f"docs/slides/slide-{lid:02d}.md")
        p_quiz = Path(f"docs/quizzes/quiz-{lid:02d}.md")
        p_exerc = Path(f"docs/exercicios/exercicio-{lid:02d}.md")
        p_proj = Path(f"docs/projetos/projeto-{lid:02d}.md")
        
        # Write Files
        if not p_aula.exists():
            p_aula.write_text(TEMPLATE_AULA.format(id=lid, title=title), encoding="utf-8")
        
        if not p_slide.exists():
            p_slide.write_text(TEMPLATE_SLIDE.format(id=lid, title=title), encoding="utf-8")
            
        if not p_quiz.exists():
            p_quiz.write_text(TEMPLATE_QUIZ.format(id=lid, title=title), encoding="utf-8")
            
        if not p_exerc.exists():
            p_exerc.write_text(TEMPLATE_EXERCICIO.format(id=lid, title=title), encoding="utf-8")
            
        if not p_proj.exists():
            p_proj.write_text(TEMPLATE_PROJETO.format(id=lid, title=title), encoding="utf-8")
            
        print(f"Generated Lesson {lid:02d}: {title}")

def generate_nav_yaml():
    nav = ["nav:", "  - Início: index.md"]
    
    nav.append("  - Aulas:")
    nav.append("      - aulas/index.md")
    
    current_module = None
    
    for lesson in SYLLABUS:
        module = lesson["module"]
        title = lesson["title"]
        lid = lesson["id"]
        filename = f"aulas/aula-{lid:02d}.md"
        
        if module != current_module:
            nav.append(f"      - {module}:")
            current_module = module
        
        nav.append(f"        - 'Aula {lid:02d} - {title}': {filename}")
    
    nav.append("  - Materiais:")
    nav.append("      - materiais.md")
    nav.append("      - Slides: slides/index.md")
    nav.append("      - Exercícios: exercicios/index.md")
    nav.append("      - Quizzes: quizzes/")
    nav.append("      - Projetos: projetos/")
    nav.append("      - Setups: setups/index.md")
    nav.append("  - Impressão: print_page.md")
    
    return "\n".join(nav)

def update_mkdocs():
    mkdocs_path = Path("mkdocs.yml")
    content = mkdocs_path.read_text(encoding="utf-8")
    
    # Remove existing 'nav:' if present (simplistic approach, assumes nav is at end or distinct)
    # We will append the new nav
    # Better: finding where nav starts
    
    if "nav:" in content:
        content = content.split("nav:")[0] # Truncate everything after nav:
    
    new_nav = generate_nav_yaml()
    
    final_content = content.strip() + "\n\n" + new_nav + "\n"
    mkdocs_path.write_text(final_content, encoding="utf-8")
    print("Updated mkdocs.yml navigation")

if __name__ == "__main__":
    create_files()
    update_mkdocs()
