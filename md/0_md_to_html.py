import sys
from pathlib import Path
import re

# ----------------------------------------------------
# Get markdown file path (drag-and-drop support)
# ----------------------------------------------------
if len(sys.argv) < 2:
    print("Drag and drop a markdown file onto this script.")
    sys.exit(1)

md_file = Path(sys.argv[1]).resolve()
if not md_file.exists():
    print(f"File not found: {md_file}")
    sys.exit(1)

# ----------------------------------------------------
# Read markdown lines
# ----------------------------------------------------
lines = md_file.read_text(encoding="utf-8").splitlines()

# ----------------------------------------------------
# Extract Aircraft Name
# ----------------------------------------------------
aircraft_name = None
for line in lines[:20]:  # check first 20 lines
    match = re.match(r'AircraftName\s*:\s*(.+)', line, re.IGNORECASE)
    if match:
        aircraft_name = match.group(1).strip()
        break

if not aircraft_name:
    print("Aircraft name not found in markdown (use 'AircraftName: Name' syntax).")
    sys.exit(1)

# ----------------------------------------------------
# Extract AdaptedFrom links
# ----------------------------------------------------
adapted_from_links = []
for line in lines[:50]:  # scan first 50 lines
    match = re.match(r'AdaptedFrom\s*:\s*(.+)', line, re.IGNORECASE)
    if match:
        adapted_from_links = match.group(1).split()
        break

# ----------------------------------------------------
# Set output directory (root/checklists/)
# ----------------------------------------------------
root_dir = Path(__file__).resolve().parent.parent  # root/md/parent = root
output_dir = root_dir / "checklists"
output_dir.mkdir(parents=True, exist_ok=True)

html_file = output_dir / md_file.with_suffix(".html").name
print(f"HTML will be written to: {html_file}")

# ----------------------------------------------------
# Helpers: convert markdown links -> eye for images, anchors for others
# ----------------------------------------------------
IMAGE_EXTS = ('.jpg', '.jpeg', '.png', '.gif', '.webp', '.webm', '.bmp', '.svg', '.avif')

def replace_md_links_with_eye(text: str) -> str:
    """
    Replace [label](url) with:
      - image preview eye if url points to an image type
      - a normal anchor (target=_blank) otherwise
    Works anywhere in the text (left or right side, or info-box content).
    """
    def _repl(m: re.Match) -> str:
        label = m.group(1)
        url = m.group(2)
        core = url.split('?', 1)[0].split('#', 1)[0].lower()
        if core.endswith(IMAGE_EXTS):
            return (f'<span class="item-with-image">{label} '
                    f'<span class="image-eye" data-img="{url}">👁</span></span>')
        else:
            return f'<a href="{url}" target="_blank" class="adapted-link">{label}</a>'

    # Replace all markdown links in the string
    return re.sub(r'\[([^\]]+)\]\(([^)]+)\)', _repl, text)

# ----------------------------------------------------
# Build AdaptedFrom HTML (number emojis + tooltips + class)
# ----------------------------------------------------
adapted_from_html = ""
if adapted_from_links:
    number_emojis = ["1️⃣","2️⃣","3️⃣","4️⃣","5️⃣","6️⃣","7️⃣","8️⃣","9️⃣","🔟"]
    links_html = " ".join(
        f'<a href="{url}" target="_blank" class="adapted-link" title="{url}">{number_emojis[i]}</a>'
        for i, url in enumerate(adapted_from_links)
        if i < len(number_emojis)  # limit to 10 links
    )
    adapted_from_html = f'<div>{links_html}</div>'

# ----------------------------------------------------
# Info box + adapted links in a flex "metadata bar"
# ----------------------------------------------------
info_box_container_html = f"""
<div class="metadata-bar">
    <div class="info-box">
        <div><span class="swatch altitude"></span>Altitude</div>
        <div><span class="swatch note"></span>Notes</div>
        <div><span class="swatch tablet"></span>EFB/Tablet</div>
        <div><span class="swatch mcdu"></span>MCDU/FMC</div>
        <div><span class="swatch atc"></span>ATC</div>
    </div>
    {adapted_from_html}
</div>
"""

# ----------------------------------------------------
# Start HTML
# ----------------------------------------------------
current_category = None
current_checklist = None

html = f"""<!DOCTYPE html>
<html lang="en">

<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{aircraft_name} | MSFS</title>
<link rel="stylesheet" href="../assets/css/style.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>✅</text></svg>">
</head>

<body>
<div class="container">

  <!-- Floating scroll button -->
  <div class="scroll-container">
      <button class="scroll-btn">☰</button>
      <div class="scroll-menu"><ul></ul></div>
  </div>

  <!-- Header -->
  <header>
      <h1>MSFS Checklists</h1>
      <p class="subtitle">{aircraft_name}</p>
  </header>

  <!-- Top nav -->
  <div class="nav">
      <a href="../index.html" class="back-link"><i class="fas fa-arrow-left"></i> Back to Aircraft List</a>
      <div class="aircraft-name">{aircraft_name}</div>
  </div>

  <!-- Swatches + AdaptedFrom -->
  {info_box_container_html}

  <!-- Categories -->
  <div class="categories">
"""

# ----------------------------------------------------
# Process markdown lines into checklist HTML
# ----------------------------------------------------
for raw_line in lines:
    line = raw_line.strip()
    if not line:
        continue

    # Category
    if line.startswith("# "):
        if current_checklist is not None:
            html += "</ul></div></div>\n"
            current_checklist = None
        if current_category is not None:
            html += "</div></div>\n"
        current_category = line[2:].strip()
        html += (f'<div class="category"><div class="category-header" onclick="toggleCategory(this)">'
                 f'<span>{current_category}</span><i class="fas fa-chevron-down"></i></div>'
                 f'<div class="checklist-items">\n')
        continue

    # Checklist Section
    if line.startswith("## "):
        if current_checklist is not None:
            html += "</ul></div></div>\n"
        current_checklist = line[3:].strip()
        html += (f'<div class="checklist"><div class="checklist-header" onclick="toggleChecklist(this)">'
                 f'<span class="checklist-title">{current_checklist}</span>'
                 f'<i class="fas fa-chevron-down checklist-icon"></i></div>'
                 f'<div class="checklist-content"><ul>\n')
        continue

    # Divider
    if line.lower().startswith("### "):
        divider_text = line[len("### "):].strip()
        html += f'<div class="divider">{divider_text}</div>\n'
        continue

    # List items
    if line.startswith("- "):
        content = line[2:].strip()

        # Info Box Items (ATC/Note/Tablet/MCDU/Altitude)
        info_match = re.match(r'^\(\s*(ATC|Note|Tablet|MCDU|Altitude)\s*\)\s*(.+)', content, re.IGNORECASE)
        if info_match:
            box_type = info_match.group(1).lower() + "-box"
            box_content = info_match.group(2).strip()
            box_content = replace_md_links_with_eye(box_content)
            html += f'<li class="info-box {box_type}">{box_content}</li>\n'
            continue

        # Standard checklist line: split into left/right on the first ":" (if any)
        parts = content.split(":", 1)
        left_raw = parts[0].strip()
        right_raw = parts[1].strip() if len(parts) > 1 else ""

        # Transform any markdown links in left/right (adds 👁 for image links)
        left = replace_md_links_with_eye(left_raw)
        right = replace_md_links_with_eye(right_raw) if right_raw else ""

        html += (f'<li><div class="checklist-item">'
                 f'<span class="item-left">{left}</span>'
                 f'<span class="item-right">{right}</span>'
                 f'</div></li>\n')
        continue

# ----------------------------------------------------
# Close remaining checklist and category divs
# ----------------------------------------------------
if current_checklist is not None:
    html += "</ul></div></div>\n"
if current_category is not None:
    html += "</div></div>\n"

# Bottom nav + tooltip root + scripts
html += f"""<br>
<div class="nav">
    <a href="../index.html" class="back-link"><i class="fas fa-arrow-left"></i> Back to Aircraft List</a>
    <div class="aircraft-name">{aircraft_name}</div>
</div>

<div class="image-tooltip" id="image-tooltip"></div>

<script src="../assets/js/script.js"></script>
</body>
</html>
"""

# Write file
html_file.write_text(html, encoding="utf-8")
print(f"Generated {html_file}")
