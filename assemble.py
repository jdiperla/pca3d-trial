from pathlib import Path
import hashlib
import shutil
import zipfile

root = Path(__file__).resolve().parent
archive = root / "trial-webgl.zip"
output = root / "_site"
expected = "179fbc09649da1c37b95adc14049dd3aba6a033538fbcb60392656be4d8cbbe6"
checksum = hashlib.sha256()
with archive.open("rb") as stream:
    while data := stream.read(1024 * 1024):
        checksum.update(data)
if checksum.hexdigest() != expected:
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
print("Verified PCA3D Trial", "0.76.8", "ready for GitHub Pages")
