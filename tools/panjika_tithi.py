"""
সনাতন বিদ্যাপীঠ — তিথি গণনা (ঢাকার সূর্যোদয়-ভিত্তিক, ephem)
তিথি = চন্দ্র-দ্রাঘিমা − সূর্য-দ্রাঘিমা (geocentric ecliptic), ১২° করে ৩০ ভাগ।
সূর্যোদয়ের সময় যে তিথি চলছে, পঞ্জিকায় সেদিনের তিথি সেটিই।
ব্যবহার: python3 tools/panjika_tithi.py 2026-12-01 2028-04-30
"""
import ephem, math, sys, json, datetime as dt

LAT, LON = '23.8103', '90.4125'          # ঢাকা
TITHI = ['প্রতিপদ','দ্বিতীয়া','তৃতীয়া','চতুর্থী','পঞ্চমী','ষষ্ঠী','সপ্তমী','অষ্টমী','নবমী','দশমী',
         'একাদশী','দ্বাদশী','ত্রয়োদশী','চতুর্দশী','পূর্ণিমা']

def sunrise(d):
    o = ephem.Observer(); o.lat, o.lon = LAT, LON
    o.pressure = 0; o.horizon = '-0:34'
    o.date = ephem.Date(ephem.Date(d.strftime('%Y/%m/%d') + ' 00:00:00'))   # UTC 00:00
    return o.next_rising(ephem.Sun())

def tithi(d):
    t = sunrise(d)
    e = (math.degrees(ephem.Ecliptic(ephem.Moon(t)).lon) - math.degrees(ephem.Ecliptic(ephem.Sun(t)).lon)) % 360
    i = int(e // 12) + 1
    return i

def label(i):
    return ('শুক্লা ' if i <= 15 else 'কৃষ্ণ ') + TITHI[(i - 1) % 15]

if __name__ == '__main__':
    a = dt.date.fromisoformat(sys.argv[1]); b = dt.date.fromisoformat(sys.argv[2])
    d, out = a, {}
    while d <= b:
        out[d.isoformat()] = tithi(d); d += dt.timedelta(days=1)
    print(json.dumps(out))
