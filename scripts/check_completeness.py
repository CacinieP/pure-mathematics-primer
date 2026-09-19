import re,json,collections
from pathlib import Path
from bs4 import BeautifulSoup

def formulas(text):
 out=[];fence=None;buf=[]
 for line in text.splitlines(True):
  m=re.match(r'^\s*(`{3,}|~{3,})',line)
  if m:
   if fence is None:fence=m[1]
   elif m[1][0]==fence[0] and len(m[1])>=len(fence):fence=None
   buf.append('\n');continue
  buf.append('\n' if fence else line)
 text=''.join(buf)
 text=re.sub(r'(`+)[^`]*?\1','',text)
 pattern=r'(?<!\\)(\${1,2})(.+?)(?<!\\)\1(?!\$)'
 for m in re.finditer(pattern,text,re.S):
  out.append((m[1]=='$$',re.sub(r'\s+',' ',m[2]).strip()))
 return out

if __name__ == '__main__':
 root=Path(__file__).resolve().parents[1];diffs=[];total=0
 for p in sorted((root/'.site-docs').rglob('*.md')):
  rel=p.relative_to(root/'.site-docs');rendered=root/'site'/rel.with_suffix('')/'index.html'
  if p.stem=='index':rendered=root/'site'/rel.parent/'index.html'
  if not rendered.exists():raise SystemExit(f'Missing rendered page: {rel}')
  expected=collections.Counter(formulas(p.read_text()));total+=expected.total()
  soup=BeautifulSoup(rendered.read_text(),'html.parser');actual=collections.Counter()
  for el in soup.select('.arithmatex'):
   t=el.get_text()[2:-2];actual[(el.name=='div',re.sub(r'\s+',' ',t).strip())]+=1
  if expected!=actual:
   diffs.append({'source':str(rel),'missing':list((expected-actual).elements()),'extra':list((actual-expected).elements())})
 print(f'Compared {total} source formulas; {len(diffs)} pages with differences')
 if diffs:
  print(json.dumps(diffs,ensure_ascii=False,indent=2))
  raise SystemExit(1)
