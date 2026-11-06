import base64
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent
src = (ROOT / "src.html").read_text(encoding="utf-8")
images = {}
for path in sorted((ROOT / "img").glob("*.jpg")):
    data = base64.b64encode(path.read_bytes()).decode()
    images[path.stem] = f"data:image/jpeg;base64,{data}"
out = src.replace("/*IMG*/{}", json.dumps(images))
target = ROOT / "index.html"
target.write_text(out, encoding="utf-8")
sys.stdout.write(f"{target} {target.stat().st_size // 1024} KB\n")
