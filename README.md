# auxilia

**auxilia** é uma ferramenta de linha de comando escrita em Python para automatizar a criação de projetos web com estrutura profissional, templates temáticos e boas práticas desde o primeiro commit.

A ideia é simples: reduzir trabalho repetitivo e acelerar o início de qualquer projeto web.

---

## ✨ Funcionalidades

- 📁 Criação automática da estrutura do projeto
- 🎨 Templates prontos (`light`, `dark`, `purple`)
- 🧩 Inicialização opcional de repositório Git
- ⚡ Execução rápida via CLI
- 🔒 Organização preparada para variáveis de ambiente (`.env`)
- 🧠 Boas práticas de organização de arquivos

---

## 🚀 Uso

```bash
python3 auxilia nome_do_projeto
````

### Criar projeto com tema específico

```bash
python3 auxilia meu_projeto --theme dark
```

### Criar projeto com Git inicializado

```bash
python3 auxilia meu_projeto --git
```

### Sobrescrever arquivos existentes

```bash
auxilia meu_projeto --force
```

---

## 🎨 Temas disponíveis

* **light** — Tema claro e simples
* **dark** — Tema escuro moderno
* **purple** — Tema roxo com estética 💜

---

## 📁 Estrutura gerada

```
meu_projeto/
├── index.html
├── css/
│   └── styles.css
├── js/
│   └── script.js
├── assets/
├── README.md
└── .gitignore
```

---

## 🧠 Objetivo do projeto

O **auxilia** foi criado para auxiliar os alunos de minha sala que tem mais dificuldade.

---
