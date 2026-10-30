
from pathlib import Path
from PIL import Image, ImageOps

assets = Path("assets")
extensions = {".png", ".jpg", ".jpeg"}

total_before = 0
total_after = 0

for file in assets.iterdir():
    if file.suffix.lower() not in extensions:
        continue

    try:
        with Image.open(file) as img:
            img = ImageOps.exif_transpose(img)

            # Batasi ukuran gambar maksimal 1600 piksel
            img.thumbnail((1600, 1600))

            output = file.with_suffix(".webp")

            img.save(
                output,
                "WEBP",
                quality=82,
                method=6
            )

        old_size = file.stat().st_size
        new_size = output.stat().st_size

        total_before += old_size
        total_after += new_size

        print(
            f"{file.name}: "
            f"{old_size / 1024 / 1024:.2f} MB -> "
            f"{new_size / 1024 / 1024:.2f} MB"
        )

    except Exception as e:
        print(f"Gagal memproses {file.name}: {e}")

print("\nSelesai!")
print(f"Ukuran awal: {total_before / 1024 / 1024:.2f} MB")
print(f"Ukuran WebP: {total_after / 1024 / 1024:.2f} MB")
