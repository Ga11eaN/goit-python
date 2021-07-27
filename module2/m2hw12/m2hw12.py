import aiohttp
from aiohttp import web
import asyncio

    
async def privat24():
    
    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5') as response:
            course_json = await response.json()
            privat = {}
            for item in course_json:
                item['rate'] = (float(item['buy']) + float(item['sale']))/2
                privat[item['ccy']] = item['rate']
    return privat
            
async def nbu24():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json') as response:
            course_json = await response.json()
            nbu = {}
            for item in course_json:
                nbu[item['cc']] = float(item['rate'])
    return nbu
    
async def output(request):
    privat_data = request.app['privat']
    nbu_data = request.app['nbu']
    text = 'Privat:\n'
    text += ('|{:^3}|{:^4}|\n').format('USD',privat_data['USD'])
    text += ('|{:^3}|{:^4}|\n').format('EUR',privat_data['EUR'])
    text += ('|{:^3}|{:^4}|\n').format('RUR',privat_data['RUR'])
    text += 'NBU:\n'
    text += ('|{:^3}|{:^4}|\n').format('USD',nbu_data['USD'])
    text += ('|{:^3}|{:^4}|\n').format('EUR',nbu_data['EUR'])
    text += ('|{:^3}|{:^4}|\n').format('RUR',nbu_data['RUB'])
    return web.Response(text = text)


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())    
loop = asyncio.get_event_loop()
tasks = privat24(), nbu24()
a,b = loop.run_until_complete(asyncio.gather(*tasks))

app = web.Application()
app['privat'] = a
app['nbu'] = b
app.add_routes([web.get('/', output)])
web.run_app(host = '127.0.0.1', app = app)