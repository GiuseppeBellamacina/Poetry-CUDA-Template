# 📦 Poetry Cheatsheet

## 🛠️ Setup iniziale

```bash
poetry init                # Crea un pyproject.toml (interattivo)
poetry new myproject       # Crea un nuovo progetto con struttura base
```

---

## 📁 Ambiente virtuale

```bash
poetry install             # Installa tutto dal pyproject.toml
poetry shell               # Attiva il virtualenv
poetry run python          # Esegue un comando dentro il venv

poetry env info            # Info sull'ambiente virtuale corrente
poetry env list            # Mostra tutti gli ambienti disponibili
poetry env remove <path>   # Rimuove un venv
```

---

## 📦 Gestione dipendenze

```bash
poetry add <pacchetto>                    # Aggiunge una dipendenza
poetry add <pacchetto>@<versione>         # Con una versione specifica
poetry add <pacchetto> --group dev        # Aggiunge come dipendenza di sviluppo

poetry remove <pacchetto>                 # Rimuove una dipendenza

poetry update                             # Aggiorna tutte le dipendenze
poetry update <pacchetto>                 # Aggiorna un solo pacchetto
```

### 🔒 Lockfile

```bash
poetry lock                               # Rigenera il file poetry.lock
```

---

## 📄 pyproject.toml – sintassi delle versioni

| Sintassi     | Significato                     |
| ------------ | ------------------------------- |
| `^1.2.3`     | >=1.2.3,<2.0.0 (default sicuro) |
| `~1.2.3`     | >=1.2.3,<1.3.0 (agg. minore)    |
| `>=1.2,<1.5` | Intervallo esplicito            |
| `*`          | Qualsiasi versione              |
| `==1.2.3`    | Solo quella versione            |

---

## 🔧 Comandi utili

```bash
poetry build              # Crea il pacchetto (.whl e .tar.gz)
poetry publish            # Pubblica su PyPI
poetry version patch      # Bump automatico (patch/minor/major)
poetry config             # Gestisci la configurazione globale/locale
```

---

## 🧪 Eseguire codice

```bash
poetry run python script.py         # Esegui script.py nel venv
poetry run pytest                   # Esegui i test (se installato)
```

---

## 📂 Struttura consigliata progetto

```
myproject/
├── pyproject.toml
├── poetry.lock
├── README.md
├── myproject/
│   └── __init__.py
└── tests/
    └── test_something.py
```

---

## 🧼 Disinstallazione & cleanup

```bash
poetry env list --full-path
poetry env remove <path>           # Rimuove un venv specifico
```

---

## 🔍 Note extra

- I venv di Poetry di default sono in:
  `~/.cache/pypoetry/virtualenvs/` (Linux/macOS)
  `C:\Users\<user>\AppData\Local\pypoetry\Cache\virtualenvs` (Windows)

- Per usare un Python diverso:

  ```bash
  poetry env use C:/Python312/python.exe
  ```

- Per disabilitare la modalità "packaging":
  Aggiungi nel `pyproject.toml`:

  ```toml
  [tool.poetry]
  package-mode = false
  ```

---

## 🚀 Torch

Per installare PyTorch con CUDA 13.0, usa il seguente comando:

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu130
```

Poetry non gestisce direttamente le versioni di PyTorch, quindi usa `pip` per installarlo nel venv creato da Poetry. Ovviamente questo comando non aggiornerà il `pyproject.toml`, quindi dovrai aggiungere manualmente PyTorch come dipendenza se necessario.

---

## 🧠 Consigli

- Blocca le versioni di pacchetti critici per evitare problemi (es. `torch`, `numpy`)
- Usa `poetry export -f requirements.txt` se ti serve `requirements.txt` per compatibilità
- Non usare `pip install` dentro un venv gestito da Poetry (rischio conflitti)

---

## 💻 VS Code Settings

```json
{
  "python.venvPath": "C:/Users/<user>/AppData/Local/pypoetry/Cache/virtualenvs"
}
```

Cerca e modifica le impostazioni di VS Code per usare il venv di Poetry in modo automatico.
