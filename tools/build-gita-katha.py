#!/usr/bin/env python3
"""content/gita-katha/chNN.part.js → app/js/gita-katha.js  (GITA_KATHA)"""
import glob, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'content', 'gita-katha')
OUT = os.path.join(ROOT, 'app', 'js', 'gita-katha.js')
BAD = re.compile(r'[\u0900-\u0963\u0966-\u097F\u0370-\u03FF\u0400-\u04FF\u0C80-\u0CFF'
                 r'\u0600-\u06FF\u4E00-\u9FFF\u3040-\u30FF\uAC00-\uD7AF]')

ENTRY = re.compile(r"^\s*'(\d+):(\d+)'\s*:\s*\{(.*?)\n\s*\},", re.M | re.S)

def check_entries(text, name):
    problems = []
    for m in ENTRY.finditer(text):
        body = m.group(3)
        k = re.search(r"katha:\s*'([^']*)'", body)
        p = re.search(r"prayog:\s*'([^']*)'", body)
        key = f"{m.group(1)}:{m.group(2)}"
        if not k or len(k.group(1)) < 40:
            problems.append(f'{name} {key}: katha অনুপস্থিত বা খুব ছোট')
        if not p or len(p.group(1)) < 20:
            problems.append(f'{name} {key}: prayog অনুপস্থিত বা খুব ছোট')
    return problems

files = sorted(glob.glob(os.path.join(SRC, 'ch*.part.js')))
if not files:
    sys.exit('no part files')

body, count, bad = [], 0, 0
for f in files:
    s = open(f, encoding='utf-8').read()
    for m in BAD.finditer(s):
        bad += 1
        print('!! non-Bengali script in', os.path.basename(f), repr(s[max(0, m.start()-25):m.start()+25]))
    words = re.sub(r"(src|katha|prayog):", "", re.sub(r"'\d+:\d+'", "", s))
    for m in re.finditer(r'[A-Za-z]{2,}', words):
        bad += 1
        print('!! latin word in', os.path.basename(f), repr(words[max(0, m.start()-25):m.start()+25]))
    for prob in check_entries(s, os.path.basename(f)):
        print('!!', prob)
        bad += 1
    if not s.rstrip().endswith(','):
        s = s.rstrip() + '\n,'
    body.append(s)
    count += len(re.findall(r"^\s*'\d+:\d+'\s*:", s, re.M))

out = ('/* শ্রীমদ্দভগবদ্গীতা — প্রতি শ্লোকের উদাহরণ-কথা ও জীবনে প্রয়োগ\n'
       '   স্বয়ংক্রিয়ভাবে তৈরি: tools/build-gita-katha.py · হাতে সম্পাদনা করবেন না */\n'
       'var GITA_KATHA = {\n' + '\n'.join(body) + '\n};\n')
open(OUT, 'w', encoding='utf-8').write(out)
print(f'built {os.path.relpath(OUT, ROOT)} — {count} শ্লোক, {len(files)} অধ্যায়-ফাইল, script-leak {bad}')
sys.exit(1 if bad else 0)
