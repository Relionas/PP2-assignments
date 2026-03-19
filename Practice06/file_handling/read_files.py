from pathlib import Path

file_path = Path("sample.txt")

# Чтение
with open(file_path, "r") as f:
    content = f.read()
    print("File content:")
    print(content)