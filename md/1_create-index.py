import sys
from pathlib import Path

# Usage: drag and drop index.md onto this script
if len(sys.argv) < 2:
    print("Usage: create-index.py <index_markdown>")
    sys.exit(1)

md_file = Path(sys.argv[1])
if not md_file.exists():
    print(f"File not found: {md_file}")
    sys.exit(1)

lines = md_file.read_text(encoding="utf-8").splitlines()

# Output index.html in root (one level above md file)
html_file = md_file.parent.parent / "index.html"

html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MSFS Checklists</title>
    <link rel="stylesheet" href="assets/css/style.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>✅</text></svg>">
</head>
<body>
<div class="container">
    <header>
        <h1>MSFS Checklists</h1>
        <p class="subtitle">A collection of checklists for simulator use only</p>

        <!-- Search Box -->
        <div class="search-container">
            <div class="search-box">
                <i class="fas fa-search"></i>
                <input type="text" id="searchInput" placeholder="Search aircraft...">
                <button id="clearSearch" class="clear-btn" aria-label="Clear search">&#10005;</button>
            </div>
        </div>
    </header>

    <div class="categories">
"""

current_category = None
current_aircraft = None
category_open = False  # Tracks if a category div is currently open

for line in lines:
    line = line.strip()
    if not line:
        continue

    # Category
    if line.startswith("# "):
        # Close previous category if open
        if category_open:
            html += '  </div>\n</div>\n'
            category_open = False

        current_category = line[2:].strip()
        html += f'<div class="category-group" data-category="{current_category.lower().replace(" ","-")}">\n'
        html += f'  <h2 class="category-title">{current_category}</h2>\n'
        html += '  <div class="category-box">\n'
        category_open = True
        current_aircraft = None

    # Aircraft entry
    elif line.startswith("## "):
        current_aircraft = {'file': line[3:].strip(), 'category': current_category, 'name': None, 'keywords': None}

    # Metadata
    elif line.startswith("- ") and current_aircraft is not None:
        parts = line[2:].split(":", 1)
        if len(parts) == 2:
            key = parts[0].strip().lower()
            val = parts[1].strip()
            current_aircraft[key] = val

        # If we now have both name and keywords, write the aircraft HTML
        if current_aircraft.get('name') and current_aircraft.get('keywords'):
            file = current_aircraft['file']
            name = current_aircraft['name']
            keywords = current_aircraft['keywords']
            category_class = current_aircraft['category'].lower().replace(" ","-")
            html += f'''    <a href="checklists/{file}.html" class="category-link {category_class}" data-name="{keywords}">
        <div class="category-icon">
            <i class="fas fa-plane"></i>
        </div>
        <div class="category-info">
            <h3>{name}</h3>
        </div>
        <div class="category-arrow">
            <i class="fas fa-chevron-right"></i>
        </div>
    </a>\n'''
            current_aircraft = None  # reset for next aircraft

# Close the last category div if still open
if category_open:
    html += '  </div>\n</div>\n'

# Footer + search script
html += """
    </div>

    <footer>
        <p>MSFS Checklists | A collection of checklists for simulator use only</p>
    </footer>
</div>

<script>
document.addEventListener('DOMContentLoaded', function () {
    const searchInput = document.getElementById('searchInput');
    const clearBtn = document.getElementById('clearSearch');
    const aircraftLinks = document.querySelectorAll('.category-link');
    const categoryGroups = document.querySelectorAll('.category-group');

    // Show/hide clear button
    searchInput.addEventListener('input', function () {
        clearBtn.style.display = this.value ? 'block' : 'none';
    });

    // Clear search
    clearBtn.addEventListener('click', function () {
        searchInput.value = '';
        clearBtn.style.display = 'none';
        aircraftLinks.forEach(link => link.style.display = 'flex');
        categoryGroups.forEach(group => group.style.display = 'block');
    });

    // Filter aircraft (case-insensitive)
    searchInput.addEventListener('input', function () {
        const searchTerm = this.value.toLowerCase().trim();
        if (searchTerm === '') {
            aircraftLinks.forEach(link => link.style.display = 'flex');
            categoryGroups.forEach(group => group.style.display = 'block');
            return;
        }

        aircraftLinks.forEach(link => {
            const name = link.getAttribute('data-name').toLowerCase();
            link.style.display = name.includes(searchTerm) ? 'flex' : 'none';
        });

        categoryGroups.forEach(group => {
            const links = group.querySelectorAll('.category-link');
            let hasVisible = false;
            links.forEach(link => { if (link.style.display !== 'none') hasVisible = true; });
            group.style.display = hasVisible ? 'block' : 'none';
        });
    });
});
</script>

</body>
</html>
"""

html_file.write_text(html, encoding="utf-8")
print(f"Generated {html_file}")
