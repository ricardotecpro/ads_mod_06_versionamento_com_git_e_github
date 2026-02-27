# Aula 01 – O que é Controle de Versão?

---

## O Caos dos Arquivos Manuais

- Quem nunca?
  - `trabalho.doc`
  - `trabalho_v2.doc`
  - `trabalho_FINAL_agora_vai.doc`
- **Problemas**:
  - Difícil saber a versão real.
  - O que mudou entre os arquivos?
  - Risco de apagar algo importante.

---

## O que é um VCS?

- **V**ersion **C**ontrol **S**ystem
- Funciona como uma **"Máquina do Tempo"**.
- Registra:
  - **Quem** mudou?
  - **O que** mudou?
  - **Quando** mudou?

---

## Centralizado vs. Distribuído

- **Centralizado (ex: SVN)**:
  - Único servidor central.
  - Se o servidor cair, o trabalho para.
- **Distribuído (ex: Git)**:
  - Cada PC tem uma **cópia completa** do histórico.
  - Segurança e velocidade.
  - Funciona offline.

---

## Git vs. GitHub

| Git | GitHub |
| :--- | :--- |
| **Software** (Ferramenta) | **Plataforma** (Site) |
| Instalado no seu PC. | Na nuvem (Internet). |
| Motor do versionamento. | Facilita a colaboração. |

---

## Por que o Git?

- **Padrão industrial**: 90%+ das empresas usam.
- **Branches leves**: Troque de contexto instantaneamente.
- **Grátis e Open Source**.

---

## Verificação

No terminal:
```bash
git --version
```
> Se aparecer um número (ex: 2.45), você está pronto!
