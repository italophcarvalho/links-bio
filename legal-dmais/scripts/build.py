from pathlib import Path
from urllib.parse import quote
from html import escape
import json, base64, shutil

ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/'src'
DIST=ROOT/'dist'
DIST.mkdir(exist_ok=True)
(DIST/'assets').mkdir(exist_ok=True)
data=json.loads((SRC/'content.json').read_text(encoding='utf-8'))
ICONS={
'instagram':'<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1"/>',
'whatsapp':'<path d="M20 11.5a8 8 0 0 1-11.7 7.1L4 20l1.4-4.1A8 8 0 1 1 20 11.5Z"/><path d="M9.2 8.8c.3-.7.6-.8 1-.8h.7c.2 0 .4.1.5.4l.8 1.8c.1.3.1.5-.1.7l-.5.6c.7 1.2 1.6 2.1 2.9 2.8l.6-.6c.2-.2.5-.2.7-.1l1.7.8c.3.1.4.3.4.6v.7c0 .4-.3.8-.8 1a4 4 0 0 1-2 .2c-3.8-.7-6.7-3.6-7.4-7.3a3.7 3.7 0 0 1 .5-1.8Z"/>',
'pin':'<path d="M12 21s7-5.1 7-12a7 7 0 0 0-14 0c0 6.9 7 12 7 12Z"/><circle cx="12" cy="9" r="2.4"/>',
'calendar':'<rect x="3" y="5" width="18" height="16" rx="3"/><path d="M8 3v4M16 3v4M3 10h18m-13 5 2.5 2.5L16 12"/>',
'gift':'<rect x="3" y="8" width="18" height="4" rx="1"/><path d="M5 12v8h14v-8M12 8v12"/><path d="M12 8H8.5a2.5 2.5 0 1 1 2.45-3L12 8Zm0 0h3.5a2.5 2.5 0 1 0-2.45-3L12 8Z"/>',
'home':'<path d="m3 10 9-7 9 7M5 9v12h14V9M9 21v-7h6v7"/>',
'gallery':'<rect x="3" y="3" width="18" height="18" rx="3"/><circle cx="8" cy="8" r="1.5"/><path d="m3 17 6-6 4 4 3-3 5 5"/>',
'arrow':'<path d="M5 12h14m-6-6 6 6-6 6"/>'
}
def icon(name):
    return '<svg class="icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false">'+ICONS[name]+'</svg>'
def wa(key):
    return 'https://wa.me/'+data['phone']+'?text='+quote(data['messages'][key],safe='')
def destination(key):
    if key in ('maps','instagram'):return data[key]
    return wa(key)
channels=[
('instagram','Instagram do '+data['name'],data['instagram']),
('whatsapp','WhatsApp do '+data['name'],wa('general')),
('pin','Localização do '+data['name'],data['maps'])
]
def action_links(footer=False):
    base='footer-icon' if footer else 'quick-action'
    out=[]
    for key,label,url in channels:
        extra=' '+base+'--'+key if key in ('instagram','whatsapp') else ''
        out.append('        <a class="'+base+extra+'" href="'+escape(url,quote=True)+'" target="_blank" rel="noopener noreferrer" aria-label="'+escape(label,quote=True)+'">'+icon(key)+'</a>')
    return '\n'.join(out)
cards=[]
for item in data['cards']:
    modifier='' if item['variant']=='default' else ' link-card--'+item['variant']
    cards.append('''      <a class="link-card'''+modifier+'''" href="'''+escape(destination(item['destination']),quote=True)+'''" target="_blank" rel="noopener noreferrer">
        <span class="link-icon" aria-hidden="true">'''+icon(item['icon'])+'''</span>
        <span class="link-content"><strong>'''+escape(item['title'])+'''</strong><span>'''+escape(item['description'])+'''</span></span>
        <span class="arrow" aria-hidden="true">'''+icon('arrow')+'''</span>
      </a>''')
def uri(path,mime):
    return 'data:'+mime+';base64,'+base64.b64encode(path.read_bytes()).decode('ascii')
favicon='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="18" fill="#0756A3"/><path d="M41 21v18M32 30h18" stroke="#FFD43B" stroke-width="6" stroke-linecap="round"/><path d="M17 17v29h14" fill="none" stroke="white" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
structured={
'@context':'https://schema.org','@type':'LocalBusiness','name':data['name'],
'description':data['description'],'telephone':'+'+data['phone'],'url':data['origin']+'/',
'image':data['origin']+'/assets/social.jpg','address':{'@type':'PostalAddress',**data['address']},
'hasMap':data['maps'],'sameAs':[data['instagram']]
}
replacements={
'TITLE':escape(data['title']),'NAME':escape(data['name'],quote=True),'SHORT_NAME':escape(data['shortName']),
'TAGLINE':escape(data['tagline']),'DESCRIPTION':escape(data['description'],quote=True),
'ORIGIN':escape(data['origin'].rstrip('/'),quote=True),
'FAVICON':'data:image/svg+xml,'+quote(favicon,safe=''),
'FONT_URI':uri(SRC/'assets/nunito-latin-variable.woff','font/woff'),
'PHOTO_URI':uri(SRC/'assets/fachada.webp','image/webp'),
'CSS':(SRC/'style.css').read_text(encoding='utf-8'),
'STRUCTURED_DATA':json.dumps(structured,ensure_ascii=False).replace('<','\\u003c'),
'QUICK_ACTIONS':action_links(),'FOOTER_ACTIONS':action_links(True),'CARDS':'\n\n'.join(cards),
'FONT_LICENSE':escape((SRC/'assets/OFL.txt').read_text(encoding='utf-8'))
}
html=(SRC/'page.html').read_text(encoding='utf-8')
for name,value in replacements.items():html=html.replace('{{'+name+'}}',value)
(DIST/'index.html').write_text(html,encoding='utf-8')
shutil.copyfile(SRC/'assets/social.jpg',DIST/'assets/social.jpg')
print(json.dumps({'html':str(DIST/'index.html'),'initial_bytes':(DIST/'index.html').stat().st_size,'social_bytes':(DIST/'assets/social.jpg').stat().st_size},ensure_ascii=False))

