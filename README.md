# NeuroDesk AI

An offline AI desktop assistant for Windows that understands natural language and automates desktop tasks using Python and local AI.

## 🚀 Current Version
**v0.2**

## ✅ Completed Features

### v0.1
- Launch Windows applications
- Parse basic commands (e.g. `open code`)
- Find applications available in `PATH`
- Open applications using `subprocess`

### v0.2
- Search common Windows installation folders
- Recursive application discovery using `os.walk()`
- Modular application search architecture
- Automatic application launching
- Handle applications that are not found

## 🏗️ Current Architecture

User Command
      │
      ▼
open_application()
      │
      ▼
find_application()
      │
 ┌────┴─────────────┐
 ▼                  ▼
find_in_path()   search_common_locations()
      │                  │
      └──────────┬───────┘
                 ▼
          Executable Path
                 │
                 ▼
        subprocess.Popen()

## 🛠️ Tech Stack

- Python
- pathlib
- shutil
- subprocess
- os
