import json
import os
import sys
from pathlib import Path


try:
    cwd = Path(os.environ.get("INPUT_PATH"))  # type: ignore[arg-type]
except TypeError:
    cwd = Path.cwd()
messages_file = cwd / "messages.json"
if not messages_file.exists():
    print(f"OK: There is no file named 'messages.json' at '{cwd}'")
    sys.exit()

try:
    content = messages_file.read_bytes()
except Exception as exp:
    print(f"ERROR reading {messages_file}")
    print(exp)
    sys.exit(1)
else:
    print(f"OK: Could read {messages_file}")

try:
    messages = json.loads(content)
except Exception as exp:
    print(f"ERROR parsing {messages_file}")
    print(exp)
    sys.exit(1)
else:
    print(f"OK: Could parse {messages_file}")

error = False
for version, relative_path in messages.items():
    path = cwd / relative_path
    if not path.exists():
        print(f"ERROR {path} does not exist")
        error = True
        continue

    try:
        path.read_text()
    except Exception as exp:
        print(f"ERROR reading {path}")
        print(exp)
        error = True
    else:
        print(f"OK: Could read {path}")


if error:
    sys.exit(1)
else:
    print("OK: All tests passed.")
    sys.exit(0)
