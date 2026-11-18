/* সনাতন বিদ্যাপীঠ — অফলাইন service worker
   কৌশল: cache-first + background refresh. অ্যাপের সব ফাইল প্রথম দেখাতেই ক্যাশ হয়,
   তাই নেট না থাকলেও অ্যাপ পুরোপুরি চলে। */
const CACHE = 'sanatana-v5';

self.addEventListener('install', () => self.skipWaiting());

self.addEventListener('activate', event => {
  event.waitUntil((async () => {
    const keys = await caches.keys();
    await Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k)));
    await self.clients.claim();
  })());
});

self.addEventListener('fetch', event => {
  const req = event.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  if (url.origin !== self.location.origin) return;

  event.respondWith((async () => {
    const cache = await caches.open(CACHE);
    const hit = await cache.match(req);
    if (hit) {
      fetch(req).then(res => { if (res && res.ok) cache.put(req, res.clone()); }).catch(() => {});
      return hit;
    }
    try {
      const res = await fetch(req);
      if (res && res.ok) cache.put(req, res.clone());
      return res;
    } catch (e) {
      const shell = await cache.match('./index.html') || await cache.match('./');
      return shell || new Response('অফলাইন — ফাইলটি এখনো ক্যাশ হয়নি।', { status: 503, headers: { 'Content-Type': 'text/plain; charset=utf-8' } });
    }
  })());
});

/* রিমাইন্ডার: পেজ থেকে পোস্ট করা হলে নোটিফিকেশন দেখায় */
self.addEventListener('notificationclick', event => {
  event.notification.close();
  event.waitUntil(self.clients.matchAll({ type: 'window' }).then(list => {
    for (const c of list) { if ('focus' in c) return c.focus(); }
    return self.clients.openWindow('./index.html#/panjika');
  }));
});
