"""
Dashboard siklus hidup interaktif (Batch 7): Roda Takdir + Grafik Usia 20-60 (Matrix Destiny) / Pinnacle (Numerologi).
Satu iframe (components.html), klik titik/segmen -> penjelasan fase tanpa rerun Streamlit. Data dari content/life_cycle.py.
"""

import json
from datetime import date

import streamlit.components.v1 as components

from content import life_cycle as LC
from engine.rotation import today_wib

SYSTEMS = ("Matrix Destiny", "Numerologi")


def payload(system, tgl, today=None):
    today = today or today_wib()
    age = LC.usia(tgl, today)
    if system == "Matrix Destiny":
        return {"system": system, "age": age, "roda": LC.roda(tgl), "grafik": LC.grafik_matrix(tgl)}
    return {"system": system, "age": age, "pin": LC.pinnacle(tgl)}


_HTML = """<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><style>
*{box-sizing:border-box}body{margin:0;font-family:'Source Sans 3','Segoe UI',system-ui,sans-serif;color:#2D2A26;background:transparent}
.tabs{display:flex;gap:6px;margin:0 0 10px}.tabs button{font:inherit;font-size:12.5px;font-weight:700;border:1px solid #E9C9A8;background:#fff;color:#C25E00;border-radius:99px;padding:6px 14px;cursor:pointer}
.tabs button.on{background:#C96234;color:#fff;border-color:#C96234}
.hint{font-size:12px;color:#8B8378;margin:0 0 6px}
svg{width:100%;height:auto;display:block}svg text{pointer-events:none}
.node{cursor:pointer}.node circle{fill:#fff;stroke:#E0A67E;stroke-width:2;transition:all .15s}.node:hover circle,.node.on circle{fill:#FFF1E3;stroke:#C96234;stroke-width:3}
.node text.n{font-size:13px;font-weight:800;fill:#C96234;text-anchor:middle;dominant-baseline:central;pointer-events:none}
.lab{font-size:11px;font-weight:700;fill:#6B635A;text-anchor:middle}.age{font-size:10.5px;fill:#8B8378;text-anchor:middle}
.oct{fill:rgba(232,166,127,.10);stroke:#EBCFA6;stroke-width:1.5}.spoke{stroke:#F0DFC4;stroke-width:1}
.core circle{fill:#C96234;stroke:#fff;stroke-width:3}.core text.n{fill:#fff}
.gl{stroke:#F0E6D8;stroke-width:1}.gt{font-size:10px;fill:#A29A8E}
.area{fill:rgba(201,98,52,.12)}.ln{fill:none;stroke:#C96234;stroke-width:2.5;stroke-linejoin:round}
.dot{cursor:pointer;fill:#fff;stroke:#C96234;stroke-width:2.5;transition:all .15s}.dot:hover,.dot.on{fill:#C96234}
.seg{fill:transparent;cursor:pointer}.seg:hover{fill:rgba(201,98,52,.07)}.seg.on{fill:rgba(201,98,52,.14)}
.now{stroke:#3F8F5E;stroke-width:2;stroke-dasharray:4 3}.nowt{font-size:10.5px;font-weight:800;fill:#3F8F5E;text-anchor:middle}
.xt{font-size:11px;fill:#6B635A;text-anchor:middle;font-weight:700}
.pn{cursor:pointer;transition:all .15s}.pn:hover{opacity:.85}.pn.on{stroke:#2D2A26;stroke-width:2.5}
.p{margin-top:12px;background:#FBF8F3;border:1px solid #F0DFC4;border-radius:14px;padding:14px 16px}
.p h3{margin:0 0 2px;font-family:'Playfair Display',Georgia,serif;font-size:18px}.p .sub{font-size:12px;color:#8B8378;margin:0 0 8px}
.p p{font-size:13.2px;line-height:1.65;margin:0 0 8px}.meter{display:flex;align-items:center;gap:8px;margin:6px 0 10px;font-size:12px;font-weight:700;color:#6B635A}
.meter .b{flex:1;height:7px;background:#F1E9DC;border-radius:99px;overflow:hidden}.meter i{display:block;height:100%;background:linear-gradient(90deg,#E8A06A,#C96234)}
.note{font-size:11.5px;color:#8B8378;margin-top:8px;line-height:1.5}
</style></head><body>
<div class="tabs" id="tabs"></div><div id="view"></div><div class="p" id="p"></div>
<script>
var D=__DATA__;
function esc(s){var d=document.createElement('div');d.textContent=String(s==null?"":s);return d.innerHTML}
var NS="http://www.w3.org/2000/svg";
function tier(s){return s>=75?"Puncak peluang":s>=55?"Stabil":"Fase belajar"}
function panel(title,sub,skor,paras,foot){
  var h='<h3>'+esc(title)+'</h3><div class="sub">'+esc(sub)+'</div>';
  if(skor!=null)h+='<div class="meter"><span>Level energi '+skor+' · '+tier(skor)+'</span><div class="b"><i style="width:'+skor+'%"></i></div></div>';
  paras.forEach(function(t){h+='<p>'+esc(t)+'</p>'});
  h+='<div class="note">'+esc(foot||"Level energi adalah interpretasi kami dari makna tiap kode, bukan prediksi pasti.")+'</div>';
  document.getElementById('p').innerHTML=h;
}
var tab=null;
function setTab(t){tab=t;var tb=document.getElementById('tabs');tb.innerHTML="";
  var names=D.system==="Matrix Destiny"?[["roda","Roda Takdir"],["grafik","Grafik Usia 20-60"]]:[["pin","Grafik Usia 20-60"]];
  names.forEach(function(n){var b=document.createElement('button');b.textContent=n[1];if(n[0]===t)b.className="on";b.onclick=function(){setTab(n[0])};tb.appendChild(b)});
  if(names.length<2)tb.style.display="none";
  (t==="roda"?roda:t==="grafik"?grafik:pin)();}
function roda(){
  var T=D.roda.titik,cx=160,cy=160,R=112,h='<div class="hint">Ketuk satu titik untuk membaca maknanya.</div><svg viewBox="0 0 320 320" id="sv">';
  var pts=T.map(function(t,i){var a=Math.PI+i*Math.PI/4;return[cx+R*Math.cos(a),cy+R*Math.sin(a)]});
  h+='<polygon class="oct" points="'+pts.map(function(p){return p[0].toFixed(1)+","+p[1].toFixed(1)}).join(" ")+'"/>';
  pts.forEach(function(p){h+='<line class="spoke" x1="'+cx+'" y1="'+cy+'" x2="'+p[0].toFixed(1)+'" y2="'+p[1].toFixed(1)+'"/>'});
  T.forEach(function(t,i){var p=pts[i],a=Math.PI+i*Math.PI/4,lx=cx+(R+34)*Math.cos(a),ly=cy+(R+34)*Math.sin(a);
    h+='<g class="node" data-i="'+i+'"><circle cx="'+p[0].toFixed(1)+'" cy="'+p[1].toFixed(1)+'" r="19"/><text class="n" x="'+p[0].toFixed(1)+'" y="'+p[1].toFixed(1)+'">'+t.arcana+'</text></g>';
    h+='<text class="lab" x="'+lx.toFixed(1)+'" y="'+(ly-2).toFixed(1)+'">'+t.kode+'</text><text class="age" x="'+lx.toFixed(1)+'" y="'+(ly+11).toFixed(1)+'">usia '+t.usia+'</text>';});
  h+='<g class="node core" data-i="c"><circle cx="'+cx+'" cy="'+cy+'" r="24"/><text class="n" x="'+cx+'" y="'+cy+'">'+D.roda.inti.arcana+'</text></g></svg>';
  document.getElementById('view').innerHTML=h;
  var nodes=document.querySelectorAll('.node');
  function pick(k){nodes.forEach(function(n){n.classList.toggle('on',n.getAttribute('data-i')===String(k))});
    var t=k==="c"?D.roda.inti:T[k];var u=t.usia==null?"Inti jiwa, sepanjang hidup":"Titik "+t.kode+" · usia "+t.usia;
    panel(t.nama+" (kode "+t.arcana+")",u+" · "+t.titik,t.skor,["Kekuatan yang bisa kamu pakai: "+t.kuat,"Yang perlu dijaga: "+t.waspada]);}
  nodes.forEach(function(n){n.onclick=function(){var k=n.getAttribute('data-i');pick(k==="c"?"c":+k)}});
  pick("c");
}
function grafik(){
  var P=D.grafik.titik,S=D.grafik.segmen,W=640,H=250,x0=50,x1=610,yt=30,yb=200;
  function X(a){return x0+(a-20)/40*(x1-x0)}function Y(s){return yb-(s-30)/70*(yb-yt)}
  var h='<div class="hint">Ketuk titik atau area di antaranya untuk membaca fase hidupmu.</div><svg viewBox="0 0 '+W+' '+H+'">';
  [55,75].forEach(function(v){h+='<line class="gl" x1="'+x0+'" x2="'+x1+'" y1="'+Y(v)+'" y2="'+Y(v)+'"/><text class="gt" x="4" y="'+(Y(v)+3)+'">'+v+'</text>'});
  S.forEach(function(s,i){h+='<rect class="seg" data-s="'+i+'" x="'+X(s.dari)+'" y="'+yt+'" width="'+(X(s.sampai)-X(s.dari))+'" height="'+(yb-yt)+'"/>'});
  var line=P.map(function(p){return X(p.usia)+","+Y(p.skor)}).join(" ");
  h+='<polygon class="area" points="'+X(20)+','+yb+' '+line+' '+X(60)+','+yb+'"/><polyline class="ln" points="'+line+'"/>';
  if(D.age>=20&&D.age<=60){var xa=X(D.age);h+='<line class="now" x1="'+xa+'" x2="'+xa+'" y1="'+(yt-8)+'" y2="'+yb+'"/><text class="nowt" x="'+xa+'" y="'+(yt-14)+'">Kamu di sini (usia '+D.age+')</text>'}
  P.forEach(function(p,i){h+='<circle class="dot" data-p="'+i+'" cx="'+X(p.usia)+'" cy="'+Y(p.skor)+'" r="9"/><text class="xt" x="'+X(p.usia)+'" y="'+(yb+22)+'">'+p.usia+'</text><text class="gt" style="text-anchor:middle" x="'+X(p.usia)+'" y="'+(Y(p.skor)-15)+'">'+p.arcana+'</text>'});
  h+='</svg>';document.getElementById('view').innerHTML=h;
  var dots=document.querySelectorAll('.dot'),segs=document.querySelectorAll('.seg');
  function clear(){dots.forEach(function(d){d.classList.remove('on')});segs.forEach(function(d){d.classList.remove('on')})}
  function pickP(i){clear();dots[i].classList.add('on');var p=P[i];panel(p.nama+" (kode "+p.arcana+")","Titik usia "+p.usia,p.skor,p.teks)}
  function pickS(i){clear();segs[i].classList.add('on');var s=S[i];panel("Usia "+s.dari+" sampai "+s.sampai,"Fase di antara dua titik",s.skor,s.teks)}
  dots.forEach(function(d){d.onclick=function(){pickP(+d.getAttribute('data-p'))}});
  segs.forEach(function(d){d.onclick=function(){pickS(+d.getAttribute('data-s'))}});
  var si=0;for(var i=0;i<S.length;i++){if(D.age>=S[i].dari&&D.age<S[i].sampai)si=i}pickS(si);
}
function pin(){
  var P=D.pin,W=640,H=250,x0=20,x1=620,yt=34,yb=200;
  function X(a){return x0+(a-20)/40*(x1-x0)}function Hh(s){return (s-30)/70*(yb-yt)}
  var h='<div class="hint">Ketuk satu periode Pinnacle untuk membaca fasenya.</div><svg viewBox="0 0 '+W+' '+H+'">';
  var rects=[];
  P.forEach(function(p,i){var a=Math.max(p.usia_awal,20),b=p.usia_akhir==null?60:Math.min(p.usia_akhir+1,60);if(a>=60||b<=20||b<=a)return;
    var hh=Hh(p.skor),col=p.skor>=75?"#6E8F5E":p.skor>=55?"#E8A67F":"#C0564B";
    h+='<rect class="pn" data-i="'+i+'" x="'+X(a)+'" y="'+(yb-hh)+'" width="'+(X(b)-X(a)-3)+'" height="'+hh+'" rx="8" fill="'+col+'"/><text class="xt" style="fill:#fff;font-size:15px" x="'+(X(a)+(X(b)-X(a)-3)/2)+'" y="'+(yb-hh/2+5)+'">'+p.angka+'</text><text class="gt" style="text-anchor:middle" x="'+(X(a)+(X(b)-X(a)-3)/2)+'" y="'+(yb+16)+'">'+(a===20&&p.usia_awal<20?"":"")+p.usia_awal+(p.usia_akhir==null?"+":"-"+p.usia_akhir)+'</text>'});
  if(D.age>=20&&D.age<=60){var xa=X(D.age);h+='<line class="now" x1="'+xa+'" x2="'+xa+'" y1="'+(yt-8)+'" y2="'+yb+'"/><text class="nowt" x="'+xa+'" y="'+(yt-14)+'">Kamu di sini (usia '+D.age+')</text>'}
  h+='</svg>';document.getElementById('view').innerHTML=h;
  var el=document.querySelectorAll('.pn');
  function pick(i){el.forEach(function(e){e.classList.toggle('on',e.getAttribute('data-i')===String(i))});var p=P[i];
    panel("Pinnacle "+p.no+": angka "+p.angka,"Usia "+p.usia_awal+(p.usia_akhir==null?" seterusnya":" sampai "+p.usia_akhir)+" · "+p.tema,p.skor,p.teks)}
  el.forEach(function(e){e.onclick=function(){pick(+e.getAttribute('data-i'))}});
  var pi=0;P.forEach(function(p,i){if(D.age>=p.usia_awal&&(p.usia_akhir==null||D.age<=p.usia_akhir))pi=i});pick(pi);
}
setTab(D.system==="Matrix Destiny"?"roda":"pin");
</script></body></html>"""


def render(system, tgl, height=640):
    if system not in SYSTEMS or not isinstance(tgl, date):
        return False
    data = json.dumps(payload(system, tgl), ensure_ascii=False).replace("</", "<\\/")
    components.html(_HTML.replace("__DATA__", data), height=height, scrolling=True)
    return True
