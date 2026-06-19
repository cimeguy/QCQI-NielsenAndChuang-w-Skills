#!/usr/bin/env python3
"""QCQI skill_set -> static HTML generator (stdlib only).

For each skill directory it renders SKILL.md + chapters/* + glossary/patterns/cheatsheet
into a single self-contained `<skill>/index.html` (offline, no CDN). An optional
`_viz/<skill>.html` fragment is injected into a top "可视化" panel. A root
`index.html` hub links all skills.
"""
import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
VIZ_DIR = ROOT / "_viz"

SKILLS = [
    ("qcqi-ch01-intro", "第一章 · 量子计算简介"),
    ("qcqi-ch02-linalg-qm", "第二章 · 线性代数与量子力学"),
    ("qcqi-ch04-circuits", "第四章 · 量子线路与模拟"),
    ("qcqi-ch05-qft", "第五章 · QFT 与 Shor"),
    ("qcqi-ch06-search", "第六章 · 量子搜索 (Grover)"),
    ("qcqi-ch08-quantum-channels", "第八章补充 · 量子信道"),
    ("qcqi-key-points", "各章关键知识点汇总"),
]

# ----------------------------------------------------------------------------
# Minimal Markdown -> HTML (handles the subset used in these notes)
# ----------------------------------------------------------------------------

def strip_frontmatter(text):
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            nl = text.find("\n", end + 1)
            text = text[nl + 1:] if nl != -1 else ""
    # drop leading HTML comments (argument-hint etc.)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    return text.lstrip("\n")


def inline(md, link_map):
    # escape first, then re-introduce markup
    s = html.escape(md, quote=False)
    # links [text](url)
    def link_sub(m):
        txt, url = m.group(1), m.group(2)
        url = link_map.get(url.split("#")[0], url) if url.endswith(".md") or ".md#" in url else url
        # rewrite intra-skill .md links to anchors
        base = url.split("/")[-1]
        if base.endswith(".md") or ".md" in base:
            key = base.split("#")[0]
            url = link_map.get(key, "#")
        ext = ' target="_blank" rel="noopener"' if url.startswith("http") else ""
        return f'<a href="{url}"{ext}>{txt}</a>'
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", link_sub, s)
    # bold **x**
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    # inline code `x`
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    return s


def protect_math(text, store):
    """Pull $$...$$ and $...$ spans out before markdown processing."""
    def repl(m):
        store.append(m.group(0))
        return "%d" % (len(store) - 1)
    text = re.sub(r"\$\$.+?\$\$", repl, text, flags=re.DOTALL)
    text = re.sub(r"\$[^$\n]+?\$", repl, text)
    return text


def restore_math(text, store):
    def repl(m):
        raw = store[int(m.group(1))]
        return raw.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return re.sub("(\\d+)", repl, text)


def md_to_html(md, link_map):
    math_store = []
    md = protect_math(md, math_store)
    lines = md.split("\n")
    out = []
    i = 0
    n = len(lines)

    def flush_para(buf):
        if buf:
            out.append("<p>" + inline(" ".join(buf), link_map) + "</p>")
            buf.clear()

    para = []
    while i < n:
        line = lines[i]
        stripped = line.strip()

        # fenced code
        if stripped.startswith("```"):
            flush_para(para)
            lang = stripped[3:].strip()
            code = []
            i += 1
            while i < n and not lines[i].strip().startswith("```"):
                code.append(lines[i])
                i += 1
            i += 1
            out.append('<pre><code>' + html.escape("\n".join(code)) + "</code></pre>")
            continue

        # blank
        if not stripped:
            flush_para(para)
            i += 1
            continue

        # hr / frontmatter sep
        if re.fullmatch(r"-{3,}", stripped):
            flush_para(para)
            out.append("<hr>")
            i += 1
            continue

        # headings
        m = re.match(r"(#{1,6})\s+(.*)", stripped)
        if m:
            flush_para(para)
            level = len(m.group(1))
            out.append(f"<h{level}>" + inline(m.group(2), link_map) + f"</h{level}>")
            i += 1
            continue

        # blockquote
        if stripped.startswith(">"):
            flush_para(para)
            quote = []
            while i < n and lines[i].strip().startswith(">"):
                quote.append(lines[i].strip()[1:].strip())
                i += 1
            out.append("<blockquote>" + inline(" ".join(quote), link_map) + "</blockquote>")
            continue

        # table (line has | and next line is separator)
        if "|" in line and i + 1 < n and re.match(r"^\s*\|?[\s:|-]+\|[\s:|-]*$", lines[i + 1]):
            flush_para(para)
            def cells(row):
                row = row.strip()
                row = row[1:] if row.startswith("|") else row
                row = row[:-1] if row.endswith("|") else row
                return [c.strip() for c in row.split("|")]
            header = cells(line)
            i += 2
            body = []
            while i < n and "|" in lines[i] and lines[i].strip():
                body.append(cells(lines[i]))
                i += 1
            t = ["<table><thead><tr>"]
            t += [f"<th>{inline(c, link_map)}</th>" for c in header]
            t.append("</tr></thead><tbody>")
            for r in body:
                t.append("<tr>" + "".join(f"<td>{inline(c, link_map)}</td>" for c in r) + "</tr>")
            t.append("</tbody></table>")
            out.append("".join(t))
            continue

        # lists (ordered / unordered, one nesting level via indent)
        if re.match(r"^\s*([-*]|\d+\.)\s+", line):
            flush_para(para)
            out.append(parse_list(lines, i, n, link_map, out))
            i = parse_list.last
            continue

        # paragraph text
        para.append(stripped)
        i += 1

    flush_para(para)
    return restore_math("\n".join(out), math_store)


def parse_list(lines, i, n, link_map, _out):
    def indent(s):
        return len(s) - len(s.lstrip(" "))

    base = indent(lines[i])
    ordered = bool(re.match(r"^\s*\d+\.\s+", lines[i]))
    tag = "ol" if ordered else "ul"
    items = []
    while i < n:
        line = lines[i]
        if not line.strip():
            # allow blank inside list only if next is deeper/same list item
            nxt = lines[i + 1] if i + 1 < n else ""
            if re.match(r"^\s*([-*]|\d+\.)\s+", nxt) and indent(nxt) >= base:
                i += 1
                continue
            break
        m = re.match(r"^(\s*)([-*]|\d+\.)\s+(.*)", line)
        if not m:
            break
        ind = len(m.group(1))
        if ind < base:
            break
        if ind > base:
            # nested
            sub = parse_list(lines, i, n, link_map, _out)
            i = parse_list.last
            if items:
                items[-1] = items[-1] + sub
            continue
        items.append("<li>" + inline(m.group(3), link_map) + "</li>")
        i += 1
    parse_list.last = i
    return f"<{tag}>" + "".join(f"<li>{c[4:-5]}</li>" if False else c for c in items) + f"</{tag}>"


parse_list.last = 0

# ----------------------------------------------------------------------------
# Section assembly
# ----------------------------------------------------------------------------

def anchor_for(filename):
    base = filename.rsplit("/", 1)[-1].replace(".md", "")
    return "sec-" + re.sub(r"[^a-zA-Z0-9]+", "-", base).strip("-").lower()


def collect_sections(skill_dir):
    """Return ordered list of (anchor, nav_label, source_filename, md_text)."""
    sections = []
    link_map = {}

    def add(fname, label):
        p = skill_dir / fname
        if not p.exists():
            return
        anchor = "top" if fname == "SKILL.md" else anchor_for(fname)
        link_map[fname.rsplit("/", 1)[-1]] = "#" + anchor
        sections.append((anchor, label, fname, strip_frontmatter(p.read_text(encoding="utf-8"))))

    add("SKILL.md", "概览")
    chap_dir = skill_dir / "chapters"
    if chap_dir.exists():
        for ch in sorted(chap_dir.glob("*.md")):
            rel = f"chapters/{ch.name}"
            anchor = anchor_for(ch.name)
            link_map[ch.name] = "#" + anchor
            # nav label = first heading
            txt = strip_frontmatter(ch.read_text(encoding="utf-8"))
            mt = re.search(r"^#\s+(.*)$", txt, flags=re.MULTILINE)
            label = mt.group(1).strip() if mt else ch.stem
            sections.append((anchor, label, rel, txt))
    for fname, label in [("glossary.md", "术语表"), ("patterns.md", "技巧/构件"), ("cheatsheet.md", "速查表")]:
        add(fname, label)
    return sections, link_map

# ----------------------------------------------------------------------------
# HTML templates
# ----------------------------------------------------------------------------

CSS = """
:root{--bg:#0f1419;--panel:#1a2330;--panel2:#141c27;--fg:#e6edf3;--muted:#8b98a9;
--accent:#5ab0ff;--accent2:#9d7bff;--border:#26313f;--code:#1e2a38;--th:#1d2733;}
[data-theme=light]{--bg:#f6f8fa;--panel:#fff;--panel2:#f0f3f7;--fg:#1f2733;--muted:#5a6b7d;
--accent:#0969da;--accent2:#7b4bff;--border:#d6dee7;--code:#eef2f6;--th:#eaf0f6;}
*{box-sizing:border-box}
body{margin:0;font-family:-apple-system,"PingFang SC","Microsoft YaHei",Segoe UI,system-ui,sans-serif;
background:var(--bg);color:var(--fg);line-height:1.7;font-size:15px}
a{color:var(--accent);text-decoration:none}a:hover{text-decoration:underline}
.layout{display:flex;min-height:100vh}
.sidebar{width:280px;flex:0 0 280px;background:var(--panel2);border-right:1px solid var(--border);
position:sticky;top:0;height:100vh;overflow-y:auto;padding:20px 0}
.sidebar h2{font-size:14px;margin:0 18px 6px;color:var(--muted);font-weight:600;letter-spacing:.04em}
.brand{padding:0 18px 14px;border-bottom:1px solid var(--border);margin-bottom:12px}
.brand .t{font-size:17px;font-weight:700}
.brand .s{font-size:12px;color:var(--muted);margin-top:3px}
.search{margin:0 14px 12px;width:calc(100% - 28px);padding:8px 10px;border-radius:8px;
border:1px solid var(--border);background:var(--panel);color:var(--fg);font-size:13px}
.nav a{display:block;padding:6px 18px;color:var(--fg);font-size:13.5px;border-left:3px solid transparent}
.nav a:hover{background:var(--panel);text-decoration:none}
.nav a.active{border-left-color:var(--accent);background:var(--panel);color:var(--accent)}
.nav a.hidden{display:none}
.main{flex:1;min-width:0;padding:34px 48px 80px;max-width:1000px}
.topbar{display:flex;align-items:center;gap:14px;margin-bottom:8px}
.topbar .home{font-size:13px;color:var(--muted)}
.toggle{margin-left:auto;cursor:pointer;border:1px solid var(--border);background:var(--panel);
color:var(--fg);border-radius:8px;padding:6px 12px;font-size:13px}
section{scroll-margin-top:20px;padding:18px 0;border-bottom:1px solid var(--border)}
h1{font-size:26px;margin:.2em 0 .5em}h2{font-size:20px;margin:1.2em 0 .5em;color:var(--accent)}
h3{font-size:16.5px;margin:1em 0 .4em;color:var(--accent2)}h4{font-size:15px;margin:.9em 0 .3em}
code{background:var(--code);padding:1.5px 6px;border-radius:5px;font-size:.9em;
font-family:"SF Mono",Menlo,Consolas,monospace}
pre{background:var(--code);padding:14px 16px;border-radius:10px;overflow-x:auto;border:1px solid var(--border)}
pre code{background:none;padding:0}
table{border-collapse:collapse;width:100%;margin:12px 0;font-size:13.5px;overflow:hidden;border-radius:8px}
th,td{border:1px solid var(--border);padding:7px 11px;text-align:left;vertical-align:top}
th{background:var(--th);font-weight:600}
tr:nth-child(even) td{background:rgba(127,127,127,.05)}
blockquote{border-left:4px solid var(--accent2);margin:10px 0;padding:6px 16px;color:var(--muted);
background:var(--panel);border-radius:0 8px 8px 0}
ul,ol{padding-left:24px}li{margin:3px 0}
hr{border:none;border-top:1px dashed var(--border);margin:16px 0}
.viz{background:var(--panel);border:1px solid var(--border);border-radius:14px;padding:20px 22px;margin:14px 0 26px}
.viz h2{margin-top:0;color:var(--accent)}
.viz svg{max-width:100%;height:auto}
.badge{display:inline-block;background:var(--accent);color:#fff;border-radius:6px;padding:2px 9px;font-size:12px;font-weight:600}
@media(max-width:820px){.sidebar{display:none}.main{padding:24px 18px}}
"""

JS = """
const toggle=document.getElementById('themeToggle');
const saved=localStorage.getItem('qcqi-theme');
if(saved)document.documentElement.setAttribute('data-theme',saved);
toggle&&toggle.addEventListener('click',()=>{
 const cur=document.documentElement.getAttribute('data-theme')==='light'?'':'light';
 document.documentElement.setAttribute('data-theme',cur);
 localStorage.setItem('qcqi-theme',cur);
});
const links=[...document.querySelectorAll('.nav a')];
const secs=[...document.querySelectorAll('section[id]')];
const obs=new IntersectionObserver(es=>{es.forEach(e=>{if(e.isIntersecting){
 links.forEach(l=>l.classList.toggle('active',l.getAttribute('href')==='#'+e.target.id));}})},
 {rootMargin:'-10% 0px -80% 0px'});
secs.forEach(s=>obs.observe(s));
const box=document.getElementById('search');
box&&box.addEventListener('input',()=>{const q=box.value.trim().toLowerCase();
 links.forEach(l=>l.classList.toggle('hidden',q&&!l.textContent.toLowerCase().includes(q)));});
"""


MATHJAX_CONFIG = r"""
window.MathJax={
 tex:{
  inlineMath:[['$','$'],['\\(','\\)']],
  displayMath:[['$$','$$'],['\\[','\\]']],
  macros:{
   ket:['{\\lvert #1\\rangle}',1],
   bra:['{\\langle #1\\rvert}',1],
   braket:['{\\langle #1\\vert #2\\rangle}',2],
   ketbra:['{\\lvert #1\\rangle\\langle #2\\rvert}',2],
   Tr:'{\\operatorname{Tr}}',
   tr:'{\\operatorname{tr}}'
  }
 },
 svg:{fontCache:'global'},
 options:{skipHtmlTags:['script','style','textarea','pre','code'],ignoreHtmlClass:'viz'}
};
"""


def page_html(title, sidebar, body, mathjax_src="../vendor/tex-svg.js"):
    return f"""<!DOCTYPE html>
<html lang="zh-CN" data-theme="">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<style>{CSS}</style>
<script>{MATHJAX_CONFIG}</script>
<script src="{mathjax_src}" id="MathJax-script" async></script>
</head>
<body>
<div class="layout">
{sidebar}
<main class="main">
{body}
</main>
</div>
<script>{JS}</script>
</body>
</html>"""


def build_skill(slug, label):
    skill_dir = ROOT / slug
    sections, link_map = collect_sections(skill_dir)

    nav = ['<aside class="sidebar">',
           f'<div class="brand"><div class="t">QCQI 知识库</div><div class="s">{html.escape(label)}</div></div>',
           '<input class="search" id="search" placeholder="过滤小节…">',
           '<nav class="nav">',
           '<a href="index.html" style="color:var(--muted)">← 返回门户</a>',
           '<a href="explained.html" style="color:var(--muted)">🗣️ 看人话版</a>',
           '<a href="student.html" style="color:var(--muted)">🎓 看大学生版</a>']
    viz_file = VIZ_DIR / f"{slug}.html"
    if viz_file.exists():
        nav.append('<a href="#viz">可视化图示</a>')
    for anchor, lab, _, _ in sections:
        nav.append(f'<a href="#{anchor}">{html.escape(lab)}</a>')
    nav.append("</nav></aside>")

    body = ['<div class="topbar"><span class="badge">QCQI</span>'
            f'<span class="home">{html.escape(label)}</span>'
            '<button class="toggle" id="themeToggle">🌓 深/浅色</button></div>']

    if viz_file.exists():
        body.append(f'<section id="viz" class="viz"><h2>可视化图示</h2>{viz_file.read_text(encoding="utf-8")}</section>')

    for anchor, _, fname, md in sections:
        body.append(f'<section id="{anchor}">{md_to_html(md, link_map)}</section>')

    out = page_html(f"{label} · QCQI 知识库", "\n".join(nav), "\n".join(body))
    (skill_dir / "index.html").write_text(out, encoding="utf-8")
    return len(sections), viz_file.exists()


def build_hub():
    cards = []
    for slug, label in SKILLS:
        sec_count = len(collect_sections(ROOT / slug)[0])
        cards.append(
            f'<a class="card" href="{slug}/index.html"><div class="ct">{html.escape(label)}</div>'
            f'<div class="cs">{html.escape(slug)} · {sec_count} 节</div></a>')
    hub_css = """
    body{margin:0;min-height:100vh;background:radial-gradient(1200px 600px at 70% -10%,#1b2740,#0f1419);
    color:#e6edf3;font-family:-apple-system,"PingFang SC","Microsoft YaHei",system-ui,sans-serif}
    .wrap{max-width:980px;margin:0 auto;padding:70px 24px}
    h1{font-size:34px;margin:0 0 6px}.sub{color:#8b98a9;margin-bottom:36px;font-size:15px;line-height:1.7}
    .grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:18px}
    .card{display:block;background:#1a2330;border:1px solid #26313f;border-radius:16px;padding:22px 22px;
    color:#e6edf3;text-decoration:none;transition:.18s}
    .card:hover{transform:translateY(-3px);border-color:#5ab0ff;box-shadow:0 10px 30px rgba(0,0,0,.35)}
    .ct{font-size:18px;font-weight:700;margin-bottom:8px}.cs{color:#8b98a9;font-size:13px}
    .foot{margin-top:40px;color:#8b98a9;font-size:13px;line-height:1.8}
    """
    body = f"""<div class="wrap">
<h1>QCQI 知识库 · 可视化门户</h1>
<div class="sub">Nielsen &amp; Chuang《量子计算与量子信息》中文学习笔记生成的 Agent 技能集。点击任意章节进入可浏览、可视化的知识页面。<br>
看不懂晦涩的公式？换个版本：<a href="explained.html" style="color:#5ab0ff">🗣️ 人话版门户</a>（程序员友好）；数学基础还不牢？<a href="student.html" style="color:#5ab0ff">🎓 大学生版门户</a>（从零补线代/概率）。</div>
<div class="grid">{''.join(cards)}</div>
<div class="foot">每页含小节导航、客户端搜索、深/浅色切换与领域可视化图示。<br>
源自 <code>skill_set/</code> 下的 Agent Skills，由 <code>build_html.py</code> 静态生成（纯标准库，离线可用）。</div>
</div>"""
    out = f"""<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>QCQI 知识库 · 门户</title><style>{hub_css}</style></head>
<body>{body}</body></html>"""
    (ROOT / "index.html").write_text(out, encoding="utf-8")


def main():
    VIZ_DIR.mkdir(exist_ok=True)
    print("Building skill pages…")
    for slug, label in SKILLS:
        nsec, has_viz = build_skill(slug, label)
        viz = "✓viz" if has_viz else "—"
        print(f"  {slug:32s} {nsec:2d} sections  {viz}")
    build_hub()
    print("Hub: index.html")
    print("Done.")


if __name__ == "__main__":
    main()
