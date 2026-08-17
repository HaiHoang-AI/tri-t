import pypdf
import re
import json
import os

reader = pypdf.PdfReader('1100-câu-Triết-học-Mác-Lênin.pdf')
full_text = '\n'.join([p.extract_text() for p in reader.pages])

blocks = re.split(r'(Câu\s+\d+\s*:)', full_text)

questions = []

for i in range(1, len(blocks), 2):
    header = blocks[i].strip()
    body = blocks[i+1].strip()
    q_num = int(re.search(r'\d+', header).group())
    
    ans_search = re.search(r'Đá\s*p\s*á\s*n\s*[:\s](.*)', body, re.IGNORECASE | re.DOTALL)
    if ans_search:
        ans_text = ans_search.group(0).strip()
        stem_and_options = body[:ans_search.start()].strip()
    else:
        ans_text = ''
        stem_and_options = body.strip()
        
    opt_pattern = r'(?:^|\n)\s*([A-Ea-e])[\.\/\)]\s*'
    opt_splits = re.split(opt_pattern, stem_and_options)
    
    stem = ' '.join(opt_splits[0].strip().split())
    options = []
    for j in range(1, len(opt_splits), 2):
        opt_key = opt_splits[j].upper()
        opt_val = ' '.join(opt_splits[j+1].split())
        options.append({
            'label': opt_key,
            'text': opt_val
        })
        
    ans_clean = re.sub(r'^Đá\s*p\s*á\s*n\s*:?\s*', '', ans_text, flags=re.IGNORECASE).strip()
    if '\n' in ans_clean:
        ans_clean = ans_clean.split('\n')[0].strip()
        
    # Extract correct key letters
    m = re.findall(r'\b([A-Ea-e])\b', ans_clean)
    correct_keys = list(dict.fromkeys([k.upper() for k in m if k.upper() in ['A','B','C','D','E']]))
    
    questions.append({
        'id': q_num,
        'question': stem,
        'options': options,
        'correct': correct_keys if len(correct_keys) > 1 else (correct_keys[0] if correct_keys else ''),
        'raw_answer': ans_clean
    })

print(f'Total extracted questions: {len(questions)}')

# Save JSON file
json_path = '1100_cau_triet_hoc.json'
with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)
print(f'Saved {json_path} ({os.path.getsize(json_path)/1024:.1f} KB)')

# Save JS file
js_path = '1100_cau_triet_hoc.js'
with open(js_path, 'w', encoding='utf-8') as f:
    f.write('window.quizQuestions = ')
    json.dump(questions, f, ensure_ascii=False, indent=2)
    f.write(';\n')
print(f'Saved {js_path} ({os.path.getsize(js_path)/1024:.1f} KB)')

# Save .quiz file
quiz_path = '1100_cau_triet_hoc.quiz'
with open(quiz_path, 'w', encoding='utf-8') as f:
    f.write('# QUIZ 1100 CÂU TRIẾT HỌC MÁC - LÊNIN\n\n')
    for q in questions:
        f.write(f"Câu {q['id']}: {q['question']}\n")
        for opt in q['options']:
            f.write(f"{opt['label']}. {opt['text']}\n")
        correct_str = ', '.join(q['correct']) if isinstance(q['correct'], list) else q['correct']
        f.write(f"Đáp án: {correct_str}\n\n")
print(f'Saved {quiz_path} ({os.path.getsize(quiz_path)/1024:.1f} KB)')
