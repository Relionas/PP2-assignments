from pathlib import Path

file_path = Path("sample.txt")

# Создание и запись
with open(file_path, "w") as f:
    f.write("Hello\nWorld\n123")

print("File created and written.")