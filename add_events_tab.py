import glob
import os

html_files = glob.glob('*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace desktop nav
    target_desktop = '<li><a href="journal.html" class="nav-link rounded-full px-3.5 py-1.5">Journal</a></li>'
    replacement_desktop = target_desktop + '\n        <li><a href="events.html" class="nav-link rounded-full px-3.5 py-1.5">Events</a></li>'
    if target_desktop in content:
        content = content.replace(target_desktop, replacement_desktop)
        
    # Replace mobile nav
    target_mobile = '<li><a href="journal.html" class="block px-5 py-3 border-b border-white/5">Journal</a></li>'
    replacement_mobile = target_mobile + '\n        <li><a href="events.html" class="block px-5 py-3 border-b border-white/5">Events</a></li>'
    if target_mobile in content:
        content = content.replace(target_mobile, replacement_mobile)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print('Done updating tabs')
