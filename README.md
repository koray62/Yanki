# Yankı — Tanıtım Sitesi

Yankı medya takip ve itibar riski platformunun tanıtım (landing) sayfası. Derleme adımı olmayan, tek dosyalık statik bir sitedir.

## Dosyalar

| Dosya | Açıklama |
| --- | --- |
| `index.html` | Sitenin tamamı (HTML + CSS, harici bağımlılık yok; yazı tipleri Google Fonts'tan yüklenir) |
| `yanki-ornek-rapor.pdf` | "Örnek raporu indirin" butonlarının indirdiği örnek rapor (kurgusal veriler) |

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
- [ ] Footer'daki **[Şirket unvanı]** alanı doldurulmalı.
- [ ] **KVKK Aydınlatma Metni, Gizlilik, Çerez Politikası ve Kullanım Koşulları** sayfaları hazırlanıp footer bağlantıları güncellenmeli.
