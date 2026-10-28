# Yankı — Tanıtım Sitesi

Yankı medya takip ve itibar riski platformunun tanıtım (landing) sayfası. Derleme adımı olmayan, tek dosyalık statik bir sitedir.

## Dosyalar

Site iki dillidir: **İngilizce** ana adreste (`/`), **Türkçe** `/tr/` altında. Ziyaretçi menüdeki EN/TR düğmesiyle dili değiştirir; seçimi tarayıcıda hatırlanır.

| Dosya | Açıklama |
| --- | --- |
| `index.html` | İngilizce ana sayfa |
| `tr/index.html` | Türkçe ana sayfa |
| `privacy-notice.html`, `privacy.html`, `cookies.html`, `terms.html` | İngilizce yasal sayfalar |
| `tr/kvkk.html`, `tr/gizlilik.html`, `tr/cerez-politikasi.html`, `tr/kullanim-kosullari.html` | Türkçe yasal sayfalar |
| `tools/build_legal.py` | Yasal sayfaları iki dilde üreten betik |
| `vercel.json` | Eski Türkçe yasal sayfa adreslerinden `/tr/` altına kalıcı yönlendirmeler |
| `yanki-ornek-rapor.pdf`, `yanki-sample-report.pdf` | Türkçe ve İngilizce sayfalardaki "örnek rapor" butonlarının indirdiği raporlar (kurgusal veriler) |
| `404.html` | Bulunamayan sayfalar için hata sayfası |
| `robots.txt`, `sitemap.xml` | Arama motorları için tarama kuralları ve iki dilli site haritası |
| `og-image.png`, `og-image-en.png` | Türkçe ve İngilizce paylaşım önizleme görselleri (1200×630) |
| `favicon.svg`, `favicon-32.png`, `apple-touch-icon.png` | Tarayıcı ve telefon simgeleri |
| `api/demo.js` | Demo formunu e-postaya ileten Vercel fonksiyonu |

### İçerik güncellerken

- Ana sayfada yapılan bir metin değişikliği **iki dosyada** da yapılmalı: `index.html` (İngilizce) ve `tr/index.html` (Türkçe).
- Yasal metinler `tools/build_legal.py` içinde durur. Metni orada güncelleyip depo kökünde `python3 tools/build_legal.py .` çalıştırın; sekiz yasal sayfa yeniden üretilir.

## Yerelde açma

Sayfalar kök adresle (`/tr/`, `/favicon.svg` gibi) bağlantı verdiği için yerel bir sunucuyla açın:

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

Site `https://www.yankitoday.com` adresine göre ayarlı. Alan adı değişirse bu adresi şu yerlerde güncelleyin: `index.html`, `tr/index.html`, `tools/build_legal.py` (`BASE`), `robots.txt` ve `sitemap.xml`.

## Arama motorlarına kayıt

1. [Google Search Console](https://search.google.com/search-console)'da siteyi ekleyin, alan adı doğrulamasını yapın ve `sitemap.xml` adresini gönderin.
2. [Bing Webmaster Tools](https://www.bing.com/webmasters)'ta aynı işlemi yapın; Search Console'dan içe aktarma seçeneği vardır.

## Yayın sonrası yapılacaklar

- [ ] **Abonelik Başlat** (Pro paketi) butonu uygulama yayına girene kadar geçici olarak demo formuna (`#demo`) gidiyor. Uygulama adresi netleşince `<uygulama adresi>/register?plan=pro` olarak güncellenmeli.
- [ ] Uygulamada KVKK metnindeki saklama süreleri otomatik silme olarak uygulanmalı: hesap verileri kapanıştan itibaren 12 ay, taranan içerik ve raporlar 6 ay, demo talepleri 6 ay, tercih çerezi en fazla 12 ay.
- [ ] Yasal metinler yayına almadan önce bir hukukçu tarafından gözden geçirilmeli.
- [ ] Sitede analitik veya pazarlama çerezi kullanılmaya başlanırsa çerez onay penceresi eklenmeli ve Çerez Politikası güncellenmeli.
