# 🚀 গিটহাবে রিপো তৈরি ও লাইভ করার নির্দেশিকা

**সনাতন বিদ্যাপীঠ** — এই ফোল্ডারটি এখন গিটহাবে তোলার জন্য সম্পূর্ণ প্রস্তুত। নিচে তিনটি উপায় দেওয়া আছে; যেটি সহজ লাগে সেটি বেছে নিন।

> 📦 **সবচেয়ে সহজ:** `sanatana-biddapith-github.zip` ফাইলটি ডাউনলোড করে **উপায় ১** অনুসরণ করুন — কোনো কমান্ড লাগবে না।

---

## ধাপ ০ · আগে যা যা লাগবে

| জিনিস | কেন |
|---|---|
| একটি **GitHub অ্যাকাউন্ট** (ফ্রি) | কোড রাখতে ও লাইভ করতে |
| রিপোর নাম ঠিক করে নিন | প্রস্তাবিত নাম: **`sanatana-biddapith`** (ইংরেজি ছোট হাতের অক্ষর, হাইফেন) |
| সিদ্ধান্ত: রিপো **Public** রাখুন | ফ্রি অ্যাকাউন্টে GitHub Pages শুধু পাবলিক রিপোতে চলে |

---

## উপায় ১ · ওয়েবসাইট থেকে আপলোড (কমান্ড ছাড়া) — সবচেয়ে সহজ

1. [github.com/new](https://github.com/new) এ যান।
2. **Repository name**: `sanatana-biddapith`
3. **Visibility**: **Public** নির্বাচন করুন।
4. **README / .gitignore / license** — কোনোটি টিক দেবেন না (আমাদের নিজের ফাইল আছে)। → **Create repository**।
5. পরের পাতায় **"uploading an existing file"** লিংকে ক্লিক করুন।
6. `sanatana-biddapith-github.zip` ফাইলটি কম্পিউটারে আনজিপ করুন, তারপর **ভেতরের সব ফাইল/ফোল্ডার** (অর্থাৎ `app`, `docs`, `.github`, `README.md`, `LICENSE`, `CONTRIBUTING.md`, `GITHUB-PUSH-GUIDE.md`, `.gitignore`) একসাথে সিলেক্ট করে ড্র্যাগ করে ব্রাউজারে ফেলুন।
   > ⚠️ **`.github` ফোল্ডারটি লুকানো (hidden)** — ফাইল ম্যানেজারে *"লুকানো ফাইল দেখাও / Show hidden files"* চালু না করলে সেটি মিস হবে। মিস হলেও সাইট চলবে, শুধু অটো-ডিপ্লয় ওয়ার্কফ্লো থাকবে না (নিচে উপায় ৩ দেখুন)।
7. নিচে **Commit changes** → **Commit changes** চাপুন।
8. এবার **উপায় ৩ (Pages চালু করা)** অনুসরণ করুন।

---

## উপায় ২ · Git কমান্ড দিয়ে (কম্পিউটারে Git থাকলে)

```bash
# ১) প্রজেক্ট ফোল্ডারে ঢুকুন
cd sanatana-biddapith

# ২) গিট চালু করে প্রথম কমিট
git init
git add .
git commit -m "সনাতন বিদ্যাপীঠ — প্রথম সংস্করণ"

# ৩) ব্রাঞ্চের নাম main
git branch -M main

# ৪) গিটহাবের রিপো জুড়ুন (আপনার ইউজারনেম বসান)
git remote add origin https://github.com/<আপনার-ইউজারনেম>/sanatana-biddapith.git

# ৫) পুশ
git push -u origin main
```

> প্রথমবার পুশে GitHub পাসওয়ার্ড চাইলে → **Personal Access Token** ব্যবহার করুন
> (GitHub → Settings → Developer settings → Personal access tokens → Fine-grained token → `repo`/`Contents: Read and write`)।
> অথবা **GitHub Desktop** অ্যাপ দিয়ে ৪-৫ ধাপ মাউসে করে ফেলুন: *Add local repository → Publish repository*।

---

## উপায় ৩ · GitHub Pages চালু করা (লাইভ লিংক পাওয়া)

### ক) Actions দিয়ে (সুপারিশকৃত — ওয়ার্কফ্লো ফাইল দেওয়াই আছে)

1. রিপোতে ঢুকে **Settings** → বাম দিকে **Pages**।
2. **Build and deployment → Source** = **GitHub Actions**।
3. **Actions** ট্যাবে গিয়ে *"Deploy to GitHub Pages"* ওয়ার্কফ্লোটি চালু/রান করুন (পুশ করলেই নিজে থেকে চলে)।
4. ১–২ মিনিট পর লিংক পাবেন:
   `https://<আপনার-ইউজারনেম>.github.io/sanatana-biddapith/`

### খ) ওয়ার্কফ্লো ছাড়া (একদম সহজ পথ)

1. **Settings → Pages** → **Source** = **Deploy from a branch**।
2. **Branch** = `main`, **Folder** = **`/app`** → **Save**।
3. ১ মিনিট পর একই লিংকে সাইট লাইভ।

> সাইট রাখা হয়েছে `app/` ফোল্ডারে, তাই ফোল্ডার হিসেবে **`/app`** বেছে নিতে হবে — শুধু `/(root)` দিলে ৪০৪ আসবে।

---

## ধাপ ৪ · লাইভ হওয়ার পর যা করবেন

| কাজ | কীভাবে |
|---|---|
| মোবাইলে ইনস্টল | ফোনের ব্রাউজারে লিংক খুলুন → মেনু → **"Add to Home screen"** |
| রিপোর বর্ণনা | রিপো পেজে ⚙️ **Edit** → Description: *"সনাতন বিদ্যাপীঠ — শাস্ত্র, পরীক্ষা, সাধনা ও সেবার এক প্ল্যাটফর্ম (PWA)"* + Website: আপনার Pages লিংক |
| টপিক্স | `bengali` `hinduism` `pwa` `javascript` `education` `bangla-calendar` |
| টিম যোগ | Settings → Collaborators (কনটেন্ট/কোড দেখাশোনার জন্য) |
| ভবিষ্যতে কাস্টম ডোমেইন | Settings → Pages → Custom domain (যেমন `sanatanabiddapith.org`) + DNS-এ CNAME |

---

## 🔄 পরে কিছু বদলালে আপডেট করবেন যেভাবে

```bash
git add .
git commit -m "গীতা দান পেজ যোগ হলো"
git push
```

পুশ হলেই Actions নিজে থেকে সাইট আপডেট করে (১-২ মিনিট)। **ব্রাউজারে পুরোনো ভার্সন দেখালে** `Ctrl+Shift+R` (মোবাইলে: ব্রাউজার ডেটা ক্লিয়ার) দিন — কারণ `index.html`-এ `?v=5` ক্যাশ-বাস্ট দেওয়া আছে, বড় পরিবর্তনে সেটি `?v=6` করে বাড়িয়ে দিলেই নতুন ফাইল লোড হবে।

---

## 🧰 সমস্যা ও সমাধান

| সমস্যা | কারণ ও সমাধান |
|---|---|
| লিংকে **404** | Pages সোর্সে ফোল্ডার **`/app`** দেওয়া হয়নি, অথবা Actions ওয়ার্কফ্লো এখনো শেষ হয়নি। (রুটে একটি ছোট `index.html` আছে যা `/app/`-এ পাঠায় — সোর্স `/(root)` হলেও সাইট খুলবে) |
| পাতা **সাদা/ফাঁকা** | `js/app.js` বা `css/app.css` লোড হয়নি — রিপোতে ফোল্ডার-স্ট্রাকচার অটুট আছে কি না দেখুন (`app/css/…`, `app/js/…`) |
| পুরোনো ভার্সন দেখাচ্ছে | হার্ড রিফ্রেশ (`Ctrl+Shift+R`), অথবা `?v=` বাড়ান |
| থিম/ডেটা সেভ হচ্ছে না | ব্রাউজারে `localStorage` বন্ধ (প্রাইভেট মোড) — সাধারণ উইন্ডোতে চেষ্টা করুন |
| Actions লাল (failed) | Settings → Pages → Source = **GitHub Actions** আছে কি না দেখুন; তারপর Actions ট্যাব → *Re-run jobs* |
| বাংলা ফন্ট অদ্ভুত দেখাচ্ছে | ডিভাইসে বাংলা ফন্ট নেই — সিস্টেম ফন্ট ফলব্যাক ব্যবহার হচ্ছে, কোডে সমস্যা নেই |

---

## 📁 রিপোতে ঠিক কী কী যাচ্ছে

```
README.md                     ← রিপোর মূল বিবরণী (এটাই প্রথমে দেখা যাবে)
LICENSE                       ← MIT লাইসেন্স
CONTRIBUTING.md               ← অবদানের নিয়ম
GITHUB-PUSH-GUIDE.md          ← এই ফাইল
.gitignore                    ← আবর্জনা/সিক্রেট বাদ দেওয়ার নিয়ম
.github/workflows/deploy-pages.yml   ← অটো-ডিপ্লয়
app/                          ← 🌐 আসল ওয়েবসাইট (index.html, css, js, manifest, server.py)
docs/guide/                   ← মাস্টার গাইড ও আইডিয়া
docs/design/                  ← ডিজাইন প্রিভিউ (ui-preview-v3.html)
```

---

## ✅ চেকলিস্ট (টিক দিয়ে এগোন)

- [ ] গিটহাব অ্যাকাউন্ট আছে
- [ ] রিপো তৈরি হয়েছে (Public)
- [ ] সব ফাইল আপলোড/পুশ হয়েছে (`app/`, `docs/`, `.github/` সহ)
- [ ] Settings → Pages → Source ঠিক করা হয়েছে
- [ ] লাইভ লিংক খুলে ৬টি ট্যাব দেখা গেছে: হোম · লাইব্রেরি · সাধনা · পরীক্ষা · সেবা · আমি
- [ ] পঞ্জিকায় বাংলা ভিউ ও গীতা দান কার্ড দেখা যাচ্ছে
- [ ] ফোনে "Add to Home screen" করা হয়েছে

---

<p align="center"><b>ॐ शान्तिः</b> · শুভ হোক আপনার সেবার পথ 🪔</p>
