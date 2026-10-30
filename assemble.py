from pathlib import Path
import hashlib
import json
import shutil
import zipfile

root = Path(__file__).resolve().parent
manifest = json.loads((root / "trial-release.json").read_text())
archive = root / "trial-webgl.zip"
output = root / "_site"
combined = hashlib.sha256()
with archive.open("wb") as stream:
    for part in manifest["parts"]:
        name = part["name"]
        if Path(name).name != name:
            raise ValueError("Invalid release part name")
        data = (root / name).read_bytes()
        if len(data) != part["size"] or hashlib.sha256(data).hexdigest() != part["sha256"]:
            raise ValueError("Release part verification failed: " + name)
        combined.update(data)
        stream.write(data)
if combined.hexdigest() != manifest["sha256"]:
    raise ValueError("Release archive checksum mismatch")
if output.exists():
    shutil.rmtree(output)
output.mkdir()
with zipfile.ZipFile(archive) as release:
    if release.testzip():
        raise ValueError("Release archive CRC failed")
    for member in release.infolist():
        if Path(member.filename).name != member.filename or member.is_dir():
            raise ValueError("Unexpected archive layout")
    release.extractall(output)
for name in ("index.html", "index.js", "index.wasm", "index.pck"):
    if not (output / name).is_file():
        raise ValueError("Missing required WebGL file: " + name)
if (output / "index.wasm").read_bytes()[:4] != b"\x00asm":
    raise ValueError("Invalid WebAssembly file")
(output / ".nojekyll").touch()
print("Verified PCA3D Trial", manifest["version"], "ready for GitHub Pages")
