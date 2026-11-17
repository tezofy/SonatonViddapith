#!/usr/bin/env python3
"""build-gita-speaker.py — প্রতি শ্লোকের বক্তা নির্ধারণ করে js/gita-speaker.js বানায়।

উৎস: content/gita-bn/ch*.part.js — যেখানে অনুবাদ শুরু হয় "সঞ্জয় বললেন —" /
"অর্জুন বললেন —" / "শ্রীভগবান বললেন —" / "ধৃতরাষ্ট্র বললেন —" দিয়ে, সেখানেই
বক্তা বদলায়; না থাকলে আগের বক্তাই চলতে থাকে। এতে আমাদের সংস্করণের
শ্লোক-সংখ্যাকেই বক্তা ঠিক বসে।
"""
import re, glob, os, json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAMES = {
    'ধৃতরাষ্ট্র': 'dhritarashtra',
    'সঞ্জয়': 'sanjaya',
    'অর্জুন': 'arjuna',
    'শ্রীভগবান': 'krishna',
    'ভগবান': 'krishna',
    'কৃষ্ণ': 'krishna',
}

def main():
    mp, segs, cur = {}, [], None
    for f in sorted(glob.glob(os.path.join(ROOT, 'content/gita-bn/ch*.part.js'))):
        src = open(f, encoding='utf-8').read()
        for key, bn in re.findall(r"'(\d+:\d+)':\s*\{\s*bn: '([^']*)'", src):
            m = re.match(r'^(\S+?) বললেন', bn)
            if m and m.group(1) in NAMES:
                cur = NAMES[m.group(1)]
            if cur is None:
                raise SystemExit('বক্তা পাওয়া যায়নি: ' + key)
            mp[key] = cur
            ch = int(key.split(':')[0])
            if segs and segs[-1][0] == cur and segs[-1][2] == ch:
                segs[-1][1] = key
            else:
                segs.append([cur, key, ch])

    lines = ["/* স্বয়ংক্রিয় ফাইল — tools/build-gita-speaker.py বানিয়েছে। হাতে সম্পাদনা নয়। */",
             "const GITA_SPEAKER = {"]
    for k, v in mp.items():
        lines.append("  '%s': '%s'," % (k, v))
    lines.append("};")
    lines.append("const GITA_SPEAKER_SEG = [" + ", ".join(
        "{ s: '%s', a: '%s', b: '%s' }" % (s, a, b) for s, a, b in segs) + "];")
    out = os.path.join(ROOT, 'app/js/gita-speaker.js')
    open(out, 'w', encoding='utf-8').write("\n".join(lines) + "\n")

    from collections import Counter
    print('built app/js/gita-speaker.js — %d শ্লোক, %d বক্তা-পর্ব, বক্তা: %s' % (
        len(mp), len(segs), ', '.join('%s %d' % (k, v) for k, v in Counter(mp.values()).most_common())))

if __name__ == '__main__':
    main()
