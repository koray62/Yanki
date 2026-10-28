// Demo talep formunu Turkticaret.net SMTP üzerinden e-postaya dönüştüren Vercel fonksiyonu.
// Gerekli ortam değişkenleri (Vercel > Settings > Environment Variables):
//   SMTP_HOST, SMTP_PORT (465 veya 587), SMTP_USER, SMTP_PASS
// İsteğe bağlı: MAIL_FROM (varsayılan SMTP_USER), DEMO_TO (varsayılan info@noratech.com.tr)
const nodemailer = require('nodemailer');

const LIMITS = { ad: 120, kurum: 160, eposta: 200, telefon: 40, hedef: 300 };
const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

function esc(s) {
  return String(s).replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
}

function readBody(req) {
  let b = req.body;
  if (typeof b === 'string') {
    try { b = JSON.parse(b); } catch { b = Object.fromEntries(new URLSearchParams(b)); }
  }
  return b && typeof b === 'object' ? b : {};
}

function clean(v, max) {
  return String(v == null ? '' : v).replace(/[\r\n\t]+/g, ' ').trim().slice(0, max);
}

module.exports = async function handler(req, res) {
  if (req.method !== 'POST') {
    res.setHeader('Allow', 'POST');
    return res.status(405).json({ ok: false, error: 'method_not_allowed' });
  }

  const body = readBody(req);

  // Bot tuzağı: görünmeyen alan doluysa sessizce başarılı dön.
  if (clean(body.website, 200)) return res.status(200).json({ ok: true });

  const data = {};
  for (const [k, max] of Object.entries(LIMITS)) data[k] = clean(body[k], max);
  const kvkk = body.kvkk === true || body.kvkk === 'on' || body.kvkk === 'true';

  const missing = [];
  if (!data.ad) missing.push('ad');
  if (!data.kurum) missing.push('kurum');
  if (!EMAIL_RE.test(data.eposta)) missing.push('eposta');
  if (!kvkk) missing.push('kvkk');
  if (missing.length) return res.status(400).json({ ok: false, error: 'invalid', fields: missing });

  const { SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASS } = process.env;
  if (!SMTP_HOST || !SMTP_USER || !SMTP_PASS) {
    console.error('demo: SMTP ayarları eksik');
    return res.status(500).json({ ok: false, error: 'not_configured' });
  }
  const port = Number(SMTP_PORT || 587);
  const to = process.env.DEMO_TO || 'info@noratech.com.tr';
  const from = process.env.MAIL_FROM || SMTP_USER;

  const transporter = nodemailer.createTransport({
    host: SMTP_HOST,
    port,
    secure: port === 465,
    auth: { user: SMTP_USER, pass: SMTP_PASS },
  });

  const rows = [
    ['Ad soyad', data.ad],
    ['Kurum', data.kurum],
    ['E-posta', data.eposta],
    ['Telefon', data.telefon || '—'],
    ['Takip edilmek istenen', data.hedef || '—'],
    ['KVKK aydınlatma', 'Okundu olarak işaretlendi'],
    ['Tarih', new Date().toLocaleString('tr-TR', { timeZone: 'Europe/Istanbul' })],
  ];

  try {
    await transporter.sendMail({
      from,
      to,
      replyTo: data.eposta,
      subject: `Yankı demo talebi: ${data.kurum} — ${data.ad}`,
      text: rows.map(([k, v]) => `${k}: ${v}`).join('\n'),
      html:
        '<h2 style="font-family:sans-serif">Yeni demo talebi</h2><table style="font-family:sans-serif;border-collapse:collapse">' +
        rows.map(([k, v]) => `<tr><td style="padding:6px 12px;color:#475569">${esc(k)}</td><td style="padding:6px 12px"><strong>${esc(v)}</strong></td></tr>`).join('') +
        '</table>',
    });
    return res.status(200).json({ ok: true });
  } catch (err) {
    console.error('demo: gönderim hatası', err && err.code, err && err.response);
    return res.status(502).json({ ok: false, error: 'send_failed' });
  }
};
