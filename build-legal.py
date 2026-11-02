"""Builds privacy.html and terms.html from the Markdown sources in the site's own style.
Run after editing privacy-policy.md or terms-of-use.md:  python3 build-legal.py   (needs: pip install markdown)"""
import markdown

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · HowYouDoin</title>
<meta name="description" content="{title} for the HowYouDoin app.">
<link rel="canonical" href="https://howyoudoin.app/{file}">
<link rel="icon" href="img/logo.svg" type="image/svg+xml">
<style>
  @font-face {{ font-family: "Manrope"; src: url("fonts/manrope.woff2") format("woff2"); font-weight: 200 800; font-display: swap; }}
  :root {{ --blue: #276BFF; --violet: #7138F5; --ink: #101936; --muted: #5A6283; --bg: #FAFAFE; --line: #DFE3F5; color-scheme: light; }}
  @media (prefers-color-scheme: dark) {{ :root {{ --ink: #EEF0FF; --muted: #A3A9C9; --bg: #0B1022; --line: #252E52; color-scheme: dark; }} }}
  * {{ box-sizing: border-box; }}
  body {{ margin: 0; background: var(--bg); color: var(--ink); font: 400 17px/1.65 "Manrope", ui-sans-serif, system-ui, sans-serif; }}
  .wrap {{ width: min(760px, 100% - 32px); margin-inline: auto; }}
  header {{ padding: 20px 0; border-bottom: 1px solid var(--line); }}
  header a {{ display: inline-flex; align-items: center; gap: 10px; text-decoration: none; color: inherit; font-weight: 800; font-size: 22px; letter-spacing: -.5px; }}
  header img {{ width: 34px; height: 34px; }}
  header span span {{ background: linear-gradient(135deg, var(--blue), var(--violet)); -webkit-background-clip: text; background-clip: text; color: transparent; }}
  main {{ padding: 40px 0 64px; }}
  h1 {{ font-size: clamp(30px, 5vw, 42px); line-height: 1.1; letter-spacing: -1px; margin: 0 0 8px; }}
  h2 {{ font-size: 22px; margin: 36px 0 10px; }}
  a {{ color: var(--blue); }}
  ul {{ padding-left: 22px; }}
  li {{ margin: 6px 0; }}
  footer {{ border-top: 1px solid var(--line); padding: 24px 0 40px; color: var(--muted); font-size: 14px; }}
  footer a {{ color: inherit; margin-right: 16px; }}
</style>
</head>
<body>
<header><div class="wrap"><a href="/"><img src="img/logo.svg" alt=""><span>howyou<span>doin</span></span></a></div></header>
<main class="wrap">
{body}
</main>
<footer><div class="wrap"><a href="/">Home</a><a href="privacy.html">Privacy policy</a><a href="terms.html">Terms of use</a></div></footer>
</body>
</html>
"""

for source, target, title in [("privacy-policy.md", "privacy.html", "Privacy policy"),
                              ("terms-of-use.md", "terms.html", "Terms of use")]:
    body = markdown.markdown(open(source, encoding="utf-8").read(), extensions=["extra", "sane_lists"])
    body = body.replace('href="privacy-policy.md"', 'href="privacy.html"').replace('href="terms-of-use.md"', 'href="terms.html"')
    open(target, "w", encoding="utf-8").write(PAGE.format(title=title, file=target, body=body))
    print("wrote", target)
