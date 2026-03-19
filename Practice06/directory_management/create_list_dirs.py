import os
from pathlib import Path

# Создание вложенных папок
Path("test_dir/subdir").mkdir(parents=True, exist_ok=True)

# Список файлов и папок
print("Directory contents:")
print(os.listdir())