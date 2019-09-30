import asyncio
from pyppeteer import connect, launch

# webSocketDebuggerUrl = 'ws://45.254.64.7:9222/devtools/browser/11ec6655-2eab-4524-ad73-0a074042c932'


async def close_dialog(dialog):
    if dialog.message == '1':
        print('detect xss')
    await dialog.dismiss()



async def scan(url):
    browser = await launch(headless=True, args=['--disable-xss-auditor'])
    # 连接chrome实例
    # browser = await connect({'browserWSEndpoint': webSocketDebuggerUrl})
    page = await browser.newPage()
    page.on('dialog', lambda dialog: asyncio.ensure_future(close_dialog(dialog)))
    await page.goto(url)
    await page.close()
    await browser.close()


if __name__ == '__main__':
    payload = '"><script>alert(1)</script>'
    url = 'http://vps.yy/info.php?id=1{payload}'.format(payload=payload)
    print(url)



    asyncio.get_event_loop().run_until_complete(scan(url))