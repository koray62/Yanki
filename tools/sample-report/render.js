// report-tr.html / report-en.html -> yanki-ornek-rapor.pdf / yanki-sample-report.pdf
// Kullanım: node tools/sample-report/render.js <html klasörü> <depo kökü>
const path = require('path');
const { chromium } = require('playwright');

const [htmlDir, repo] = process.argv.slice(2);
const jobs = [['report-tr.html', 'yanki-ornek-rapor.pdf'], ['report-en.html', 'yanki-sample-report.pdf']];

(async () => {
  const browser = await chromium.launch();
  for (const [src, out] of jobs) {
    const page = await browser.newPage();
    await page.goto('file://' + path.resolve(htmlDir, src));
    await page.waitForTimeout(400);
    const meta = await page.evaluate(() => window.__pageFoot);
    await page.pdf({
      path: path.resolve(repo, out), format: 'A4', printBackground: true, preferCSSPageSize: true,
      displayHeaderFooter: true, headerTemplate: '<span></span>',
      footerTemplate: `<div style="width:100%;margin:0 16mm;font-family:Helvetica,Arial,sans-serif;font-size:7px;color:#94A3B8;display:flex;justify-content:space-between"><span>${meta.text}</span><span>${meta.page} <span class="pageNumber"></span> / <span class="totalPages"></span></span></div>`,
    });
    console.log('wrote', out);
  }
  await browser.close();
})();
