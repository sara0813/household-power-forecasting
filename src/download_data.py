
from pathlib import Path
import shutil
import kagglehub

path = kagglehub.dataset_download("uciml/electric-power-consumption-data-set")
print("Kagglehub cache path:", path)

src_dir = Path(path)
dst_dir = Path("data/raw")
dst_dir.mkdir(parents=True, exist_ok=True)

for p in src_dir.rglob("*"):
    if p.is_file():
        target = dst_dir / p.name
        shutil.copy2(p, target)
        print("Copied:", p.name, "->", target)
