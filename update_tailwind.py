import os
import glob

html_files = glob.glob("*.html")

old_colors = """          colors: {
            void: '#050505',
            base: '#0a0a0b',
            surface: '#101012',
            elevated: '#16161a',
          },"""

new_colors = """          colors: {
            white: 'rgb(var(--color-white) / <alpha-value>)',
            black: 'rgb(var(--color-black) / <alpha-value>)',
            void: 'var(--bg-void)',
            base: 'var(--bg-base)',
            surface: 'var(--bg-surface)',
            elevated: 'var(--bg-elevated)',
          },"""

updated_count = 0

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if old_colors in content:
        content = content.replace(old_colors, new_colors)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        updated_count += 1
        print(f"Updated {f}")
    elif "white: 'rgb(var(--color-white)" in content:
        print(f"Already updated {f}")
    else:
        print(f"Could not find target string in {f}")

print(f"Updated {updated_count} files total.")
