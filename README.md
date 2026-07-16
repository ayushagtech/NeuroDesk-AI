# NeuroDesk AI

An offline AI desktop assistant that automates Windows tasks using Python and local AI.

**v0.1**
### Features 
- Launch Windows applications
- Parse basic commands (e.g.`open code`)
- Find applications available in PATH
- Open applications using subprocess

## Current Version
**v0.2**
### Features 
- Search common Windows installation folders
- Recursive application discovery using `os.walk()`
- Modular application search architecture
- Automatic application launching
- Handle applications that are not found

# NeuroDesk AI

An offline AI desktop assistant for Windows that understands natural language and automates desktop tasks.

## Current Architecture

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

## Tech Stack

- Python
- pathlib
- shutil
- subprocess
- os
