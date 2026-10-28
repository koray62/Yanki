"""Yankı yasal sayfalarını (İngilizce ve Türkçe) sitenin görsel diliyle üretir.

Kullanım (depo kökünden):  python3 tools/build_legal.py .
İngilizce sayfalar köke, Türkçe sayfalar tr/ klasörüne yazılır.
"""
import sys, os

OUT = sys.argv[1] if len(sys.argv) > 1 else "."
BASE = "https://www.yankitoday.com"
CO = "Nora Finansal Yazılımlar A.Ş."
ADDR = "Şehit İlknur Keleş Sk. No:2 Kozyatağı, İstanbul"
MERSIS = "06311925104000001"
MAIL = "info@noratech.com.tr"

# Aynı belgenin iki dildeki adresi (dil seçici ve hreflang için)
PAIRS = {
    "kvkk": ("/privacy-notice.html", "/tr/kvkk.html"),
    "privacy": ("/privacy.html", "/tr/gizlilik.html"),
    "cookies": ("/cookies.html", "/tr/cerez-politikasi.html"),
    "terms": ("/terms.html", "/tr/kullanim-kosullari.html"),
}

LANG = {
    "en": dict(
        html="en", locale="en_US", home="/", updated="Last updated: 28 October 2026",
        eyebrow="Legal", back="Back to home", tag="Hear what matters, not the noise.",
        rights="All rights reserved.", tabs_label="Legal documents", foot_label="Legal",
        switch_href_idx=1, switch_text="TR", switch_label="Türkçe", switch_lang="tr",
        og_image="/og-image-en.png",
        titles={"kvkk": "Privacy Notice (KVKK)", "privacy": "Privacy Policy", "cookies": "Cookie Policy", "terms": "Terms of Use"},
    ),
    "tr": dict(
        html="tr", locale="tr_TR", home="/tr/", updated="Son güncelleme: 28 Ekim 2026",
        eyebrow="Yasal", back="Ana sayfaya dön", tag="Gürültüyü değil, önemli olanı duyun.",
        rights="Tüm hakları saklıdır.", tabs_label="Yasal metinler", foot_label="Yasal",
        switch_href_idx=0, switch_text="EN", switch_label="English", switch_lang="en",
        og_image="/og-image.png",
        titles={"kvkk": "KVKK Aydınlatma Metni", "privacy": "Gizlilik Politikası", "cookies": "Çerez Politikası", "terms": "Kullanım Koşulları"},
    ),
}

ORDER = ["kvkk", "privacy", "cookies", "terms"]


def href(lang, key):
    return PAIRS[key][0 if lang == "en" else 1]


def page(lang, key, lead, body):
    L = LANG[lang]
    title = L["titles"][key]
    me = href(lang, key)
    other = PAIRS[key][L["switch_href_idx"]]
    tabs = "".join(
        f'<a href="{href(lang, k)}"{" aria-current=\"page\"" if k == key else ""}>{L["titles"][k]}</a>' for k in ORDER
    )
    foot = "".join(f'<a href="{href(lang, k)}">{L["titles"][k]}</a>' for k in ORDER)
    return f"""<!doctype html>
<html lang="{L['html']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — Yankı</title>
<meta name="description" content="{lead}">
<link rel="canonical" href="{BASE}{me}">
<link rel="alternate" hreflang="en" href="{BASE}{PAIRS[key][0]}">
<link rel="alternate" hreflang="tr" href="{BASE}{PAIRS[key][1]}">
<link rel="alternate" hreflang="x-default" href="{BASE}{PAIRS[key][0]}">
<meta name="robots" content="index, follow">
<meta name="theme-color" content="#0B1220">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta property="og:type" content="article">
<meta property="og:site_name" content="Yankı">
<meta property="og:locale" content="{L['locale']}">
<meta property="og:url" content="{BASE}{me}">
<meta property="og:title" content="{title} — Yankı">
<meta property="og:description" content="{lead}">
<meta property="og:image" content="{BASE}{L['og_image']}">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@500;600;700&amp;family=Inter:wght@400;500;600&amp;display=swap" rel="stylesheet">
<style>
:root{{--ink:#0B1220;--muted:#475569;--soft:#64748B;--line:#E2E6EC;--bg:#F7F8FA;--accent:#C2410C;--accent-dk:#9A3412;--tint:#FFF1E8}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--bg);color:var(--ink);font-family:Inter,system-ui,sans-serif;font-size:17px;line-height:1.65}}
a{{color:var(--accent)}}a:hover{{color:var(--accent-dk)}}
header{{background:rgba(247,248,250,.92);border-bottom:1px solid var(--line);position:sticky;top:0;backdrop-filter:blur(8px);z-index:5}}
.bar{{max-width:1200px;margin:0 auto;padding:14px 24px;display:flex;align-items:center;justify-content:space-between;gap:16px}}
.logo{{display:flex;align-items:center;gap:10px;text-decoration:none;color:var(--ink);min-width:0}}
.logo .name{{display:flex;flex-direction:column;line-height:1.15}}.logo .name b{{font-family:Sora,sans-serif;font-weight:700;font-size:22px}}.logo .name small{{font-size:12px;font-weight:500;color:var(--soft)}}
.acts{{display:flex;align-items:center;gap:8px;flex:none}}
.back,.lang{{display:inline-flex;align-items:center;gap:8px;flex:none;font-size:15px;font-weight:600;text-decoration:none;color:var(--ink);border:1px solid #CBD2DC;background:#fff;padding:10px 16px;border-radius:8px}}
.lang{{padding:10px 12px}}
.back:hover,.lang:hover{{color:var(--ink);border-color:#94A3B8}}
main{{max-width:820px;margin:0 auto;padding:64px 24px 96px}}
.eyebrow{{margin:0 0 12px;font-size:14px;font-weight:600;color:var(--accent);text-transform:uppercase;letter-spacing:.06em}}
h1{{margin:0;font-family:Sora,sans-serif;font-weight:700;font-size:clamp(32px,4.4vw,44px);line-height:1.12;letter-spacing:-.02em}}
.meta{{margin:14px 0 0;color:var(--soft);font-size:15px}}
.lead{{margin:28px 0 0;font-size:18px;color:var(--muted)}}
.tabs{{margin:36px 0 0;display:flex;flex-wrap:wrap;gap:8px}}
.tabs a{{font-size:14px;font-weight:600;text-decoration:none;color:#334155;background:#fff;border:1px solid var(--line);padding:8px 14px;border-radius:999px}}
.tabs a[aria-current]{{background:var(--ink);color:#fff;border-color:var(--ink)}}
article{{margin-top:40px;background:#fff;border:1px solid var(--line);border-radius:18px;padding:clamp(24px,4vw,48px)}}
h2{{margin:40px 0 12px;font-family:Sora,sans-serif;font-size:22px;font-weight:600;line-height:1.3}}
h2:first-child{{margin-top:0}}
h3{{margin:24px 0 8px;font-size:17px;font-weight:600}}
p{{margin:0 0 14px}}
ul,ol{{margin:0 0 14px;padding-left:22px}}li{{margin:0 0 6px}}
.box{{background:var(--tint);border:1px solid #FED7BF;border-radius:12px;padding:18px 20px;margin:0 0 18px}}
.box p:last-child{{margin:0}}
.note{{background:var(--bg);border:1px solid var(--line);border-radius:12px;padding:14px 18px;margin:0 0 24px;font-size:15px;color:var(--muted)}}
.tbl{{overflow-x:auto;margin:0 0 18px;border:1px solid var(--line);border-radius:12px}}
table{{border-collapse:collapse;width:100%;font-size:15px;min-width:560px}}
th,td{{text-align:left;vertical-align:top;padding:12px 14px;border-bottom:1px solid var(--line)}}
th{{background:var(--bg);font-weight:600}}tr:last-child td{{border-bottom:0}}
footer{{background:var(--ink);color:#B6C0CE;font-size:14px}}
.foot{{max-width:1200px;margin:0 auto;padding:40px 24px;display:flex;flex-wrap:wrap;justify-content:space-between;gap:24px}}
.foot nav{{display:flex;flex-wrap:wrap;gap:12px 24px}}.foot a{{color:#B6C0CE;text-decoration:none}}.foot a:hover{{color:#fff}}
@media (max-width:640px){{
.bar{{padding:10px 16px}}.logo .name b{{font-size:20px}}.logo .name small{{font-size:11.5px}}
.back{{width:44px;height:44px;padding:0;justify-content:center;border-radius:10px}}.back span{{display:none}}
.lang{{height:44px;border-radius:10px}}
main{{padding-top:40px}}
nav.tabs{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px}}
nav.tabs a{{display:flex;align-items:center;justify-content:center;text-align:center;min-height:48px;padding:8px 10px;border-radius:12px;font-size:14px;line-height:1.25}}
}}
@media (max-width:380px){{.logo .name small{{display:none}}}}
</style>
</head>
<body>
<header><div class="bar">
<a class="logo" href="{L['home']}"><svg width="30" height="30" viewBox="0 0 30 30" aria-hidden="true" fill="none" stroke="#C2410C" stroke-width="2.2" stroke-linecap="round"><circle cx="9" cy="15" r="3" fill="#C2410C" stroke="none"></circle><path d="M15 9a8.5 8.5 0 0 1 0 12"></path><path d="M20 5a14 14 0 0 1 0 20"></path></svg><span class="name"><b>Yankı</b><small>{L['tag']}</small></span></a>
<div class="acts">
<a class="lang" href="{other}" hreflang="{L['switch_lang']}" lang="{L['switch_lang']}" aria-label="{L['switch_label']}" data-lang="{L['switch_lang']}"><svg width="18" height="18" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"></circle><path d="M3 12h18"></path><path d="M12 3a14 14 0 0 1 0 18"></path><path d="M12 3a14 14 0 0 0 0 18"></path></svg>{L['switch_text']}</a>
<a class="back" href="{L['home']}" aria-label="{L['back']}"><svg width="20" height="20" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 11l9-7 9 7"></path><path d="M5 10v10h14V10"></path></svg><span>{L['back']}</span></a>
</div>
</div></header>
<main>
<p class="eyebrow">{L['eyebrow']}</p>
<h1>{title}</h1>
<p class="meta">{L['updated']}</p>
<p class="lead">{lead}</p>
<nav class="tabs" aria-label="{L['tabs_label']}">{tabs}</nav>
<article>
{body}
</article>
</main>
<footer><div class="foot">
<span>© 2026 {CO}. {L['rights']}</span>
<nav aria-label="{L['foot_label']}">{foot}</nav>
</div></footer>
<script>
document.querySelectorAll('[data-lang]').forEach(function (a) {{
  a.addEventListener('click', function () {{ try {{ localStorage.setItem('yanki-lang', a.getAttribute('data-lang')); }} catch (e) {{}} }});
}});
</script>
</body>
</html>
"""


# ---------------------------------------------------------------- Türkçe

CONTROLLER = f"""<div class="box">
<p><strong>Veri sorumlusu:</strong> {CO}<br>
<strong>Adres:</strong> {ADDR}<br>
<strong>MERSİS:</strong> {MERSIS}<br>
<strong>E-posta:</strong> <a href="mailto:{MAIL}">{MAIL}</a></p>
</div>"""

KVKK = f"""
<h2>1. Veri sorumlusu</h2>
<p>6698 sayılı Kişisel Verilerin Korunması Kanunu (“KVKK”) uyarınca kişisel verileriniz, veri sorumlusu sıfatıyla aşağıda bilgileri yer alan şirketimiz tarafından işlenmektedir.</p>
{CONTROLLER}

<h2>2. İşlenen kişisel veriler ve kaynakları</h2>
<div class="tbl"><table>
<thead><tr><th>Veri kategorisi</th><th>Örnekler</th><th>Nasıl toplanır</th></tr></thead>
<tbody>
<tr><td>Kimlik</td><td>Ad, soyad</td><td>Demo talep formu, hesap oluşturma</td></tr>
<tr><td>İletişim</td><td>E-posta adresi, telefon numarası (isteğe bağlı)</td><td>Demo talep formu, hesap ve rapor alıcısı ayarları</td></tr>
<tr><td>Müşteri işlem</td><td>Kurum adı, takip edilmek istenen marka veya kişi, paket, abonelik ve fatura bilgileri, destek yazışmaları</td><td>Form, hesap paneli, e-posta</td></tr>
<tr><td>İşlem güvenliği</td><td>Kullanıcı adı, şifre özeti (şifrenin kendisi saklanmaz), şifrelenmiş AI API anahtarları, IP adresi, oturum ve erişim kayıtları</td><td>Hesap kullanımı sırasında otomatik olarak</td></tr>
<tr><td>Hizmet içeriği</td><td>Takip profilleri, anahtar kelimeler, gündem brifleri, üretilen raporlar</td><td>Hesap paneli</td></tr>
<tr><td>Kamuya açık yayın içeriği</td><td>Taranan haber ve yayınlarda yer alabilen kişilere ait adlar ve bilgiler</td><td>Müşterinin tanımladığı konular için kamuya açık kaynakların taranması</td></tr>
</tbody></table></div>
<p>Kişisel verileriniz, yukarıdaki kanallar aracılığıyla elektronik ortamda ve kısmen otomatik yollarla toplanır.</p>

<h2>3. İşleme amaçları ve hukuki sebepler</h2>
<div class="tbl"><table>
<thead><tr><th>Amaç</th><th>Hukuki sebep (KVKK m. 5/2)</th></tr></thead>
<tbody>
<tr><td>Demo talebinizi değerlendirmek ve sizinle iletişime geçmek</td><td>Sözleşmenin kurulmasıyla doğrudan ilgili olması (c)</td></tr>
<tr><td>Hesabınızı oluşturmak, hizmeti sunmak, takip ve raporlama işlemlerini yürütmek, raporları e-postayla iletmek</td><td>Sözleşmenin ifası (c)</td></tr>
<tr><td>Abonelik, faturalandırma ve muhasebe işlemleri</td><td>Kanunlarda açıkça öngörülmesi ve hukuki yükümlülük (a, ç)</td></tr>
<tr><td>Bilgi güvenliğini sağlamak, kötüye kullanımı önlemek, erişim kayıtlarını tutmak</td><td>Hukuki yükümlülük (ç) ve meşru menfaat (f)</td></tr>
<tr><td>Hizmeti geliştirmek, destek taleplerini yanıtlamak</td><td>Meşru menfaat (f)</td></tr>
<tr><td>Uyuşmazlık hâlinde hakların tesisi, kullanılması veya korunması</td><td>Bir hakkın tesisi, kullanılması veya korunması (e)</td></tr>
</tbody></table></div>
<p>Ticari elektronik ileti (kampanya, bülten vb.) gönderimi yalnızca 6563 sayılı Kanun uyarınca ayrıca onay vermeniz hâlinde yapılır. Bu onayı dilediğiniz zaman geri alabilirsiniz.</p>

<h2>4. Kamuya açık yayınlarda yer alan kişiler</h2>
<p>Yankı, müşterilerin tanımladığı marka, kişi ve konular için yalnızca kamuya açık yayımlanmış içerikleri tarar. Bu içeriklerde adı geçen kişilere ait veriler, müşterinin takip talimatı doğrultusunda ve yalnızca medya takibi ve raporlama amacıyla işlenir. Takip edilecek kişi ve konuları belirleyen müşteri, bu verilere ilişkin olarak kendi veri sorumluluğu yükümlülüklerinden sorumludur; şirketimiz bu kapsamda müşteri adına veri işleyen sıfatıyla hareket eder.</p>

<h2>5. Kişisel verilerin aktarılması</h2>
<p>Kişisel verileriniz, yukarıdaki amaçlarla sınırlı olarak ve KVKK m. 8 ve m. 9'a uygun şekilde aşağıdaki alıcı gruplarına aktarılabilir:</p>
<ul>
<li><strong>Barındırma ve altyapı hizmeti sağlayıcıları:</strong> Tanıtım sitesi Vercel Inc. (ABD) altyapısında yayınlanmaktadır; siteyi ziyaret ettiğinizde IP adresi gibi teknik bağlantı verileri bu sağlayıcı tarafından işlenir. Sitede kullanılan yazı tipleri Google Fonts (Google LLC, ABD) üzerinden yüklenir.</li>
<li><strong>E-posta gönderim hizmeti sağlayıcısı:</strong> Raporların ve bildirimlerin iletilmesi için Turkticaret.net.</li>
<li><strong>Ödeme hizmeti sağlayıcısı:</strong> Abonelik ödemeleri için iyzico (İyzi Ödeme ve Elektronik Para Hizmetleri A.Ş.). Kart bilgileriniz şirketimiz tarafından saklanmaz.</li>
<li><strong>Yetkili kamu kurum ve kuruluşları:</strong> Hukuki yükümlülüklerin yerine getirilmesi kapsamında.</li>
</ul>
<h3>Kendi AI anahtarınızla (BYOK) yapılan analizler</h3>
<p>Haber analizleri, hesabınıza tanımladığınız yapay zekâ sağlayıcısında (ör. Anthropic, OpenAI, Google) <strong>sizin kendi API anahtarınız ve hesabınız</strong> üzerinden yapılır. Bu analiz için gönderilen içerik, sizin söz konusu sağlayıcıyla aranızdaki sözleşme ve o sağlayıcının veri politikaları kapsamında işlenir. Hangi sağlayıcının kullanılacağına siz karar verirsiniz.</p>
<p>Yurt dışına yapılan aktarımlarda KVKK m. 9 ve Kişisel Verilerin Yurt Dışına Aktarılmasına İlişkin Usul ve Esaslar Hakkında Yönetmelik kapsamındaki uygun güvencelere (ör. Kurul tarafından ilan edilen standart sözleşmeler) dayanılır.</p>

<h2>6. Saklama süresi</h2>
<p>Kişisel verileriniz işleme amacının gerektirdiği süre boyunca ve ilgili mevzuatta öngörülen süreler kadar saklanır; süre sona erdiğinde silinir, yok edilir veya anonim hâle getirilir. Bu kapsamda:</p>
<ul>
<li>Hesap ve hizmet verileri, abonelik süresince ve aboneliğin sona ermesinden veya hesabın kapatılmasından itibaren 12 ay boyunca,</li>
<li>Taranan yayın içerikleri ve üretilen raporlar, oluşturulmalarından itibaren 6 ay boyunca,</li>
<li>Fatura ve muhasebe kayıtları, Vergi Usul Kanunu ve Türk Ticaret Kanunu uyarınca 10 yıl boyunca,</li>
<li>Sonuçlanmayan demo talepleri, talep tarihinden itibaren 6 ay boyunca</li>
</ul>
<p>saklanır.</p>

<h2>7. KVKK m. 11 kapsamındaki haklarınız</h2>
<p>Şirketimize başvurarak kişisel verilerinizle ilgili olarak:</p>
<ol type="a">
<li>İşlenip işlenmediğini öğrenme,</li>
<li>İşlenmişse buna ilişkin bilgi talep etme,</li>
<li>İşlenme amacını ve bunların amacına uygun kullanılıp kullanılmadığını öğrenme,</li>
<li>Yurt içinde veya yurt dışında aktarıldığı üçüncü kişileri bilme,</li>
<li>Eksik veya yanlış işlenmiş olması hâlinde düzeltilmesini isteme,</li>
<li>KVKK m. 7'de öngörülen şartlar çerçevesinde silinmesini veya yok edilmesini isteme,</li>
<li>(e) ve (f) bentleri uyarınca yapılan işlemlerin, verilerin aktarıldığı üçüncü kişilere bildirilmesini isteme,</li>
<li>İşlenen verilerin münhasıran otomatik sistemler vasıtasıyla analiz edilmesi suretiyle aleyhinize bir sonucun ortaya çıkmasına itiraz etme,</li>
<li>Kanuna aykırı olarak işlenmesi sebebiyle zarara uğramanız hâlinde zararın giderilmesini talep etme</li>
</ol>
<p>haklarına sahipsiniz.</p>

<h2>8. Başvuru yöntemi</h2>
<p>Haklarınıza ilişkin taleplerinizi, Veri Sorumlusuna Başvuru Usul ve Esasları Hakkında Tebliğ'e uygun olarak; kimliğinizi tespit edici bilgilerle birlikte yazılı olarak yukarıdaki adrese, kayıtlı elektronik posta (KEP) yoluyla, güvenli elektronik imza veya mobil imza ile ya da şirketimizde kayıtlı e-posta adresinizden <a href="mailto:{MAIL}">{MAIL}</a> adresine iletebilirsiniz.</p>
<p>Başvurunuz, talebin niteliğine göre en kısa sürede ve en geç 30 gün içinde ücretsiz olarak sonuçlandırılır. İşlemin ayrıca bir maliyet gerektirmesi hâlinde Kurul tarafından belirlenen tarifedeki ücret alınabilir.</p>
"""

PRIVACY = f"""
<h2>1. Kapsam</h2>
<p>Bu politika, Yankı tanıtım sitesini ve Yankı medya takip platformunu (“Hizmet”) kullanırken bilgilerinizin nasıl toplandığını, kullanıldığını ve korunduğunu açıklar. Kişisel verilerinizin işlenmesine ilişkin yasal bilgilendirme için <a href="kvkk.html">KVKK Aydınlatma Metni</a>'ni inceleyiniz.</p>

<h2>2. Topladığımız bilgiler</h2>
<ul>
<li><strong>Bize verdiğiniz bilgiler:</strong> Demo talep formunda ve hesap oluştururken paylaştığınız ad, kurum, e-posta, telefon ve takip etmek istediğiniz marka veya kişi bilgileri.</li>
<li><strong>Hizmeti kullanırken oluşan bilgiler:</strong> Takip profilleriniz, anahtar kelimeleriniz, gündem brifleriniz, tarama sıklığınız, rapor alıcılarınız ve üretilen raporlar.</li>
<li><strong>AI API anahtarlarınız:</strong> Analiz için tanımladığınız anahtarlar.</li>
<li><strong>Teknik bilgiler:</strong> IP adresi, tarayıcı türü, erişim zamanı ve hata kayıtları.</li>
</ul>

<h2>3. Bilgileri nasıl kullanırız</h2>
<ul>
<li>Hizmeti sunmak: taramaları yapmak, analizleri çalıştırmak, raporları hazırlamak ve e-postayla göndermek,</li>
<li>Demo ve destek taleplerinize yanıt vermek,</li>
<li>Abonelik ve faturalandırma işlemlerini yürütmek,</li>
<li>Hizmetin güvenliğini sağlamak ve kötüye kullanımı önlemek,</li>
<li>Hizmeti iyileştirmek.</li>
</ul>
<p>Bilgilerinizi <strong>satmayız</strong> ve reklam amacıyla üçüncü kişilerle paylaşmayız.</p>

<h2>4. AI API anahtarlarınız ve yapay zekâ analizi</h2>
<p>Yankı “kendi anahtarını getir” (BYOK) modeliyle çalışır:</p>
<ul>
<li>API anahtarlarınız veritabanında şifrelenmiş olarak saklanır ve arayüzde hiçbir zaman açık hâliyle gösterilmez.</li>
<li>Anahtarlarınız yalnızca sizin adınıza analiz yapmak için, seçtiğiniz sağlayıcıya yapılan isteklerde kullanılır.</li>
<li>Analiz için sağlayıcıya haber metinleri ve özetleme talimatları gönderilir. Bu içerik, sizin sağlayıcıyla aranızdaki sözleşme ve sağlayıcının veri politikaları kapsamında işlenir.</li>
<li>Anahtarınızı dilediğiniz an panelden silebilir veya sağlayıcınızın panelinden iptal edebilirsiniz.</li>
</ul>

<h2>5. Taranan içerikler</h2>
<p>Yankı yalnızca herkese açık yayımlanmış içerikleri tarar. Bazı yayınların tam metnine erişim, ilgili kaynağa bireysel veya kurumsal abonelik gerektirebilir; Yankı bu tür içeriklerde ödeme duvarını aşmaz. Raporlarda haberin kısa bir özeti ve orijinal kaynağın bağlantısı yer alır.</p>

<h2>6. Paylaşım</h2>
<p>Bilgileriniz yalnızca Hizmetin sunulması için gerekli olan hizmet sağlayıcılarla (barındırma, e-posta gönderimi, ödeme) ve yasal zorunluluk hâlinde yetkili kurumlarla paylaşılır. Ayrıntılar <a href="kvkk.html">KVKK Aydınlatma Metni</a>'nde yer alır.</p>

<h2>7. Güvenlik</h2>
<ul>
<li>Site ve uygulama trafiği HTTPS ile şifrelenir.</li>
<li>Şifreler geri döndürülemez biçimde özetlenerek saklanır; API anahtarları şifrelenir.</li>
<li>Her müşterinin verileri diğer hesaplardan ayrı tutulur.</li>
<li>Erişim yalnızca yetkili kişilerle sınırlıdır.</li>
</ul>
<p>Hiçbir sistem tamamen risksiz değildir. Bir güvenlik ihlali fark etmemiz hâlinde mevzuatın öngördüğü bildirimleri yaparız.</p>

<h2>8. Saklama ve silme</h2>
<p>Bilgileriniz hesabınız açık olduğu sürece ve yasal saklama süreleri boyunca tutulur. Hesabınızı kapattığınızda verileriniz, yasal yükümlülükler saklı kalmak üzere silinir veya anonim hâle getirilir. Süreler <a href="kvkk.html">KVKK Aydınlatma Metni</a>'nde belirtilmiştir.</p>

<h2>9. Çocuklar</h2>
<p>Hizmet 18 yaşından küçükler için tasarlanmamıştır ve bu kişilerden bilerek bilgi toplanmaz.</p>

<h2>10. Değişiklikler ve iletişim</h2>
<p>Bu politikayı güncelleyebiliriz; önemli değişiklikleri sitede ve gerekirse e-postayla duyururuz. Sorularınız için <a href="mailto:{MAIL}">{MAIL}</a> adresine yazabilirsiniz.</p>
"""

COOKIES = f"""
<h2>1. Çerez nedir?</h2>
<p>Çerezler, bir web sitesini ziyaret ettiğinizde tarayıcınıza kaydedilen küçük metin dosyalarıdır. Benzer amaçla tarayıcının yerel depolama alanı da kullanılabilir; bu politikada her ikisi “çerez” olarak anılır.</p>

<h2>2. Tanıtım sitesinde kullandığımız çerezler</h2>
<div class="box"><p>Yankı tanıtım sitesi şu anda <strong>reklam, pazarlama veya analitik çerezi kullanmamaktadır</strong> ve ziyaretçileri izlemez. Bu nedenle sitede çerez onay penceresi gösterilmemektedir.</p></div>
<p>Siteyi görüntülediğinizde, sayfaların ve yazı tiplerinin size iletilebilmesi için barındırma sağlayıcımız (Vercel) ve yazı tipi hizmeti (Google Fonts) IP adresiniz gibi teknik bağlantı bilgilerini işler. Bu işlem sitenin çalışması için gereklidir.</p>
<p>Sitenin dilini değiştirirseniz, bir sonraki ziyaretinizde aynı dili görmeniz için tercihiniz tarayıcınızın yerel depolama alanında saklanır. Bu işlevsel bir tercihtir, bize gönderilmez ve tarayıcı ayarlarınızdan silinebilir.</p>

<h2>3. Uygulamada kullandığımız çerezler</h2>
<p>Yankı paneline giriş yaptığınızda yalnızca hizmetin çalışması için zorunlu olan çerezler kullanılır:</p>
<div class="tbl"><table>
<thead><tr><th>Tür</th><th>Amacı</th><th>Süresi</th></tr></thead>
<tbody>
<tr><td>Oturum / kimlik doğrulama</td><td>Giriş yaptığınızı hatırlamak ve hesabınızı korumak</td><td>Oturum süresince veya çıkış yapana kadar</td></tr>
<tr><td>Güvenlik</td><td>Yetkisiz erişimi ve sahte istekleri önlemek</td><td>Oturum süresince</td></tr>
<tr><td>Tercih</td><td>Arayüz dili gibi tercihlerinizi hatırlamak</td><td>12 ay</td></tr>
</tbody></table></div>
<p>Zorunlu çerezler, hizmetin sunulması için gerekli olduğundan açık rızanıza dayanmaz.</p>

<h2>4. İleride kullanılabilecek çerezler</h2>
<p>Analitik veya pazarlama amaçlı çerez kullanmaya başlarsak, bu politikayı güncelleyecek ve bu çerezleri yalnızca açık rızanızı aldıktan sonra etkinleştireceğiz. Rızanızı dilediğiniz zaman geri alabileceksiniz.</p>

<h2>5. Çerezleri nasıl yönetebilirsiniz?</h2>
<p>Tarayıcınızın ayarlarından çerezleri silebilir veya engelleyebilirsiniz. Zorunlu çerezleri engellemeniz hâlinde Yankı paneline giriş yapamayabilirsiniz.</p>

<h2>6. İletişim</h2>
<p>Çerezlerle ilgili sorularınız için <a href="mailto:{MAIL}">{MAIL}</a> adresine yazabilirsiniz. Kişisel verilerinize ilişkin haklarınız için <a href="kvkk.html">KVKK Aydınlatma Metni</a>'ni inceleyiniz.</p>
"""

TERMS = f"""
<h2>1. Taraflar ve kapsam</h2>
<p>Bu Kullanım Koşulları, {CO} (“Şirket”) tarafından sunulan Yankı medya takip platformunun (“Hizmet”) kullanımını düzenler. Hesap oluşturarak veya Hizmeti kullanarak bu koşulları kabul etmiş olursunuz. Hizmeti bir kurum adına kullanıyorsanız, o kurumu bu koşullarla bağlama yetkiniz olduğunu beyan edersiniz.</p>

<h2>2. Hizmetin tanımı</h2>
<p>Yankı; kullanıcının tanımladığı marka, kişi, rakip ve konular için kamuya açık yayınları belirlenen sıklıkta tarar, içerikleri yapay zekâ yardımıyla özetler ve sınıflandırır, sonuçları PDF rapor olarak e-postayla iletir. Hizmetin kapsamı seçilen pakete göre değişir.</p>

<h2>3. Hesap</h2>
<ul>
<li>Hesap oluştururken doğru ve güncel bilgi vermeniz gerekir.</li>
<li>Şifrenizin ve hesabınızın güvenliğinden siz sorumlusunuz. Yetkisiz bir kullanım fark ederseniz bize hemen bildirin.</li>
<li>Hizmet 18 yaşını doldurmuş kişiler içindir.</li>
</ul>

<h2>4. Kendi AI anahtarınız (BYOK)</h2>
<ul>
<li>Analizler, tanımladığınız yapay zekâ sağlayıcısında sizin API anahtarınızla yapılır.</li>
<li>Sağlayıcının kullanım ücretleri doğrudan size aittir ve Yankı abonelik ücretine dahil değildir.</li>
<li>Seçtiğiniz sağlayıcının kullanım koşullarına ve politikalarına uymaktan siz sorumlusunuz.</li>
<li>Sağlayıcıdan kaynaklanan kesinti, limit veya ücret değişikliklerinden Şirket sorumlu değildir.</li>
</ul>

<h2>5. Paketler, ücretler ve deneme süresi</h2>
<ul>
<li>Güncel paketler ve ücretler sitede yayımlanır. Ücretlere KDV dahil değildir.</li>
<li>Başlangıç ve Pro paketleri 15 gün ücretsiz denenebilir. Deneme süresi sonunda abonelik, iptal etmediğiniz sürece seçtiğiniz pakette ücretli olarak devam eder.</li>
<li>Abonelikler aylık olarak yenilenir. Aboneliğinizi dilediğiniz zaman iptal edebilirsiniz; iptal, içinde bulunulan dönemin sonunda geçerli olur.</li>
<li>Mevzuattan doğan haklarınız saklı kalmak üzere, kullanılmış dönemler için ücret iadesi yapılmaz.</li>
<li>Kurumsal paket koşulları ayrıca yapılan sözleşmeyle belirlenir.</li>
<li>Şirket ücretleri değiştirebilir; değişiklik, en az 30 gün önceden bildirilir ve bir sonraki dönemden itibaren uygulanır.</li>
</ul>

<h2>6. Kabul edilebilir kullanım</h2>
<p>Hizmeti aşağıdaki amaçlarla kullanamazsınız:</p>
<ul>
<li>Kamuya mal olmamış özel kişileri izlemek, fişlemek, takip etmek veya taciz etmek,</li>
<li>Kişisel verileri hukuka aykırı biçimde işlemek veya ayrımcılık amacıyla kullanmak,</li>
<li>Hukuka aykırı herhangi bir faaliyette bulunmak,</li>
<li>Hizmeti veya rapor içeriklerini izinsiz olarak üçüncü kişilere yeniden satmak,</li>
<li>Hizmetin güvenliğini aşmaya çalışmak, tersine mühendislik yapmak veya sistemlere aşırı yük bindirmek.</li>
</ul>
<p>Takip edilecek kişi ve konuları siz belirlersiniz ve bu tercihlerin hukuka uygunluğundan siz sorumlusunuz. Bu maddenin ihlali hâlinde Şirket hesabı askıya alabilir veya kapatabilir.</p>

<h2>7. İçerik ve fikri mülkiyet</h2>
<ul>
<li>Taranan haber ve yayınların hakları ilgili yayıncılara aittir. Raporlar, bu içeriklerin kısa özetlerini ve orijinal kaynak bağlantılarını içerir.</li>
<li>Bazı yayınların tam metnine erişim, ilgili kaynağa bireysel veya kurumsal abonelik gerektirebilir.</li>
<li>Yankı yazılımı, markası ve tasarımı Şirkete aittir. Size yalnızca abonelik süresince Hizmeti kullanma hakkı tanınır.</li>
<li>Takip profilleriniz ve size ait raporlar sizindir. Bunları kendi iç kullanımınız için dilediğiniz gibi kullanabilirsiniz.</li>
</ul>

<h2>8. Yapay zekâ çıktıları</h2>
<p>Özetler, duygu etiketleri, PR Riski ve rekabet değerlendirmeleri yapay zekâ tarafından otomatik olarak üretilir ve hatalı veya eksik olabilir. Bu çıktılar karar desteği amaçlıdır; önemli kararlar vermeden önce orijinal kaynağı incelemeniz gerekir. Hizmet hukuki, finansal veya yatırım danışmanlığı değildir.</p>

<h2>9. Hizmetin sürekliliği</h2>
<p>Hizmeti kesintisiz sunmak için makul çabayı gösteririz; ancak bakım, altyapı arızaları, üçüncü taraf kaynaklarda veya sağlayıcılarda yaşanan sorunlar nedeniyle kesinti olabilir. Kaynak sitelerin yapısındaki değişiklikler bazı kanalların geçici olarak taranamamasına yol açabilir. Kurumsal paket dışında belirli bir erişilebilirlik oranı taahhüt edilmez.</p>

<h2>10. Sorumluluğun sınırlandırılması</h2>
<p>Kanunun izin verdiği ölçüde Şirketin, Hizmetle ilgili toplam sorumluluğu, talebe konu olaydan önceki 12 ay içinde ödediğiniz abonelik ücretleriyle sınırlıdır. Şirket; kâr kaybı, itibar kaybı veya dolaylı zararlardan ve yapay zekâ çıktılarına dayanılarak alınan kararlardan sorumlu tutulamaz. Bu sınırlama, kasıt ve ağır kusur hâllerinde ve tüketicilerin kanundan doğan haklarında uygulanmaz.</p>

<h2>11. Fesih</h2>
<p>Aboneliğinizi dilediğiniz zaman sonlandırabilirsiniz. Şirket, bu koşulların ihlali hâlinde hesabınızı askıya alabilir veya kapatabilir. Hesap kapandığında verileriniz <a href="kvkk.html">KVKK Aydınlatma Metni</a>'ndeki sürelere göre silinir.</p>

<h2>12. Tüketiciler</h2>
<p>Hizmeti tüketici sıfatıyla kullanıyorsanız, 6502 sayılı Tüketicinin Korunması Hakkında Kanun ve Mesafeli Sözleşmeler Yönetmeliği'nden doğan haklarınız saklıdır. Elektronik ortamda anında ifa edilen hizmetlerde cayma hakkı, mevzuattaki istisnalar çerçevesinde uygulanır.</p>

<h2>13. Değişiklikler</h2>
<p>Bu koşulları güncelleyebiliriz. Önemli değişiklikleri yürürlüğe girmeden önce e-postayla veya panel üzerinden duyururuz. Değişiklikten sonra Hizmeti kullanmaya devam etmeniz, güncel koşulları kabul ettiğiniz anlamına gelir.</p>

<h2>14. Uygulanacak hukuk ve yetki</h2>
<p>Bu koşullar Türkiye Cumhuriyeti hukukuna tabidir. Uyuşmazlıklarda İstanbul (Çağlayan) Mahkemeleri ve İcra Daireleri yetkilidir. Tüketiciler için, yasal parasal sınırlar dahilinde Tüketici Hakem Heyetleri ve Tüketici Mahkemeleri yetkilidir.</p>

<h2>15. İletişim</h2>
<p>{CO} · {ADDR} · <a href="mailto:{MAIL}">{MAIL}</a></p>
"""


# ---------------------------------------------------------------- English

EN_NOTE = """<div class="note"><p>This English version is provided for convenience. In case of any discrepancy, the <a href="{tr}" hreflang="tr" lang="tr">Turkish version</a> prevails.</p></div>"""

EN_CONTROLLER = f"""<div class="box">
<p><strong>Data controller:</strong> {CO}<br>
<strong>Address:</strong> {ADDR}, Türkiye<br>
<strong>Central Registration System (MERSİS) No:</strong> {MERSIS}<br>
<strong>Email:</strong> <a href="mailto:{MAIL}">{MAIL}</a></p>
</div>"""

EN_KVKK = f"""
{EN_NOTE.format(tr=PAIRS['kvkk'][1])}
<h2>1. Data controller</h2>
<p>Under the Turkish Personal Data Protection Law No. 6698 (“KVKK”), your personal data is processed by our company, acting as data controller, whose details are given below.</p>
{EN_CONTROLLER}

<h2>2. Personal data we process and its sources</h2>
<div class="tbl"><table>
<thead><tr><th>Data category</th><th>Examples</th><th>How it is collected</th></tr></thead>
<tbody>
<tr><td>Identity</td><td>First and last name</td><td>Demo request form, account sign-up</td></tr>
<tr><td>Contact</td><td>Email address, phone number (optional)</td><td>Demo request form, account and report recipient settings</td></tr>
<tr><td>Customer transaction</td><td>Organisation name, brand or person to be monitored, plan, subscription and billing details, support correspondence</td><td>Form, account dashboard, email</td></tr>
<tr><td>Transaction security</td><td>Username, password hash (the password itself is never stored), encrypted AI API keys, IP address, session and access logs</td><td>Automatically, while you use your account</td></tr>
<tr><td>Service content</td><td>Monitoring profiles, keywords, agenda briefs, generated reports</td><td>Account dashboard</td></tr>
<tr><td>Publicly available publications</td><td>Names and information of people who may appear in the news and publications scanned</td><td>Scanning public sources for the topics defined by the customer</td></tr>
</tbody></table></div>
<p>Your personal data is collected electronically through the channels above, partly by automated means.</p>

<h2>3. Purposes and legal grounds</h2>
<div class="tbl"><table>
<thead><tr><th>Purpose</th><th>Legal ground (KVKK Art. 5/2)</th></tr></thead>
<tbody>
<tr><td>Assessing your demo request and contacting you</td><td>Directly related to the conclusion of a contract (c)</td></tr>
<tr><td>Creating your account, providing the service, running monitoring and reporting, emailing reports</td><td>Performance of a contract (c)</td></tr>
<tr><td>Subscription, billing and accounting</td><td>Expressly provided by law and legal obligation (a, ç)</td></tr>
<tr><td>Ensuring information security, preventing misuse, keeping access logs</td><td>Legal obligation (ç) and legitimate interest (f)</td></tr>
<tr><td>Improving the service, answering support requests</td><td>Legitimate interest (f)</td></tr>
<tr><td>Establishing, exercising or defending a right in case of a dispute</td><td>Establishment, exercise or protection of a right (e)</td></tr>
</tbody></table></div>
<p>Commercial electronic messages (campaigns, newsletters, etc.) are sent only if you give separate consent under Law No. 6563. You can withdraw this consent at any time.</p>

<h2>4. People mentioned in public publications</h2>
<p>Yankı only scans content that has been published publicly, for the brands, people and topics defined by customers. Data relating to people named in this content is processed on the customer's instruction and solely for media monitoring and reporting. The customer who decides which people and topics are monitored is responsible for its own data controller obligations for this data; for this processing our company acts as a data processor on the customer's behalf.</p>

<h2>5. Transfers of personal data</h2>
<p>Your personal data may be transferred, limited to the purposes above and in line with KVKK Articles 8 and 9, to the following recipient groups:</p>
<ul>
<li><strong>Hosting and infrastructure providers:</strong> The website is hosted on Vercel Inc. (USA) infrastructure; when you visit it, technical connection data such as your IP address is processed by this provider. The fonts used on the site are loaded from Google Fonts (Google LLC, USA).</li>
<li><strong>Email delivery provider:</strong> Turkticaret.net, for delivering reports and notifications.</li>
<li><strong>Payment service provider:</strong> iyzico (İyzi Ödeme ve Elektronik Para Hizmetleri A.Ş.), for subscription payments. Your card details are not stored by our company.</li>
<li><strong>Authorised public authorities:</strong> Where required to comply with legal obligations.</li>
</ul>
<h3>Analyses run with your own AI key (BYOK)</h3>
<p>News analysis is performed by the AI provider you configure on your account (e.g. Anthropic, OpenAI, Google) <strong>using your own API key and account</strong>. Content sent for this analysis is processed under your contract with that provider and its data policies. You decide which provider is used.</p>
<p>Transfers abroad rely on the appropriate safeguards set out in KVKK Article 9 and the Regulation on the Procedures and Principles for the Transfer of Personal Data Abroad (e.g. standard contracts published by the Personal Data Protection Board).</p>

<h2>6. Retention</h2>
<p>Your personal data is kept for as long as the processing purpose requires and for the periods set by law; once this period ends it is erased, destroyed or anonymised. In particular:</p>
<ul>
<li>Account and service data: during the subscription and for 12 months after the subscription ends or the account is closed,</li>
<li>Scanned publication content and generated reports: for 6 months from their creation,</li>
<li>Invoices and accounting records: for 10 years under the Tax Procedure Law and the Turkish Commercial Code,</li>
<li>Demo requests that do not lead to a contract: for 6 months from the request date.</li>
</ul>

<h2>7. Your rights under KVKK Article 11</h2>
<p>By applying to our company, you have the right to:</p>
<ol type="a">
<li>Learn whether your personal data is processed,</li>
<li>Request information if it has been processed,</li>
<li>Learn the purpose of processing and whether it is used in line with that purpose,</li>
<li>Know the third parties in Türkiye or abroad to whom it is transferred,</li>
<li>Request correction if it is incomplete or inaccurate,</li>
<li>Request erasure or destruction under the conditions in KVKK Article 7,</li>
<li>Request that third parties to whom data was transferred be notified of actions taken under (e) and (f),</li>
<li>Object to a result against you arising exclusively from analysis by automated systems,</li>
<li>Claim compensation for damages caused by unlawful processing.</li>
</ol>

<h2>8. How to apply</h2>
<p>You can submit requests regarding your rights, in line with the Communiqué on the Procedures and Principles of Application to the Data Controller, in writing to the address above together with information that identifies you, via registered electronic mail (KEP), with a secure electronic or mobile signature, or from the email address registered with us to <a href="mailto:{MAIL}">{MAIL}</a>.</p>
<p>Your request will be concluded free of charge as soon as possible and within 30 days at the latest, depending on its nature. If the process requires an additional cost, the fee set by the Personal Data Protection Board may be charged.</p>
"""

EN_PRIVACY = f"""
{EN_NOTE.format(tr=PAIRS['privacy'][1])}
<h2>1. Scope</h2>
<p>This policy explains how your information is collected, used and protected when you use the Yankı website and the Yankı media monitoring platform (the “Service”). For the statutory notice on how your personal data is processed, please see the <a href="/privacy-notice.html">Privacy Notice (KVKK)</a>.</p>

<h2>2. Information we collect</h2>
<ul>
<li><strong>Information you give us:</strong> Your name, organisation, email, phone and the brand or person you want to monitor, shared in the demo request form and when creating an account.</li>
<li><strong>Information created as you use the Service:</strong> Your monitoring profiles, keywords, agenda briefs, scan frequency, report recipients and generated reports.</li>
<li><strong>Your AI API keys:</strong> The keys you add for analysis.</li>
<li><strong>Technical information:</strong> IP address, browser type, access times and error logs.</li>
</ul>

<h2>3. How we use information</h2>
<ul>
<li>To provide the Service: run scans, perform analyses, prepare reports and send them by email,</li>
<li>To respond to demo and support requests,</li>
<li>To handle subscriptions and billing,</li>
<li>To keep the Service secure and prevent misuse,</li>
<li>To improve the Service.</li>
</ul>
<p>We <strong>do not sell</strong> your information or share it with third parties for advertising.</p>

<h2>4. Your AI API keys and AI analysis</h2>
<p>Yankı works on a “bring your own key” (BYOK) model:</p>
<ul>
<li>Your API keys are stored encrypted in the database and are never shown in plain text in the interface.</li>
<li>Your keys are used only for requests to the provider you chose, to run analyses on your behalf.</li>
<li>News text and summarisation instructions are sent to the provider for analysis. This content is processed under your contract with the provider and the provider's data policies.</li>
<li>You can delete your key from the dashboard or revoke it in your provider's console at any time.</li>
</ul>

<h2>5. Scanned content</h2>
<p>Yankı only scans content that has been published publicly. Access to the full text of some publications may require an individual or corporate subscription to that source; Yankı does not bypass paywalls. Reports contain a short summary of each story and a link to the original source.</p>

<h2>6. Sharing</h2>
<p>Your information is shared only with service providers needed to deliver the Service (hosting, email delivery, payments) and with authorised authorities where required by law. Details are in the <a href="/privacy-notice.html">Privacy Notice (KVKK)</a>.</p>

<h2>7. Security</h2>
<ul>
<li>Website and application traffic is encrypted with HTTPS.</li>
<li>Passwords are stored as irreversible hashes; API keys are encrypted.</li>
<li>Each customer's data is kept separate from other accounts.</li>
<li>Access is limited to authorised personnel.</li>
</ul>
<p>No system is entirely risk-free. If we become aware of a security breach, we will make the notifications required by law.</p>

<h2>8. Retention and deletion</h2>
<p>Your information is kept while your account is open and for statutory retention periods. When you close your account, your data is deleted or anonymised, subject to legal obligations. Periods are listed in the <a href="/privacy-notice.html">Privacy Notice (KVKK)</a>.</p>

<h2>9. Children</h2>
<p>The Service is not designed for people under 18, and we do not knowingly collect information from them.</p>

<h2>10. Changes and contact</h2>
<p>We may update this policy; we will announce significant changes on the website and, where needed, by email. For questions, write to <a href="mailto:{MAIL}">{MAIL}</a>.</p>
"""

EN_COOKIES = f"""
{EN_NOTE.format(tr=PAIRS['cookies'][1])}
<h2>1. What is a cookie?</h2>
<p>Cookies are small text files saved in your browser when you visit a website. The browser's local storage may be used for similar purposes; both are referred to as “cookies” in this policy.</p>

<h2>2. Cookies on the website</h2>
<div class="box"><p>The Yankı website currently <strong>does not use advertising, marketing or analytics cookies</strong> and does not track visitors. For this reason no cookie consent banner is shown.</p></div>
<p>When you view the site, our hosting provider (Vercel) and font service (Google Fonts) process technical connection information such as your IP address so that pages and fonts can be delivered to you. This is necessary for the site to work.</p>
<p>If you switch the site language, your choice is remembered in your browser's local storage so that you see the same language on your next visit. This is a functional preference, is never sent to us and can be cleared from your browser settings.</p>

<h2>3. Cookies in the application</h2>
<p>When you sign in to the Yankı dashboard, only cookies that are strictly necessary for the service are used:</p>
<div class="tbl"><table>
<thead><tr><th>Type</th><th>Purpose</th><th>Duration</th></tr></thead>
<tbody>
<tr><td>Session / authentication</td><td>Remembering that you are signed in and protecting your account</td><td>For the session or until you sign out</td></tr>
<tr><td>Security</td><td>Preventing unauthorised access and forged requests</td><td>For the session</td></tr>
<tr><td>Preference</td><td>Remembering preferences such as interface language</td><td>12 months</td></tr>
</tbody></table></div>
<p>Strictly necessary cookies are required to provide the service and therefore do not rely on your explicit consent.</p>

<h2>4. Cookies we may use in the future</h2>
<p>If we start using analytics or marketing cookies, we will update this policy and enable those cookies only after obtaining your explicit consent. You will be able to withdraw your consent at any time.</p>

<h2>5. Managing cookies</h2>
<p>You can delete or block cookies in your browser settings. If you block strictly necessary cookies, you may not be able to sign in to the Yankı dashboard.</p>

<h2>6. Contact</h2>
<p>For questions about cookies, write to <a href="mailto:{MAIL}">{MAIL}</a>. For your rights regarding personal data, see the <a href="/privacy-notice.html">Privacy Notice (KVKK)</a>.</p>
"""

EN_TERMS = f"""
{EN_NOTE.format(tr=PAIRS['terms'][1])}
<h2>1. Parties and scope</h2>
<p>These Terms of Use govern the use of the Yankı media monitoring platform (the “Service”) provided by {CO} (the “Company”). By creating an account or using the Service, you accept these terms. If you use the Service on behalf of an organisation, you confirm that you are authorised to bind that organisation to these terms.</p>

<h2>2. The Service</h2>
<p>Yankı scans publicly available publications at the chosen frequency for the brands, people, competitors and topics defined by the user, summarises and classifies content with the help of artificial intelligence, and delivers the results by email as PDF reports. The scope of the Service depends on the selected plan.</p>

<h2>3. Account</h2>
<ul>
<li>You must provide accurate and up-to-date information when creating an account.</li>
<li>You are responsible for the security of your password and account. Tell us immediately if you notice any unauthorised use.</li>
<li>The Service is intended for people aged 18 or over.</li>
</ul>

<h2>4. Your own AI key (BYOK)</h2>
<ul>
<li>Analyses run with your API key at the AI provider you configure.</li>
<li>The provider's usage charges are yours and are not included in the Yankı subscription fee.</li>
<li>You are responsible for complying with your chosen provider's terms and policies.</li>
<li>The Company is not responsible for outages, limits or price changes caused by the provider.</li>
</ul>

<h2>5. Plans, fees and trial</h2>
<ul>
<li>Current plans and fees are published on the website. Fees exclude VAT.</li>
<li>The Starter and Pro plans can be tried free for 15 days. At the end of the trial, unless you cancel, the subscription continues as a paid subscription on the plan you chose.</li>
<li>Subscriptions renew monthly. You can cancel at any time; cancellation takes effect at the end of the current billing period.</li>
<li>Subject to your statutory rights, fees for periods already used are not refunded.</li>
<li>Enterprise plan terms are set out in a separate agreement.</li>
<li>The Company may change its fees; changes are announced at least 30 days in advance and apply from the next billing period.</li>
</ul>

<h2>6. Acceptable use</h2>
<p>You may not use the Service to:</p>
<ul>
<li>Monitor, profile, stalk or harass private individuals who are not public figures,</li>
<li>Process personal data unlawfully or use it for discrimination,</li>
<li>Carry out any unlawful activity,</li>
<li>Resell the Service or report content to third parties without permission,</li>
<li>Attempt to bypass the Service's security, reverse engineer it or overload its systems.</li>
</ul>
<p>You decide which people and topics are monitored and are responsible for the lawfulness of those choices. If this section is breached, the Company may suspend or close the account.</p>

<h2>7. Content and intellectual property</h2>
<ul>
<li>Rights in the news and publications scanned belong to their publishers. Reports contain short summaries of this content and links to the original sources.</li>
<li>Access to the full text of some publications may require an individual or corporate subscription to that source.</li>
<li>The Yankı software, brand and design belong to the Company. You are granted only a right to use the Service during your subscription.</li>
<li>Your monitoring profiles and your reports belong to you, and you may use them freely for your internal purposes.</li>
</ul>

<h2>8. AI outputs</h2>
<p>Summaries, sentiment labels, PR Risk and competitive assessments are generated automatically by artificial intelligence and may be inaccurate or incomplete. These outputs are intended to support decisions; you should review the original source before making important decisions. The Service is not legal, financial or investment advice.</p>

<h2>9. Service availability</h2>
<p>We make reasonable efforts to provide the Service without interruption, but outages may occur due to maintenance, infrastructure failures or problems with third-party sources or providers. Changes to source websites may temporarily prevent some channels from being scanned. Outside the Enterprise plan, no specific availability level is guaranteed.</p>

<h2>10. Limitation of liability</h2>
<p>To the extent permitted by law, the Company's total liability in connection with the Service is limited to the subscription fees you paid in the 12 months before the event giving rise to the claim. The Company is not liable for loss of profit, loss of reputation or indirect damages, or for decisions taken in reliance on AI outputs. This limitation does not apply in cases of intent or gross negligence, or to consumers' statutory rights.</p>

<h2>11. Termination</h2>
<p>You can end your subscription at any time. The Company may suspend or close your account if these terms are breached. When an account is closed, your data is deleted according to the periods in the <a href="/privacy-notice.html">Privacy Notice (KVKK)</a>.</p>

<h2>12. Consumers</h2>
<p>If you use the Service as a consumer, your rights under Turkish Consumer Protection Law No. 6502 and the Distance Contracts Regulation are reserved. For services performed instantly in electronic form, the right of withdrawal applies subject to the exceptions in the legislation.</p>

<h2>13. Changes</h2>
<p>We may update these terms. We will announce significant changes by email or in the dashboard before they take effect. Continuing to use the Service after a change means you accept the updated terms.</p>

<h2>14. Governing law and jurisdiction</h2>
<p>These terms are governed by the laws of the Republic of Türkiye. Istanbul (Çağlayan) Courts and Enforcement Offices have jurisdiction over disputes. For consumers, Consumer Arbitration Committees and Consumer Courts have jurisdiction within the statutory monetary limits.</p>

<h2>15. Contact</h2>
<p>{CO} · {ADDR}, Türkiye · <a href="mailto:{MAIL}">{MAIL}</a></p>
"""

DOCS = {
    "en": {
        "kvkk": ("How we process your personal data under Turkish data protection law (KVKK), on what legal grounds, and your rights.", EN_KVKK),
        "privacy": ("How we collect, use and protect your information when you use Yankı, in plain language.", EN_PRIVACY),
        "cookies": ("Which cookies are used on the website and in the application, and why.", EN_COOKIES),
        "terms": ("The rules that apply when you use Yankı, including pricing and each party's responsibilities.", EN_TERMS),
    },
    "tr": {
        "kvkk": ("Kişisel verilerinizin hangi amaçlarla, hangi hukuki sebeplere dayanılarak işlendiğini ve haklarınızı açıklar.", KVKK),
        "privacy": ("Yankı'yı kullanırken bilgilerinizi nasıl topladığımızı, kullandığımızı ve koruduğumuzu sade bir dille anlatır.", PRIVACY),
        "cookies": ("Sitede ve uygulamada hangi çerezlerin, hangi amaçla kullanıldığını açıklar.", COOKIES),
        "terms": ("Yankı'yı kullanırken geçerli olan kuralları, ücretlendirmeyi ve tarafların sorumluluklarını düzenler.", TERMS),
    },
}

if __name__ == "__main__":
    for lang, docs in DOCS.items():
        for key, (lead, body) in docs.items():
            path = os.path.join(OUT, href(lang, key).lstrip("/"))
            os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(page(lang, key, lead, body.strip()))
            print("wrote", path)
