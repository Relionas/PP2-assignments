import shutil
from pathlib import Path

source = Path("sample.txt")
destination = Path("test_dir/subdir/sample.txt")

# Перемещение
shutil.move(source, destination)

print("File moved.")