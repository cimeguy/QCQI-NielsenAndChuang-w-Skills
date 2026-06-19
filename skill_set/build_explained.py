#!/usr/bin/env python3
"""QCQI skill_set -> plain-language ("人话版") static HTML generator.

Renders each skill's `explained.md` (authored by the qcqi-explained team) into a
self-contained, programmer-friendly `<skill>/explained.html` (offline, local
MathJax). Callout blockquotes (💡 人话 / 🧠 类比 / ⚠️ 坑 / 🔑 记住) get colored
boxes. A root `explained.html` hub links all chapters. Reuses the math pipeline
(md_to_html + MathJax config) from build_html.py.
"""
import html
import re
from pathlib import Path

import build_html as bh

ROOT = Path(__file__).resolve().parent
SKILLS = bh.SKILLS

# callout marker -> css class
CALLOUTS = {"💡": "tip", "🧠": "analogy", "⚠️": "pitfall", "🔑": "key"}


def split_sections(md):
    """Return (page_title, [(section_title, body_md), ...]).

    The part after the first `# ` title but before the first `## ` becomes a
    leading "导读" section; each subsequent `## ` starts a new section.
    """
    md = bh.strip_frontmatter(md)
    lines = md.split("\n")
    title = None
    pre = []          # content before first ##
    sections = []
    cur_title = None
    cur_body = []
    for ln in lines:
        m1 = re.match(r"^#\s+(.*)", ln)
        m2 = re.match(r"^##\s+(.*)", ln)
        if m2:
            if cur_title is None:
                pre_body = "\n".join(cur_body).strip()
                if pre_body:
                    sections.append(("导读", pre_body))
            else:
                sections.append((cur_title, "\n".join(cur_body)))
            cur_title = m2.group(1).strip()
            cur_body = []
            continue
        if m1 and title is None and cur_title is None:
            title = m1.group(1).strip()
            continue
        cur_body.append(ln)
    if cur_title is not None:
        sections.append((cur_title, "\n".join(cur_body)))
    elif not sections:
        body = "\n".join(cur_body).strip()
        if body:
            sections.append(("正文", body))
    return title or "人话版", sections


def style_callouts(html_text):
    """Add a class to blockquotes that begin with a callout emoji."""
    def repl(m):
        emoji = m.group(1)
        cls = CALLOUTS.get(emoji, "")
        return f'<blockquote class="callout {cls}">{emoji}'
    # blockquote may start with whitespace before the emoji
    return re.sub(r"<blockquote>\s*(💡|🧠|⚠️|🔑)", repl, html_text)


CSS = """
:root{--bg:#fbf7f0;--panel:#fff;--panel2:#f3ede2;--fg:#2a2620;--muted:#7a7163;
--accent:#c2410c;--accent2:#7c3aed;--border:#e6ddcd;--code:#f1ebde;--th:#efe7d6;
--tip:#15803d;--tipbg:#ecfdf3;--analogy:#7c3aed;--analogybg:#f5f0ff;
--pitfall:#b45309;--pitfallbg:#fff7ed;--key:#0369a1;--keybg:#eff8ff;}
[data-theme=dark]{--bg:#15110c;--panel:#1f1a13;--panel2:#1a1610;--fg:#ece3d4;--muted:#9a8f7d;
--accent:#fb923c;--accent2:#c4b5fd;--border:#332b20;--code:#241e16;--th:#241e16;
--tipbg:#0f2417;--analogybg:#1c1430;--pitfallbg:#2a1d0c;--keybg:#0b1f2e;}
*{box-sizing:border-box}
body{margin:0;font-family:-apple-system,"PingFang SC","Microsoft YaHei",Segoe UI,system-ui,sans-serif;
background:var(--bg);color:var(--fg);line-height:1.85;font-size:16px}
a{color:var(--accent);text-decoration:none}a:hover{text-decoration:underline}
.layout{display:flex;min-height:100vh}
.sidebar{width:300px;flex:0 0 300px;background:var(--panel2);border-right:1px solid var(--border);
position:sticky;top:0;height:100vh;overflow-y:auto;padding:20px 0}
.sidebar h2{font-size:14px;margin:0 18px 6px;color:var(--muted);font-weight:600}
.brand{padding:0 18px 14px;border-bottom:1px solid var(--border);margin-bottom:12px}
.brand .t{font-size:18px;font-weight:800}
.brand .s{font-size:12.5px;color:var(--muted);margin-top:3px}
.search{margin:0 14px 12px;width:calc(100% - 28px);padding:9px 11px;border-radius:9px;
border:1px solid var(--border);background:var(--panel);color:var(--fg);font-size:13px}
.nav a{display:block;padding:6px 18px;color:var(--fg);font-size:13.5px;border-left:3px solid transparent}
.nav a:hover{background:var(--panel);text-decoration:none}
.nav a.active{border-left-color:var(--accent);background:var(--panel);color:var(--accent)}
.nav a.hidden{display:none}
.main{flex:1;min-width:0;padding:34px 52px 90px;max-width:920px}
.topbar{display:flex;align-items:center;gap:14px;margin-bottom:8px;flex-wrap:wrap}
.topbar .home{font-size:13px;color:var(--muted)}
.toggle{margin-left:auto;cursor:pointer;border:1px solid var(--border);background:var(--panel);
color:var(--fg);border-radius:8px;padding:6px 12px;font-size:13px}
section{scroll-margin-top:20px;padding:16px 0;border-bottom:1px solid var(--border)}
h1{font-size:28px;margin:.2em 0 .5em;line-height:1.3}
h2{font-size:21px;margin:1.1em 0 .5em;color:var(--accent)}
h3{font-size:17px;margin:1em 0 .4em;color:var(--accent2)}h4{font-size:15.5px;margin:.9em 0 .3em}
code{background:var(--code);padding:1.5px 6px;border-radius:5px;font-size:.9em;
font-family:"SF Mono",Menlo,Consolas,monospace}
pre{background:var(--code);padding:14px 16px;border-radius:10px;overflow-x:auto;border:1px solid var(--border)}
pre code{background:none;padding:0}
table{border-collapse:collapse;width:100%;margin:12px 0;font-size:14px;border-radius:8px;overflow:hidden}
th,td{border:1px solid var(--border);padding:7px 11px;text-align:left;vertical-align:top}
th{background:var(--th);font-weight:600}
ul,ol{padding-left:24px}li{margin:4px 0}
hr{border:none;border-top:1px dashed var(--border);margin:16px 0}
blockquote{border-left:4px solid var(--accent2);margin:12px 0;padding:8px 16px;color:var(--muted);
background:var(--panel);border-radius:0 8px 8px 0}
blockquote.callout{border-left-width:5px;border-radius:10px;padding:12px 18px;color:var(--fg);
margin:14px 0;font-size:15px}
blockquote.callout.tip{border-left-color:var(--tip);background:var(--tipbg)}
blockquote.callout.analogy{border-left-color:var(--analogy);background:var(--analogybg)}
blockquote.callout.pitfall{border-left-color:var(--pitfall);background:var(--pitfallbg)}
blockquote.callout.key{border-left-color:var(--key);background:var(--keybg);font-weight:600}
.legend{display:flex;gap:10px;flex-wrap:wrap;margin:6px 0 18px;font-size:12.5px;color:var(--muted)}
.legend span{background:var(--panel);border:1px solid var(--border);border-radius:20px;padding:3px 11px}
.badge{display:inline-block;background:var(--accent);color:#fff;border-radius:6px;padding:2px 9px;font-size:12px;font-weight:700}
@media(max-width:820px){.sidebar{display:none}.main{padding:24px 18px}}
"""


def page(title, sidebar, body):
    return f"""<!DOCTYPE html>
<html lang="zh-CN" data-theme="">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<style>{CSS}</style>
<script>{bh.MATHJAX_CONFIG}</script>
<script src="../vendor/tex-svg.js" id="MathJax-script" async></script>
</head>
<body>
<div class="layout">
{sidebar}
<main class="main">
{body}
</main>
</div>
<script>{bh.JS}</script>
</body>
</html>"""


def build_skill(slug, label):
    path = ROOT / slug / "explained.md"
    if not path.exists():
        return None
    page_title, sections = split_sections(path.read_text(encoding="utf-8"))

    nav = ['<aside class="sidebar">',
           f'<div class="brand"><div class="t">QCQI · 人话版</div><div class="s">{html.escape(label)}</div></div>',
           '<input class="search" id="search" placeholder="过滤小节…">',
           '<nav class="nav">',
           '<a href="../explained.html" style="color:var(--muted)">← 返回人话版门户</a>',
           f'<a href="index.html" style="color:var(--muted)">≡ 看公式精简版</a>']
    secs_html = []
    for idx, (stitle, body) in enumerate(sections):
        anchor = f"s{idx}"
        nav.append(f'<a href="#{anchor}">{html.escape(stitle)}</a>')
        inner = style_callouts(bh.md_to_html(("## " + stitle + "\n\n" + body) if idx else ("# " + page_title + "\n\n" + ("## " + stitle + "\n\n" + body)), {}))
        secs_html.append(f'<section id="{anchor}">{inner}</section>')
    nav.append("</nav></aside>")

    legend = ('<div class="legend"><span>💡 人话</span><span>🧠 类比</span>'
              '<span>⚠️ 坑</span><span>🔑 记住</span></div>')
    body = ['<div class="topbar"><span class="badge">人话版</span>'
            f'<span class="home">{html.escape(label)}</span>'
            '<button class="toggle" id="themeToggle">🌓 深/浅色</button></div>',
            legend]
    body.extend(secs_html)

    out = page(f"{label} · 人话版 · QCQI", "\n".join(nav), "\n".join(body))
    (ROOT / slug / "explained.html").write_text(out, encoding="utf-8")
    return len(sections)


HUB_CSS = """
body{margin:0;min-height:100vh;background:radial-gradient(1200px 600px at 70% -10%,#f6ad55,#fbf7f0);
color:#2a2620;font-family:-apple-system,"PingFang SC","Microsoft YaHei",system-ui,sans-serif}
.wrap{max-width:980px;margin:0 auto;padding:70px 24px}
h1{font-size:34px;margin:0 0 6px}.sub{color:#7a7163;margin-bottom:14px;font-size:15px;line-height:1.7}
.legend{display:flex;gap:10px;flex-wrap:wrap;margin-bottom:30px;font-size:13px;color:#7a7163}
.legend span{background:#fff;border:1px solid #e6ddcd;border-radius:20px;padding:4px 13px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:18px}
.card{display:block;background:#fff;border:1px solid #e6ddcd;border-radius:16px;padding:22px;
color:#2a2620;text-decoration:none;transition:.18s}
.card:hover{transform:translateY(-3px);border-color:#c2410c;box-shadow:0 10px 30px rgba(120,60,0,.18)}
.ct{font-size:18px;font-weight:800;margin-bottom:8px}.cs{color:#7a7163;font-size:13px}
.foot{margin-top:40px;color:#7a7163;font-size:13px;line-height:1.8}
.foot a{color:#c2410c}
"""


def build_hub(built):
    cards = []
    for slug, label in SKILLS:
        if slug not in built:
            continue
        cards.append(
            f'<a class="card" href="{slug}/explained.html"><div class="ct">{html.escape(label)}</div>'
            f'<div class="cs">{built[slug]} 节 · 人话讲解</div></a>')
    body = f"""<div class="wrap">
<h1>QCQI 知识库 · 人话版 🗣️</h1>
<div class="sub">把晦涩的量子数学翻译成「程序员能懂的人话」：每条公式都配直觉解释、编程类比与避坑提示。<br>
想看严谨的公式精简版？打开 <a href="index.html">公式版门户</a>。</div>
<div class="legend"><span>💡 人话＝公式在说什么</span><span>🧠 类比＝用代码/数据结构理解</span>
<span>⚠️ 坑＝容易误解的地方</span><span>🔑 记住＝一句话带走</span></div>
<div class="grid">{''.join(cards)}</div>
<div class="foot">面向计算机背景读者，无需物理基础。源自 <code>skill_set/&lt;skill&gt;/explained.md</code>，
由 <code>build_explained.py</code> 静态生成（纯标准库 + 内置 MathJax，离线可用）。</div>
</div>"""
    out = f"""<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>QCQI 人话版 · 门户</title><style>{HUB_CSS}</style></head>
<body>{body}</body></html>"""
    (ROOT / "explained.html").write_text(out, encoding="utf-8")


def main():
    print("Building plain-language (人话版) pages…")
    built = {}
    for slug, label in SKILLS:
        n = build_skill(slug, label)
        if n is None:
            print(f"  {slug:32s} — (no explained.md, skipped)")
        else:
            built[slug] = n
            print(f"  {slug:32s} {n:2d} sections  ✓")
    build_hub(built)
    print(f"Hub: explained.html  ({len(built)} skills)")
    print("Done.")


if __name__ == "__main__":
    main()
