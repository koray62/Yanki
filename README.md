# Yankı — Tanıtım Sitesi

Yankı medya takip ve itibar riski platformunun tanıtım (landing) sayfası. Derleme adımı olmayan, tek dosyalık statik bir sitedir.

## Dosyalar

| Dosya | Açıklama |
| --- | --- |
| `index.html` | Sitenin tamamı (HTML + CSS, harici bağımlılık yok; yazı tipleri Google Fonts'tan yüklenir) |
| `yanki-ornek-rapor.pdf` | "Örnek raporu indirin" butonlarının indirdiği örnek rapor (kurgusal veriler) |
| `kvkk.html` | KVKK Aydınlatma Metni |
| `gizlilik.html` | Gizlilik Politikası |
| `cerez-politikasi.html` | Çerez Politikası |
| `kullanim-kosullari.html` | Kullanım Koşulları |

## Yerelde açma

`index.html` dosyasını tarayıcıda açmanız yeterlidir. İsterseniz basit bir sunucu ile:

```bash
npx serve .
```

## Vercel'de yayınlama

1. Vercel'de **Add New → Project** ile bu depoyu içe aktarın.
2. Framework Preset: **Other**. Build Command ve Output Directory boş kalabilir.
3. **Deploy**'a basın. Site `main` dalına yapılan her gönderimde otomatik güncellenir.

## Yayın sonrası yapılacaklar

- [ ] **Abonelik Başlat** (Pro paketi) butonu uygulama yayına girene kadar geçici olarak demo formuna (`#demo`) gidiyor. Uygulama adresi netleşince `<uygulama adresi>/register?plan=pro` olarak güncellenmeli.
- [ ] **Demo talep formu** henüz bir sunucuya bağlı değil. Bir form servisi (Formspree, Vercel fonksiyonu vb.) ya da uygulamanın API'si ile bağlanmalı.
- [ ] Yasal sayfalardaki kalan köşeli parantezli alanlar doldurulmalı: KVKK metnindeki veri saklama süreleri ve Çerez Politikası'ndaki tercih çerezi süresi.
- [ ] Yasal metinler yayına almadan önce bir hukukçu tarafından gözden geçirilmeli.
- [ ] Sitede analitik veya pazarlama çerezi kullanılmaya başlanırsa çerez onay penceresi eklenmeli ve Çerez Politikası güncellenmeli.
