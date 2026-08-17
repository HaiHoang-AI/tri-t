import json
import os

print("Bundling dataset and application into a single standalone HTML file...")

# Load questions JSON
with open('1100_cau_triet_hoc.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# Load base index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Replace <script src="1100_cau_triet_hoc.js"></script> with inline script
json_str = json.dumps(questions, ensure_ascii=False)
inline_script = f'<script>\nwindow.quizQuestions = {json_str};\n</script>'

# Replace the external script tag
target_tag = '<script src="1100_cau_triet_hoc.js"></script>'
if target_tag in html_content:
    bundled_html = html_content.replace(target_tag, inline_script)
else:
    print("Warning: target script tag not found, appending to head/body.")
    bundled_html = html_content.replace('</head>', f'{inline_script}\n</head>')

# Output filenames
output_path1 = 'index.html'
output_path2 = 'triet_1100_cau_trac_nghiem_standalone.html'

with open(output_path1, 'w', encoding='utf-8') as f:
    f.write(bundled_html)

with open(output_path2, 'w', encoding='utf-8') as f:
    f.write(bundled_html)

size_mb = os.path.getsize(output_path2) / (1024 * 1024)
print(f"Successfully created standalone HTML file: {output_path2} ({size_mb:.2f} MB)")
print(f"Successfully updated index.html to be fully self-contained.")
