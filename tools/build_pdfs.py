"""Render every story/*.md file to pdf/<name>.pdf with headless Chromium."""
import glob
import os
import subprocess
import tempfile

import markdown

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHROME = os.environ.get("CHROME", "/opt/pw-browsers/chromium-1194/chrome-linux/chrome")

CSS = """
@page { size: Letter; margin: 0.8in 0.75in; }
body { font-family: Georgia, 'Times New Roman', serif; font-size: 11pt; line-height: 1.45; color: #111; }
h1 { font-family: Helvetica, Arial, sans-serif; color: #b3121d; border-bottom: 3px solid #b3121d; padding-bottom: 6px; }
h2 { font-family: Helvetica, Arial, sans-serif; color: #b3121d; margin-top: 28px; page-break-after: avoid; }
h3 { font-family: Helvetica, Arial, sans-serif; color: #333; page-break-after: avoid; }
table { border-collapse: collapse; width: 100%; margin: 10px 0; font-size: 10pt; page-break-inside: avoid; }
th, td { border: 1px solid #999; padding: 5px 8px; text-align: left; vertical-align: top; }
th { background: #eee; }
blockquote { border-left: 4px solid #b3121d; background: #f6f6f6; margin: 10px 0; padding: 6px 14px; page-break-inside: avoid; }
pre { font-family: 'Courier New', Courier, monospace; font-size: 10pt; line-height: 1.3; white-space: pre-wrap; background: none; }
code { font-family: 'Courier New', Courier, monospace; }
hr { border: none; border-top: 1px solid #bbb; margin: 20px 0; }
"""


def build(md_path):
    name = os.path.splitext(os.path.basename(md_path))[0]
    with open(md_path, encoding="utf-8") as f:
        body = markdown.markdown(f.read(), extensions=["tables", "fenced_code", "nl2br"])
    html = f"<!doctype html><html><head><meta charset='utf-8'><title>{name}</title><style>{CSS}</style></head><body>{body}</body></html>"
    out = os.path.join(ROOT, "pdf", f"{name}.pdf")
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as tmp:
        tmp.write(html)
    subprocess.run(
        [CHROME, "--headless", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
         f"--print-to-pdf={out}", f"file://{tmp.name}"],
        check=True, capture_output=True,
    )
    os.unlink(tmp.name)
    print(out)


if __name__ == "__main__":
    os.makedirs(os.path.join(ROOT, "pdf"), exist_ok=True)
    for path in sorted(glob.glob(os.path.join(ROOT, "story", "*.md")) + glob.glob(os.path.join(ROOT, "story", "films", "*.md")) + glob.glob(os.path.join(ROOT, "story", "series", "*.md")) + glob.glob(os.path.join(ROOT, "story", "chapters", "*.md"))):
        build(path)
