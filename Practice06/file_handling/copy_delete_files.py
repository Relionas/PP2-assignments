import shutil
from pathlib import Path

file_path = Path("sample.txt")
backup_path = Path("backup.txt")

# Копирование
shutil.copy(file_path, backup_path)
print("File copied.")

# Проверка
if backup_path.exists():
    print("Backup exists.")

# Удаление
backup_path.unlink()
print("Backup deleted.")