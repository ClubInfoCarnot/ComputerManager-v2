import asyncio
from playwright.async_api import async_playwright

async def html_to_pdf(html_content, output_path):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.set_content(html_content)
        await page.pdf(path=output_path)
        await browser.close()

with open('template.html', 'r') as f:
    html_content = f.read()

output_path = 'custom-html-to-pdf-output.pdf'

asyncio.run(html_to_pdf(html_content, output_path))
