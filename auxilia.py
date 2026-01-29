import re
import argparse
import subprocess
from pathlib import Path
import sys
import os

VERSION = "1.3.0"

# ──────────────────── LOGO ────────────────────
def banner():
    print("\033[95m")
    print(" █████╗  ██████╗ ██╗   ██╗███████╗███████╗██╗")
    print("██╔══██╗██╔════╝ ██║   ██║██╔════╝██╔════╝██║")
    print("███████║██║  ███╗██║   ██║███████╗███████╗██║")
    print("██╔══██║██║   ██║██║   ██║╚════██║╚════██║██║")
    print("██║  ██║╚██████╔╝╚██████╔╝███████║███████║██║")
    print("╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚═╝")
    print("        A C U S S I   C L I  •  CYBERPUNK")
    print("\033[0m")

# ──────────────────── TEMPLATES ────────────────────
TEMPLATES = {
    "light": {
        "html": """<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>{{title}}</title>
  <link rel="stylesheet" href="css/styles.css">
</head>
<body>
  <h1>{{title}}</h1>
</body>
</html>
""",
        "css": "body { font-family: Arial; padding: 40px; }\n"
    },
    "dark": {
        "html": """<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>{{title}}</title>
  <link rel="stylesheet" href="css/styles.css">
</head>
<body>
  <h1>{{title}} 🌙</h1>
</body>
</html>
""",
        "css": "body { background:#0f0f0f; color:#f1f1f1; padding:40px; }\n"
    },
    "purple": {
        "html": """<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>{{title}}</title>
  <link rel="stylesheet" href="css/styles.css">
</head>
<body>
  <h1>{{title}} 💜</h1>
</body>
</html>
""",
        "css": "body { background:#0b0614; color:#e5d9ff; padding:40px; }\n"
    }
}

# ──────────────────── DB TEMPLATE ────────────────────
DB_PHP = """<?php
$host = getenv('ALTERAR');
$db   = getenv('ALTERAR');
$user = getenv('ALTERAR');
$pass = getenv('ALTERAR');

try {
    $pdo = new PDO(
        "mysql:host=$host;dbname=$db;charset=utf8mb4",
        $user,
        $pass,
        [
            PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
            PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
            PDO::ATTR_EMULATE_PREPARES => false
        ]
    );
} catch (PDOException $e) {
    error_log($e->getMessage());
    die("Erro ao conectar ao banco de dados.");
}
"""
ENV_FILE = "DB_HOST=\nDB_NAME=\nDB_USER=\nDB_PASS=\n"

# ──────────────────── CORE ────────────────────
def sanitize_name(name: str) -> str:
    name = name.lower().strip()
    name = re.sub(r"\s+", "_", name)
    return re.sub(r"[^a-z0-9_]", "", name)

def create_file(path: Path, content: str, force: bool):
    if path.exists() and not force:
        print(f"⚠️ Já existe: {path}")
        return
    path.write_text(content, encoding="utf-8")
    print(f"📄 Criado: {path}")

def main():
    banner()

    parser = argparse.ArgumentParser(description="ACUSSI — Criador profissional Web")
    parser.add_argument("name", nargs="?")
    parser.add_argument("--theme", default="light", choices=TEMPLATES.keys())
    parser.add_argument("--git", action="store_true")
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--version", action="version", version=VERSION)

    args = parser.parse_args()

    # Se abriu sem argumentos (duplo clique)
    if not args.name:
        parser.print_help()
        return

    project_name = sanitize_name(args.name)
    project = Path(project_name)

    (project / "css").mkdir(parents=True, exist_ok=True)
    (project / "js").mkdir(exist_ok=True)
    (project / "assets").mkdir(exist_ok=True)
    (project / "config").mkdir(exist_ok=True)

    tpl = TEMPLATES[args.theme]

    create_file(project / "index.html", tpl["html"].replace("{{title}}", project_name), args.force)
    create_file(project / "css/styles.css", tpl["css"], args.force)
    create_file(project / "js/script.js", "// JS\n", args.force)
    create_file(project / "config/db.php", DB_PHP, args.force)
    create_file(project / ".env", ENV_FILE, args.force)
    create_file(project / ".gitignore", ".env\nnode_modules/\n", args.force)

    if args.git:
        subprocess.run(["git", "init"], cwd=project, check=False)

    print(f"✅ Projeto '{project_name}' criado com DB configurável!")

# ──────────────────── EXECUÇÃO SEGURA ────────────────────
if __name__ == "__main__":
    os.system("title Só Auxilia - CLI")
    
    # Se abrir por duplo clique, força -h
    if len(sys.argv) == 1:
        sys.argv.append("-h")

    main()
    input("\nPressione ENTER para sair...")
