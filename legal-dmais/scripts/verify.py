from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse, parse_qs
from PIL import Image
import json, re, base64, io, subprocess

ROOT=Path(__file__).resolve().parents[1]
html=(ROOT/'dist/index.html').read_text(encoding='utf-8')
config=json.loads((ROOT/'src/content.json').read_text(encoding='utf-8'))
class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links=[];self.images=[];self.h1=0;self.main=0;self.lang=None
    def handle_starttag(self,tag,attrs):
        attrs=dict(attrs)
        if tag=='a':self.links.append(attrs)
        if tag=='img':self.images.append(attrs)
        if tag=='h1':self.h1+=1
        if tag=='main':self.main+=1
        if tag=='html':self.lang=attrs.get('lang')
p=Page();p.feed(html);p.close()
assert p.lang=='pt-BR' and p.h1==1 and p.main==1
cards=[a for a in p.links if 'link-card' in a.get('class','').split()]
quick=[a for a in p.links if 'quick-action' in a.get('class','').split()]
footer=[a for a in p.links if 'footer-icon' in a.get('class','').split()]
assert (len(cards),len(quick),len(footer),len(p.links))==(5,3,3,11)
for link in p.links:
    url=urlparse(link['href'])
    assert url.scheme=='https' and url.netloc in ('wa.me','www.instagram.com','www.google.com')
    assert link['href'] not in ('','#')
    assert link.get('target')=='_blank'
    assert {'noopener','noreferrer'} <= set(link.get('rel','').split())
    if url.netloc=='wa.me':
        assert url.path=='/'+config['phone']
        message=parse_qs(url.query)['text'][0]
        assert message.startswith('Olá! Vim pelo link da bio do Legal D+')
    if url.netloc=='www.google.com':
        assert parse_qs(url.query)['cid']==['14167918038953408247']
for link in quick+footer:assert link.get('aria-label')
budget=parse_qs(urlparse(cards[0]['href']).query)['text'][0]
assert '\nData da festa:\nQuantidade de convidados:\nTipo de comemoração:' in budget
for item in config['cards']:
    assert item['title'] in html and item['description'] in html
assert len(p.images)==1 and p.images[0].get('alt') and p.images[0].get('width')=='680'
img_uri=p.images[0]['src'];assert img_uri.startswith('data:image/webp;base64,')
with Image.open(io.BytesIO(base64.b64decode(img_uri.split(',',1)[1]))) as im:assert im.size==(680,453)
font_uri=re.search(r'data:font/woff;base64,([A-Za-z0-9+/=]+)',html).group(1)
assert base64.b64decode(font_uri)[:4]==b'wOFF'
assert len(html.encode('utf-8'))<=500*1024
assert not re.search(r'\{\{[A-Z_]+\}\}',html)
assert 'Carla Dias' not in html and 'cursodescomplicandosites' not in html and '3.499' not in html
assert not any(s in html for s in ['fonts.googleapis.com','fonts.gstatic.com'])
definitions=set(re.findall(r'(--ds-[\w-]+)\s*:',html))
references=set(re.findall(r'var\((--ds-[\w-]+)',html))
assert not references-definitions
for attrs,body in re.findall(r'<script([^>]*)>(.*?)</script>',html,re.S):
    if 'application/ld+json' in attrs:
        data=json.loads(body);assert data['name']==config['name']
        assert 'aggregateRating' not in data and 'openingHours' not in data and 'priceRange' not in data
    else:
        check=subprocess.run(['node','--check'],input=body,text=True,capture_output=True)
        assert check.returncode==0,check.stderr
assert 'prefers-reduced-motion' in html and ':focus-visible' in html and 'minmax(0, 1fr)' in html
assert 'SIL OPEN FONT LICENSE' in html
assert (ROOT/'dist/assets/social.jpg').is_file()
print(json.dumps({'status':'passed','cards':5,'quick_links':3,'footer_links':3,'initial_bytes':len(html.encode('utf-8')),'self_contained_font_and_hero':True,'valid_whatsapp_messages':True,'css_variables_resolved':True,'javascript_syntax':'valid'},ensure_ascii=False))

