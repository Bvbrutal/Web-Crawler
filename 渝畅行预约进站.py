import requests
import time

url = 'https://ycx.cqmetro.cn/bas/ncp/v1/appiont/list'
print(int(time.time() * 1000))
header = {
    'Host': 'ycx.cqmetro.cn',
    'Referer': 'https://ycx.cqmetro.cn/app-h5/appointment/',
    'appid': 'A500120190100001',
    'Cookie': 'acw_tc=2f624a1616929484974907065e62a480a84d6264e27445431c2374459c8fb3',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 BWTJSBridge/1.1.0',
    'random': '',
    'app_version': '1.21.0',
    'Origin': 'https://ycx.cqmetro.cn',
    'signature': 'IQzdjc3IX734TcTpJ/YRr1IvWQ+BKOifGAYuj+SJaa66UidC8IPFLlB0MU8MjEBXWyE18E8uOrmP/0hjlcO7sy7LczddGJJeH0I6iRQGf+dawTE+DatDoTcL1vi+xEE5pS97M2Z6LpBSyoXtCqK3jXrp1V4OisD6cE+snlTujXQ=',
    'version': '0100',
    'nonce': 'yryAMBrsB8EiNPmYbJ4DrJfeYfYrSb4B',
    'Content-Length': '33',
    'bundleId': 'com.bwton.msx.ycx',
    'token': 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJjMzk4YWNhMS01ZmJjLTRhY2QtODAzMS0xN2RhZjZhNmE1YTYiLCJpc3MiOiJZYW5ZYW4iLCJzdWIiOiJ7XCJ1c2VySWRcIjpcIjc5MDExMTI2ODI5MjA5NjBcIixcInVuaW9uSWRcIjpcIjEwMDAwMDE1NzkwMTExMjY4MjkyMDk2MFwiLFwib3BlbmFwaWFjY291bnRcIjpcIjc5MDExMTI2ODI5MjA5NjBcIixcIm5ld0RldmljZUlkXCI6XCIxNGI4N2UxZmQ4NjA5MjI1MDQwNmQxYjViNjAyZTY5N1wiLFwibmV3RGV2aWNlVHlwZVwiOlwiMVwifSIsImlhdCI6MTY5MjcwMDQyMywiZXhwIjoxNjk1MjkyNDIzfQ.4y1bfxivuFHQNn5CVQWH9UQbXHE-YOfebzNwAfSwahw',
    'cityId': '5000',
    'timestamp': int(time.time() * 1000),
    'Accept-Language': 'zh-cn',
    'Connection': 'keep-alive',
    'X-Ca-Version': 'v1.0',
    'Accept': 'application/json',
    'Content-Type': 'application/json;charset=utf-8',
    'sequence': '202308251556408903549839',
    'X-Ca-Signature-Version': '1',
    'Accept-Encoding': 'gzip, deflate, br',

}
print(int(time.time() * 1000))
data = {"cityId": 5000, "stationId": "210"}

rea = requests.post(url, header, json=data)
print(rea.text)

url2 = 'http://mtop.damai.cn/gw/mtop.trade.order.build/4.0?rnd=A5B3B78E41351774724FCDAB36261111&wua=1P7U_OySDnE54lF3m4t8xl8PEqXl4RaIYPxB73wHx8FxcLYtrsPnRc75h9eXWOTvT5WtKUzJpWh%2BcEIwSu4zm6jg0JksfBRAXcMpBwMlsBhJgFy2MKLDagasuXy0o%2Btv%2BQoCjfMhtPpiEacJrUEaZyYSicX9i4pJgPe98bPmXy783XudX6tDm9htQNb8ACmd6BuWjeMzOvhvhqv9Ggbv%2F0N%2BMLNtCsnqC%2BKq3xu9WBB7Ca64A2AkVhEST8YKOJ7IvLqzwIHX806fF5dKItYX%2FWlifKoZIbZ%2FZn4wfR0G7wRBRzciE8jbYjmGJJWRsq3qQ1jXGLH%2B01oZiDRsu1HFmFPIC%2BOz9COu%2BO8qstxQ1q8DFBJE%3D'

header2 = {

    'User-Agent': 'MTOPSDK%2F1.9.3.48%20%28iOS%3B13.6.1%3BApple%3BiPhone11%2C8%29',
    'x-page-name': 'TBHomeViewController',
    'Cookie': '_tb_token_=e83713fafe67e; cookie2=1ad1067080535f33ff0e63a69e84d17d; csg=3add52f7; damai_cn_user=f9IXUDOWV2g2FuOySlGvxodyTMsV4A6V+5bGlCz/TmcYZPn60idPE9y/ZEQU3zRRGxb2+Rjuqig=; loginkey=9d963c55dd7842849decc48d2f376129_3_2; munb=2211530728434; sgcookie=W100vGAmOIEL6F27S5RxI5q%2BTwpc5sXFWRzh0GU2O7E0KETvdfdLbbUdQgZR25gO6%2FlrVKahb1ezEPN%2BBtCgAN3pQJ2y6OQ7kBOXmfHUprl7e%2FRcRvTjOJ2DxoU%2BpXe0VpkF; t=399f5ce8daa89445feaf674bffa9543a; l=fBrck7gHNf51BiZEBOfZPurza77tsCdgYuPzaNbMi9fP_vfp5x_fW1OkQS89Cn1REsjpx3WcUOUkB0YnKyU6hmwQTA5FWCeqUKvMR3zQR; tfstk=dzSkWFfPeCqGnaMFz0K727x1Pj1kVbtBK6np9HdUuIRfeBUWwBWFg9np8Wa5xHfJMgLp4zOhi_9MaBUWwBlFg9ILNQeWLZf5QUChd89eT65H9aLuXT6WAHPT6lEOFtiszRHYkMn1LMKU65ETXT6WAHSdGYxfE3zU2a_-RLLzi2c3jZUPGUANne0KAgo9JCWyif85mOAE3BdjxKYOvM3xRUJXn0yrcR1..; cna=3afAHK1EhhkBASQOBDHy0dCY',
    'f-refer': 'mtop',
    'x-sgext': 'JBEzLJ1X4OBhG6qvKirPliwGHAIPCxkCGAQPBRwQDwIaCh4KGQcdAxoQHAMeBRwDHFEcAxwDHAMcAw8DDwMPAxwQHAMcAw8DDwIPAg8CDwIPAg8CDwMPAxwDHAMPAUhSDwAPCw8DD3Rocn8QDBMfUAwTDAM%3D',
    'x-app-ver': '8.5.3',
    'x-utdid': 'YIeC8RNJjJQDAMIORSyHwGDm',
    'x-uid': '2211530728434',
    'x-cmd-v': '0%7C0',
    'Content-Length': '866',
    'Connection': 'keep-alive',
    'x-sign': 'izKMHp004xAAL20bQgI%2BbLc6Apve320fZ8WuiSHL3ThmIt0PADve13ZSzDf3h5%2FLQ7bhp9SitwfefakTPSYpSL8ou7%2FNH20fbT9tH2',
    'x-mini-wua': 'i3QSckWJxQxSXkWkq9l2Hs252EDr3lYyuZjEnOMj0sg%2FqxuVLYyaIangli8sqoghZnWSJK7srOqUhT0Y3DkEM143%2FEuYd%2BSDqWlLwefji%2Fy3rEpHkoA3xFo1GPRC1bC%2BL0ULrQi5VAZAOwWc5KQ3N%2Bt0dZE5ii9g82pszpc13T7kadG1TNxUD0aU4',
    'x-appkey': '23782110',
    'x-sid': '1ad1067080535f33ff0e63a69e84d17d',
    'x-features': '11',
    'x-umt': 'U1IBCKRLPBbTVRKKK%2Blkoqvs7ceYFsr8',
    'Accept-Language': 'zh-cn',
    'Accept': '*/*',
    'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
    'x-ttid': 'cn.damai.iphone%40damai_iphone_8.5.3',
    'x-nq': 'WiFi',
    'x-t': '1692954790',
    'Accept-Encoding': 'gzip, deflate',

}
daa = {
    "exParams": "{\n  \"novacv\" : \"4.0\",\n  \"novab\" : \"mtop.trade.order.build\",\n  \"channel\" : \"damai_app\",\n  \"novaav\" : \"5.0\",\n  \"coupon\" : \"true\",\n  \"novac\" : \"mtop.trade.order.create\",\n  \"umpChannel\" : \"10001\",\n  \"novaa\" : \"mtop.trade.order.adjust\",\n  \"coVersion\" : \"2.0\",\n  \"novabv\" : \"4.0\",\n  \"atomSplit\" : \"1\",\n  \"novad\" : \"mtop.damai.cn\"\n}",
    "buyNow": "true",
    "buyParam": "732585805221_1_5241047482075"
}
print(daa["exParams"])
res1 = requests.post(url2, header2, json=daa)
print(res1.text)
