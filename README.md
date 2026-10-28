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
| `404.html` | Bulunamayan sayfalar için hata sayfası |
| `robots.txt`, `sitemap.xml` | Arama motorları için tarama kuralları ve site haritası |
| `og-image.png` | Paylaşım önizleme görseli (1200×630) |
| `favicon.svg`, `favicon-32.png`, `apple-touch-icon.png` | Tarayıcı ve telefon simgeleri |
| `api/demo.js` | Demo formunu e-postaya ileten Vercel fonksiyonu |

## Yerelde açma

`index.html` dosyasını tarayıcıda açmanız yeterlidir. İsterseniz basit bir sunucu ile:

```bash
npx serve .
```

## Vercel'de yayınlama

1. Vercel'de **Add New → Project** ile bu depoyu içe aktarın.
2. Framework Preset: **Other**. Build Command ve Output Directory boş kalabilir.
3. **Deploy**'a basın. Site `main` dalına yapılan her gönderimde otomatik güncellenir.

## Demo talep formu (e-posta gönderimi)

Form, `api/demo.js` Vercel fonksiyonuna gönderilir; fonksiyon talebi Turkticaret.net SMTP hesabı üzerinden `info@noratech.com.tr` adresine e-postayla iletir. Yanıtla dediğinizde doğrudan talep sahibine yazılır.

Vercel'de **Project → Settings → Environment Variables** altına şu değişkenleri ekleyin, ardından **Deployments → Redeploy** yapın:

| Değişken | Örnek | Açıklama |
| --- | --- | --- |
| `SMTP_HOST` | Turkticaret panelindeki giden posta sunucusu | SMTP sunucu adresi |
| `SMTP_PORT` | `465` (SSL) veya `587` (STARTTLS) | Turkticaret'in önerdiği port |
| `SMTP_USER` | `info@noratech.com.tr` | Gönderen e-posta hesabı |
| `SMTP_PASS` | — | Bu hesabın şifresi |
| `MAIL_FROM` | `Yankı <info@noratech.com.tr>` | İsteğe bağlı; girilmezse gönderen adı "Yankı", adresi `SMTP_USER` olur |
| `DEMO_TO` | `info@noratech.com.tr` | İsteğe bağlı, talebin gideceği adres |

Sorun olursa Vercel'de **Deployments → (son yayın) → Functions → api/demo** loglarına bakın: `SMTP ayarları eksik` ya da `gönderim hatası` satırı nedeni gösterir.

## Alan adı değişirse

Site `https://www.yankitoday.com` adresine göre ayarlı. Alan adı değişirse bu adresi şu yerlerde güncelleyin: `index.html` ve yasal sayfalardaki `canonical`, `og:url`, `og:image` ve yapılandırılmış veri (JSON-LD), ayrıca `robots.txt` ve `sitemap.xml`.

## Arama motorlarına kayıt

1. [Google Search Console](https://search.google.com/search-console)'da siteyi ekleyin, alan adı doğrulamasını yapın ve `sitemap.xml` adresini gönderin.
2. [Bing Webmaster Tools](https://www.bing.com/webmasters)'ta aynı işlemi yapın; Search Console'dan içe aktarma seçeneği vardır.

## Yayın sonrası yapılacaklar

- [ ] **Abonelik Başlat** (Pro paketi) butonu uygulama yayına girene kadar geçici olarak demo formuna (`#demo`) gidiyor. Uygulama adresi netleşince `<uygulama adresi>/register?plan=pro` olarak güncellenmeli.
- [ ] Uygulamada KVKK metnindeki saklama süreleri otomatik silme olarak uygulanmalı: hesap verileri kapanıştan itibaren 12 ay, taranan içerik ve raporlar 6 ay, demo talepleri 6 ay, tercih çerezi en fazla 12 ay.
- [ ] Yasal metinler yayına almadan önce bir hukukçu tarafından gözden geçirilmeli.
- [ ] Sitede analitik veya pazarlama çerezi kullanılmaya başlanırsa çerez onay penceresi eklenmeli ve Çerez Politikası güncellenmeli.
