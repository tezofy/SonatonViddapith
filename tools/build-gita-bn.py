#!/usr/bin/env python3
"""content/gita-bn/chNN.part.js → app/js/gita-bn.js একত্র করা"""
import glob, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
parts = sorted(glob.glob(os.path.join(ROOT, 'content/gita-bn/ch*.part.js')))
out = ["/* ==========================================================================\n"
       "   শ্রীমদ্ভগবদ্গীতা — বাংলা অনুবাদ ও সহজ ভাষ্য\n"
       "   উৎস ফাইল: content/gita-bn/chNN.part.js  →  এই ফাইল স্বয়ংক্রিয়ভাবে তৈরি\n"
       "   পুনরায় বানাতে:  python3 tools/build-gita-bn.py\n"
       "   ========================================================================== */\n",
       "const GITA_BN = {\n"]
total = 0
for p in parts:
    body = open(p, encoding='utf-8').read().strip()
    if not body.endswith(','):
        body += ','   # অংশগুলোর মাঝে কমা নিশ্চিত
    out.append("\n/* ---------- %s ---------- */\n" % os.path.basename(p))
    out.append(body + "\n")
    total += len(re.findall(r"'(\d+):(\d+)'\s*:", body))
out.append("\n};\n")
open(os.path.join(ROOT, 'app/js/gita-bn.js'), 'w', encoding='utf-8').write(''.join(out))
print('built app/js/gita-bn.js — %d শ্লোক, %d অধ্যায়-ফাইল' % (total, len(parts)))
