from pathlib import Path
import sys

if len(sys.argv) != 2:
    print("Usage: python3 merge.py <page>")
    print("Example: python3 merge.py about")
    sys.exit(1)

page_name = sys.argv[1]
page_file = f"{page_name}.html"

if not Path(page_file).exists():
    print(f"❌ {page_file} not found!")
    sys.exit(1)

base = Path("base.html").read_text(encoding="utf-8")
page = Path(page_file).read_text(encoding="utf-8")

final = base.replace(
    "<!-- PAGE CONTENT GOES HERE -->",
    page
)

Path(page_file).write_text(
    final,
    encoding="utf-8"
)

print(f"✅ {page_file} converted successfully!")