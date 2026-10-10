"""
Kalender Energi (Daily Free, wajib login): kalender bulanan interaktif dengan tanda Bisnis / Konflik / Romansa (gratis).
Detail per hari (pesan, aksi, hindari, jam baik, angka, warna dari 4 sistem) = berbayar per bulan kalender.
Kalender digambar di iframe (HTML+JS, data JSON tertanam) supaya klik tanggal tanpa rerun Python.
"""

import html
import json
from datetime import date

import streamlit as st

from utils import resume as _resume
import streamlit.components.v1 as components
from content import pricing as P

from components import auth, form_kit
from components import close_confirm as cc
from components.daily_energy import _loaded, _need_tgl, _tgl_lahir
from components.dialog_bus import request_open
from content import energy_calendar as C
from engine.rotation import BULAN, today_wib

PRICE = P.CALENDAR_MONTH
_E = html.escape
MAX_AHEAD = 5  # bulan ke depan yang boleh dibuka


# ─────────────── state ───────────────
def _ym():
    ss = st.session_state
    t = today_wib()
    ym = ss.get("dh_cal_ym")
    if not ym or ym < (t.year, t.month):
        ym = ss.dh_cal_ym = (t.year, t.month)
    return ym


def _shift(n):
    y, m = _ym()
    m += n
    y += (m - 1) // 12
    m = (m - 1) % 12 + 1
    t = today_wib()
    lo, hi = (t.year, t.month), _add(t.year, t.month, MAX_AHEAD)
    if lo <= (y, m) <= hi:
        st.session_state.dh_cal_ym = (y, m)


def _add(y, m, n):
    m += n
    return (y + (m - 1) // 12, (m - 1) % 12 + 1)


def _paid_key(u, ym):
    return f"{u['email']}|{ym[0]}-{ym[1]:02d}"


def _is_paid(u, ym):
    return _paid_key(u, ym) in st.session_state.get("dh_cal_paid", set())


def _cb_pay():
    ss = st.session_state
    u = auth.current_user()
    ym = _ym()
    if not u or u.get("koin", 0) < PRICE or _is_paid(u, ym):
        return
    u["koin"] -= PRICE
    _resume.scanned("kalender")  # fitur lain yang kuesionernya tertunda di-reset
    ss.setdefault("dh_cal_paid", set()).add(_paid_key(u, ym))


# ─────────────── data ───────────────
@st.cache_data(show_spinner=False)
def _payload(tgl, y, m, paid):
    hari = C.bulan(tgl, y, m)
    out = []
    for h in hari:
        row = {"n": h["d"].day, "wd": h["d"].weekday(), "off": h["off"], "pd": h["pd"], "house": h["house"],
               "rel": h["rel"], "skor": h["skor"], "tier": h["tier"],
               "marks": [{"t": t, "lv": lv, "why": w} for t, lv, w in h["marks"]]}
        if paid:
            row["detail"] = C.detail_hari(tgl, h["d"])
            row["txt"] = _day_text(row, y, BULAN[m - 1])
        out.append(row)
    return {"y": y, "m": m, "bulan": BULAN[m - 1], "days": out, "today": today_wib().day if (y, m) == (today_wib().year, today_wib().month) else 0,
            "paid": paid, "sum": C.ringkas(hari)}


_HTML = r"""<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<style>
*{box-sizing:border-box}html,body{margin:0;background:transparent;font-family:'Plus Jakarta Sans',system-ui,sans-serif;color:#2D2A26}
.hd{display:grid;grid-template-columns:repeat(7,1fr);gap:6px;text-align:center;font-size:11px;font-weight:700;color:#8B8378;margin-bottom:6px}
.g{display:grid;grid-template-columns:repeat(7,1fr);gap:6px}
.c{aspect-ratio:1/0.6;min-height:50px;border:1px solid #E8E0D5;background:#fff;border-radius:12px;padding:5px 6px;cursor:pointer;display:flex;flex-direction:column;justify-content:space-between;transition:.15s;font:inherit;text-align:left}
.c:hover{border-color:#E0A67E;transform:translateY(-1px)}
.c.e{visibility:hidden}.c.t{box-shadow:0 0 0 2px #C96234 inset}.c.s{background:#FFF3E6;border-color:#C96234}
.c b{font-size:13px}.dots{display:flex;gap:3px;flex-wrap:wrap}.dots i{width:8px;height:8px;border-radius:50%;display:block}
.bisnis{background:#3F8F5E}.konflik{background:#C0392B}.romansa{background:#D6568B}
.dots i.lv-prima,.dots i.lv-tinggi,.dots i.lv-puncak{box-shadow:0 0 0 2px rgba(0,0,0,.12)}
.lg{display:flex;flex-wrap:wrap;gap:14px;margin:12px 2px;font-size:12px;color:#4A443D}
.lg span{display:flex;align-items:center;gap:6px}.lg i{width:10px;height:10px;border-radius:50%;display:inline-block}
.p{margin-top:6px;background:#fff;border:1px solid #E8E0D5;border-radius:16px;padding:16px}
.pt{font-family:'Playfair Display',Georgia,serif;font-size:19px;font-weight:700;margin:0}
.ps{font-size:12px;color:#8B8378;margin:2px 0 10px}
.ch{display:flex;flex-wrap:wrap;gap:6px;margin:8px 0}
.ch span{font-size:11.5px;font-weight:700;border-radius:99px;padding:4px 10px;color:#fff}
.m{border-left:3px solid;padding:6px 10px;margin:8px 0;font-size:12.5px;line-height:1.55;background:#FBF8F3;border-radius:0 10px 10px 0}
.sk{display:flex;align-items:center;gap:10px;margin:10px 0;font-size:12.5px}.sk .bar{flex:1;height:7px;background:#F1E9DC;border-radius:99px;overflow:hidden}
.sk .bar i{display:block;height:100%;background:linear-gradient(90deg,#E8A06A,#C96234)}
.tabs{display:flex;gap:6px;margin:14px 0 8px;flex-wrap:wrap}.tabs button{font:inherit;font-size:12px;font-weight:700;border:1px solid #E9C9A8;background:#fff;color:#C25E00;border-radius:99px;padding:5px 12px;cursor:pointer}
.tabs button.on{background:#C96234;color:#fff;border-color:#C96234}
.dt p{font-size:13px;line-height:1.65;margin:0 0 8px}.dt h4{font-size:12px;margin:10px 0 4px;color:#C96234;letter-spacing:.04em}
.dt ul{margin:0;padding-left:18px;font-size:12.5px;line-height:1.6}.meta{display:flex;flex-wrap:wrap;gap:8px;margin-top:10px;font-size:12px}
.meta span{background:#FFF6EA;border:1px solid #F0DFC4;border-radius:99px;padding:3px 10px}
.lock{position:relative;margin-top:12px;padding:14px;border-radius:12px;background:#FBF8F3;border:1px dashed #E0A67E;font-size:12.5px;color:#6B635A;line-height:1.55}
.lock .bl{filter:blur(4px);user-select:none;margin-top:8px}
.ok{background:#E9F1EA;border:1px solid #CFDFD2;border-radius:12px;padding:10px 14px;margin:12px 0 0;font-size:12.5px;color:#3F6B4D}
.bar{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:12px 0 4px}
.bar button{font:inherit;font-weight:700;font-size:14px;height:46px;border-radius:100px;cursor:pointer;transition:background .15s,color .15s}
.bar .o{background:#fff;border:1px solid #E9C9A8;color:#C25E00}.bar .o:hover{background:#FFF6EA}.bar .o.done{background:#EAF3EC;border-color:#BBD4C0;color:#4A6B53}
.bar .s{background:#C96234;border:1px solid #C96234;color:#fff;font-weight:600}.bar .s:hover{background:#B5552B}
</style></head><body>
<div class="hd"><span>Sen</span><span>Sel</span><span>Rab</span><span>Kam</span><span>Jum</span><span>Sab</span><span>Min</span></div>
<div class="g" id="g"></div>
<div class="lg"><span><i class="bisnis"></i>Hari bisnis baik</span><span><i class="konflik"></i>Rawan konflik</span><span><i class="romansa"></i>Peluang romansa</span><span>◉ titik bercincin = level kuat</span></div>
<div id="w"><div class="p" id="p"></div><div id="ft"></div></div>
<script>
var D=__DATA__;
var NAMA={bisnis:"Bisnis baik",konflik:"Rawan konflik",romansa:"Peluang romansa"},COL={bisnis:"#3F8F5E",konflik:"#C0392B",romansa:"#D6568B"};
var HARI=["Senin","Selasa","Rabu","Kamis","Jumat","Sabtu","Minggu"];
function esc(s){var d=document.createElement('div');d.textContent=String(s==null?"":s);return d.innerHTML}
var sel=D.today||((D.days.find(function(x){return x.marks.length})||D.days[0]).n),sys=null;
function grid(){var g=document.getElementById('g'),h="",lead=D.days[0].wd,i;
 for(i=0;i<lead;i++)h+='<div class="c e"></div>';
 D.days.forEach(function(x){var dots=x.marks.map(function(m){return '<i class="'+m.t+' lv-'+m.lv+'"></i>'}).join('');
  h+='<button class="c'+(x.n===D.today?' t':'')+(x.n===sel?' s':'')+'" data-n="'+x.n+'"><b>'+x.n+'</b><span class="dots">'+dots+'</span></button>'});
 g.innerHTML=h;[].forEach.call(g.querySelectorAll('.c:not(.e)'),function(b){b.onclick=function(){sel=+b.dataset.n;sys=null;grid();panel()}})}
function panel(){var x=D.days.filter(function(y){return y.n===sel})[0],p=document.getElementById('p');
 var h='<p class="pt">'+HARI[x.wd]+', '+x.n+' '+esc(D.bulan)+' '+D.y+'</p><p class="ps">Pejabat hari: '+esc(x.off.id)+' ('+esc(x.off.nama)+') · Personal day '+x.pd+' · Bulan di rumah '+x.house+' · Relasi shio: '+esc(x.rel)+'</p>';
 h+='<div class="ch">'+(x.marks.length?x.marks.map(function(m){return '<span style="background:'+COL[m.t]+'">'+NAMA[m.t]+' · '+esc(m.lv)+'</span>'}).join(''):'<span style="background:#B5ADA1">Hari biasa</span>')+'</div>';
 x.marks.forEach(function(m){h+='<div class="m" style="border-color:'+COL[m.t]+'">'+esc(m.why)+'</div>'});
 h+='<div class="m" style="border-color:#B5ADA1">'+esc(x.off.desc)+'</div>';
 h+='<div class="sk"><b>Skor energi '+x.skor+'</b><div class="bar"><i style="width:'+x.skor+'%"></i></div><span>'+esc(x.tier)+'</span></div>';
 if(D.paid&&x.detail){var ks=Object.keys(x.detail);if(!sys||!x.detail[sys])sys=ks[0];
  h+='<div class="tabs">'+ks.map(function(k){return '<button data-k="'+esc(k)+'" class="'+(k===sys?'on':'')+'">'+esc(k)+'</button>'}).join('')+'</div>';
  var d=x.detail[sys];h+='<div class="dt"><p>'+esc(d.pesan)+'</p>';
  if(d.aksi&&d.aksi.length)h+='<h4>YANG BISA DILAKUKAN</h4><ul>'+d.aksi.map(function(a){return '<li>'+esc(a)+'</li>'}).join('')+'</ul>';
  if(d.hindari&&d.hindari.length)h+='<h4>HINDARI</h4><ul>'+d.hindari.map(function(a){return '<li>'+esc(a)+'</li>'}).join('')+'</ul>';
  h+='<div class="meta"><span>Jam baik: '+esc(d.jam_baik)+'</span><span>Angka: '+esc([].concat(d.angka).join(', '))+'</span><span>Warna: '+esc(d.warna)+'</span></div></div>'}
 else if(!D.paid){h+='<div class="lock">🔒 <b>Detail per hari</b>: pesan, langkah, hal yang dihindari, jam baik, angka, dan warna dari Zodiak, Shio, Weton &amp; Numerologi terbuka setelah kamu membuka bulan ini di bawah.<div class="bl">Hari ini cocok untuk mengambil langkah yang sudah lama kamu pikirkan. Pilih jam baik dan fokus pada satu prioritas utama.</div></div>'}
 p.innerHTML=h;[].forEach.call(p.querySelectorAll('.tabs button'),function(b){b.onclick=function(){sys=b.dataset.k;panel()}})}
function fit(){try{var h=Math.ceil(document.getElementById('w').getBoundingClientRect().bottom+window.scrollY)+6;var f=window.frameElement;if(f){f.style.transition='height .3s ease';f.style.height=h+'px';f.setAttribute('height',h);var e=f.parentElement;for(var i=0;i<3&&e&&e.getAttribute('data-testid')!=='stVerticalBlock';i++){e.style.height=h+'px';e.style.minHeight=h+'px';e=e.parentElement}}}catch(e){}}
var _g=grid,_p=panel;grid=function(){_g();fit()};panel=function(){_p();fit()};
function foot(){var f=document.getElementById('ft');if(!D.paid){f.innerHTML='';return}
 f.innerHTML='<div class="ok">✅ Akses Terbuka · Detail bulan ini sudah terbuka. Klik tanggal lalu pilih sistem.</div><div class="bar"><button class="o" id="cp" type="button">📋 Salin Teks Hasil Seluruhnya</button><button class="s" id="dn" type="button">Selesai &amp; Tutup</button></div>';
 var cp=document.getElementById('cp');function ok(){cp.textContent='✓ Tersalin!';cp.className='o done';setTimeout(function(){cp.textContent='📋 Salin Teks Hasil Seluruhnya';cp.className='o'},2000)}
 function fb(t){var a=document.createElement('textarea');a.value=t;a.style.position='fixed';a.style.opacity=0;document.body.appendChild(a);a.select();try{document.execCommand('copy');ok()}catch(e){}document.body.removeChild(a)}
 cp.onclick=function(){var x=D.days.filter(function(y){return y.n===sel})[0],t=(x&&x.txt)||'';if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(t).then(ok,function(){fb(t)})}else{fb(t)}};
 document.getElementById('dn').onclick=function(){try{window.parent.document.querySelector('.st-key-dhcal_done_btn button').click()}catch(e){}}}
grid();panel();foot();window.addEventListener('resize',fit);fit();
</script></body></html>"""


def _calendar_html(data):
    js = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    return _HTML.replace("__DATA__", js)


def _day_text(d, y, bulan):
    """Ringkasan satu tanggal (4 sistem) untuk tombol salin."""
    hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"][d["wd"]]
    out = [f'Kalender Energi · {hari}, {d["n"]} {bulan} {y}', f'Skor energi {d["skor"]} ({d["tier"]})']
    for m in d["marks"]:
        out.append(f'- {m["why"]}')
    for sis, x in (d.get("detail") or {}).items():
        out.append(f"\n[{sis}]\n{x['pesan']}")
        if x.get("aksi"):
            out.append("Yang bisa dilakukan: " + "; ".join(x["aksi"]))
        if x.get("hindari"):
            out.append("Hindari: " + "; ".join(x["hindari"]))
        ang = x["angka"]
        ang = ", ".join(str(v) for v in ang) if isinstance(ang, (list, tuple)) else ang
        out.append(f"Jam baik: {x['jam_baik']} · Angka: {ang} · Warna: {x['warna']}")
    return "\n".join(out) + "\n#DestinyReveal"


def _cur_paid():
    u = auth.current_user()
    return bool(u and _is_paid(u, _ym()))


def _cb_cal_dismiss():
    """X: kalau bulan yang lagi dibuka sudah dibayar -> tanya konfirmasi dulu. Gratis -> langsung nutup."""
    cc.dismiss("kalender", _cur_paid())


# ─────────────── dialog ───────────────
@st.dialog("Kalender Energi", width="large", on_dismiss=_cb_cal_dismiss)
def kalender_dialog():
    if not form_kit.login_gate("kalender"):
        return
    ss = st.session_state
    u = auth.current_user()
    cc.wrap("kalender", _kalender_body, leave=None, icon="🗓️", title="Yakin Mau Tutup Halaman Ini?",
            text="Apakah kamu yakin ingin menutup halaman ini? Pastikan teks hasil sudah disalin.",
            tip=None, stay="Batal", go="Ya, Tutup")


def _kalender_body():
    ss = st.session_state
    u = auth.current_user()
    st.markdown('<div class="dh-step dh-step-cal"></div>' + ('<div class="dh-nodismiss"></div>' if _cur_paid() else '') +
                '<div class="dh-mn-title"><div class="dh-mn-ico">🗓️</div><div><div class="dh-mn-h">Kalender Energi</div>'
                '<div class="dh-mn-sub">Tanggal penting bulananmu dari Zodiak · Shio · Weton · Numerologi · BaZi</div></div></div>',
                unsafe_allow_html=True)
    tgl = _tgl_lahir()
    if not _need_tgl():
        return
    _loaded("kalender")
    ym = _ym()
    t = today_wib()
    with st.container(key="dhcal_nav"):
        c1, c2, c3 = st.columns([1, 3, 1], gap="small", vertical_alignment="center")
        with c1:
            st.button("‹ Sebelumnya", key="dhcal_prev", on_click=_shift, args=(-1,), disabled=ym <= (t.year, t.month),
                      use_container_width=True)
        with c2:
            st.markdown(f'<div class="dh-cal-month">{BULAN[ym[1] - 1]} {ym[0]}</div>', unsafe_allow_html=True)
        with c3:
            st.button("Berikutnya ›", key="dhcal_next", on_click=_shift, args=(1,), disabled=ym >= _add(t.year, t.month, MAX_AHEAD),
                      use_container_width=True)
    paid = _is_paid(u, ym)
    data = _payload(tgl, ym[0], ym[1], paid)
    s = data["sum"]
    st.markdown(f'<div class="dh-cal-sum"><span class="b">{s["bisnis"]} hari bisnis baik</span>'
                f'<span class="k">{s["konflik"]} rawan konflik</span><span class="r">{s["romansa"]} peluang romansa</span></div>',
                unsafe_allow_html=True)
    components.html(_calendar_html(data), height=620, scrolling=False)
    if paid:  # tombol salin + selesai ada di dalam kalender (satu iframe, tanpa gap); tombol ini dipicu dari sana
        with st.container(key="dhcal_hidden"):
            st.button("Selesai & Tutup", key="dhcal_done_btn", on_click=cc.cb_ask, args=("kalender",))
        return
    saldo = u.get("koin", 0)
    st.markdown(f'<div class="dh-cal-pay"><b>Buka detail {BULAN[ym[1] - 1]} {ym[0]}</b><span>Pesan, langkah, hindari, jam baik, '
                f'angka &amp; warna hoki untuk semua tanggal. Saldo kamu: <b>{saldo} ✨</b></span></div>', unsafe_allow_html=True)
    if saldo < PRICE:
        if st.button(f"Top-up Saldo (butuh {PRICE} ✨) →", key="dhcal_topup", type="primary", use_container_width=True):
            request_open("pricing_keep", dh_pr_tab="koin")
    else:
        st.button(f"🔓 Buka Detail Bulan Ini ({PRICE} ✨)", key="dhcal_pay", type="primary", use_container_width=True,
                  on_click=_cb_pay)


DIALOGS = {"kalender": kalender_dialog}
