<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>TRACE — Exposure Report</title>
<meta name="description" content="TRACE — breach & exposure check. See where your identifiers show up across breaches, stealer logs, and gaming profiles.">
<!-- link preview / social card -->
<meta property="og:type" content="website">
<meta property="og:site_name" content="TRACE">
<meta property="og:title" content="TRACE — Breach & Exposure Check">
<meta property="og:description" content="See where your identifiers show up across breaches, stealer logs, and gaming profiles.">
<meta property="og:image" content="https://supidaf.com/og-trace.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:url" content="https://supidaf.com/">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="TRACE — Breach & Exposure Check">
<meta name="twitter:description" content="See where your identifiers show up across breaches, stealer logs, and gaming profiles.">
<meta name="twitter:image" content="https://supidaf.com/og-trace.png">
<meta name="theme-color" content="#0b0d18">
<link rel="icon" type="image/png" href="/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<script src="https://identity.netlify.com/v1/netlify-identity-widget.js"></script>
<style>
  :root {
    --void: #04050b;
    --ink: #eef1fa;
    --muted: #9aa3bd;
    --faint: #6b7390;
    --glass: rgba(14,17,32,.55);
    --glass-2: rgba(20,24,44,.5);
    --line: rgba(255,255,255,.09);
    --line-strong: rgba(255,255,255,.16);
    --violet: #8b6dff;
    --violet-2: #a98bff;
    --cyan: #3fd6e6;
    --clear: #36d99a;
    --clear-bg: rgba(54,217,154,.12);
    --flag: #ff5d6c;
    --flag-bg: rgba(255,93,108,.13);
    --amber: #f5b94a;
    --mono: 'IBM Plex Mono', ui-monospace, monospace;
    --sans: 'IBM Plex Sans', system-ui, sans-serif;
    --display: 'Space Grotesk', system-ui, sans-serif;
  }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  html { -webkit-text-size-adjust: 100%; }
  body {
    background: var(--void);
    color: var(--ink);
    font-family: var(--sans);
    line-height: 1.5;
    min-height: 100vh;
    overflow-x: hidden;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-rendering: optimizeLegibility;
  }
  #galaxy { position: fixed; inset: 0; width: 100%; height: 100%; z-index: 0; display: block; }
  .vignette {
    position: fixed; inset: 0; z-index: 1; pointer-events: none;
    background: radial-gradient(ellipse 80% 60% at 50% 40%, transparent 30%, rgba(4,5,11,.55) 100%);
  }
  .wrap { position: relative; z-index: 2; width: 100%; max-width: 1040px; margin: 0 auto; padding: 30px 22px 90px; }

  .topbar { display: flex; align-items: center; justify-content: space-between; margin-bottom: 46px; }
  .brand { display: flex; align-items: center; gap: 11px; }
  .brand-name {
    font-family: var(--display); font-weight: 700; font-size: 18px; letter-spacing: 1.5px;
    background: linear-gradient(120deg, var(--ink), var(--violet-2));
    -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
  }
  .ver { font-family: var(--mono); font-size: 11px; color: var(--faint); letter-spacing: .5px; }

  .hero { margin-bottom: 36px; }
  .eyebrow {
    font-family: var(--mono); font-size: 11px; font-weight: 500; letter-spacing: 2.5px;
    text-transform: uppercase; color: var(--cyan); margin-bottom: 16px;
    display: flex; align-items: center; gap: 9px;
  }
  .eyebrow::before { content: ""; width: 22px; height: 1px; background: var(--cyan); }
  h1 {
    font-family: var(--display); font-weight: 600; font-size: clamp(32px, 7.5vw, 50px);
    line-height: 1.03; letter-spacing: -1.2px; margin-bottom: 15px;
    text-shadow: 0 2px 40px rgba(139,109,255,.25);
  }
  h1 em {
    font-style: italic; font-weight: 500;
    background: linear-gradient(120deg, var(--violet-2), var(--cyan));
    -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
    padding-right: .12em; margin-right: -.04em;
  }
  .lede { font-size: 15px; color: var(--muted); max-width: 47ch; }

  .panel {
    background: var(--glass); border: 1px solid var(--line);
    border-radius: 16px; padding: 22px; margin-bottom: 16px;
    backdrop-filter: blur(14px) saturate(120%); -webkit-backdrop-filter: blur(14px) saturate(120%);
    box-shadow: 0 8px 40px rgba(0,0,0,.35), inset 0 1px 0 rgba(255,255,255,.04);
  }
  .panel-head {
    font-family: var(--mono); font-size: 11px; font-weight: 600; letter-spacing: 1.5px;
    text-transform: uppercase; color: var(--faint);
    display: flex; align-items: center; justify-content: space-between; margin-bottom: 16px;
  }

  .key-row { display: flex; gap: 8px; position: relative; }
  .key-wrap { position: relative; }
  #accessCode.masked { -webkit-text-security: disc; text-security: disc; }
  .phone-row { display: flex; gap: 8px; }
  .phone-in { flex: 1; background: rgba(0,0,0,.3); border: 1px solid var(--line-strong); border-radius: 10px; padding: 12px 14px; color: var(--ink); font-family: var(--mono); font-size: 14px; }
  .phone-in:focus { outline: none; border-color: var(--violet); }
  .phone-btn { background: linear-gradient(135deg, var(--violet), #6d52e0); border: none; border-radius: 10px; color: #fff; font-family: var(--display); font-weight: 600; font-size: 14px; padding: 0 22px; cursor: pointer; transition: filter .15s; flex-shrink: 0; }
  .phone-btn:hover { filter: brightness(1.1); }
  .phone-card { background: var(--glass); border: 1px solid var(--line); border-radius: 16px; padding: 18px; margin-top: 18px; backdrop-filter: blur(14px); -webkit-backdrop-filter: blur(14px); }
  .phone-head { display: flex; align-items: center; gap: 12px; margin-bottom: 16px; flex-wrap: wrap; }
  .phone-num { font-family: var(--display); font-weight: 600; font-size: 22px; color: var(--ink); }
  .phone-badge { font-family: var(--mono); font-size: 10px; letter-spacing: .8px; text-transform: uppercase; padding: 4px 9px; border-radius: 6px; }
  .phone-badge.ok { color: var(--clear); background: rgba(54,217,154,.12); }
  .phone-badge.bad { color: var(--flag); background: var(--flag-bg); }
  .phone-grid { gap: 10px; }
  .scope-seg { display: inline-flex; gap: 2px; padding: 3px; background: rgba(255,255,255,.04); border: 1px solid var(--line); border-radius: 9px; }
  .scope-opt {
    font-family: var(--mono); font-size: 10.5px; letter-spacing: .5px; text-transform: none;
    color: var(--faint); background: none; border: none; cursor: pointer; padding: 4px 11px; border-radius: 6px;
    transition: color .15s, background .15s;
  }
  .scope-opt:hover { color: var(--muted); }
  .scope-opt.on { color: #fff; background: linear-gradient(135deg, var(--violet), #6d52e0); box-shadow: 0 2px 8px rgba(139,109,255,.3); }
  .key-row input { flex: 1; padding-right: 44px; }
  .key-eye {
    position: absolute; right: 8px; top: 50%; transform: translateY(-50%);
    background: none; border: none; cursor: pointer; color: var(--faint); padding: 6px;
    display: flex; align-items: center; justify-content: center; transition: color .15s;
  }
  .key-eye:hover { color: var(--violet-2); }
  .key-remaining {
    position: absolute; right: 12px; bottom: -19px; font-family: var(--mono); font-size: 11px;
    color: var(--muted); pointer-events: none; transition: opacity .2s; opacity: 0;
  }
  .key-remaining.show { opacity: 1; }
  .key-remaining.flag { color: var(--flag); }
  .key-remaining.clear { color: var(--clear); }
  .discord-link {
    position: fixed; left: 16px; bottom: 16px; z-index: 900;
    display: inline-flex; align-items: center; gap: 8px;
    padding: 8px 13px; border-radius: 999px;
    background: rgba(20,22,40,.82); border: 1px solid var(--line-strong);
    color: var(--muted); font-family: var(--mono); font-size: 12px; text-decoration: none;
    backdrop-filter: blur(10px); -webkit-backdrop-filter: blur(10px);
    transition: color .15s, border-color .15s, transform .15s, background .15s;
  }
  .discord-link:hover { color: #fff; border-color: #5865F2; background: rgba(88,101,242,.18); transform: translateY(-1px); }
  .discord-link svg { color: #5865F2; flex-shrink: 0; }
  .discord-link:hover svg { color: #fff; }
  @media (max-width: 560px) { .discord-link span { display: none; } .discord-link { padding: 9px; } }
  input[type=text], input[type=password] {
    flex: 1; min-width: 0;
    background: rgba(0,0,0,.3); border: 1px solid var(--line-strong); border-radius: 10px;
    color: var(--ink); font-family: var(--mono); font-size: 13.5px; padding: 11px 13px;
    outline: none; transition: border-color .15s, box-shadow .15s;
  }
  input::placeholder { color: var(--faint); font-family: var(--sans); }
  input:focus { border-color: var(--violet); box-shadow: 0 0 0 3px rgba(139,109,255,.22); }
  .ghost-btn {
    background: rgba(255,255,255,.04); border: 1px solid var(--line-strong); border-radius: 10px;
    color: var(--muted); cursor: pointer; font-family: var(--mono); font-size: 12px;
    padding: 0 14px; white-space: nowrap; transition: all .15s;
  }
  .ghost-btn:hover { border-color: var(--violet); color: var(--violet-2); }
  .hint { font-size: 12px; color: var(--faint); margin-top: 11px; line-height: 1.55; }

  .scope { display: flex; gap: 7px; margin-bottom: 16px; flex-wrap: wrap; }
  .chip {
    background: rgba(255,255,255,.04); border: 1px solid var(--line-strong); border-radius: 999px;
    color: var(--muted); cursor: pointer; font-size: 12.5px; font-weight: 500;
    padding: 7px 15px; transition: all .15s; font-family: var(--sans);
  }
  .chip:hover { border-color: var(--violet); }
  .chip.on {
    background: linear-gradient(120deg, var(--violet), #6d52e0); border-color: transparent;
    color: #fff; box-shadow: 0 3px 16px rgba(139,109,255,.4);
  }

  .id-list { display: flex; flex-direction: column; gap: 8px; margin-bottom: 12px; }
  .id-row { display: flex; gap: 8px; align-items: center; }
  .del {
    background: rgba(255,255,255,.04); border: 1px solid var(--line-strong); border-radius: 10px;
    color: var(--faint); cursor: pointer; font-size: 17px; width: 40px; height: 42px;
    display: flex; align-items: center; justify-content: center; flex-shrink: 0; transition: all .15s;
  }
  .del:hover { border-color: var(--flag); color: var(--flag); }
  .add {
    background: none; border: 1px dashed var(--line-strong); border-radius: 10px;
    color: var(--muted); cursor: pointer; font-family: var(--mono); font-size: 12px;
    letter-spacing: .5px; padding: 10px; width: 100%; transition: all .15s;
  }
  .add:hover { border-color: var(--violet); color: var(--violet-2); }
  .result-search {
    display: flex; align-items: center; gap: 9px; padding: 12px 20px;
    border-bottom: 1px solid var(--line); color: var(--faint);
  }
  .result-search input {
    flex: 1; min-width: 0; background: rgba(0,0,0,.3); border: 1px solid var(--line-strong);
    border-radius: 9px; color: var(--ink); font-family: var(--mono); font-size: 13px; padding: 9px 12px; outline: none;
  }
  .result-search input:focus { border-color: var(--violet); box-shadow: 0 0 0 3px rgba(139,109,255,.18); }

  .run {
    background: linear-gradient(120deg, var(--violet), #6d52e0); border: none; border-radius: 12px;
    color: #fff; cursor: pointer; font-family: var(--sans); font-size: 15px; font-weight: 600;
    padding: 15px; width: 100%; margin-top: 6px;
    display: flex; align-items: center; justify-content: center; gap: 9px;
    box-shadow: 0 6px 28px rgba(139,109,255,.42); transition: transform .08s, box-shadow .2s;
  }
  .run:hover { box-shadow: 0 8px 36px rgba(139,109,255,.55); }
  .run:active { transform: translateY(1px); }
  .run:disabled { opacity: .5; cursor: not-allowed; }
  .run svg { transition: transform .2s; }
  .run:hover svg { transform: translateX(3px); }

  .report { margin-top: 28px; }
  .report-frame {
    background: var(--glass); border: 1px solid var(--line); border-radius: 16px;
    backdrop-filter: blur(14px) saturate(120%); -webkit-backdrop-filter: blur(14px) saturate(120%);
    box-shadow: 0 8px 40px rgba(0,0,0,.4); overflow: hidden; position: relative;
  }
  .scanline {
    position: absolute; left: 0; right: 0; height: 70px; pointer-events: none; z-index: 5;
    background: linear-gradient(180deg, transparent, rgba(139,109,255,.18), transparent);
    opacity: 0;
  }
  .scanline.go { animation: sweep 1.05s linear infinite; opacity: 1; }
  @keyframes sweep { 0% { top: -70px; } 100% { top: 100%; } }

  .verdict { padding: 26px 24px; display: flex; align-items: center; gap: 18px; border-bottom: 1px solid var(--line); }
  .verdict.clear { background: var(--clear-bg); }
  .verdict.flag { background: var(--flag-bg); }
  .seal {
    width: 54px; height: 54px; flex-shrink: 0; border-radius: 50%;
    display: flex; align-items: center; justify-content: center; border: 2px solid currentColor;
  }
  .verdict.clear .seal, .verdict.clear .v-title { color: var(--clear); }
  .verdict.flag .seal, .verdict.flag .v-title { color: var(--flag); }
  .v-title { font-family: var(--display); font-weight: 600; font-size: 22px; letter-spacing: -.3px; }
  .v-sub { font-size: 13px; color: var(--muted); margin-top: 3px; }
  .seal-anim { animation: stamp .4s cubic-bezier(.2,.9,.3,1.2) both; }
  @keyframes stamp { 0% { transform: scale(.4) rotate(-12deg); opacity: 0; } 100% { transform: scale(1) rotate(0); opacity: 1; } }

  .rep-body { padding: 4px 0; }
  .rep-row { padding: 16px 24px; border-bottom: 1px solid var(--line); }
  .rep-row:last-child { border-bottom: none; }
  .rep-id { display: flex; align-items: center; gap: 11px; margin-bottom: 4px; flex-wrap: wrap; }
  .dot { width: 9px; height: 9px; border-radius: 50%; flex-shrink: 0; }
  .dot.clear { background: var(--clear); box-shadow: 0 0 8px var(--clear); }
  .dot.warn { background: var(--amber); box-shadow: 0 0 8px var(--amber); }
  .dot.flag { background: var(--flag); box-shadow: 0 0 8px var(--flag); }
  .rep-id .name { font-family: var(--mono); font-size: 14px; font-weight: 500; word-break: break-all; }
  .count { font-family: var(--mono); font-size: 11px; font-weight: 600; letter-spacing: .5px; padding: 2px 9px; border-radius: 999px; }
  .count.clear { background: var(--clear-bg); color: var(--clear); }
  .count.flag { background: var(--flag-bg); color: var(--flag); }
  .sub-label { font-family: var(--mono); font-size: 10px; letter-spacing: 1.5px; text-transform: uppercase; color: var(--faint); margin: 14px 0 7px; }
  .fold { border: 1px solid var(--line); border-radius: 12px; margin-top: 12px; overflow: hidden; background: rgba(255,255,255,.02); }
  .rep-sections { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; align-items: start; }
  .rep-sections .fold { margin-top: 0; }
  @media (max-width: 760px) { .rep-sections { grid-template-columns: 1fr; } }
  .fold-head {
    width: 100%; display: flex; align-items: center; gap: 10px; cursor: pointer;
    background: rgba(255,255,255,.03); border: none; color: var(--ink);
    padding: 13px 16px; font-family: var(--sans); font-size: 14px; text-align: left; transition: background .15s;
  }
  .fold-head:hover { background: rgba(255,255,255,.06); }
  .fold-chev { color: var(--faint); transition: transform .2s; flex-shrink: 0; }
  .fold.open .fold-chev { transform: rotate(90deg); }
  .fold-title { font-weight: 600; flex: 1; }
  .fold-count { font-family: var(--mono); font-size: 11px; font-weight: 600; padding: 2px 9px; border-radius: 999px; }
  .fold-count.flag { background: var(--flag-bg); color: var(--flag); }
  .fold-count.clean { background: var(--clear-bg); color: var(--clear); }
  .fold-body { display: none; padding: 14px 16px 16px; }
  .fold.open .fold-body { display: block; }
  .records { display: flex; flex-direction: column; gap: 10px; }
  .rec {
    background: rgba(0,0,0,.28); border: 1px solid var(--line); border-radius: 11px;
    padding: 10px 12px; display: flex; flex-direction: column; gap: 8px;
  }
  .rec-head { display: flex; align-items: center; justify-content: space-between; gap: 10px; flex-wrap: wrap; }
  .rec-head-left { display: flex; align-items: center; gap: 10px; flex-wrap: wrap; min-width: 0; }
  .rec-head-right { display: flex; align-items: center; gap: 8px; flex-shrink: 0; }
  .rec-check {
    display: inline-flex; align-items: center; gap: 6px; cursor: pointer; user-select: none;
    font-family: var(--mono); font-size: 11px; color: var(--faint); padding: 4px 8px;
    border: 1px solid var(--line); border-radius: 8px; transition: all .15s;
  }
  .rec-check:hover { color: var(--muted); border-color: var(--line-strong); }
  .rec-check input {
    -webkit-appearance: none; appearance: none; margin: 0; cursor: pointer;
    width: 13px; height: 13px; border-radius: 4px; flex-shrink: 0;
    border: 1px solid var(--line-strong); background: rgba(255,255,255,.03);
    position: relative; transition: all .15s;
  }
  .rec-check input:hover { border-color: var(--violet); }
  .rec-check input:checked { background: var(--violet); border-color: var(--violet); }
  .rec-check input:checked::after {
    content: ""; position: absolute; left: 3.5px; top: 1px; width: 3.5px; height: 7px;
    border: solid #fff; border-width: 0 2px 2px 0; transform: rotate(45deg);
  }
  .rec.checked { opacity: .72; }
  .rec.checked .rec-check { color: var(--clear); border-color: rgba(54,217,154,.4); background: rgba(54,217,154,.07); }
  .rec.checked .rec-body { display: none; }
  .rec.checked .copy-all { display: none; }
  .rec.checked .src { opacity: .6; }
  .rec .src { font-weight: 600; font-family: var(--mono); font-size: 13px; color: var(--muted); word-break: break-all; }
  .tag-stealer {
    background: var(--flag-bg); color: var(--flag); font-family: var(--mono); font-weight: 700;
    font-size: 10px; letter-spacing: .8px; padding: 3px 8px; border-radius: 6px;
  }
  .copy-all {
    display: inline-flex; align-items: center; gap: 6px;
    background: rgba(255,255,255,.04); border: 1px solid var(--line-strong); border-radius: 8px;
    color: var(--muted); cursor: pointer; font-family: var(--mono); font-size: 11.5px;
    padding: 5px 10px; transition: all .15s; flex-shrink: 0;
  }
  .copy-all:hover { border-color: var(--violet); color: var(--violet-2); }
  .copy-all.done { border-color: var(--clear); color: var(--clear); }
  .rec-body { display: flex; flex-direction: column; gap: 8px; }
  .rec-url .kv { background: rgba(139,109,255,.06); }
  .kv-grid { display: flex; flex-wrap: wrap; gap: 8px; }
  .kv {
    flex: 1 1 180px; min-width: 0;
    background: rgba(255,255,255,.025); border: 1px solid var(--line); border-radius: 8px; padding: 4px 9px;
  }
  .kv-label {
    font-family: var(--mono); font-size: 9px; letter-spacing: 1px; text-transform: uppercase;
    color: var(--faint); margin-bottom: 1px;
  }
  .kv-row { display: flex; align-items: center; gap: 8px; }
  .kv-val {
    font-family: var(--mono); font-size: 12.5px; color: #c2c9e0; line-height: 1.6; letter-spacing: .2px;
    white-space: nowrap; overflow: hidden; text-overflow: ellipsis; flex: 1; min-width: 0;
  }
  a.kv-val { color: #c2c9e0; text-decoration: none; }
  a.kv-val:hover { color: var(--cyan); text-decoration: underline; }
  .kv-actions { display: flex; flex-direction: row; gap: 5px; flex-shrink: 0; }
  .cp {
    position: relative;
    background: none; border: 1px solid var(--line-strong); border-radius: 7px; color: var(--faint);
    cursor: pointer; width: 23px; height: 23px; display: flex; align-items: center; justify-content: center;
    flex-shrink: 0; transition: all .15s;
  }
  .cp:hover { border-color: var(--violet); color: var(--violet-2); }
  .cp.send:hover { border-color: var(--cyan); color: var(--cyan); }
  .cp.done { border-color: var(--clear); color: var(--clear); }
  .rec-seen { font-family: var(--mono); font-size: 10px; color: var(--faint); letter-spacing: .5px; margin-top: 2px; }
  .view-log {
    display: inline-flex; align-items: center; gap: 6px; align-self: flex-start;
    background: rgba(63,214,230,.08); border: 1px solid rgba(63,214,230,.35); border-radius: 8px;
    color: var(--cyan); cursor: pointer; font-family: var(--mono); font-size: 11.5px;
    padding: 6px 11px; transition: all .15s; margin-top: 2px;
  }
  .view-log:hover { background: rgba(63,214,230,.16); }
  .vl-chev { transition: transform .2s; }
  .view-log.open .vl-chev { transform: rotate(90deg); }
  .vl-cost { color: var(--faint); }
  .fl-modal { position: fixed; inset: 0; z-index: 140; background: rgba(4,5,11,.55); backdrop-filter: blur(4px); -webkit-backdrop-filter: blur(4px); }
  .fl-window {
    position: fixed; width: min(620px, 94vw); height: min(70vh, 560px);
    min-width: 320px; min-height: 240px; max-width: 97vw; max-height: 92vh;
    display: flex; flex-direction: column;
    background: #0e1120; border: 1px solid var(--line-strong); border-radius: 16px; overflow: hidden;
    box-shadow: 0 24px 70px rgba(0,0,0,.6);
  }
  .fl-bar {
    display: flex; align-items: center; justify-content: space-between; gap: 10px;
    padding: 11px 14px; cursor: grab; user-select: none; touch-action: none; flex-shrink: 0;
    background: linear-gradient(180deg, rgba(139,109,255,.14), rgba(139,109,255,.04)); border-bottom: 1px solid var(--line);
  }
  .fl-bar:active { cursor: grabbing; }
  .fl-title { font-family: var(--mono); font-size: 12px; letter-spacing: .5px; color: var(--ink); word-break: break-all; }
  .fl-close { background: none; border: none; color: var(--faint); font-size: 14px; cursor: pointer; transition: color .15s; flex-shrink: 0; padding: 2px 4px; }
  .fl-close:hover { color: var(--flag); }
  .fl-content {
    padding: 14px 16px 18px; overflow: auto; flex: 1; min-height: 0;
    scrollbar-width: thin; scrollbar-color: var(--violet) transparent;
  }
  .fl-content::-webkit-scrollbar { width: 10px; height: 10px; }
  .fl-content::-webkit-scrollbar-track { background: transparent; margin: 6px 0; }
  .fl-content::-webkit-scrollbar-thumb { background: linear-gradient(180deg, var(--violet), #6d52e0); border-radius: 999px; border: 2px solid transparent; background-clip: padding-box; }
  .fl-content::-webkit-scrollbar-thumb:hover { background: linear-gradient(180deg, var(--violet-2), var(--violet)); background-clip: padding-box; }
  .fl-content::-webkit-scrollbar-corner { background: transparent; }
  .fl-resize { position: absolute; right: 2px; bottom: 2px; width: 18px; height: 18px; cursor: nwse-resize; touch-action: none; z-index: 3; }
  .fl-resize::after {
    content: ""; position: absolute; right: 3px; bottom: 3px; width: 9px; height: 9px;
    border-right: 2px solid var(--violet-2); border-bottom: 2px solid var(--violet-2);
    border-bottom-right-radius: 3px; opacity: .55; transition: opacity .15s;
  }
  .fl-resize:hover::after { opacity: 1; }
  .fl-msg { font-family: var(--mono); font-size: 12px; color: var(--muted); padding: 8px 0; display: flex; align-items: center; gap: 8px; }
  .fl-msg.flag { color: var(--flag); }
  .fl-section { font-family: var(--mono); font-size: 10px; letter-spacing: 1px; text-transform: uppercase; color: var(--violet-2); margin: 16px 0 8px; }
  .fl-meta { display: flex; flex-wrap: wrap; gap: 8px; }
  .fl-meta-item { background: rgba(255,255,255,.03); border: 1px solid var(--line); border-radius: 8px; padding: 6px 10px; }
  .fl-meta-k { font-family: var(--mono); font-size: 9px; letter-spacing: .8px; text-transform: uppercase; color: var(--faint); display: block; }
  .fl-meta-v { font-family: var(--mono); font-size: 12.5px; color: #c2c9e0; word-break: break-all; }
  .fl-cards { display: flex; flex-direction: column; gap: 10px; }
  .fl-raw { font-family: var(--mono); font-size: 11px; color: var(--muted); white-space: pre-wrap; word-break: break-all; margin: 6px 0 0; background: rgba(0,0,0,.3); padding: 10px; border-radius: 8px; }
  .fl-raw-wrap { margin-top: 16px; }
  .fl-raw-wrap summary { font-family: var(--mono); font-size: 11px; color: var(--faint); cursor: pointer; }
  .fl-foot { display: flex; align-items: center; justify-content: space-between; gap: 10px; margin-top: 16px; padding-top: 14px; border-top: 1px solid var(--line); flex-wrap: wrap; }
  .fl-foot-note { font-family: var(--mono); font-size: 11px; color: var(--faint); display: inline-flex; align-items: center; gap: 6px; }
  .fl-next { background: linear-gradient(135deg, var(--violet), #6d52e0); border: none; border-radius: 9px; color: #fff; font-family: var(--display); font-weight: 600; font-size: 12.5px; padding: 8px 14px; cursor: pointer; transition: filter .15s; }
  .fl-next:hover { filter: brightness(1.1); }
  .fl-next .vl-cost { font-weight: 400; opacity: .8; font-size: 11px; }
  .fl-next.ghost { background: rgba(255,255,255,.05); border: 1px solid var(--line-strong); color: var(--muted); }
  .fl-next.ghost:hover { filter: none; color: var(--ink); border-color: var(--violet); }
  .vbrowser { display: grid; grid-template-columns: minmax(170px, 240px) minmax(0, 1fr); gap: 12px; height: 100%; min-height: 240px; }
  .vtree { overflow: auto; border: 1px solid var(--line); border-radius: 10px; padding: 6px; background: rgba(0,0,0,.18);
    scrollbar-width: thin; scrollbar-color: var(--violet) transparent; }
  .vtree::-webkit-scrollbar { width: 8px; } .vtree::-webkit-scrollbar-thumb { background: var(--violet); border-radius: 999px; }
  .vt-row { display: flex; align-items: center; gap: 7px; padding: 5px 8px; border-radius: 7px; font-family: var(--mono); font-size: 12px; white-space: nowrap; }
  .vt-bar { display: flex; gap: 6px; padding: 2px 4px 8px; position: sticky; top: 0; }
  .vt-btn { background: rgba(139,109,255,.1); border: 1px solid var(--line-strong); color: var(--violet-2);
    font-family: var(--mono); font-size: 10px; padding: 4px 9px; border-radius: 7px; cursor: pointer; transition: all .12s; }
  .vt-btn:hover { color: #fff; border-color: var(--violet); background: rgba(139,109,255,.22); }
  .vt-chev { display: inline-block; width: 14px; color: var(--muted); transition: transform .12s; flex-shrink: 0; font-size: 15px; line-height: 1; }
  .vt-chev.open { transform: rotate(90deg); color: var(--violet-2); }
  .vt-dir { color: var(--violet-2); }
  .vt-file { color: var(--muted); cursor: pointer; transition: background .12s, color .12s; }
  .vt-file:hover { background: rgba(139,109,255,.1); color: var(--ink); }
  .vt-file.active { background: rgba(139,109,255,.18); color: var(--ink); }
  .vt-name { overflow: hidden; text-overflow: ellipsis; }
  .vt-size { margin-left: auto; display: inline-flex; align-items: center; gap: 6px; font-size: 10px; color: var(--faint); }
  .vt-cost { background: var(--violet); color: #fff; border-radius: 5px; padding: 0 5px; font-size: 9px; }
  .vt-cost::before { content: '◦ '; }
  .vpane { overflow: auto; border: 1px solid var(--line); border-radius: 10px; background: rgba(0,0,0,.18); min-height: 0;
    scrollbar-width: thin; scrollbar-color: var(--violet) transparent; }
  .vpane::-webkit-scrollbar { width: 8px; } .vpane::-webkit-scrollbar-thumb { background: var(--violet); border-radius: 999px; }
  .vfile-head { display: flex; align-items: center; justify-content: space-between; gap: 10px; padding: 9px 12px; border-bottom: 1px solid var(--line);
    font-family: var(--mono); font-size: 12px; color: var(--ink); position: sticky; top: 0; background: rgba(20,22,40,.9); backdrop-filter: blur(8px); }
  .vfile-actions { display: inline-flex; gap: 6px; flex-shrink: 0; }
  .vfile-body { margin: 0; padding: 12px; font-family: var(--mono); font-size: 12px; line-height: 1.55; color: var(--ink); white-space: pre-wrap; word-break: break-word; }
  @media (max-width: 620px) { .vbrowser { grid-template-columns: 1fr; } .vtree { max-height: 180px; } }
  .cp-tip {
    position: absolute; right: calc(100% + 8px); top: 50%; transform: translateY(-50%);
    background: #000; color: var(--ink); border: 1px solid var(--line-strong); border-radius: 6px;
    font-family: var(--sans); font-size: 11px; white-space: nowrap; padding: 4px 8px;
    opacity: 0; pointer-events: none; transition: opacity .12s; z-index: 10;
  }
  .cp:hover .cp-tip { opacity: 1; }
  .pager { display: flex; align-items: center; justify-content: center; gap: 14px; margin-top: 12px; }
  .pg {
    background: rgba(255,255,255,.04); border: 1px solid var(--line-strong); border-radius: 8px;
    color: var(--muted); cursor: pointer; font-family: var(--mono); font-size: 12px;
    padding: 7px 14px; transition: all .15s;
  }
  .pg:hover:not(:disabled) { border-color: var(--violet); color: var(--violet-2); }
  .pg:disabled { opacity: .35; cursor: not-allowed; }
  .pg-info { font-family: var(--mono); font-size: 11.5px; color: var(--faint); }
  .none { color: var(--clear); font-size: 12.5px; display: flex; align-items: center; gap: 7px; font-family: var(--mono); }
  .err { color: var(--flag); font-size: 12.5px; font-family: var(--mono); margin-top: 6px; }

  .empty {
    background: var(--glass-2); border: 1px dashed var(--line-strong); border-radius: 16px;
    padding: 38px 24px; text-align: center;
    backdrop-filter: blur(10px); -webkit-backdrop-filter: blur(10px);
  }
  .empty .glyph { color: var(--line-strong); margin-bottom: 12px; }
  .empty p { color: var(--muted); font-size: 13.5px; }

  .status { font-family: var(--mono); font-size: 12px; color: var(--muted); text-align: center; min-height: 18px; margin-top: 14px; letter-spacing: .3px; }
  .spin { display: inline-block; width: 11px; height: 11px; border: 2px solid var(--line-strong); border-top-color: var(--violet-2); border-radius: 50%; animation: rot .7s linear infinite; margin-right: 7px; vertical-align: -1px; }
  @keyframes rot { to { transform: rotate(360deg); } }
  .reveal { animation: rise .4s ease both; }
  @keyframes rise { from { opacity: 0; transform: translateY(8px); } to { opacity: 1; transform: none; } }

  a { color: var(--cyan); }

  @media (max-width: 480px) {
    .verdict { padding: 20px 16px; gap: 14px; }
    .rep-row, .panel { padding: 16px; }
    .v-title { font-size: 19px; }
  }
  @media (prefers-reduced-motion: reduce) {
    .scanline.go, .seal-anim, .reveal, .spin { animation: none !important; }
  }
  /* ---- tabs ---- */
  .tabs { display: flex; gap: 8px; margin-bottom: 28px; }
  .tab {
    background: rgba(255,255,255,.04); border: 1px solid var(--line-strong); border-radius: 10px;
    color: var(--muted); cursor: pointer; font-family: var(--sans); font-size: 14px; font-weight: 600;
    padding: 9px 18px; transition: all .15s;
  }
  .tab:hover { border-color: var(--violet); color: var(--ink); }
  .tab.on { background: linear-gradient(120deg, var(--violet), #6d52e0); border-color: transparent; color: #fff; box-shadow: 0 3px 16px rgba(139,109,255,.35); }

  /* ---- OSINT web canvas ---- */
  .osint-toolbar {
    display: flex; align-items: center; gap: 8px; flex-wrap: wrap;
    background: var(--glass); border: 1px solid var(--line); border-radius: 14px;
    padding: 12px; margin-bottom: 14px; backdrop-filter: blur(14px); -webkit-backdrop-filter: blur(14px);
  }
  .ot-btn {
    background: rgba(255,255,255,.05); border: 1px solid var(--line-strong); border-radius: 9px;
    color: var(--ink); cursor: pointer; font-family: var(--sans); font-size: 13px; font-weight: 500;
    padding: 8px 13px; transition: all .15s; white-space: nowrap;
  }
  .ot-btn:hover { border-color: var(--violet); color: var(--violet-2); }
  .ot-btn.on { background: linear-gradient(120deg, var(--violet), #6d52e0); border-color: transparent; color: #fff; }
  .ot-btn.danger:hover { border-color: var(--flag); color: var(--flag); }
  .ot-hint { font-size: 11.5px; color: var(--faint); font-family: var(--mono); margin-left: auto; }

  .osint-stage {
    position: relative; width: 100%; height: 70vh; min-height: 460px;
    background: rgba(0,0,0,.28); border: 1px solid var(--line); border-radius: 14px;
    overflow: hidden; cursor: grab;
    background-image: radial-gradient(circle at 1px 1px, rgba(255,255,255,.06) 1px, transparent 0);
    background-size: 26px 26px;
  }
  .osint-stage.panning { cursor: grabbing; }
  .osint-edges { position: absolute; inset: 0; width: 100%; height: 100%; pointer-events: none; overflow: visible; z-index: 1; transform-origin: 0 0; }
  .osint-world { position: absolute; top: 0; left: 0; transform-origin: 0 0; z-index: 2; }
  .osint-empty {
    position: absolute; inset: 0; display: flex; align-items: center; justify-content: center;
    text-align: center; color: var(--faint); font-size: 13.5px; pointer-events: none; padding: 20px;
  }

  .node {
    position: absolute; width: 220px; background: var(--glass-2);
    border: 1px solid var(--line-strong); border-radius: 12px;
    box-shadow: 0 6px 24px rgba(0,0,0,.4); cursor: grab; user-select: none;
    backdrop-filter: blur(6px); -webkit-backdrop-filter: blur(6px);
  }
  .node.sel { border-color: var(--violet); box-shadow: 0 0 0 2px rgba(139,109,255,.4), 0 6px 24px rgba(0,0,0,.4); }
  .node.dragging { cursor: grabbing; z-index: 50; }
  .node-head {
    display: flex; align-items: center; justify-content: space-between; gap: 6px;
    padding: 7px 10px; border-bottom: 1px solid var(--line);
    font-family: var(--mono); font-size: 10px; letter-spacing: 1px; text-transform: uppercase; color: var(--faint);
  }
  .node-type { color: var(--violet-2); font-weight: 600; }
  .node-del { background: none; border: none; color: var(--faint); cursor: pointer; font-size: 14px; line-height: 1; padding: 0 2px; }
  .node-del:hover { color: var(--flag); }
  .node-body {
    padding: 10px 11px; font-family: var(--mono); font-size: 13px; color: var(--ink);
    word-break: break-word; white-space: pre-wrap; min-height: 20px; outline: none;
  }
  .node-body:focus { box-shadow: inset 0 0 0 1px var(--violet); border-radius: 6px; }
  .port {
    position: absolute; width: 12px; height: 12px; border-radius: 50%;
    background: var(--violet); border: 2px solid var(--void); cursor: crosshair; z-index: 3;
    transition: transform .12s;
  }
  .port:hover { transform: scale(1.4); background: var(--cyan); }
  .port.l { left: -7px; top: 50%; margin-top: -6px; }
  .port.r { right: -7px; top: 50%; margin-top: -6px; }
  .port.t { top: -7px; left: 50%; margin-left: -6px; }
  .port.b { bottom: -7px; left: 50%; margin-left: -6px; }
  .edge { stroke: var(--cyan); stroke-width: 2; fill: none; opacity: .8; }
  .edge-hit { stroke: transparent; stroke-width: 14; fill: none; cursor: pointer; pointer-events: stroke; }
  .edge-grp:hover .edge { stroke: var(--flag); }
  .userbar { display: flex; align-items: center; gap: 12px; }
  .visually-hidden { position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; border: 0; }

  /* ---- results: full-width + three lanes ---- */
  .report.wide { position: relative; left: 50%; right: 50%; width: 100vw; margin-left: -50vw; margin-right: -50vw; }
  .report-frame { max-width: 1480px; margin: 0 auto; }
  .lanes { display: grid; grid-template-columns: 260px minmax(0, 1fr) minmax(0, 1fr); gap: 16px; align-items: start; padding: 16px 22px 22px; }
  .lanes.lanes-2 { grid-template-columns: 260px minmax(0, 1fr); }
  @media (max-width: 980px) { .lanes, .lanes.lanes-2 { grid-template-columns: 1fr; } }
  .lane { min-width: 0; }
  .lane-title { font-family: var(--mono); font-size: 10px; letter-spacing: 1.5px; text-transform: uppercase; color: var(--violet-2); margin: 0 0 10px 2px; }
  .lane-body { display: flex; flex-direction: column; gap: 12px; }
  .lane-group { background: rgba(0,0,0,.18); border: 1px solid var(--line); border-radius: 12px; padding: 10px; }
  .lane-group-head { display: flex; align-items: center; justify-content: space-between; gap: 8px; margin-bottom: 8px; }
  .lg-name { font-family: var(--mono); font-size: 12px; color: var(--muted); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
  .lg-count { font-family: var(--mono); font-size: 11px; padding: 1px 8px; border-radius: 999px; }
  .lg-count.flag { color: var(--flag); background: var(--flag-bg); }
  .lg-count.clean { color: var(--clear); background: rgba(74,222,128,.1); }
  .lane-empty { color: var(--faint); font-size: 12.5px; padding: 14px 6px; display: flex; align-items: center; gap: 8px; }
  .rbx-card {
    background: var(--glass); border: 1px solid var(--line); border-radius: 16px; padding: 16px;
    backdrop-filter: blur(14px); -webkit-backdrop-filter: blur(14px); margin-bottom: 12px;
  }
  .rbx-head { display: flex; align-items: center; gap: 14px; }
  .rbx-avatar {
    width: 64px; height: 64px; border-radius: 14px; flex-shrink: 0; overflow: hidden;
    background: rgba(255,255,255,.04); border: 1px solid var(--line-strong);
    display: flex; align-items: center; justify-content: center; color: var(--faint);
  }
  .rbx-avatar img { width: 100%; height: 100%; object-fit: cover; display: block; }
  .rbx-id-head { min-width: 0; }
  .rbx-display { font-family: var(--display); font-weight: 600; font-size: 17px; color: var(--ink); word-break: break-word; }
  .rbx-username { font-family: var(--mono); font-size: 12px; color: var(--muted); margin-top: 2px; word-break: break-all; }
  .rbx-banned { display: inline-block; margin-top: 6px; font-family: var(--mono); font-size: 10px; letter-spacing: .8px;
    color: var(--flag); background: var(--flag-bg); border-radius: 6px; padding: 3px 8px; }
  .rbx-grid { display: flex; flex-direction: column; gap: 8px; margin-top: 14px; }
  .rbx-field { background: rgba(255,255,255,.025); border: 1px solid var(--line); border-radius: 9px; padding: 7px 11px; }
  .rbx-field .l { font-family: var(--mono); font-size: 9px; letter-spacing: 1px; text-transform: uppercase; color: var(--faint); margin-bottom: 2px; }
  .rbx-field .v { font-family: var(--mono); font-size: 12.5px; color: var(--muted); word-break: break-word; }
  .rbx-past { margin-top: 14px; }  .rbx-past-title { font-family: var(--mono); font-size: 9px; letter-spacing: 1px; text-transform: uppercase; color: var(--faint); margin-bottom: 7px; }
  .rbx-tags { display: flex; flex-wrap: wrap; gap: 6px; }
  .rbx-tag { font-family: var(--mono); font-size: 11.5px; color: var(--cyan); background: rgba(63,214,230,.08); border: 1px solid rgba(63,214,230,.25); border-radius: 7px; padding: 3px 8px; word-break: break-all; cursor: pointer; transition: all .15s; }
  .rbx-tag:hover { background: rgba(63,214,230,.18); border-color: var(--cyan); }
  .rbx-none { color: var(--faint); font-size: 12.5px; }
  .rbx-value { border-color: rgba(54,217,154,.3); background: rgba(54,217,154,.06); }
  .rbx-value .v { color: var(--clear); }
  .xbl-card { border-color: rgba(16,185,80,.25); }
  .xbl-avatar { border-color: rgba(16,185,80,.4); color: #10b550; background: rgba(16,185,80,.06); }
  .xbl-badge { display: inline-flex; align-items: center; gap: 4px; font-family: var(--mono); font-size: 9px; letter-spacing: 1px; text-transform: uppercase; color: #2fd07a; margin-bottom: 3px; }
  .xbl-bio { font-family: var(--sans); font-size: 12.5px; color: var(--muted); line-height: 1.5; }
  .x-card { border-color: rgba(120,150,180,.3); }
  .x-avatar { border-color: rgba(160,180,200,.45); color: var(--ink); background: rgba(120,140,160,.08); }
  .x-badge { display: inline-flex; align-items: center; gap: 4px; font-family: var(--mono); font-size: 9px; letter-spacing: 1px; text-transform: uppercase; color: var(--ink); margin-bottom: 3px; }
  .rbx-user { font-family: var(--mono); font-size: 12px; color: var(--muted); margin-top: 2px; word-break: break-all; }
  .rbx-menu {
    position: absolute; z-index: 200; min-width: 190px;
    background: #14182a; border: 1px solid var(--line-strong); border-radius: 11px;
    padding: 6px; box-shadow: 0 12px 36px rgba(0,0,0,.55);
  }
  .rbx-menu-name { font-family: var(--mono); font-size: 11px; color: var(--cyan); padding: 6px 9px 7px; border-bottom: 1px solid var(--line); margin-bottom: 4px; word-break: break-all; }
  .rbx-menu-item { display: block; width: 100%; text-align: left; background: none; border: none; cursor: pointer;
    color: var(--ink); font-family: var(--sans); font-size: 13px; padding: 8px 9px; border-radius: 7px; transition: background .12s; }
  .rbx-menu-item:hover { background: rgba(139,109,255,.16); color: var(--violet-2); }
  .signin-btn {
    background: linear-gradient(120deg, var(--violet), #6d52e0); border: none; border-radius: 9px;
    color: #fff; cursor: pointer; font-family: var(--sans); font-size: 13px; font-weight: 600;
    padding: 8px 16px; transition: box-shadow .2s; box-shadow: 0 3px 14px rgba(139,109,255,.35);
  }
  .signin-btn:hover { box-shadow: 0 5px 20px rgba(139,109,255,.5); }
  .user-email {
    font-family: var(--mono); font-size: 12px; color: var(--muted); max-width: 200px; overflow: hidden;
    text-overflow: ellipsis; white-space: nowrap; background: none; border: none; cursor: pointer;
    filter: blur(5px); transition: filter .18s; padding: 0;
  }
  .user-email:hover { filter: blur(0); color: var(--violet-2); }

  .stats-modal {
    position: fixed; inset: 0; z-index: 120; display: flex; align-items: center; justify-content: center;
    padding: 20px; background: rgba(4,5,11,.72); backdrop-filter: blur(8px); -webkit-backdrop-filter: blur(8px);
  }
  .stats-card {
    position: relative; width: 100%; max-width: 520px; background: var(--glass); border: 1px solid var(--line-strong);
    border-radius: 20px; padding: 26px; box-shadow: 0 16px 60px rgba(0,0,0,.55);
    backdrop-filter: blur(18px); -webkit-backdrop-filter: blur(18px);
  }
  .stats-close { position: absolute; top: 16px; right: 16px; background: none; border: none; color: var(--faint); font-size: 16px; cursor: pointer; transition: color .15s; }
  .stats-close:hover { color: var(--flag); }
  .stats-head { display: flex; align-items: center; gap: 14px; margin-bottom: 22px; }
  .stats-avatar { width: 46px; height: 46px; border-radius: 12px; background: linear-gradient(135deg, var(--violet), #3fd6e6); display: flex; align-items: center; justify-content: center; color: #fff; font-family: var(--display); font-weight: 700; font-size: 20px; flex-shrink: 0; }
  .stats-title { font-family: var(--display); font-weight: 600; font-size: 20px; }
  .stats-sub { font-family: var(--mono); font-size: 12px; color: var(--muted); margin-top: 2px; word-break: break-all; }
  .stats-meter { background: rgba(0,0,0,.25); border: 1px solid var(--line); border-radius: 14px; padding: 16px; margin-bottom: 16px; }
  .sm-top { display: flex; justify-content: space-between; font-family: var(--mono); font-size: 12px; color: var(--muted); margin-bottom: 9px; }
  .sm-top span:last-child { color: var(--ink); }
  .sm-bar { height: 8px; border-radius: 999px; background: var(--line-strong); overflow: hidden; }
  .sm-fill { height: 100%; border-radius: 999px; background: linear-gradient(90deg, var(--violet), #6d52e0); transition: width .4s ease; }
  .sm-foot { font-family: var(--mono); font-size: 11px; color: var(--faint); margin-top: 9px; }
  .stats-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; }
  @media (max-width: 460px) { .stats-grid { grid-template-columns: repeat(2, 1fr); } }
  .stat-tile { background: rgba(255,255,255,.025); border: 1px solid var(--line); border-radius: 12px; padding: 14px 12px; text-align: center; }
  .st-num { font-family: var(--display); font-weight: 600; font-size: 22px; color: var(--ink); }
  .st-label { font-family: var(--mono); font-size: 9.5px; letter-spacing: .8px; text-transform: uppercase; color: var(--faint); margin-top: 5px; }
  .admin-panel { margin-top: 20px; border-top: 1px solid var(--line); padding-top: 16px; }
  .pay-menu { position: fixed; inset: 0; z-index: 1200; display: flex; align-items: center; justify-content: center;
    background: rgba(4,5,12,.6); backdrop-filter: blur(4px); -webkit-backdrop-filter: blur(4px); }
  .pay-card { position: relative; width: min(380px, 92vw); background: rgba(18,20,36,.97); border: 1px solid var(--line-strong);
    border-radius: 18px; padding: 22px; box-shadow: 0 24px 70px rgba(0,0,0,.6); }
  .pay-close { position: absolute; top: 12px; right: 14px; background: none; border: none; color: var(--faint); font-size: 16px; cursor: pointer; }
  .pay-close:hover { color: var(--ink); }
  .pay-title { font-family: var(--display); font-weight: 600; font-size: 17px; color: var(--ink); }
  .pay-sub { font-family: var(--mono); font-size: 12px; color: var(--violet-2); margin: 3px 0 16px; }
  .pay-methods { display: flex; flex-direction: column; gap: 9px; }
  .pay-method { display: grid; grid-template-columns: 28px 1fr; grid-template-rows: auto auto; column-gap: 12px; align-items: center;
    text-align: left; padding: 13px 15px; cursor: pointer; background: rgba(255,255,255,.03);
    border: 1px solid var(--line-strong); border-radius: 12px; color: var(--ink); transition: all .15s; }
  .pay-method:hover { border-color: var(--violet); background: rgba(139,109,255,.12); transform: translateY(-1px); }
  .pay-method svg { grid-row: 1 / 3; color: var(--violet-2); }
  .pm-name { font-family: var(--display); font-weight: 600; font-size: 14px; }
  .pm-note { font-family: var(--mono); font-size: 10.5px; color: var(--faint); }
  .pay-foot { min-height: 16px; margin: 14px 0 0; font-family: var(--mono); font-size: 11.5px; color: var(--muted); text-align: center; }
  .buy-code-btn { margin-left: auto; background: rgba(139,109,255,.14); border: 1px solid var(--line-strong); border-radius: 8px;
    color: var(--violet-2); font-family: var(--mono); font-size: 11px; padding: 5px 11px; cursor: pointer; transition: all .15s; }
  .buy-code-btn:hover { color: #fff; border-color: var(--violet); background: rgba(139,109,255,.25); }
  .pay-packs { display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; margin: 4px 0 16px; }
  .pay-pack { display: flex; flex-direction: column; align-items: center; gap: 2px; padding: 11px 6px; cursor: pointer;
    background: rgba(255,255,255,.03); border: 1px solid var(--line-strong); border-radius: 11px; transition: all .15s; }
  .pay-pack:hover { border-color: var(--violet); }
  .pay-pack.sel { border-color: var(--violet); background: rgba(139,109,255,.16); }
  .pay-pack b { font-family: var(--display); font-size: 18px; color: var(--ink); }
  .pay-pack b::after { content: ''; }
  .pay-pack span { font-family: var(--mono); font-size: 11px; color: var(--violet-2); }
  .pay-methods-label { font-family: var(--mono); font-size: 10px; letter-spacing: 1px; text-transform: uppercase; color: var(--faint); margin-bottom: 8px; }
  .code-show { font-family: var(--mono); font-size: 15px; color: var(--clear); background: rgba(0,0,0,.35); border: 1px dashed var(--line-strong);
    border-radius: 10px; padding: 13px; text-align: center; word-break: break-all; user-select: all; }
  .cx-coins { display: grid; grid-template-columns: repeat(2, 1fr); gap: 8px; margin: 6px 0 4px; }
  .cx-coin { display: flex; flex-direction: column; align-items: flex-start; gap: 2px; padding: 12px 14px; cursor: pointer;
    background: rgba(255,255,255,.03); border: 1px solid var(--line-strong); border-radius: 11px; transition: all .15s; }
  .cx-coin:hover { border-color: var(--violet); background: rgba(139,109,255,.12); transform: translateY(-1px); }
  .cx-coin-name { font-family: var(--display); font-weight: 600; font-size: 14px; color: var(--ink); }
  .cx-coin-t { font-family: var(--mono); font-size: 10px; color: var(--faint); }
  .cx-qr { display: flex; justify-content: center; margin: 6px 0 12px; }
  .cx-qr img { border-radius: 10px; background: #0f1120; padding: 8px; border: 1px solid var(--line); }
  .cx-field { margin-bottom: 10px; }
  .cx-l { font-family: var(--mono); font-size: 9px; letter-spacing: 1px; text-transform: uppercase; color: var(--faint); margin-bottom: 4px; }
  .cx-copyrow { display: flex; align-items: center; gap: 8px; background: rgba(0,0,0,.3); border: 1px solid var(--line); border-radius: 9px; padding: 8px 10px; }
  .cx-copyrow code { font-family: var(--mono); font-size: 13px; color: var(--clear); flex: 1; word-break: break-all; }
  .cx-copyrow .cx-addr { font-size: 11.5px; color: var(--ink); }
  .cx-status { margin-top: 12px; font-family: var(--mono); font-size: 12px; color: var(--violet-2); display: flex; align-items: center; gap: 8px; flex-wrap: wrap; }
  .cx-mins { color: var(--faint); }
  .pay-toast { position: fixed; bottom: 22px; left: 50%; transform: translateX(-50%); z-index: 9999;
    background: rgba(20,22,40,.96); border: 1px solid var(--line-strong); color: var(--ink);
    font-family: var(--mono); font-size: 13px; padding: 12px 18px; border-radius: 12px; backdrop-filter: blur(12px); }
  .pay-toast.ok { border-color: rgba(54,217,154,.5); color: var(--clear); }
  .admin-title { font-family: var(--mono); font-size: 10px; letter-spacing: 1.5px; text-transform: uppercase; color: var(--violet-2); margin-bottom: 12px; }
  .admin-add { display: flex; gap: 8px; margin-bottom: 14px; flex-wrap: wrap; }
  .admin-in { flex: 1; min-width: 120px; background: rgba(0,0,0,.3); border: 1px solid var(--line-strong); border-radius: 8px; padding: 8px 11px; color: var(--ink); font-family: var(--mono); font-size: 12px; }
  .admin-in:focus { outline: none; border-color: var(--violet); }
  .admin-in-num { flex: 0 0 70px; min-width: 0; }
  .admin-btn { background: rgba(255,255,255,.05); border: 1px solid var(--line-strong); border-radius: 8px; padding: 8px 12px; color: var(--muted); font-family: var(--mono); font-size: 11px; cursor: pointer; transition: all .15s; }
  .admin-btn:hover { color: var(--ink); border-color: var(--violet); }
  .admin-btn.primary { background: linear-gradient(135deg, var(--violet), #6d52e0); color: #fff; border: none; }
  .admin-list { display: flex; flex-direction: column; gap: 7px; max-height: 280px; overflow: auto; scrollbar-width: thin; scrollbar-color: var(--violet) transparent; }
  .admin-list::-webkit-scrollbar { width: 8px; }
  .admin-list::-webkit-scrollbar-thumb { background: var(--violet); border-radius: 999px; }
  .admin-row { display: flex; align-items: center; gap: 8px; background: rgba(255,255,255,.025); border: 1px solid var(--line); border-radius: 9px; padding: 8px 11px; }
  .admin-code { flex: 1; min-width: 0; font-family: var(--mono); font-size: 12px; color: var(--ink); word-break: break-all; }
  .admin-usage { font-family: var(--mono); font-size: 10.5px; color: var(--faint); white-space: nowrap; }
  .admin-lim { width: 52px; background: rgba(0,0,0,.3); border: 1px solid var(--line); border-radius: 6px; padding: 4px 6px; color: var(--muted); font-family: var(--mono); font-size: 11px; text-align: center; }
  .admin-x { background: none; border: none; color: var(--faint); cursor: pointer; font-size: 13px; padding: 2px 5px; transition: color .15s; }
  .admin-x:hover { color: var(--flag); }
  .admin-mini { background: none; border: 1px solid var(--line); border-radius: 6px; color: var(--faint); cursor: pointer; font-family: var(--mono); font-size: 10px; padding: 3px 7px; transition: all .15s; }
  .admin-mini:hover { color: var(--cyan); border-color: var(--cyan); }
  .logout-btn {
    background: rgba(255,255,255,.04); border: 1px solid var(--line-strong); border-radius: 8px;
    color: var(--muted); cursor: pointer; font-family: var(--mono); font-size: 11.5px; padding: 5px 11px; transition: all .15s;
  }
  .logout-btn:hover { border-color: var(--flag); color: var(--flag); }

  /* ---- music ---- */
  .music-toolbar {
    display: flex; align-items: center; gap: 10px; flex-wrap: wrap;
    background: var(--glass); border: 1px solid var(--line); border-radius: 14px;
    padding: 12px; margin-bottom: 14px; backdrop-filter: blur(14px); -webkit-backdrop-filter: blur(14px);
  }
  .playlist {
    background: rgba(0,0,0,.28); border: 1px solid var(--line); border-radius: 14px;
    padding: 8px; margin-bottom: 16px; max-height: 46vh; overflow-y: auto; min-height: 120px;
    scrollbar-width: thin; scrollbar-color: var(--violet) transparent;
  }
  .playlist::-webkit-scrollbar { width: 10px; }
  .playlist::-webkit-scrollbar-track { background: transparent; margin: 6px 0; }
  .playlist::-webkit-scrollbar-thumb {
    background: linear-gradient(180deg, var(--violet), #6d52e0);
    border-radius: 999px; border: 2px solid rgba(0,0,0,.28);
  }
  .playlist::-webkit-scrollbar-thumb:hover { background: linear-gradient(180deg, var(--violet-2), var(--violet)); }
  .music-empty { color: var(--faint); font-size: 13.5px; text-align: center; padding: 36px 16px; }
  .reactive-toggle { display: inline-flex; align-items: center; gap: 8px; cursor: pointer; user-select: none; }
  .reactive-toggle input { position: absolute; opacity: 0; width: 0; height: 0; }
  .rt-track { width: 38px; height: 21px; border-radius: 999px; background: var(--line-strong); position: relative; transition: background .18s; flex-shrink: 0; }
  .rt-knob { position: absolute; top: 2px; left: 2px; width: 17px; height: 17px; border-radius: 50%; background: #fff; transition: transform .18s; }
  .reactive-toggle input:checked + .rt-track { background: linear-gradient(120deg, var(--violet), #6d52e0); }
  .reactive-toggle input:checked + .rt-track .rt-knob { transform: translateX(17px); }
  .rt-label { font-family: var(--mono); font-size: 12px; color: var(--muted); }

  /* ---- mini player (persists across tabs) ---- */
  .mini-player {
    position: fixed; left: 18px; bottom: 68px; z-index: 80;
    display: flex; align-items: center; gap: 12px; max-width: 340px;
    background: rgba(16,18,32,.82); border: 1px solid var(--line-strong); border-radius: 14px;
    padding: 10px 14px 10px 10px; box-shadow: 0 10px 36px rgba(0,0,0,.5);
    backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px);
    animation: miniIn .25s ease;
  }
  @keyframes miniIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: none; } }
  .mini-art {
    width: 40px; height: 40px; border-radius: 10px; flex-shrink: 0; cursor: pointer;
    background: linear-gradient(135deg, var(--violet), #3fd6e6); border: none; color: #fff; font-size: 18px;
    display: flex; align-items: center; justify-content: center;
  }
  .mini-mid { min-width: 0; }
  .mini-title {
    font-family: var(--mono); font-size: 12.5px; color: var(--ink); cursor: pointer;
    white-space: nowrap; overflow: hidden; text-overflow: ellipsis; max-width: 270px; margin-bottom: 5px;
  }
  .mini-title:hover { color: var(--violet-2); }
  .mini-controls { display: flex; align-items: center; gap: 6px; }
  .mini-btn {
    background: none; border: none; color: var(--muted); cursor: pointer; font-size: 13px;
    width: 26px; height: 26px; border-radius: 6px; display: flex; align-items: center; justify-content: center; transition: all .15s;
  }
  .mini-btn:hover { background: rgba(255,255,255,.08); color: var(--ink); }
  .mini-btn.play { color: var(--violet-2); font-size: 14px; }
  .mini-vol { width: 64px; }
  @media (max-width: 560px) { .mini-vol { display: none; } .mini-player { max-width: 250px; } }
  .track {
    display: flex; align-items: center; gap: 12px; padding: 10px 12px; border-radius: 10px;
    cursor: pointer; transition: background .12s;
  }
  .track:hover { background: rgba(255,255,255,.04); }
  .track.active { background: rgba(139,109,255,.14); }
  .track-eq { width: 16px; flex-shrink: 0; color: var(--violet-2); font-size: 12px; text-align: center; }
  .track.active .track-eq::after { content: '♪'; }
  .track-art { width: 34px; height: 34px; flex-shrink: 0; border-radius: 6px; overflow: hidden; }
  .track-art img { width: 100%; height: 100%; object-fit: cover; display: block; }
  .np-art {
    width: 52px; height: 52px; flex-shrink: 0; border-radius: 10px; overflow: hidden;
    display: flex; align-items: center; justify-content: center;
    background: linear-gradient(135deg, rgba(139,109,255,.3), rgba(63,214,230,.3)); color: var(--violet-2); font-size: 22px;
  }
  .np-art img { width: 100%; height: 100%; object-fit: cover; display: block; }
  .np-meta { min-width: 0; flex: 1; }
  .np { display: flex; align-items: center; gap: 12px; margin-bottom: 12px; }
  .mini-art img { width: 100%; height: 100%; object-fit: cover; display: block; border-radius: 10px; }
  .track-name { flex: 1; min-width: 0; font-family: var(--mono); font-size: 13px; color: var(--ink); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
  .track-del { background: none; border: none; color: var(--faint); cursor: pointer; font-size: 16px; flex-shrink: 0; padding: 0 4px; }
  .track-del:hover { color: var(--flag); }

  .player {
    background: var(--glass); border: 1px solid var(--line); border-radius: 16px;
    padding: 16px 18px; backdrop-filter: blur(14px); -webkit-backdrop-filter: blur(14px);
    box-shadow: 0 8px 40px rgba(0,0,0,.4);
  }
  .np-meta { display: flex; align-items: baseline; justify-content: space-between; gap: 10px; }
  .np-title { font-family: var(--display); font-weight: 600; font-size: 16px; color: var(--ink); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
  .np-time { font-family: var(--mono); font-size: 12px; color: var(--faint); flex-shrink: 0; }
  input[type=range].seek, input[type=range].vol {
    -webkit-appearance: none; appearance: none; height: 5px; border-radius: 999px;
    background: var(--line-strong); outline: none; cursor: pointer; width: 100%;
  }
  .seek { margin-bottom: 14px; }
  input[type=range]::-webkit-slider-thumb {
    -webkit-appearance: none; width: 14px; height: 14px; border-radius: 50%;
    background: var(--violet-2); cursor: pointer; box-shadow: 0 0 8px rgba(139,109,255,.6);
  }
  input[type=range]::-moz-range-thumb { width: 14px; height: 14px; border: none; border-radius: 50%; background: var(--violet-2); cursor: pointer; }
  .controls { display: flex; align-items: center; justify-content: center; gap: 14px; }
  .pbtn {
    background: rgba(255,255,255,.05); border: 1px solid var(--line-strong); border-radius: 50%;
    color: var(--ink); cursor: pointer; width: 42px; height: 42px; font-size: 15px;
    display: flex; align-items: center; justify-content: center; transition: all .15s;
  }
  .pbtn:hover { border-color: var(--violet); color: var(--violet-2); }
  .pbtn svg { width: 18px; height: 18px; display: block; }
  .pbtn.play svg { width: 22px; height: 22px; }
  .pbtn.small svg { width: 16px; height: 16px; }
  .mini-btn svg { width: 15px; height: 15px; display: block; }
  .mini-btn.play svg { width: 17px; height: 17px; }
  .mini-art svg, .np-art svg { width: 55%; height: 55%; display: block; }
  .track-eq svg { width: 15px; height: 15px; display: block; margin: 0 auto; }
  .pbtn.play { width: 52px; height: 52px; font-size: 18px; background: linear-gradient(120deg, var(--violet), #6d52e0); border-color: transparent; color: #fff; box-shadow: 0 4px 18px rgba(139,109,255,.45); }
  .pbtn.small { width: 36px; height: 36px; font-size: 14px; }
  .vol-wrap { display: flex; align-items: center; gap: 8px; margin-left: 10px; }
  .vol { width: 90px; }
</style>
</head>
<body>
<canvas id="galaxy"></canvas>
<div class="vignette"></div>

<div class="wrap" id="appWrap">
  <div class="topbar">
    <div class="brand">
      <svg width="26" height="26" viewBox="0 0 26 26" fill="none">
        <circle cx="13" cy="13" r="11" stroke="#a98bff" stroke-width="1.5"/>
        <circle cx="13" cy="13" r="6" stroke="#3fd6e6" stroke-width="1.5"/>
        <circle cx="13" cy="13" r="1.8" fill="#a98bff"/>
        <path d="M13 2V8M13 18V24M2 13H8M18 13H24" stroke="#a98bff" stroke-width="1.5"/>
      </svg>
      <span class="brand-name">TRACE</span>
    </div>
    <div class="userbar">
      <button class="signin-btn" id="signinBtn" onclick="netlifyIdentity.open('login')">Sign in</button>
      <button class="user-email" id="userEmail" style="display:none" onclick="openStats()" title="Open your dashboard"></button>
      <button class="logout-btn" id="logoutBtn" onclick="netlifyIdentity.logout()" style="display:none">log out</button>
    </div>
  </div>

  <div id="statsModal" class="stats-modal" style="display:none" onclick="if(event.target===this)closeStats()">
    <div class="stats-card">
      <button class="stats-close" onclick="closeStats()" aria-label="Close">✕</button>
      <div class="stats-head">
        <div class="stats-avatar" id="statsAvatar"></div>
        <div>
          <div class="stats-title">Your dashboard</div>
          <div class="stats-sub" id="statsWho">Guest</div>
        </div>
      </div>

      <div class="stats-meter">
        <div class="sm-top"><span>Searches used</span><span id="smCount">—</span></div>
        <div class="sm-bar"><div class="sm-fill" id="smFill" style="width:0%"></div></div>
        <div class="sm-foot" id="smFoot">Enter an access code to see usage.</div>
      </div>

      <div class="stats-grid">
        <div class="stat-tile"><div class="st-num" id="stRemaining">—</div><div class="st-label">Searches left</div></div>
        <div class="stat-tile"><div class="st-num" id="stRun">0</div><div class="st-label">Searches run</div></div>
        <div class="stat-tile"><div class="st-num" id="stRecords">0</div><div class="st-label">Records found</div></div>
        <div class="stat-tile"><div class="st-num" id="stRoblox">0</div><div class="st-label">Roblox lookups</div></div>
        <div class="stat-tile"><div class="st-num" id="stMusic">0</div><div class="st-label">Songs saved</div></div>
        <div class="stat-tile"><div class="st-num" id="stSince">—</div><div class="st-label">First seen</div></div>
      </div>

      <div id="adminPanel" class="admin-panel" style="display:none">
        <div class="admin-title">Manage access codes</div>
        <div class="admin-add">
          <input type="text" id="acNew" class="admin-in" placeholder="new code (e.g. friend-abc123)"
                 autocomplete="off" autocorrect="off" autocapitalize="off" spellcheck="false"
                 name="trace-newcode-x9" data-lpignore="true" data-1p-ignore data-bwignore data-form-type="other">
          <input type="number" id="acLimit" class="admin-in admin-in-num" placeholder="limit" value="10" min="0">
          <button class="admin-btn" onclick="adminGen()">Random</button>
          <button class="admin-btn primary" onclick="adminAdd()">Add</button>
        </div>
        <div class="admin-list" id="adminList"></div>
      </div>
    </div>
  </div>

  <div id="payMenu" class="pay-menu" style="display:none" onclick="if(event.target===this)closePayMenu()">
    <div class="pay-card">
      <button class="pay-close" onclick="closePayMenu()" aria-label="Close">✕</button>
      <div class="pay-title">Buy a code</div>
      <div class="pay-sub" id="paySub">—</div>
      <div class="pay-packs">
        <button class="pay-pack" data-pack="starter" onclick="selectPack('starter')"><b>25</b><span>£3</span></button>
        <button class="pay-pack" data-pack="plus" onclick="selectPack('plus')"><b>100</b><span>£9</span></button>
        <button class="pay-pack" data-pack="pro" onclick="selectPack('pro')"><b>500</b><span>£35</span></button>
      </div>
      <div class="pay-methods-label">Pay with</div>
      <div class="pay-methods">
        <button class="pay-method" onclick="payWith('crypto')">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="9" stroke="currentColor" stroke-width="1.7"/><path d="M9.5 8.5h3.2c1.2 0 2 .7 2 1.8s-.8 1.7-2 1.7H9.5m0 0h3.4c1.3 0 2.1.7 2.1 1.8s-.8 1.7-2.1 1.7H9.5m0-7v9M11 6.5V8m0 8v1.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
          <span class="pm-name">Crypto</span><span class="pm-note">BTC, ETH, SOL, USDT, USDC, BNB, XMR</span>
        </button>
      </div>
      <p class="pay-foot" id="payFoot"></p>
    </div>
  </div>

  <div id="fullLogModal" class="fl-modal" style="display:none" onclick="if(event.target===this)closeFullLog()">
    <div class="fl-window" id="flWindow">
      <div class="fl-bar" id="flBar">
        <span class="fl-title" id="flTitle">Stealer log</span>
        <button class="fl-close" onclick="closeFullLog()" aria-label="Close">✕</button>
      </div>
      <div class="fl-content" id="flContent"></div>
      <div class="fl-resize" id="flResize" title="Drag to resize"></div>
    </div>
  </div>

  <div class="tabs">
    <button class="tab on" data-tab="search" onclick="switchTab('search')">Breach Search</button>
    <button class="tab" data-tab="osint" onclick="switchTab('osint')">OSINT Web</button>
    <button class="tab" data-tab="phone" onclick="switchTab('phone')">Phone</button>
    <button class="tab" data-tab="music" onclick="switchTab('music')">Music</button>
  </div>

  <div id="tab-search" class="tab-panel">
  <div class="hero">
    <h1>Tuffer tuff <em>tuffer tuff&nbsp;</em></h1>
  </div>

  <div class="panel">
    <div class="panel-head"><span>Access code</span><button class="buy-code-btn" onclick="openBuyMenu()">+ Buy a code</button></div>
    <div class="key-wrap">
      <div class="key-row">
        <input type="text" id="accessCode" class="masked" placeholder="Enter your access code"
               autocomplete="off" autocorrect="off" autocapitalize="off" spellcheck="false"
               name="trace-key-x9" data-lpignore="true" data-1p-ignore data-bwignore data-form-type="other"
               oninput="onCodeInput()">
        <button class="key-eye" id="keyEye" type="button" onclick="toggleCodeBlur()" title="Show / hide" aria-label="Show or hide code"></button>
      </div>
      <span class="key-remaining" id="keyRemaining"></span>
    </div>
  </div>

  <div class="panel">
    <div class="panel-head">
      <span>What to check</span>
      <div class="scope-seg" id="scopeSeg">
        <button type="button" class="scope-opt" data-scope="both" onclick="setScope('both')">Both</button>
        <button type="button" class="scope-opt" data-scope="breach" onclick="setScope('breach')">Breach</button>
        <button type="button" class="scope-opt" data-scope="stealer" onclick="setScope('stealer')">Stealer</button>
      </div>
    </div>
    <div class="id-list" id="ids">
      <div class="id-row">
        <input type="text" placeholder="email, username, or domain" autocomplete="off" spellcheck="false">
      </div>
    </div>
    <button class="add" onclick="addId()">+ add identifier</button>
    <p class="hint" id="scopeNote" style="margin-top:10px"></p>
  </div>

  <button class="run" id="runBtn" onclick="run()">
    Run check
    <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M2 8h11M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
  </button>
  <div class="status" id="status"></div>

  <div class="report" id="report">
    <div class="empty">
      <svg class="glyph" width="40" height="40" viewBox="0 0 40 40" fill="none">
        <rect x="7" y="5" width="26" height="30" rx="3" stroke="currentColor" stroke-width="1.5"/>
        <path d="M13 13h14M13 19h14M13 25h9" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
      </svg>
      <p>No check has been run yet. Add what you want to look for, then run a check.</p>
    </div>
  </div>
  </div><!-- /tab-search -->

  <div id="tab-osint" class="tab-panel" style="display:none">
    <div class="osint-toolbar">
      <button class="ot-btn" onclick="osintAddBox()">＋ New box</button>
      <button class="ot-btn" id="osintLinkBtn" onclick="osintToggleLink()">🔗 Connect</button>
      <button class="ot-btn" onclick="osintZoom(1.2)">＋ Zoom</button>
      <button class="ot-btn" onclick="osintZoom(0.8)">－ Zoom</button>
      <button class="ot-btn" onclick="osintResetView()">⤢ Fit</button>
      <button class="ot-btn danger" onclick="osintClear()">🗑 Clear</button>
      <span class="ot-hint" id="osintHint">Drag boxes to move · drag a side dot to another box to connect · double-click a box to edit</span>
    </div>
    <div class="osint-stage" id="osintStage">
      <svg class="osint-edges" id="osintEdges"></svg>
      <div class="osint-world" id="osintWorld"></div>
      <div class="osint-empty" id="osintEmpty">
        <p>Your investigation canvas is empty.<br>Create a box with the toolbar, or hit “Send to OSINT Web” on any search result.</p>
      </div>
    </div>
  </div><!-- /tab-osint -->

  <div id="tab-phone" class="tab-panel" style="display:none">
    <div class="hero">
      <div class="eyebrow">phone intel</div>
      <h1>Phone <em>lookup</em></h1>
    </div>
    <div class="panel">
      <div class="panel-head"><span>Phone number</span></div>
      <div class="phone-row">
        <input type="tel" id="phoneInput" class="phone-in" placeholder="+1 415 555 2671" autocomplete="off" spellcheck="false"
               onkeydown="if(event.key==='Enter')runPhone()">
        <button class="phone-btn" onclick="runPhone()">Look up</button>
      </div>
      <p class="hint" id="phoneHint">Include the country code (e.g. +44…). A key is required to use this feature, but it doesn't take any of your search credits.</p>
    </div>
    <div id="phoneResult"></div>
  </div><!-- /tab-phone -->

  <div id="tab-music" class="tab-panel" style="display:none">
    <div class="music-toolbar">
      <label class="ot-btn" for="musicFile" style="cursor:pointer">＋ Add songs</label>
      <input type="file" id="musicFile" accept="audio/*" multiple class="visually-hidden">
      <label class="reactive-toggle">
        <input type="checkbox" id="reactiveToggle" onchange="toggleReactive(this)">
        <span class="rt-track"><span class="rt-knob"></span></span>
        <span class="rt-label">React to music</span>
      </label>
      <span class="ot-hint" id="musicHint">Songs are saved in your browser for this account — never uploaded.</span>
    </div>

    <div class="playlist" id="playlist">
      <div class="music-empty" id="musicEmpty">No songs yet. Hit “Add songs” to load audio files from your device.</div>
    </div>

    <div class="player" id="player">
      <div class="np">
        <span class="np-art" id="npArt"></span>
        <div class="np-meta">
          <div class="np-title" id="npTitle">Nothing playing</div>
          <div class="np-time"><span id="curTime">0:00</span> / <span id="durTime">0:00</span></div>
        </div>
      </div>
      <input type="range" class="seek" id="seek" min="0" max="1000" value="0">
      <div class="controls">
        <button class="pbtn" id="prevBtn" onclick="musicPrev()" title="Previous"></button>
        <button class="pbtn play" id="playBtn" onclick="musicTogglePlay()" title="Play/Pause"></button>
        <button class="pbtn" id="nextBtn" onclick="musicNext()" title="Next"></button>
        <div class="vol-wrap">
          <button class="pbtn small" id="muteBtn" onclick="musicToggleMute()" title="Mute"></button>
          <input type="range" class="vol" id="vol" min="0" max="100" value="100">
        </div>
      </div>
    </div>
  </div><!-- /tab-music -->

  <div id="miniPlayer" class="mini-player" style="display:none">
    <button class="mini-art" id="miniArt" onclick="switchTab('music')" title="Open music"></button>
    <div class="mini-mid">
      <div class="mini-title" id="miniTitle" onclick="switchTab('music')">Nothing playing</div>
      <div class="mini-controls">
        <button class="mini-btn" data-icon="prev" onclick="musicPrev()" title="Previous"></button>
        <button class="mini-btn play" id="miniPlay" onclick="musicTogglePlay()" title="Play/Pause"></button>
        <button class="mini-btn" data-icon="next" onclick="musicNext()" title="Next"></button>
        <button class="mini-btn" id="miniMute" onclick="musicToggleMute()" title="Mute"></button>
        <input type="range" class="mini-vol" id="miniVol" min="0" max="100" value="100" title="Volume">
      </div>
    </div>
  </div>
</div><!-- /wrap -->

<script>
  /* ============ AUTH (optional sign-in, top-right) ============ */
  (function () {
    function signedIn(user) {
      const em = document.getElementById('userEmail'), lo = document.getElementById('logoutBtn'), si = document.getElementById('signinBtn');
      if (user) {
        si.style.display = 'none';
        em.style.display = ''; em.textContent = user.email || '';
        lo.style.display = '';
      } else {
        si.style.display = '';
        em.style.display = 'none'; em.textContent = '';
        lo.style.display = 'none';
      }
      // refresh music for the active account if that tab is showing
      if (window.__musicReady) musicReloadForUser();
    }
    if (!window.netlifyIdentity) { signedIn(null); return; }
    netlifyIdentity.on('init', (user) => signedIn(user));
    netlifyIdentity.on('login', (user) => { signedIn(user); netlifyIdentity.close(); });
    netlifyIdentity.on('logout', () => signedIn(null));
    netlifyIdentity.init({ APIUrl: window.location.origin + '/.netlify/identity' });
  })();

  /* ============ REACTIVE GALAXY BACKGROUND ============ */
  (function () {
    const canvas = document.getElementById('galaxy');
    const ctx = canvas.getContext('2d');
    const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    let W, H, DPR, stars = [], nebulae = [], t = 0;
    let mx = 0, my = 0, px = 0, py = 0;
    const PALETTE = ['#8b6dff', '#3fd6e6', '#c77dff', '#5b8cff', '#ffffff', '#ff8fd0'];

    function resize() {
      DPR = Math.min(window.devicePixelRatio || 1, 2);
      W = canvas.width = innerWidth * DPR;
      H = canvas.height = innerHeight * DPR;
      canvas.style.width = innerWidth + 'px';
      canvas.style.height = innerHeight + 'px';
      build();
    }
    function build() {
      const count = Math.min(520, Math.floor((innerWidth * innerHeight) / 2600));
      stars = [];
      for (let i = 0; i < count; i++) {
        const depth = Math.random();
        stars.push({
          x: Math.random() * W, y: Math.random() * H, z: depth,
          r: (0.4 + depth * 1.8) * DPR, base: 0.25 + depth * 0.65,
          tw: Math.random() * Math.PI * 2, tws: 0.5 + Math.random() * 1.5,
          ph: Math.random() * Math.PI * 2,
          col: PALETTE[(Math.random() * PALETTE.length) | 0]
        });
      }
      nebulae = [
        { x: 0.28, y: 0.30, r: 0.55, col: '139,109,255', a: 0.22 },
        { x: 0.74, y: 0.38, r: 0.48, col: '63,214,230', a: 0.16 },
        { x: 0.55, y: 0.78, r: 0.6,  col: '199,125,255', a: 0.18 },
        { x: 0.15, y: 0.82, r: 0.4,  col: '91,140,255', a: 0.14 }
      ];
    }
    function drawNebulae(lvl) {
      lvl = lvl || 0;
      for (const n of nebulae) {
        const cx = n.x * W + px * 26 * DPR;
        const cy = n.y * H + py * 26 * DPR;
        const rad = n.r * Math.max(W, H) * (1 + lvl * 0.1);
        const drift = Math.sin(t * 0.0003 + n.x * 6) * 18 * DPR;
        const a = n.a * (1 + lvl * 0.45);
        const g = ctx.createRadialGradient(cx + drift, cy, 0, cx + drift, cy, rad);
        g.addColorStop(0, `rgba(${n.col},${a})`);
        g.addColorStop(0.5, `rgba(${n.col},${a * 0.35})`);
        g.addColorStop(1, 'rgba(0,0,0,0)');
        ctx.fillStyle = g; ctx.fillRect(0, 0, W, H);
      }
    }
    function drawCore(lvl) {
      lvl = lvl || 0;
      const cx = W * 0.5 + px * 12 * DPR, cy = H * 0.42 + py * 12 * DPR;
      ctx.save(); ctx.translate(cx, cy); ctx.rotate(t * 0.00006);
      const rad = 230 * DPR * (1 + lvl * 0.12);
      const g = ctx.createRadialGradient(0, 0, 0, 0, 0, rad);
      g.addColorStop(0, `rgba(255,245,230,${0.10 + lvl * 0.07})`);
      g.addColorStop(0.4, `rgba(170,140,255,${0.05 + lvl * 0.04})`);
      g.addColorStop(1, 'rgba(0,0,0,0)');
      ctx.fillStyle = g;
      ctx.beginPath(); ctx.ellipse(0, 0, rad, 95 * DPR * (1 + lvl * 0.12), 0, 0, Math.PI * 2); ctx.fill();
      ctx.restore();
    }
    function frame() {
      t += 16;
      px += (mx - px) * 0.05; py += (my - py) * 0.05;
      // live audio level (0..1) when music-reactive mode is on
      const lvl = (window.__reactiveOn !== false && window.__getAudioLevel) ? window.__getAudioLevel() : 0;
      const burst = (window.__reactiveOn !== false && window.__getBurst) ? window.__getBurst() : 0;
      const pulse = 1 + lvl * 1.6;
      ctx.clearRect(0, 0, W, H);
      ctx.fillStyle = '#04050b'; ctx.fillRect(0, 0, W, H);
      drawNebulae(lvl);
      const gx = (mx * 0.5 + 0.5) * W, gy = (my * 0.5 + 0.5) * H;
      const cx = W * 0.5, cy = H * 0.42;          // ripple origin (galactic core)
      ctx.globalCompositeOperation = 'lighter';
      for (const s of stars) {
        let x = s.x + px * (12 + s.z * 55) * DPR;
        let y = s.y + py * (12 + s.z * 55) * DPR;
        x = ((x % W) + W) % W; y = ((y % H) + H) % H;
        // sound-reactive motion: sudden outward burst on hits, quick snap back
        if (burst > 0.001) {
          const ddx = x - cx, ddy = y - cy;
          const d = Math.sqrt(ddx * ddx + ddy * ddy) || 1;
          const push = burst * (10 + s.z * 18) * DPR;
          x += (ddx / d) * push;
          y += (ddy / d) * push;
        }
        const tw = 0.6 + 0.4 * Math.sin(t * 0.001 * s.tws + s.tw);
        const dx = x - gx, dy = y - gy;
        const dist = Math.sqrt(dx * dx + dy * dy);
        const near = Math.max(0, 1 - dist / (220 * DPR));
        const alpha = Math.min(1, s.base * tw + near * 0.6 + lvl * s.z * 0.3);
        const r = s.r * (1 + near * 1.4) * (1 + lvl * s.z * 0.8);
        ctx.beginPath(); ctx.fillStyle = s.col; ctx.globalAlpha = alpha;
        ctx.arc(x, y, r, 0, Math.PI * 2); ctx.fill();
      }
      ctx.globalAlpha = 1; ctx.globalCompositeOperation = 'source-over';
      requestAnimationFrame(frame);
    }
    function staticRender() {
      ctx.fillStyle = '#04050b'; ctx.fillRect(0, 0, W, H);
      drawNebulae();
      ctx.globalCompositeOperation = 'lighter';
      for (const s of stars) {
        ctx.beginPath(); ctx.fillStyle = s.col; ctx.globalAlpha = s.base;
        ctx.arc(s.x, s.y, s.r, 0, Math.PI * 2); ctx.fill();
      }
      ctx.globalAlpha = 1; ctx.globalCompositeOperation = 'source-over';
    }
    window.addEventListener('resize', resize);
    window.addEventListener('pointermove', (e) => {
      mx = (e.clientX / innerWidth) * 2 - 1; my = (e.clientY / innerHeight) * 2 - 1;
    });
    window.addEventListener('deviceorientation', (e) => {
      if (e.gamma != null) { mx = Math.max(-1, Math.min(1, e.gamma / 30)); my = Math.max(-1, Math.min(1, (e.beta - 45) / 30)); }
    });
    resize();
    if (reduce) staticRender(); else requestAnimationFrame(frame);
  })();

  /* ============ APP LOGIC ============ */
  let LAST_RESULTS = null, LAST_TOTAL = 0, RESULT_QUERY = '';

  function onResultSearch(v) {
    RESULT_QUERY = (v || '').trim().toLowerCase();
    if (LAST_RESULTS) render(LAST_RESULTS, LAST_TOTAL, true);
  }
  // a record matches the results-search box if any of its fields contain the text
  function passesFilter(it) {
    if (!RESULT_QUERY) return true;
    const hay = [it.dbname, it.source, it.domain, it.url, it.host, it.email, it.username, it.password]
      .filter(Boolean).join(' ').toLowerCase();
    return hay.includes(RESULT_QUERY);
  }

  let currentTab = 'search';
  function switchTab(name) {
    currentTab = name;
    document.querySelectorAll('.tab').forEach(t => t.classList.toggle('on', t.dataset.tab === name));
    document.getElementById('tab-search').style.display = name === 'search' ? '' : 'none';
    document.getElementById('tab-osint').style.display = name === 'osint' ? '' : 'none';
    document.getElementById('tab-phone').style.display = name === 'phone' ? '' : 'none';
    document.getElementById('tab-music').style.display = name === 'music' ? '' : 'none';
    if (name === 'osint') osintInit();
    if (name === 'music') musicInit();
    updateMiniPlayer();
  }
  let scope = 'both';
  try { const ss = localStorage.getItem('trace_scope'); if (ss === 'breach' || ss === 'stealer' || ss === 'both') scope = ss; } catch (e) {}
  function setScope(s) {
    scope = s;
    try { localStorage.setItem('trace_scope', s); } catch (e) {}
    document.querySelectorAll('.scope-opt').forEach(b => b.classList.toggle('on', b.dataset.scope === s));
    const note = document.getElementById('scopeNote');
    if (note) note.textContent = s === 'both'
      ? 'Checks breach records and stealer logs — uses 2 searches per identifier.'
      : `Checks ${s === 'breach' ? 'breach records' : 'stealer logs'} only — uses 1 search per identifier.`;
  }
  setScope(scope);   // initialize toggle + note from saved choice

  /* ---- account dashboard / stats ---- */
  function statsLoad() {
    let s = {};
    try { s = JSON.parse(localStorage.getItem('trace_stats') || '{}'); } catch (e) {}
    if (!s.firstSeen) { s.firstSeen = Date.now(); statsSave(s); }
    s.searchesRun = s.searchesRun || 0;
    s.recordsFound = s.recordsFound || 0;
    s.robloxLookups = s.robloxLookups || 0;
    return s;
  }
  function statsSave(s) { try { localStorage.setItem('trace_stats', JSON.stringify(s)); } catch (e) {} }
  function statsBump(field, by) {
    const s = statsLoad(); s[field] = (s[field] || 0) + (by || 1); statsSave(s);
  }
  function openStats() {
    const m = document.getElementById('statsModal');
    m.style.display = 'flex';
    const s = statsLoad();
    let email = 'Guest';
    try { const u = window.netlifyIdentity && netlifyIdentity.currentUser(); if (u && u.email) email = u.email; } catch (e) {}
    document.getElementById('statsWho').textContent = email;
    document.getElementById('statsAvatar').textContent = (email[0] || 'G').toUpperCase();
    document.getElementById('stRun').textContent = s.searchesRun;
    document.getElementById('stRecords').textContent = s.recordsFound;
    document.getElementById('stRoblox').textContent = s.robloxLookups;
    document.getElementById('stMusic').textContent = (typeof mTracks !== 'undefined' ? mTracks.length : 0);
    document.getElementById('stSince').textContent = s.firstSeen ? new Date(s.firstSeen).toLocaleDateString(undefined, { month: 'short', year: '2-digit' }) : '—';
    // admin panel: only attempt to load (the backend decides if this code is really admin)
    const code0 = (document.getElementById('accessCode').value || '').trim();
    adminRefresh(code0);
    // usage from the backend for the current code
    const code = (document.getElementById('accessCode').value || '').trim();
    const fill = document.getElementById('smFill'), cnt = document.getElementById('smCount'), foot = document.getElementById('smFoot'), rem = document.getElementById('stRemaining');
    if (!code) { cnt.textContent = '—'; fill.style.width = '0%'; foot.textContent = 'Enter an access code to see usage.'; rem.textContent = '—'; return; }
    cnt.textContent = 'checking…'; foot.textContent = '';
    statsFetchUsage(code, fill, cnt, foot, rem);
  }
  async function statsFetchUsage(code, fill, cnt, foot, rem) {
    try {
      const qs = `type=status&code=${encodeURIComponent(code)}`;
      let r = await fetch(`/api/search?${qs}`);
      if (r.status === 404) r = await fetch(`/.netlify/functions/proxy?${qs}`);
      let j; try { j = await r.json(); } catch (e) { j = {}; }
      if (j.admin) { cnt.textContent = '∞'; fill.style.width = '100%'; foot.textContent = 'Admin code — unlimited searches.'; rem.textContent = '∞'; return; }
      if (r.status === 403) { cnt.textContent = '—'; fill.style.width = '0%'; foot.textContent = 'That code isn’t valid.'; rem.textContent = '—'; return; }
      const limit = j.limit || 10;
      if (j.remaining == null) { cnt.textContent = '—'; foot.textContent = 'Usage unavailable right now.'; rem.textContent = '—'; return; }
      const used = limit - j.remaining;
      cnt.textContent = `${used} / ${limit}`;
      fill.style.width = Math.round((used / limit) * 100) + '%';
      foot.textContent = `${j.remaining} search${j.remaining === 1 ? '' : 'es'} remaining on this code.`;
      rem.textContent = j.remaining;
    } catch (e) {
      cnt.textContent = '—'; foot.textContent = 'Usage unavailable right now.';
    }
  }
  function closeStats() { document.getElementById('statsModal').style.display = 'none'; }

  /* ---- admin: live code management ---- */
  async function adminApi(action, extra) {
    const code = (document.getElementById('accessCode').value || '').trim();
    let qs = `type=admin-${action}&code=${encodeURIComponent(code)}`;
    if (extra) for (const k in extra) qs += `&${k}=${encodeURIComponent(extra[k])}`;
    let r = await fetch(`/api/search?${qs}`);
    if (r.status === 404) r = await fetch(`/.netlify/functions/proxy?${qs}`);
    return r;
  }
  async function adminRefresh(code) {
    const panel = document.getElementById('adminPanel');
    if (!code) { panel.style.display = 'none'; return; }
    try {
      const r = await adminApi('list');
      if (!r.ok) { panel.style.display = 'none'; return; }   // not admin -> stay hidden
      const j = await r.json();
      panel.style.display = 'block';
      renderAdminList(j.codes || []);
    } catch (e) { panel.style.display = 'none'; }
  }
  function renderAdminList(codes) {
    const box = document.getElementById('adminList');
    if (!codes.length) { box.innerHTML = `<div class="lane-empty" style="padding:8px 2px">No codes yet — add one above.</div>`; return; }
    box.innerHTML = codes.map(c => `
      <div class="admin-row">
        <span class="admin-code">${esc(c.code)}</span>
        <span class="admin-usage">${c.used}/${c.limit}</span>
        <input class="admin-lim" type="number" min="0" value="${c.limit}" title="Search limit"
               onchange="adminSetLimit('${esc(c.code).replace(/'/g, "\\'")}', this.value)">
        <button class="admin-mini" onclick="adminReset('${esc(c.code).replace(/'/g, "\\'")}')" title="Reset usage to 0">reset</button>
        <button class="admin-x" onclick="adminDelete('${esc(c.code).replace(/'/g, "\\'")}')" title="Delete code">✕</button>
      </div>`).join('');
  }
  async function adminAdd() {
    const inp = document.getElementById('acNew'), limEl = document.getElementById('acLimit');
    const target = inp.value.trim(); if (!target) return;
    const limit = parseInt(limEl.value, 10); 
    await adminApi('add', { target, limit: isNaN(limit) ? 10 : limit });
    inp.value = '';
    adminRefresh((document.getElementById('accessCode').value || '').trim());
  }
  async function adminSetLimit(code, limit) {
    await adminApi('update', { target: code, limit: parseInt(limit, 10) || 0 });
    adminRefresh((document.getElementById('accessCode').value || '').trim());
  }
  async function adminReset(code) {
    await adminApi('reset', { target: code });
    adminRefresh((document.getElementById('accessCode').value || '').trim());
  }
  async function adminDelete(code) {
    await adminApi('delete', { target: code });
    adminRefresh((document.getElementById('accessCode').value || '').trim());
  }
  function adminGen() {
    const words = ['brisk','vex','onyx','lumen','quill','mossy','cobalt','frost','nova','slate','vortex','flare','koda','wisp','ember'];
    const w = words[Math.floor(Math.random() * words.length)];
    let rnd = '';
    const chars = 'ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz0123456789';
    const arr = new Uint8Array(16); (window.crypto || {}).getRandomValues ? crypto.getRandomValues(arr) : arr.forEach((_, i) => arr[i] = Math.random() * 256);
    for (let i = 0; i < 16; i++) rnd += chars[arr[i] % chars.length];
    document.getElementById('acNew').value = `${w}-${rnd}`;
  }

  /* ---- buy credits: pick a pack, then a payment method (mints a fresh code) ---- */
  const PACK_LABELS = { starter: '25 credits — £3', plus: '100 credits — £9', pro: '500 credits — £35' };
  let SELECTED_PACK = null;

  function openBuyMenu() { openPayMenu('plus'); }   // default selection; user can pick another in-menu

  function openPayMenu(pack) {
    SELECTED_PACK = pack;
    document.getElementById('paySub').textContent = PACK_LABELS[pack] || '';
    document.getElementById('payFoot').textContent = '';
    // reflect the chosen pack in the menu
    document.querySelectorAll('.pay-pack').forEach(b => b.classList.toggle('sel', b.getAttribute('data-pack') === pack));
    document.getElementById('payMenu').style.display = 'flex';
  }
  function selectPack(pack) { openPayMenu(pack); }
  function closePayMenu() { document.getElementById('payMenu').style.display = 'none'; }

  async function payWith(method) {
    if (!SELECTED_PACK) return;
    if (method === 'crypto') return payWithCrypto(SELECTED_PACK);
  }

  async function payWithCrypto(pack) {
    closePayMenu();
    openCryptoPicker(pack);
  }

  const CRYPTO_COINS = [
    { id: 'btc', name: 'Bitcoin', t: 'BTC' },
    { id: 'eth', name: 'Ethereum', t: 'ETH' },
    { id: 'sol', name: 'Solana', t: 'SOL' },
    { id: 'usdt', name: 'USDT', t: 'ERC-20' },
    { id: 'usdc', name: 'USDC', t: 'ERC-20' },
    { id: 'bnb', name: 'BNB', t: 'BSC' },
  ];
  let CX_POLL = null;

  function cxClose() {
    if (CX_POLL) { clearInterval(CX_POLL); CX_POLL = null; }
    const w = document.getElementById('cxModal'); if (w) w.remove();
  }
  function cxShell(inner) {
    cxClose();
    const wrap = document.createElement('div');
    wrap.id = 'cxModal'; wrap.className = 'pay-menu'; wrap.style.display = 'flex';
    wrap.onclick = (e) => { if (e.target === wrap) cxClose(); };
    wrap.innerHTML = `<div class="pay-card">${inner}</div>`;
    document.body.appendChild(wrap);
    return wrap;
  }

  function openCryptoPicker(pack) {
    const w = cxShell(`
      <button class="pay-close" onclick="cxClose()" aria-label="Close">✕</button>
      <div class="pay-title">Pay with crypto</div>
      <div class="pay-sub">${esc(PACK_LABELS[pack] || '')}</div>
      <div class="cx-coins">
        ${CRYPTO_COINS.map(c => `<button class="cx-coin" onclick="cryptoPickCoin('${pack}','${c.id}')">
          <span class="cx-coin-name">${esc(c.name)}</span><span class="cx-coin-t">${esc(c.t)}</span></button>`).join('')}
      </div>
      <p class="pay-foot">Pick a coin. You'll get an address and an exact amount to send — pay the exact amount and your code unlocks automatically once it confirms on-chain.</p>`);
    return w;
  }

  async function cryptoPickCoin(pack, coin) {
    const card = document.querySelector('#cxModal .pay-card');
    if (card) card.innerHTML = `<div class="fl-msg"><span class="spin"></span> getting a live quote…</div>`;
    try {
      const qs = `action=quote&pack=${encodeURIComponent(pack)}&coin=${encodeURIComponent(coin)}`;
      let r = await fetch(`/api/cryptopay?${qs}`);
      if (r.status === 404) r = await fetch(`/.netlify/functions/cryptopay?${qs}`);
      const j = await r.json();
      if (!j.orderId) { if (card) card.innerHTML = `<button class="pay-close" onclick="cxClose()">✕</button><div class="fl-msg flag">${esc(j.error || 'could not get a quote')}</div>`; return; }
      cryptoPayScreen(j);
    } catch (e) {
      if (card) card.innerHTML = `<button class="pay-close" onclick="cxClose()">✕</button><div class="fl-msg flag">could not reach the payment service</div>`;
    }
  }

  function cryptoPayScreen(o) {
    const qr = `https://api.qrserver.com/v1/create-qr-code/?size=170x170&bgcolor=15-17-32&color=235-235-245&data=${encodeURIComponent(o.address)}`;
    const card = document.querySelector('#cxModal .pay-card');
    card.innerHTML = `
      <button class="pay-close" onclick="cxClose()" aria-label="Close">✕</button>
      <div class="pay-title">Send ${esc(o.coinName || o.coin)}</div>
      <div class="pay-sub">≈ £${esc(String(o.gbp))} · pay the <b>exact</b> amount below</div>
      <div class="cx-qr"><img src="${esc(qr)}" alt="address QR" width="150" height="150"></div>
      <div class="cx-field"><div class="cx-l">Exact amount</div>
        <div class="cx-copyrow"><code id="cxAmt">${esc(o.amount)}</code><button class="admin-mini" onclick="cxCopy('${esc(o.amount)}',this)">copy</button></div></div>
      <div class="cx-field"><div class="cx-l">To address</div>
        <div class="cx-copyrow"><code class="cx-addr" id="cxAddr">${esc(o.address)}</code><button class="admin-mini" onclick="cxCopy('${esc(o.address)}',this)">copy</button></div></div>
      <div class="cx-status" id="cxStatus"><span class="spin"></span> waiting for payment…</div>
      <p class="pay-foot" id="cxFoot">Send the <b>exact</b> amount — a different amount won't match. Keep this open; ${o.coin === 'btc' ? 'BTC confirmations typically take 10–30 minutes.' : o.coin === 'sol' ? 'SOL confirms in seconds.' : 'confirmations typically take 1–3 minutes.'}</p>`;
    const started = Date.now();
    // BTC blocks ~10 min → poll every 2 min; SOL finalises in seconds → 10s; EVM ~12s block → 20s
    const POLL_MS = o.coin === 'btc' ? 120000 : o.coin === 'sol' ? 10000 : 20000;
    const tick = async () => {
      try {
        const qs = `action=check&order=${encodeURIComponent(o.orderId)}`;
        let r = await fetch(`/api/cryptopay?${qs}`);
        if (r.status === 404) r = await fetch(`/.netlify/functions/cryptopay?${qs}`);
        const j = await r.json();
        const st = document.getElementById('cxStatus');
        if (j.status === 'paid') {
          cxClose();
          presentCode(j.code, j.credits, true);
        } else if (j.status === 'expired') {
          if (CX_POLL) { clearInterval(CX_POLL); CX_POLL = null; }
          if (st) st.innerHTML = '<span style="color:var(--flag)">This quote expired. Close and start again for a fresh amount.</span>';
        } else if (st) {
          const mins = Math.max(0, Math.round((o.expiresAt - Date.now()) / 60000));
          st.innerHTML = `<span class="spin"></span> waiting for payment… <span class="cx-mins">(${mins}m left${j.note ? ' · ' + esc(j.note) : ''})</span>`;
        }
      } catch (e) {}
    };
    // BTC: skip the immediate pointless tick — first confirmation is at least ~10 minutes away
    if (o.coin !== 'btc') tick();
    CX_POLL = setInterval(tick, POLL_MS);
  }

  function cxCopy(text, btn) {
    navigator.clipboard.writeText(text).catch(() => {});
    const o = btn.textContent; btn.textContent = 'copied'; setTimeout(() => { btn.textContent = o; }, 1200);
  }

  // show the freshly-bought code to the buyer (called from cryptoPayScreen once on-chain confirms)
  function presentCode(code, credits, activeNow) {
    closePayMenu();
    const wrap = document.createElement('div');
    wrap.className = 'pay-menu';
    wrap.style.display = 'flex';
    wrap.onclick = (e) => { if (e.target === wrap) wrap.remove(); };
    wrap.innerHTML = `<div class="pay-card">
      <button class="pay-close" aria-label="Close">✕</button>
      <div class="pay-title">${activeNow ? 'Payment complete 🎉' : 'Payment started'}</div>
      <div class="pay-sub">${credits ? credits + ' searches' : 'Your credits'} on this code:</div>
      <div class="code-show" id="codeShow">${esc(code)}</div>
      <button class="admin-btn primary code-copy" style="width:100%;margin-top:10px">Copy code</button>
      <p class="pay-foot">${activeNow
        ? 'Save this code — paste it into the access box to start searching. It\u2019s active now.'
        : 'Save this code. It activates automatically once your crypto payment confirms on-chain (usually a few minutes).'}</p>
    </div>`;
    document.body.appendChild(wrap);
    wrap.querySelector('.pay-close').onclick = () => wrap.remove();
    wrap.querySelector('.code-copy').onclick = () => {
      navigator.clipboard.writeText(code).catch(() => {});
      wrap.querySelector('.code-copy').textContent = 'Copied ✓';
    };
  }
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape') { closeStats(); closeFullLog(); } });

  /* ---- phone lookup (Veriphone) ---- */
  function phoneValidLocal(raw) {
    const digits = (raw || '').replace(/[^\d]/g, '');
    return digits.length >= 7 && digits.length <= 15;
  }
  async function runPhone() {
    const inp = document.getElementById('phoneInput');
    const out = document.getElementById('phoneResult');
    const raw = inp.value.trim();
    const code = (document.getElementById('accessCode').value || '').trim();
    if (!raw) return;
    if (!phoneValidLocal(raw)) {
      out.innerHTML = `<div class="phone-card"><div class="fl-msg flag">That doesn't look like a valid phone number — enter 7–15 digits, ideally with a country code like +1 or +44.</div></div>`;
      return;
    }
    if (!code) {
      out.innerHTML = `<div class="phone-card"><div class="fl-msg flag">Enter your access code on the Breach Search tab first.</div></div>`;
      return;
    }
    out.innerHTML = `<div class="phone-card"><div class="fl-msg"><span class="spin"></span>Looking up…</div></div>`;
    try {
      const qs = `type=phone&q=${encodeURIComponent(raw)}&code=${encodeURIComponent(code)}`;
      const ctrl = new AbortController(); const t = setTimeout(() => ctrl.abort(), 18000);
      let r;
      try {
        r = await fetch(`/api/search?${qs}`, { signal: ctrl.signal });
        if (r.status === 404) r = await fetch(`/.netlify/functions/proxy?${qs}`, { signal: ctrl.signal });
      } finally { clearTimeout(t); }
      if (r.status === 403) { out.innerHTML = `<div class="phone-card"><div class="fl-msg flag">That access code isn't valid.</div></div>`; return; }
      let j; try { j = await r.json(); } catch (e) { j = {}; }
      out.innerHTML = renderPhone(j);
    } catch (e) {
      out.innerHTML = `<div class="phone-card"><div class="fl-msg flag">${esc(e.name === 'AbortError' ? 'request timed out' : 'lookup failed')}</div></div>`;
    }
  }
  function renderPhone(j) {
    if (j && j.invalid) return `<div class="phone-card"><div class="fl-msg flag">${esc(j.reason || 'invalid number')}</div></div>`;
    if (j && j.error === 'no key') return `<div class="phone-card"><div class="fl-msg flag">Phone lookups aren't configured yet (missing API key).</div></div>`;
    if (!j || !j.found) {
      const why = j && j.status && j.status !== 'success' ? ` (${esc(j.status)})` : '';
      return `<div class="phone-card"><div class="fl-msg">No valid result for that number${why}.</div></div>`;
    }
    const d = j.data || {};
    const valid = d.phone_valid;
    const fields = [];
    if (d.international_number) fields.push(['International', d.international_number]);
    if (d.local_number) fields.push(['Local', d.local_number]);
    if (d.e164) fields.push(['E.164', d.e164]);
    if (d.phone_type) fields.push(['Line type', d.phone_type.replace(/_/g, ' ')]);
    if (d.carrier) fields.push(['Carrier', d.carrier]);
    if (d.country) fields.push(['Country', d.country]);
    if (d.phone_region) fields.push(['Region', d.phone_region]);
    if (d.country_code) fields.push(['Country code', d.country_code]);
    if (d.country_prefix) fields.push(['Dial prefix', '+' + d.country_prefix]);
    return `<div class="phone-card">
      <div class="phone-head">
        <div class="phone-num">${esc(d.international_number || d.e164 || d.phone || '')}</div>
        <span class="phone-badge ${valid ? 'ok' : 'bad'}">${valid ? 'Valid' : 'Invalid'}</span>
      </div>
      <div class="rbx-grid phone-grid">
        ${fields.map(([l, v]) => `<div class="rbx-field"><div class="l">${esc(l)}</div><div class="v">${esc(String(v))}</div></div>`).join('')}
      </div>
    </div>`;
  }

  /* ---- access code: blur toggle + live remaining-searches check ---- */
  const EYE_OPEN = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none"><path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7-10-7-10-7z" stroke="currentColor" stroke-width="1.7"/><circle cx="12" cy="12" r="3" stroke="currentColor" stroke-width="1.7"/></svg>';
  const EYE_OFF = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none"><path d="M3 3l18 18" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/><path d="M10.6 6.2A9.9 9.9 0 0 1 12 5c6.5 0 10 7 10 7a17 17 0 0 1-3.3 4.1M6.5 7.6A17 17 0 0 0 2 12s3.5 7 10 7a9.7 9.7 0 0 0 3.4-.6" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/><path d="M9.5 10.6a3 3 0 0 0 4 4" stroke="currentColor" stroke-width="1.7"/></svg>';
  function toggleCodeBlur() {
    const inp = document.getElementById('accessCode'), eye = document.getElementById('keyEye');
    const nowMasked = inp.classList.toggle('masked');
    eye.innerHTML = nowMasked ? EYE_OPEN : EYE_OFF;
  }
  let codeCheckTimer = null;
  function onCodeInput() {
    const code = document.getElementById('accessCode').value.trim();
    try { localStorage.setItem('trace_code', code); } catch (e) {}
    const el = document.getElementById('keyRemaining');
    el.className = 'key-remaining'; el.textContent = '';
    clearTimeout(codeCheckTimer);
    if (code.length < 4) return;
    codeCheckTimer = setTimeout(() => checkCodeStatus(code), 450);
  }
  async function checkCodeStatus(code) {
    const el = document.getElementById('keyRemaining');
    el.className = 'key-remaining show'; el.textContent = 'checking…';
    try {
      const qs = `type=status&code=${encodeURIComponent(code)}`;
      const ctrl = new AbortController(); const t = setTimeout(() => ctrl.abort(), 12000);
      let r;
      try {
        r = await fetch(`/api/search?${qs}`, { signal: ctrl.signal });
        if (r.status === 404) r = await fetch(`/.netlify/functions/proxy?${qs}`, { signal: ctrl.signal });
      } finally { clearTimeout(t); }
      if (document.getElementById('accessCode').value.trim() !== code) return; // changed since
      if (r.status === 403) { el.className = 'key-remaining show flag'; el.textContent = 'invalid code'; return; }
      let j; try { j = await r.json(); } catch (e) { j = {}; }
      if (j.admin) { el.className = 'key-remaining show clear'; el.textContent = 'admin · unlimited'; return; }
      if (j.unknown || j.remaining == null) { el.className = 'key-remaining show'; el.textContent = ''; return; }
      const n = j.remaining;
      el.className = 'key-remaining show ' + (n === 0 ? 'flag' : n <= 3 ? 'flag' : 'clear');
      el.textContent = `${n} search${n === 1 ? '' : 'es'} left`;
    } catch (e) {
      el.className = 'key-remaining'; el.textContent = '';
    }
  }

  (function initCode() {
    const eye = document.getElementById('keyEye'); if (eye) eye.innerHTML = EYE_OPEN;
    try {
      const sc = localStorage.getItem('trace_code');
      if (sc) { document.getElementById('accessCode').value = sc; if (sc.trim().length >= 4) checkCodeStatus(sc.trim()); }
    } catch (e) {}
  })();
  function addId() {
    const list = document.getElementById('ids');
    const row = document.createElement('div'); row.className = 'id-row';
    row.innerHTML = `<input type="text" placeholder="email, username, or domain" autocomplete="off" spellcheck="false">
      <button class="del" onclick="this.parentElement.remove()">×</button>`;
    list.appendChild(row); row.querySelector('input').focus();
  }
  function getIds() { return Array.from(document.querySelectorAll('#ids input')).map(i => i.value.trim()).filter(Boolean); }
  function esc(s) { return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;'); }
  function redact(v) { return v ? esc(v) : ''; }

  let lastRemaining = null;
  async function callProxy(endpoint, q, code) {
    const qs = `type=${encodeURIComponent(endpoint)}&q=${encodeURIComponent(q)}&code=${encodeURIComponent(code)}`;
    const fetchWithTimeout = async (url) => {
      const ctrl = new AbortController();
      const t = setTimeout(() => ctrl.abort(), 25000);
      try { return await fetch(url, { signal: ctrl.signal }); }
      finally { clearTimeout(t); }
    };
    let r;
    try {
      r = await fetchWithTimeout(`/api/search?${qs}`);
      if (r.status === 404) r = await fetchWithTimeout(`/.netlify/functions/proxy?${qs}`);
    } catch (e) {
      throw new Error(e.name === 'AbortError' ? 'request timed out' : 'network error');
    }
    const rem = r.headers.get('X-RateLimit-Remaining');
    if (rem !== null) lastRemaining = parseInt(rem, 10);
    let j;
    try { j = await r.json(); } catch (e) { j = {}; }
    if (!r.ok) {
      const err = new Error(j.error || `service responded ${r.status}`);
      err.status = r.status; err.resetAt = j.resetAt;
      throw err;
    }
    return j;
  }
  function fmtReset(ts) {
    if (!ts) return '';
    const ms = ts - Date.now();
    if (ms <= 0) return 'now';
    const h = Math.floor(ms / 3600000), m = Math.round((ms % 3600000) / 60000);
    return h > 0 ? `${h}h ${m}m` : `${m}m`;
  }
  async function run() {
    const code = document.getElementById('accessCode').value.trim();
    if (!code) { loadSample(); return; }
    try { localStorage.setItem('trace_code', code); } catch (e) {}
    const ids = getIds();
    if (!ids.length) { flashStatus('Add at least one identifier to check.'); return; }
    const btn = document.getElementById('runBtn'), status = document.getElementById('status');
    btn.disabled = true; scanlineOn();
    const results = []; let total = 0; let blocked = null;
    SEARCH_SCOPE = scope;   // remember what we actually searched for, for the render
    try {
      for (let i = 0; i < ids.length; i++) {
        const q = ids[i];
        status.innerHTML = `<span class="spin"></span>scanning ${i+1}/${ids.length} — ${esc(q)}`;
        const res = { query: q, breach: null, stealer: null, errors: [] };
        if (scope === 'breach' || scope === 'both') {
          try { const d = await callProxy('breach', q, code); res.breach = d?.data?.items || []; total += res.breach.length; }
          catch (e) { if (e.status === 429 || e.status === 403 || e.status === 401 || e.status === 503) { blocked = e; break; } res.errors.push('Breaches — ' + e.message); }
        }
        if (blocked) break;
        if (scope === 'stealer' || scope === 'both') {
          try { const d = await callProxy('stealer', q, code); res.stealer = d?.data?.items || []; total += res.stealer.length; }
          catch (e) { if (e.status === 429 || e.status === 403 || e.status === 401 || e.status === 503) { blocked = e; break; } res.errors.push('Stealer logs — ' + e.message); }
        }
        results.push(res);
        if (blocked) break;
        if (i < ids.length - 1) await new Promise(r => setTimeout(r, 350));
      }
    } catch (e) {
      scanlineOff(); btn.disabled = false;
      const rep0 = document.getElementById('report'); rep0.classList.remove('wide');
      rep0.innerHTML = `<div class="empty"><p style="color:var(--flag)">Something went wrong: ${esc(e.message || 'unknown error')}. Please try again.</p></div>`;
      return;
    }
    scanlineOff(); btn.disabled = false; status.textContent = '';

    if (blocked) {
      if (blocked.status === 503) {
        status.innerHTML = `<span style="color:var(--flag)">This service is down for a while — contact the developers on <a href="https://discord.gg/tracercodes" target="_blank" rel="noopener" style="color:var(--violet-2);text-decoration:underline">Discord</a> for more info. (Your search wasn\u2019t counted.)</span>`;
        try { if (results.length) render(results, total); } catch (e) {}
        return;
      }
      let msg;
      if (blocked.status === 403) msg = 'That access code isn\u2019t valid.';
      else if (blocked.status === 401) msg = 'An access code is required.';
      else msg = 'This code has ran out of searches.';
      status.innerHTML = `<span style="color:var(--flag)">${esc(msg)}</span>`;
      try { if (results.length) render(results, total); } catch (e) {}
      return;
    }
    if (lastRemaining !== null) {
      status.innerHTML = `<span style="color:var(--muted)">${lastRemaining} search${lastRemaining === 1 ? '' : 'es'} left</span>`;
      const el = document.getElementById('keyRemaining');
      if (el) { el.className = 'key-remaining show ' + (lastRemaining <= 3 ? 'flag' : 'clear'); el.textContent = `${lastRemaining} search${lastRemaining === 1 ? '' : 'es'} left`; }
    }
    try { render(results, total); statsBump('searchesRun', results.length); statsBump('recordsFound', total); }
    catch (e) {
      const repE = document.getElementById('report'); repE.classList.remove('wide');
      repE.innerHTML = `<div class="empty"><p style="color:var(--flag)">Couldn't display results: ${esc(e.message || 'render error')}.</p></div>`;
    }
    // also try resolving the identifiers as Roblox usernames (free via RoProxy)
    lookupRoblox(ids, code);
  }

  /* ============ ROBLOX PROFILE (RoProxy) ============ */
  async function robloxCall(q, code) {
    const qs = `type=roblox&q=${encodeURIComponent(q)}&code=${encodeURIComponent(code)}`;
    const ctrl = new AbortController(); const t = setTimeout(() => ctrl.abort(), 20000);
    let r;
    try {
      r = await fetch(`/api/search?${qs}`, { signal: ctrl.signal });
      if (r.status === 404) r = await fetch(`/.netlify/functions/proxy?${qs}`, { signal: ctrl.signal });
    } finally { clearTimeout(t); }
    if (!r.ok) return null;
    try { return await r.json(); } catch (e) { return null; }
  }
  async function lookupRoblox(ids, code) {
    const lane = document.getElementById('robloxLane');
    if (!lane) return;
    lane.innerHTML = `<div class="lane-empty"><span class="spin"></span> Checking…</div>`;
    const rbx = [], xbl = [], twt = [];
    for (const q of ids) {
      try { const p = await robloxCall(q, code); if (p && p.found) rbx.push(p); } catch (e) {}
      try { const x = await xboxCall(q, code); if (x && x.found) xbl.push(x); } catch (e) {}
      try { const t2 = await twitterCall(q, code); if (t2 && t2.found) twt.push(t2); } catch (e) {}
    }
    const cur = document.getElementById('robloxLane');   // may have been rebuilt; re-grab
    if (!cur) return;
    if (rbx.length) statsBump('robloxLookups', rbx.length);
    const html = rbx.map(renderRobloxCard).join('') + xbl.map(renderXboxCard).join('') + twt.map(renderTwitterCard).join('');
    cur.innerHTML = html || `<div class="lane-empty">No Roblox, Xbox or X account found.</div>`;
  }

  async function twitterCall(q, code) {
    const qs = `type=twitter&q=${encodeURIComponent(q)}&code=${encodeURIComponent(code)}`;
    const ctrl = new AbortController(); const t = setTimeout(() => ctrl.abort(), 15000);
    let r;
    try {
      r = await fetch(`/api/search?${qs}`, { signal: ctrl.signal });
      if (r.status === 404) r = await fetch(`/.netlify/functions/proxy?${qs}`, { signal: ctrl.signal });
    } finally { clearTimeout(t); }
    if (!r.ok) return null;
    try { return await r.json(); } catch (e) { return null; }
  }

  async function xboxCall(q, code) {
    const qs = `type=xbox&q=${encodeURIComponent(q)}&code=${encodeURIComponent(code)}`;
    const ctrl = new AbortController(); const t = setTimeout(() => ctrl.abort(), 18000);
    let r;
    try {
      r = await fetch(`/api/search?${qs}`, { signal: ctrl.signal });
      if (r.status === 404) r = await fetch(`/.netlify/functions/proxy?${qs}`, { signal: ctrl.signal });
    } finally { clearTimeout(t); }
    if (!r.ok) return null;
    try { return await r.json(); } catch (e) { return null; }
  }

  function renderXboxCard(p) {
    const fields = [];
    if (p.xuid) fields.push(['XUID', p.xuid]);
    if (p.gamerscore !== '' && p.gamerscore != null) fields.push(['Gamerscore', Number(p.gamerscore).toLocaleString()]);
    if (p.tier) fields.push(['Tier', p.tier]);
    if (p.tenure !== '' && p.tenure != null) fields.push(['Tenure', p.tenure + (Number(p.tenure) === 1 ? ' year' : ' years')]);
    if (p.rep) fields.push(['Reputation', p.rep]);
    if (p.presence) fields.push(['Status', p.presence]);
    if (p.followers !== '' && p.followers != null) fields.push(['Followers', Number(p.followers).toLocaleString()]);
    if (p.following !== '' && p.following != null) fields.push(['Following', Number(p.following).toLocaleString()]);
    if (p.location) fields.push(['Location', p.location]);
    if (p.realName) fields.push(['Real name', p.realName]);
    return `<div class="rbx-card xbl-card">
      <div class="rbx-head">
        <div class="rbx-avatar xbl-avatar">${p.avatarUrl ? `<img src="${esc(p.avatarUrl)}" alt="" referrerpolicy="no-referrer">` : ICON_XBL}</div>
        <div class="rbx-id-head">
          <div class="xbl-badge">${ICON_XBL_SM} Xbox</div>
          <div class="rbx-display">${esc(p.gamertag || 'Unknown')}</div>
        </div>
      </div>
      <div class="rbx-grid">
        ${fields.map(([l, v]) => `<div class="rbx-field"><div class="l">${esc(l)}</div><div class="v">${esc(String(v))}</div></div>`).join('')}
      </div>
      ${p.bio ? `<div class="rbx-past"><div class="rbx-past-title">Bio</div><div class="xbl-bio">${esc(p.bio)}</div></div>` : ''}
    </div>`;
  }
  const ICON_XBL = '<svg width="32" height="32" viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="1.5"/><path d="M5 18C7 13 10 9 12 7c2 2 5 6 7 11M8 5c2 1 3 2 4 3 1-1 2-2 4-3" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>';
  const ICON_XBL_SM = '<svg width="11" height="11" viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="2"/><path d="M5 18C7 13 10 9 12 7c2 2 5 6 7 11" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>';
  const ICON_X = '<svg width="30" height="30" viewBox="0 0 24 24" fill="currentColor"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>';
  const ICON_X_SM = '<svg width="10" height="10" viewBox="0 0 24 24" fill="currentColor"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>';
  const ICON_VERIFIED = '<svg width="14" height="14" viewBox="0 0 24 24" fill="#1d9bf0" style="vertical-align:-2px"><path d="M12 2l2.4 1.8 3-.1 1 2.8 2.4 1.7-.9 2.9.9 2.9-2.4 1.7-1 2.8-3-.1L12 22l-2.4-1.8-3 .1-1-2.8L3.2 16l.9-2.9L3.2 10l2.4-1.7 1-2.8 3 .1z"/><path d="M8.5 12.5l2.2 2.2 4.3-4.6" stroke="#fff" stroke-width="1.6" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>';

  function renderTwitterCard(p) {
    const fields = [];
    if (p.followers !== '' && p.followers != null) fields.push(['Followers', Number(p.followers).toLocaleString()]);
    if (p.following !== '' && p.following != null) fields.push(['Following', Number(p.following).toLocaleString()]);
    if (p.tweets !== '' && p.tweets != null) fields.push(['Posts', Number(p.tweets).toLocaleString()]);
    if (p.location) fields.push(['Location', p.location]);
    if (p.created) { const d = new Date(p.created); if (!isNaN(d)) fields.push(['Joined', d.toLocaleDateString(undefined, { year: 'numeric', month: 'long' })]); }
    if (p.id) fields.push(['User ID', p.id]);
    return `<div class="rbx-card x-card">
      <div class="rbx-head">
        <div class="rbx-avatar x-avatar">${p.avatarUrl ? `<img src="${esc(p.avatarUrl)}" alt="" referrerpolicy="no-referrer">` : ICON_X}</div>
        <div class="rbx-id-head">
          <div class="x-badge">${ICON_X_SM} X</div>
          <div class="rbx-display">${esc(p.name || p.username)} ${p.verified ? ICON_VERIFIED : ''}</div>
          <div class="rbx-user">@${esc(p.username)}</div>
        </div>
      </div>
      <div class="rbx-grid">
        ${fields.map(([l, v]) => `<div class="rbx-field"><div class="l">${esc(l)}</div><div class="v">${esc(String(v))}</div></div>`).join('')}
      </div>
      ${p.bio ? `<div class="rbx-past"><div class="rbx-past-title">Bio</div><div class="xbl-bio">${esc(p.bio)}</div></div>` : ''}
    </div>`;
  }
  function renderRobloxCard(p) {
    const created = p.created ? new Date(p.created).toLocaleDateString(undefined, { year: 'numeric', month: 'long', day: 'numeric' }) : '—';
    const ageYears = p.created ? ((Date.now() - new Date(p.created).getTime()) / 31557600000) : 0;
    const ageStr = p.created ? `${ageYears.toFixed(1)} years old` : '';
    const past = (p.pastUsernames || []).filter(Boolean);
    return `<div class="rbx-card">
      <div class="rbx-head">
        <div class="rbx-avatar">${p.avatarUrl ? `<img src="${esc(p.avatarUrl)}" alt="">` : ICON_RBX}</div>
        <div class="rbx-id-head">
          <div class="rbx-display">${esc(p.displayName || p.name || 'Unknown')}</div>
          <div class="rbx-username">@${esc(p.name || '')}</div>
          ${p.isBanned ? '<span class="rbx-banned">BANNED</span>' : ''}
        </div>
      </div>
      <div class="rbx-grid">
        <div class="rbx-field"><div class="l">User ID</div><div class="v">${esc(String(p.id))}</div></div>
        <div class="rbx-field"><div class="l">Created</div><div class="v">${esc(created)}${ageStr ? ` · ${esc(ageStr)}` : ''}</div></div>
        ${(p.value != null) ? `<div class="rbx-field rbx-value"><div class="l">Value (Rolimons)</div><div class="v">${esc(Number(p.value).toLocaleString())} R$</div></div>` : ''}
      </div>
      <div class="rbx-past">
        <div class="rbx-past-title">Past usernames${past.length ? ` (${past.length})` : ''}</div>
        ${past.length ? `<div class="rbx-tags">${past.map(u => `<button class="rbx-tag" onclick="rbxTagMenu(this, '${esc(u).replace(/'/g, "\\'")}')">${esc(u)}</button>`).join('')}</div>` : '<div class="rbx-none">None on record.</div>'}
      </div>
    </div>`;
  }
  const ICON_RBX = '<svg width="34" height="34" viewBox="0 0 24 24" fill="none"><rect x="4" y="4" width="16" height="16" rx="3" stroke="currentColor" stroke-width="1.5"/><rect x="10" y="10" width="4" height="4" fill="currentColor"/></svg>';

  let rbxMenuEl = null;
  function rbxCloseMenu() { if (rbxMenuEl) { rbxMenuEl.remove(); rbxMenuEl = null; } }
  function rbxTagMenu(btn, username) {
    rbxCloseMenu();
    const menu = document.createElement('div');
    menu.className = 'rbx-menu';
    menu.innerHTML = `
      <div class="rbx-menu-name">${esc(username)}</div>
      <button class="rbx-menu-item" data-act="search">Search this username</button>
      <button class="rbx-menu-item" data-act="osint">Send to OSINT web</button>`;
    document.body.appendChild(menu);
    const r = btn.getBoundingClientRect();
    menu.style.top = (r.bottom + window.scrollY + 6) + 'px';
    menu.style.left = Math.min(r.left + window.scrollX, window.innerWidth - 220) + 'px';
    menu.querySelector('[data-act="search"]').onclick = () => { rbxCloseMenu(); rbxSearchUsername(username); };
    menu.querySelector('[data-act="osint"]').onclick = () => { rbxCloseMenu(); osintInit(); osintAddBox('Username', username); osintRender(); flashStatus('Sent “' + username + '” to OSINT web.'); };
    rbxMenuEl = menu;
    setTimeout(() => document.addEventListener('click', rbxMenuOutside), 0);
  }
  function rbxMenuOutside(e) {
    if (rbxMenuEl && !rbxMenuEl.contains(e.target)) { rbxCloseMenu(); document.removeEventListener('click', rbxMenuOutside); }
  }
  function rbxSearchUsername(username) {
    // put it into the first identifier box (clear extras) and run a check
    const list = document.getElementById('ids');
    list.innerHTML = `<div class="id-row"><input type="text" placeholder="email, username, or domain" autocomplete="off" spellcheck="false"></div>`;
    list.querySelector('input').value = username;
    switchTab('search');
    window.scrollTo({ top: 0, behavior: 'smooth' });
    run();
  }
  function flashStatus(msg) {
    const s = document.getElementById('status'); s.textContent = msg;
    setTimeout(() => { if (s.textContent === msg) s.textContent = ''; }, 3500);
  }
  function scanlineOn() {
    document.getElementById('report').innerHTML =
      `<div class="report-frame" style="min-height:120px"><div class="scanline go"></div>
       <div style="padding:40px 24px;text-align:center;color:var(--faint);font-family:var(--mono);font-size:12px;letter-spacing:1px">RUNNING CHECK…</div></div>`;
  }
  function scanlineOff() { const sl = document.querySelector('.scanline'); if (sl) sl.classList.remove('go'); }
  function copyField(btn) {
    const v = btn.getAttribute('data-v') || '';
    navigator.clipboard.writeText(v).then(() => {
      btn.classList.add('done');
      const orig = btn.innerHTML;
      btn.innerHTML = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none"><path d="M5 12l4.5 4.5L19 7" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>';
      setTimeout(() => { btn.classList.remove('done'); btn.innerHTML = orig; }, 1100);
    }).catch(() => {});
  }
  const COPY_ICON = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none"><rect x="9" y="9" width="11" height="11" rx="2" stroke="currentColor" stroke-width="1.6"/><path d="M5 15V5a2 2 0 0 1 2-2h10" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>';
  const SEND_ICON = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none"><circle cx="6" cy="12" r="2.4" stroke="currentColor" stroke-width="1.6"/><circle cx="18" cy="6" r="2.4" stroke="currentColor" stroke-width="1.6"/><circle cx="18" cy="18" r="2.4" stroke="currentColor" stroke-width="1.6"/><path d="M8.2 11l7.6-4M8.2 13l7.6 4" stroke="currentColor" stroke-width="1.6"/></svg>';

  function kvBox(label, value, opts) {
    if (!value) return '';
    opts = opts || {};
    const safe = esc(value);
    const asLink = opts.link && /^https?:\/\//i.test(value);
    const valHtml = asLink
      ? `<a class="kv-val" href="${safe}" target="_blank" rel="noopener" title="${safe}">${safe}</a>`
      : `<span class="kv-val" title="${safe}">${safe}</span>`;
    return `<div class="kv">
      <div class="kv-label">${esc(label)}</div>
      <div class="kv-row">
        ${valHtml}
        <div class="kv-actions">
          <button class="cp send" data-type="${esc(label)}" data-v="${safe}" onclick="sendFieldToOsint(this)" aria-label="Send to OSINT web">${SEND_ICON}<span class="cp-tip">Send to OSINT web</span></button>
          <button class="cp" data-v="${safe}" onclick="copyField(this)" aria-label="Copy">${COPY_ICON}<span class="cp-tip">Copy</span></button>
        </div>
      </div>
    </div>`;
  }

  // Send a single field as its own box on the OSINT canvas
  function sendFieldToOsint(btn) {
    const type = btn.getAttribute('data-type') || 'Note';
    const value = btn.getAttribute('data-v') || '';
    osintInit();
    osintAddBox(type, value);
    osintRender();
    btn.classList.add('done');
    setTimeout(() => btn.classList.remove('done'), 1000);
  }

  const PAGE_SIZE = 10;
  const REPORT = { sections: {} };
  let SEARCH_SCOPE = 'both';   // which lanes to show (set per search)

  function recCard(it, type) {
    const realSource = it.dbname || it.source || '';
    const source = realSource || (type === 'stealer' ? '' : 'unknown source');
    const seen = it.indexed_at ? String(it.indexed_at).slice(0, 10) : '';
    const all = [];
    if (it.domain)   all.push(`url: ${it.domain}`);
    if (it.email)    all.push(`email: ${it.email}`);
    if (it.username) all.push(`username: ${it.username}`);
    if (it.password) all.push(`password: ${it.password}`);
    if (seen)        all.push(`seen: ${seen}`);
    const allText = esc(all.join('\n'));
    const logId = it.log_id || it.logId || it.id || '';
    const sig = recSig(it, type);
    const isChecked = CHECKED.has(sig);

    return `<div class="rec${isChecked ? ' checked' : ''}" data-sig="${esc(sig)}">
      <div class="rec-head">
        <div class="rec-head-left">
          ${type === 'stealer' ? '<span class="tag-stealer">STEALER LOG</span>' : ''}
          ${source ? `<span class="src">${esc(source)}</span>` : ''}
        </div>
        <div class="rec-head-right">
          <label class="rec-check" title="Mark as checked to minimize">
            <input type="checkbox" ${isChecked ? 'checked' : ''} onchange="toggleChecked(this)"><span>Checked</span>
          </label>
          <button class="copy-all" data-v="${allText}" onclick="copyField(this)">${COPY_ICON}<span>Copy all</span></button>
        </div>
      </div>
      <div class="rec-body">
        ${it.domain ? `<div class="rec-url">${kvBox('URL / Host', it.domain, { link: true })}</div>` : ''}
        <div class="kv-grid">
          ${kvBox('Email', it.email)}
          ${kvBox('Username', it.username)}
          ${kvBox('Password', it.password)}
        </div>
        ${seen ? `<div class="rec-seen">seen ${esc(seen)}</div>` : ''}
        ${type === 'stealer' && logId ? `
          <button class="view-log" data-logid="${esc(String(logId))}" onclick="openFullLog(this)">
            <svg class="vl-chev" width="13" height="13" viewBox="0 0 24 24" fill="none"><path d="M9 6l6 6-6 6" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
            View full log <span class="vl-cost">· uses 1 search</span>
          </button>` : ''}
      </div>
    </div>`;
  }

  // remember which records are "checked" (collapsed), surviving filter/pagination re-renders
  const CHECKED = new Set();
  function recSig(it, type) {
    return `${type}|${it.dbname || it.source || ''}|${it.domain || ''}|${it.email || ''}|${it.username || ''}|${it.password || ''}|${it.log_id || it.id || ''}`;
  }
  function toggleChecked(box) {
    const card = box.closest('.rec');
    if (!card) return;
    const sig = card.getAttribute('data-sig');
    if (box.checked) { card.classList.add('checked'); if (sig) CHECKED.add(sig); }
    else { card.classList.remove('checked'); if (sig) CHECKED.delete(sig); }
  }

  // Victim log browser: manifest = folder/file tree, then open individual files.
  // Each OathNet call (manifest, each file) costs 1 search; cached so reopening is free.
  let VL = null;            // { logId, tree, files:{id:text}, openId, sample }
  let CURRENT_LOG = null;

  function openFullLog(btn) {
    const logId = btn.getAttribute('data-logid');
    CURRENT_LOG = logId;
    const win = document.getElementById('flWindow');
    document.getElementById('flTitle').textContent = 'Stealer log';
    document.getElementById('fullLogModal').style.display = 'block';
    win.style.left = Math.max((window.innerWidth - win.offsetWidth) / 2, 12) + 'px';
    win.style.top = Math.max((window.innerHeight - win.offsetHeight) / 2, 40) + 'px';

    // same log already loaded this session — show it again for free
    if (VL && VL.logId === logId) { paintVictim(); return; }

    // preview (no code/backend)
    if (String(logId).startsWith('sample-log-')) {
      VL = { logId, tree: sampleManifest(), files: { 'f1': sampleFileText() }, openId: null, sample: true };
      paintVictim();
      return;
    }
    fetchManifest(logId);
  }

  function updateRemainingFromHeaders(r) {
    const rem = r.headers.get('X-RateLimit-Remaining');
    if (rem === null) return;
    lastRemaining = parseInt(rem, 10);
    const st = document.getElementById('status');
    if (st && !isNaN(lastRemaining)) st.innerHTML = `<span style="color:var(--muted)">${lastRemaining} search${lastRemaining === 1 ? '' : 'es'} left</span>`;
    const ke = document.getElementById('keyRemaining');
    if (ke && !isNaN(lastRemaining)) { ke.className = 'key-remaining show ' + (lastRemaining <= 3 ? 'flag' : 'clear'); ke.textContent = `${lastRemaining} search${lastRemaining === 1 ? '' : 'es'} left`; }
  }
  function flError(r, j) {
    return r.status === 429 ? 'Not enough searches left for this lookup.'
      : r.status === 403 ? 'That access code isn\u2019t valid.'
      : r.status === 503 ? 'Service is down for a while — contact the developers on Discord (discord.gg/tracercodes).'
      : ((j && j.error) || `service responded ${r.status}`);
  }

  async function fetchManifest(logId) {
    const content = document.getElementById('flContent');
    const code = (document.getElementById('accessCode').value || '').trim();
    if (!code) { content.innerHTML = `<div class="fl-msg flag">Enter your access code first.</div>`; return; }
    content.innerHTML = `<div class="fl-msg"><span class="spin"></span>loading file tree…</div>`;
    try {
      const qs = `type=manifest&log_id=${encodeURIComponent(logId)}&code=${encodeURIComponent(code)}`;
      let r = await fetch(`/api/search?${qs}`);
      if (r.status === 404) r = await fetch(`/.netlify/functions/proxy?${qs}`);
      updateRemainingFromHeaders(r);
      let j; try { j = await r.json(); } catch (e) { j = {}; }
      if (!r.ok) { content.innerHTML = `<div class="fl-msg flag">${esc(flError(r, j))}</div>`; return; }
      const tree = j.victim_tree || (j.data && j.data.victim_tree) || null;
      VL = { logId, tree, logName: j.log_name || (j.data && j.data.log_name) || '', files: {}, openId: null, sample: false };
      if (CURRENT_LOG === logId) paintVictim();
    } catch (e) {
      content.innerHTML = `<div class="fl-msg flag">${esc(e.name === 'AbortError' ? 'request timed out' : 'could not load file tree')}</div>`;
    }
  }

  async function openVictimFile(fileId) {
    if (!VL) return;
    VL.openId = fileId;
    // cached already → free, just repaint
    if (VL.files[fileId] != null) { paintVictim(); return; }
    if (VL.sample) { VL.files[fileId] = sampleFileText(); paintVictim(); return; }
    paintVictim(true);  // show tree + a loading state in the file pane
    const code = (document.getElementById('accessCode').value || '').trim();
    try {
      const qs = `type=file&log_id=${encodeURIComponent(VL.logId)}&file_id=${encodeURIComponent(fileId)}&code=${encodeURIComponent(code)}`;
      let r = await fetch(`/api/search?${qs}`);
      if (r.status === 404) r = await fetch(`/.netlify/functions/proxy?${qs}`);
      updateRemainingFromHeaders(r);
      const text = await r.text();
      if (!r.ok) {
        let j = {}; try { j = JSON.parse(text); } catch (e) {}
        VL.files[fileId] = `⚠ ${flError(r, j)}`;
      } else {
        VL.files[fileId] = text || '(empty file)';
      }
      paintVictim();
    } catch (e) {
      VL.files[fileId] = '⚠ could not load file';
      paintVictim();
    }
  }

  // flatten the tree into rows for display (folders then files), tracking depth
  function flattenTree(node, depth, out) {
    if (!node) return out;
    if (Array.isArray(node.children)) {
      // directory
      if (node.name && node.name !== '/') out.push({ kind: 'dir', name: node.name, depth });
      const kids = node.children.slice().sort((a, b) => {
        const ad = Array.isArray(a.children) ? 0 : 1, bd = Array.isArray(b.children) ? 0 : 1;
        return ad - bd || String(a.name).localeCompare(String(b.name));
      });
      kids.forEach(c => flattenTree(c, node.name && node.name !== '/' ? depth + 1 : depth, out));
    } else {
      out.push({ kind: 'file', name: node.name, id: node.id, size: node.size_bytes, depth });
    }
    return out;
  }
  function humanSize(n) {
    if (!Number.isFinite(n)) return '';
    if (n < 1024) return n + ' B';
    if (n < 1024 * 1024) return (n / 1024).toFixed(1) + ' KB';
    return (n / 1048576).toFixed(1) + ' MB';
  }

  // visible rows honouring collapse state (all folders folded by default)
  function victimVisibleRows() {
    const exp = VL.expanded || (VL.expanded = new Set());
    const out = [];
    (function walk(node, depth, myKey, isRoot) {
      if (!node) return;
      if (Array.isArray(node.children)) {
        let childDepth = depth;
        if (!isRoot) {
          const expanded = exp.has(myKey);
          out.push({ kind: 'dir', name: node.name, depth, key: myKey, expanded, count: node.children.length });
          if (!expanded) return;
          childDepth = depth + 1;
        }
        const kids = node.children.slice().sort((a, b) => {
          const ad = Array.isArray(a.children) ? 0 : 1, bd = Array.isArray(b.children) ? 0 : 1;
          return ad - bd || String(a.name).localeCompare(String(b.name));
        });
        kids.forEach((c, i) => walk(c, childDepth, myKey + '>' + i, false));
      } else {
        out.push({ kind: 'file', name: node.name, id: node.id, size: node.size_bytes, depth });
      }
    })(VL.tree, 0, 'r', true);
    return out;
  }
  function collectFolderKeys() {
    const keys = [];
    (function walk(node, myKey, isRoot) {
      if (!node || !Array.isArray(node.children)) return;
      if (!isRoot) keys.push(myKey);
      const kids = node.children.slice().sort((a, b) => {
        const ad = Array.isArray(a.children) ? 0 : 1, bd = Array.isArray(b.children) ? 0 : 1;
        return ad - bd || String(a.name).localeCompare(String(b.name));
      });
      kids.forEach((c, i) => walk(c, myKey + '>' + i, false));
    })(VL.tree, 'r', true);
    return keys;
  }
  function vtToggle(key) {
    if (!VL) return;
    VL.expanded = VL.expanded || new Set();
    if (VL.expanded.has(key)) VL.expanded.delete(key); else VL.expanded.add(key);
    paintVictim();
  }
  function vtExpandAll() { if (VL) { VL.expanded = new Set(collectFolderKeys()); paintVictim(); } }
  function vtCollapseAll() { if (VL) { VL.expanded = new Set(); paintVictim(); } }

  function paintVictim(fileLoading) {
    const content = document.getElementById('flContent');
    if (!VL) { content.innerHTML = `<div class="fl-msg">No data.</div>`; return; }
    if (!VL.tree) { content.innerHTML = `<div class="fl-msg">This log has no file tree.</div>`; return; }
    const rows = victimVisibleRows();
    const treeHtml = rows.map(row => {
      if (row.kind === 'dir') {
        return `<div class="vt-row vt-dir" onclick="vtToggle('${row.key}')" style="padding-left:${8 + row.depth * 14}px">
          <span class="vt-chev${row.expanded ? ' open' : ''}">▸</span>${FOLDER_ICON}<span class="vt-name">${esc(row.name)}</span>
          <span class="vt-size">${row.count}</span>
        </div>`;
      }
      const active = VL.openId === row.id ? ' active' : '';
      const cached = VL.files[row.id] != null;
      return `<div class="vt-row vt-file${active}" style="padding-left:${8 + row.depth * 14 + 16}px" onclick="openVictimFile('${esc(String(row.id)).replace(/'/g, "\\'")}')">
        ${FILE_ICON}<span class="vt-name">${esc(row.name)}</span>
        <span class="vt-size">${cached ? '' : '<span class=\"vt-cost\">1</span>'}${row.size != null ? esc(humanSize(row.size)) : ''}</span>
      </div>`;
    }).join('');
    const toolbar = `<div class="vt-bar">
      <button class="vt-btn" onclick="vtExpandAll()">Expand all</button>
      <button class="vt-btn" onclick="vtCollapseAll()">Collapse all</button>
    </div>`;

    let pane;
    if (fileLoading) {
      pane = `<div class="fl-msg"><span class="spin"></span>opening file…</div>`;
    } else if (VL.openId && VL.files[VL.openId] != null) {
      const name = (flattenTree(VL.tree, 0, []).find(r => r.id === VL.openId) || {}).name || 'file';
      pane = `<div class="vfile-head"><span>${esc(name)}</span>
        <span class="vfile-actions">
          <button class="admin-mini" onclick="downloadVictimFile()">download</button>
          <button class="admin-mini" onclick="copyVictimFile()">copy</button>
        </span></div>
        <pre class="vfile-body" id="vfileBody">${esc(VL.files[VL.openId])}</pre>`;
    } else {
      pane = `<div class="fl-msg">Select a file from the tree to view its contents. Each file opens for 1 search; files you've already opened are free to reopen.</div>`;
    }

    content.innerHTML = `<div class="vbrowser">
      <div class="vtree">${toolbar}${treeHtml || '<div class="fl-msg">empty</div>'}</div>
      <div class="vpane">${pane}</div>
    </div>`;
  }
  function copyVictimFile() {
    if (!VL || !VL.openId) return;
    const t = VL.files[VL.openId] || '';
    navigator.clipboard.writeText(t).catch(() => {});
  }

  // saves the already-fetched (cached) file text — no OathNet call, no search used
  function downloadVictimFile() {
    if (!VL || !VL.openId || VL.files[VL.openId] == null) return;
    const text = VL.files[VL.openId];
    let name = 'file.txt';
    const node = flattenTree(VL.tree, 0, []).find(r => r.id === VL.openId);
    if (node && node.name) name = String(node.name).replace(/[^\w.\- ]+/g, '_');
    if (!/\.[a-z0-9]{1,8}$/i.test(name)) name += '.txt';
    const blob = new Blob([text], { type: 'text/plain;charset=utf-8' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url; a.download = `${VL.logId}_${name}`;
    document.body.appendChild(a); a.click(); a.remove();
    setTimeout(() => URL.revokeObjectURL(url), 1500);
  }

  function closeFullLog() { document.getElementById('fullLogModal').style.display = 'none'; }

  const FOLDER_ICON = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V7z" stroke="currentColor" stroke-width="1.6"/></svg>';
  const FILE_ICON = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none"><path d="M6 3h8l4 4v14a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1z" stroke="currentColor" stroke-width="1.6"/><path d="M14 3v4h4" stroke="currentColor" stroke-width="1.6"/></svg>';

  function sampleManifest() {
    return { id: 'root', name: '/', type: 'directory', children: [
      { id: 'd1', name: 'Passwords', type: 'directory', children: [
        { id: 'f1', name: 'Chrome_Passwords.txt', type: 'file', size_bytes: 2048 },
        { id: 'f2', name: 'Edge_Passwords.txt', type: 'file', size_bytes: 1024 } ] },
      { id: 'd2', name: 'Cookies', type: 'directory', children: [
        { id: 'f3', name: 'discord.com_cookies.txt', type: 'file', size_bytes: 8192 } ] },
      { id: 'd3', name: 'System', type: 'directory', children: [
        { id: 'f4', name: 'UserInformation.txt', type: 'file', size_bytes: 512 } ] } ] };
  }
  function sampleFileText() {
    return 'URL: https://discord.com/login\nUsername: sample_user@example.com\nPassword: ••••••••••\n\n(sample preview — real logs show captured credentials, cookies and tokens here)';
  }

  // make the window draggable by its title bar
  (function initFullLogDrag() {
    let drag = null;
    const bar = document.getElementById('flBar');
    if (!bar) return;
    bar.addEventListener('pointerdown', (e) => {
      if (e.target.closest('.fl-close')) return;
      const win = document.getElementById('flWindow');
      drag = { px: e.clientX, py: e.clientY, ox: win.offsetLeft, oy: win.offsetTop };
      bar.setPointerCapture(e.pointerId);
    });
    bar.addEventListener('pointermove', (e) => {
      if (!drag) return;
      const win = document.getElementById('flWindow');
      win.style.left = Math.min(Math.max(drag.ox + (e.clientX - drag.px), 0), window.innerWidth - 60) + 'px';
      win.style.top = Math.min(Math.max(drag.oy + (e.clientY - drag.py), 0), window.innerHeight - 40) + 'px';
    });
    bar.addEventListener('pointerup', () => { drag = null; });
  })();

  // resize the window from the bottom-right grip
  (function initFullLogResize() {
    let rz = null;
    const grip = document.getElementById('flResize');
    if (!grip) return;
    grip.addEventListener('pointerdown', (e) => {
      e.stopPropagation();
      const win = document.getElementById('flWindow');
      rz = { px: e.clientX, py: e.clientY, w: win.offsetWidth, h: win.offsetHeight };
      grip.setPointerCapture(e.pointerId);
    });
    grip.addEventListener('pointermove', (e) => {
      if (!rz) return;
      const win = document.getElementById('flWindow');
      const w = Math.min(Math.max(rz.w + (e.clientX - rz.px), 320), window.innerWidth * 0.97);
      const h = Math.min(Math.max(rz.h + (e.clientY - rz.py), 240), window.innerHeight * 0.92);
      win.style.width = w + 'px';
      win.style.height = h + 'px';
    });
    grip.addEventListener('pointerup', () => { rz = null; });
  })();

  // demo payload shaped like a typical victim/full-log response
  function sampleFullLog(logId) {
    const sites = ['https://roblox.com/login','https://gmail.com','https://discord.com/login','https://steamcommunity.com','https://paypal.com','https://192.168.0.1/admin','https://netflix.com','https://coinbase.com'];
    const users = ['shadowfox','me@example.com','shadow.fox99','admin','foxgamer2018'];
    const pws = ['hunter2','dragon99','p@ssw0rd!','qwerty123','trustno1','redleaf88'];
    const creds = [];
    for (let i = 0; i < 8; i++) {
      creds.push({ url: sites[i % sites.length], username: users[i % users.length], password: pws[i % pws.length] });
    }
    return { data: {
      log_id: logId,
      computer_name: 'DESKTOP-7F3KQ9',
      os: 'Windows 10 Pro x64',
      ip: '102.89.45.221',
      country: 'NG',
      malware: 'RedLine Stealer',
      date: '2023-10-20',
      credentials: creds,
      cookies: [{ domain: '.roblox.com', name: '.ROBLOSECURITY', value: '••••••••(redacted)••••••••' }, { domain: '.discord.com', name: 'token', value: '••••••••(redacted)••••••••' }],
    }};
  }


  // Collapse duplicate records: exact copies (ignoring date) and "thinner"
  // copies that are fully covered by a richer record (same site+user, missing a field).
  function dedupe(items) {
    if (!items || items.length < 2) return items || [];
    const fields = ['domain', 'email', 'username', 'password'];
    const str = (v) => (v == null ? '' : String(v));
    const recs = items.map(it => ({
      raw: it,
      domain: str(it.domain).toLowerCase().trim(),
      email: str(it.email).toLowerCase().trim(),
      username: str(it.username).toLowerCase().trim(),
      password: str(it.password).trim(),
    }));
    // 1) exact dedupe (ignore date)
    const seen = new Map();
    for (const r of recs) {
      const k = fields.map(f => r[f]).join('|');
      if (!seen.has(k)) seen.set(k, r);
    }
    const uniq = [...seen.values()];
    // 2) drop records strictly covered by a richer one
    const keep = uniq.filter((r, ri) => !uniq.some((u, ui) => {
      if (ui === ri) return false;
      let coversAll = true, uExtra = 0;
      for (const f of fields) {
        if (r[f] && u[f] !== r[f]) coversAll = false;
        if (u[f] && !r[f]) uExtra++;
      }
      return coversAll && uExtra > 0;
    }));
    return keep.map(r => r.raw);
  }

  function recordsSection(items, type, sid, page) {
    if (!items || !items.length) return `<div class="none">✓ nothing found</div>`;
    const pages = Math.ceil(items.length / PAGE_SIZE);
    page = Math.max(0, Math.min(page || 0, pages - 1));
    const start = page * PAGE_SIZE;
    const slice = items.slice(start, start + PAGE_SIZE);
    const rows = slice.map(it => recCard(it, type)).join('');
    const pager = pages > 1 ? `<div class="pager">
      <button class="pg" ${page === 0 ? 'disabled' : ''} onclick="gotoPage('${sid}',${page - 1})">‹ Prev</button>
      <span class="pg-info">${start + 1}–${Math.min(start + PAGE_SIZE, items.length)} of ${items.length} · page ${page + 1}/${pages}</span>
      <button class="pg" ${page >= pages - 1 ? 'disabled' : ''} onclick="gotoPage('${sid}',${page + 1})">Next ›</button>
    </div>` : '';
    return `<div class="records">${rows}</div>${pager}`;
  }

  function foldSection(title, count, sid, type, items, openByDefault) {
    const badge = count > 0
      ? `<span class="fold-count flag">${count}</span>`
      : `<span class="fold-count clean">0</span>`;
    return `<div class="fold ${openByDefault ? 'open' : ''}">
      <button class="fold-head" onclick="toggleFold(this)">
        <svg class="fold-chev" width="14" height="14" viewBox="0 0 24 24" fill="none"><path d="M9 6l6 6-6 6" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
        <span class="fold-title">${esc(title)}</span>
        ${badge}
      </button>
      <div class="fold-body">
        <div class="records-wrap" id="${sid}">${recordsSection(items, type, sid, 0)}</div>
      </div>
    </div>`;
  }
  function toggleFold(btn) {
    btn.parentElement.classList.toggle('open');
  }

  function gotoPage(sid, page) {
    const sec = REPORT.sections[sid];
    const wrap = document.getElementById(sid);
    if (!sec || !wrap) return;
    wrap.innerHTML = recordsSection(sec.items, sec.type, sid, page);
    wrap.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  }
  function render(results, total, isRefilter) {
    const rep = document.getElementById('report');
    if (!isRefilter) {
      results.forEach(r => {
        if (r.breach) r.breach = dedupe(r.breach);
        if (r.stealer) r.stealer = dedupe(r.stealer);
      });
      LAST_RESULTS = results;            // keep pristine (deduped) copy for re-filtering
    }
    // apply the field filters to a working copy
    const view = results.map(r => ({
      query: r.query, errors: r.errors,
      breach: r.breach ? r.breach.filter(passesFilter) : r.breach,
      stealer: r.stealer ? r.stealer.filter(passesFilter) : r.stealer,
    }));
    total = view.reduce((n, r) => n + (r.breach ? r.breach.length : 0) + (r.stealer ? r.stealer.length : 0), 0);
    LAST_TOTAL = results.reduce((n, r) => n + (r.breach ? r.breach.length : 0) + (r.stealer ? r.stealer.length : 0), 0);
    const searchClear = LAST_TOTAL === 0;

    REPORT.sections = {};
    const laneGroup = (r, i, type) => {
      const items = (type === 'breach' ? r.breach : r.stealer) || [];
      const sid = `sec-${i}-${type === 'breach' ? 'b' : 's'}`;
      REPORT.sections[sid] = { items, type };
      return `<div class="lane-group">
        <div class="lane-group-head"><span class="lg-name">${esc(r.query)}</span><span class="lg-count ${items.length ? 'flag' : 'clean'}">${items.length}</span></div>
        <div class="records-wrap" id="${sid}">${recordsSection(items, type, sid, 0)}</div>
      </div>`;
    };
    const breachLane = view.map((r, i) => laneGroup(r, i, 'breach')).join('');
    const stealerLane = view.map((r, i) => laneGroup(r, i, 'stealer')).join('');
    const showBreach = SEARCH_SCOPE === 'breach' || SEARCH_SCOPE === 'both';
    const showStealer = SEARCH_SCOPE === 'stealer' || SEARCH_SCOPE === 'both';

    const subText = searchClear ? 'Nothing surfaced for what you checked.'
      : (RESULT_QUERY && total === 0 ? 'No results match your search.' : `${total} record${total !== 1 ? 's' : ''} shown.`);

    // incremental update when just filtering — keeps the search box & profiles lane intact
    if (isRefilter && document.getElementById('robloxLane')) {
      const lb = document.getElementById('laneBreach'); if (lb) lb.innerHTML = breachLane;
      const ls = document.getElementById('laneStealer'); if (ls) ls.innerHTML = stealerLane;
      const vs = document.getElementById('verdictSub');
      if (vs) vs.textContent = subText;
      return;
    }

    const verdict = `
      <div class="verdict ${searchClear ? 'clear' : 'flag'}">
        <div class="seal seal-anim">
          ${searchClear
            ? '<svg width="24" height="24" viewBox="0 0 24 24" fill="none"><path d="M5 12l4.5 4.5L19 7" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
            : '<svg width="24" height="24" viewBox="0 0 24 24" fill="none"><path d="M12 7v6M12 17h.01" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>'}
        </div>
        <div>
          <div class="v-title">${searchClear ? 'All clear' : 'Results'}</div>
          <div class="v-sub" id="verdictSub">${subText}</div>
        </div>
      </div>`;
    const searchBox = !searchClear ? `
      <div class="result-search">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none"><circle cx="11" cy="11" r="7" stroke="currentColor" stroke-width="1.8"/><path d="M21 21l-4.3-4.3" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
        <input id="resultSearch" type="text" placeholder="Search within results…" autocomplete="off" spellcheck="false"
               value="${esc(RESULT_QUERY)}" oninput="onResultSearch(this.value)">
      </div>` : '';
    const laneCount = 1 + (showBreach ? 1 : 0) + (showStealer ? 1 : 0);
    const lanes = `
      <div class="lanes lanes-${laneCount}">
        <div class="lane">
          <div class="lane-title">Profiles</div>
          <div class="lane-body" id="robloxLane"><div class="lane-empty">Checking…</div></div>
        </div>
        ${showBreach ? `<div class="lane">
          <div class="lane-title">Breach records</div>
          <div class="lane-body" id="laneBreach">${breachLane}</div>
        </div>` : ''}
        ${showStealer ? `<div class="lane">
          <div class="lane-title">Stealer logs</div>
          <div class="lane-body" id="laneStealer">${stealerLane}</div>
        </div>` : ''}
      </div>`;
    rep.classList.add('wide');
    rep.innerHTML = `<div class="report-frame reveal">${verdict}${searchBox}${lanes}</div>`;
    if (!isRefilter) rep.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  }

  function loadSample() {
    const status = document.getElementById('status');
    const dbs = ['collection_2019','forum_dump_2021','shop_leak_2020','cloud_breach_2022','social_2018','game_db_2023','mail_dump_2017','retail_2021','crypto_2022','vpn_logs_2020'];
    const pw = ['hunter2','p@ssw0rd!','letmein1','qwerty123','sunshine','dragon99','iloveyou','admin123','redleaf88','trustno1','baseball7','monkey55','football','shadow22','master11','princess','welcome9','ninja2020','flower44','batman77','zaq12wsx','passw0rd','liverpool','starwars1'];
    const breach = [];
    for (let i = 0; i < 23; i++) {
      breach.push({
        dbname: dbs[i % dbs.length],
        email: 'me@example.com',
        username: i % 3 === 0 ? 'shadowfox' + i : undefined,
        password: pw[i % pw.length],
        indexed_at: `20${15 + (i % 9)}-0${1 + (i % 9)}-1${i % 9}T00:00:00Z`
      });
    }
    const stealer = [];
    for (let i = 0; i < 12; i++) {
      stealer.push({
        domain: `http://192.168.${i}.1/`,
        email: 'me@example.com',
        username: i % 2 ? 'super' : 'admin' + i,
        password: pw[(i + 5) % pw.length],
        indexed_at: `2023-1${i % 2}-2${i % 8}T00:00:00Z`,
        log_id: 'sample-log-' + i
      });
    }
    const sample = [
      { query: 'me@example.com', errors: [], breach, stealer },
      { query: 'shadowfox', errors: [], breach: [], stealer: [] }
    ];
    const total = sample.reduce((n, r) => n + (r.breach?.length || 0) + (r.stealer?.length || 0), 0);
    SEARCH_SCOPE = 'both';
    render(sample, total);
    status.innerHTML = `<span style="color:var(--amber)">Example preview — enter an access code to run a real check.</span>`;

    // sample Roblox + Xbox profiles so the Profiles lane is visible in the preview
    const lane = document.getElementById('robloxLane');
    if (lane) {
      lane.innerHTML = renderRobloxCard({
        found: true,
        id: 10961076258,
        name: 'shadowfox',
        displayName: 'ShadowFox',
        created: '2018-04-12T00:00:00Z',
        isBanned: false,
        pastUsernames: ['xX_shadow_Xx', 'shadowfoxx99', 'foxgamer2018'],
        avatarUrl: null
      }) + renderXboxCard({
        found: true,
        xuid: '2533274912212211',
        gamertag: 'ShadowFox',
        gamerscore: '48720',
        tier: 'Gold',
        rep: 'GoodPlayer',
        location: 'Seattle, WA',
        realName: '',
        bio: 'just here for the games',
        avatarUrl: null
      });
    }
  }

  /* ============ OSINT WEB CANVAS ============ */
  let osintReady = false, osintStage, osintWorld, osintEdges, osintEmpty;
  const osintNodes = new Map();      // id -> {id, type, text, x, y, el}
  const osintLinks = [];             // {id, a, b}
  let osintView = { x: 0, y: 0, k: 1 };
  let osintSeq = 1, osintLinkMode = false;
  let linkDrag = null;

  function osintInit() {
    if (osintReady) return;
    osintStage = document.getElementById('osintStage');
    osintWorld = document.getElementById('osintWorld');
    osintEdges = document.getElementById('osintEdges');
    osintEmpty = document.getElementById('osintEmpty');

    let panning = false, panStart = null;
    osintStage.addEventListener('pointerdown', (e) => {
      if (e.target !== osintStage && e.target !== osintEdges && e.target !== osintEmpty) return;
      panning = true; osintStage.classList.add('panning');
      panStart = { x: e.clientX, y: e.clientY, vx: osintView.x, vy: osintView.y };
      clearSelection();
    });
    window.addEventListener('pointermove', (e) => {
      if (panning) {
        osintView.x = panStart.vx + (e.clientX - panStart.x);
        osintView.y = panStart.vy + (e.clientY - panStart.y);
        applyView();
      }
      if (linkDrag) { const p = stagePoint(e); linkDrag.x2 = p.x; linkDrag.y2 = p.y; osintRender(); }
    });
    window.addEventListener('pointerup', (e) => {
      panning = false; osintStage.classList.remove('panning');
      if (linkDrag) {
        const target = e.target.closest && e.target.closest('.node');
        if (target && target.dataset.id !== linkDrag.fromId) osintConnect(linkDrag.fromId, target.dataset.id, linkDrag.fromSide);
        linkDrag = null; osintRender();
      }
    });
    osintStage.addEventListener('wheel', (e) => { e.preventDefault(); zoomAt(e.clientX, e.clientY, e.deltaY < 0 ? 1.1 : 0.9); }, { passive: false });

    osintReady = true; applyView(); osintRender();
  }

  function stagePoint(e) {
    const r = osintStage.getBoundingClientRect();
    return { x: (e.clientX - r.left - osintView.x) / osintView.k, y: (e.clientY - r.top - osintView.y) / osintView.k };
  }
  function applyView() {
    const t = `translate(${osintView.x}px, ${osintView.y}px) scale(${osintView.k})`;
    osintWorld.style.transform = t; osintEdges.style.transform = t;
    osintRender();
  }
  function zoomAt(clientX, clientY, factor) {
    const r = osintStage.getBoundingClientRect();
    const mx = clientX - r.left, my = clientY - r.top;
    const nk = Math.max(0.25, Math.min(2.5, osintView.k * factor));
    osintView.x = mx - (mx - osintView.x) * (nk / osintView.k);
    osintView.y = my - (my - osintView.y) * (nk / osintView.k);
    osintView.k = nk; applyView();
  }
  function osintZoom(factor) { const r = osintStage.getBoundingClientRect(); zoomAt(r.left + r.width / 2, r.top + r.height / 2, factor); }
  function osintResetView() {
    if (!osintNodes.size) { osintView = { x: 0, y: 0, k: 1 }; applyView(); return; }
    let minX = Infinity, minY = Infinity, maxX = -Infinity, maxY = -Infinity;
    osintNodes.forEach(n => { minX = Math.min(minX, n.x); minY = Math.min(minY, n.y); maxX = Math.max(maxX, n.x + 220); maxY = Math.max(maxY, n.y + 90); });
    const pad = 60, w = osintStage.clientWidth, h = osintStage.clientHeight;
    const k = Math.max(0.25, Math.min(1.3, Math.min(w / (maxX - minX + pad * 2), h / (maxY - minY + pad * 2))));
    osintView.k = k;
    osintView.x = (w - (maxX - minX) * k) / 2 - minX * k;
    osintView.y = (h - (maxY - minY) * k) / 2 - minY * k;
    applyView();
  }
  function osintToggleLink() {
    osintLinkMode = !osintLinkMode;
    document.getElementById('osintLinkBtn').classList.toggle('on', osintLinkMode);
    document.getElementById('osintHint').textContent = osintLinkMode
      ? 'Connect mode on \u2014 drag from a node\u2019s side dot to another node'
      : 'Drag boxes to move \u00b7 drag a side dot to another box to connect \u00b7 double-click a box to edit';
  }

  function osintAddBox(type, text, x, y) {
    osintInit();
    if (x == null) x = (-osintView.x + osintStage.clientWidth / 2) / osintView.k - 110 + (Math.random() * 60 - 30);
    if (y == null) y = (-osintView.y + osintStage.clientHeight / 2) / osintView.k - 40 + (Math.random() * 60 - 30);
    const id = 'n' + (osintSeq++);
    const node = { id, type: type || 'Note', text: text != null ? text : 'New note', x, y, el: null };
    osintNodes.set(id, node); buildNodeEl(node); osintRender();
    return node;
  }
  function buildNodeEl(node) {
    const el = document.createElement('div');
    el.className = 'node'; el.dataset.id = node.id;
    el.innerHTML = `
      <div class="node-head">
        <span class="node-type" contenteditable="true" spellcheck="false">${esc(node.type)}</span>
        <button class="node-del" title="delete">×</button>
      </div>
      <div class="node-body" contenteditable="true" spellcheck="false">${esc(node.text)}</div>
      <div class="port l"></div><div class="port r"></div><div class="port t"></div><div class="port b"></div>`;
    osintWorld.appendChild(el); node.el = el; positionNode(node);

    const typeEl = el.querySelector('.node-type'), bodyEl = el.querySelector('.node-body');
    typeEl.addEventListener('blur', () => { node.type = typeEl.textContent.trim() || 'Note'; });
    bodyEl.addEventListener('blur', () => { node.text = bodyEl.textContent; });
    el.querySelector('.node-del').addEventListener('pointerdown', (e) => { e.stopPropagation(); });
    el.querySelector('.node-del').addEventListener('click', (e) => { e.stopPropagation(); e.preventDefault(); osintDelete(node.id); });

    let dragging = false, ds = null;
    el.addEventListener('pointerdown', (e) => {
      if (e.target.classList.contains('port') || e.target.isContentEditable || e.target.closest('.node-del')) return;
      e.stopPropagation(); selectNode(node.id);
      dragging = true; el.classList.add('dragging'); el.setPointerCapture(e.pointerId);
      ds = { px: e.clientX, py: e.clientY, nx: node.x, ny: node.y };
    });
    el.addEventListener('pointermove', (e) => {
      if (!dragging) return;
      node.x = ds.nx + (e.clientX - ds.px) / osintView.k;
      node.y = ds.ny + (e.clientY - ds.py) / osintView.k;
      positionNode(node); osintRender();
    });
    el.addEventListener('pointerup', () => { dragging = false; el.classList.remove('dragging'); });

    el.querySelectorAll('.port').forEach(p => {
      p.addEventListener('pointerdown', (e) => {
        e.stopPropagation();
        const pt = stagePoint(e);
        const side = ['l','r','t','b'].find(s => p.classList.contains(s)) || 'r';
        linkDrag = { fromId: node.id, fromSide: side, x2: pt.x, y2: pt.y };
      });
    });
  }
  function positionNode(node) { node.el.style.left = node.x + 'px'; node.el.style.top = node.y + 'px'; }
  function selectNode(id) { clearSelection(); const n = osintNodes.get(id); if (n) n.el.classList.add('sel'); }
  function clearSelection() { osintNodes.forEach(n => n.el && n.el.classList.remove('sel')); }

  function osintConnect(a, b, fromSide, toSide) {
    if (a === b) return;
    if (osintLinks.some(l => (l.a === a && l.b === b) || (l.a === b && l.b === a))) return;
    osintLinks.push({ id: 'e' + (osintSeq++), a, b, fromSide: fromSide || null, toSide: toSide || null }); osintRender();
  }
  function osintDelete(id) {
    const n = osintNodes.get(id); if (n && n.el) n.el.remove(); osintNodes.delete(id);
    for (let i = osintLinks.length - 1; i >= 0; i--) if (osintLinks[i].a === id || osintLinks[i].b === id) osintLinks.splice(i, 1);
    osintRender();
  }
  function osintClear() {
    if (osintNodes.size && !confirm('Clear the whole canvas?')) return;
    osintNodes.forEach(n => n.el && n.el.remove()); osintNodes.clear(); osintLinks.length = 0; osintRender();
  }
  function nodeSize(n) { return { w: n.el ? n.el.offsetWidth : 220, h: n.el ? n.el.offsetHeight : 70 }; }
  function portPos(n, side) {
    const { w, h } = nodeSize(n);
    switch (side) {
      case 'l': return { x: n.x, y: n.y + h / 2, dx: -1, dy: 0 };
      case 'r': return { x: n.x + w, y: n.y + h / 2, dx: 1, dy: 0 };
      case 't': return { x: n.x + w / 2, y: n.y, dx: 0, dy: -1 };
      default:  return { x: n.x + w / 2, y: n.y + h, dx: 0, dy: 1 }; // 'b'
    }
  }
  function bestSides(A, B, fixedA, fixedB) {
    const sides = ['l', 'r', 't', 'b'];
    let best = null;
    for (const sa of (fixedA ? [fixedA] : sides)) {
      const pa = portPos(A, sa);
      for (const sb of (fixedB ? [fixedB] : sides)) {
        const pb = portPos(B, sb);
        const d = Math.hypot(pa.x - pb.x, pa.y - pb.y);
        if (!best || d < best.d) best = { d, sa, sb };
      }
    }
    return best;
  }
  function edgePath(A, B, sa, sb) {
    const pa = portPos(A, sa), pb = portPos(B, sb);
    const dist = Math.hypot(pb.x - pa.x, pb.y - pa.y);
    const off = Math.max(40, Math.min(dist * 0.45, 140));
    const c1x = pa.x + pa.dx * off, c1y = pa.y + pa.dy * off;
    const c2x = pb.x + pb.dx * off, c2y = pb.y + pb.dy * off;
    return `M ${pa.x} ${pa.y} C ${c1x} ${c1y}, ${c2x} ${c2y}, ${pb.x} ${pb.y}`;
  }
  function osintRender() {
    if (!osintReady) return;
    osintEmpty.style.display = osintNodes.size ? 'none' : 'flex';
    let svg = '';
    for (const l of osintLinks) {
      const A = osintNodes.get(l.a), B = osintNodes.get(l.b);
      if (!A || !B) continue;
      const sides = bestSides(A, B, l.fromSide, l.toSide);
      const path = edgePath(A, B, sides.sa, sides.sb);
      svg += `<g class="edge-grp" onclick="osintRemoveLink('${l.id}')"><path class="edge-hit" d="${path}"/><path class="edge" d="${path}"/></g>`;
    }
    if (linkDrag) {
      const A = osintNodes.get(linkDrag.fromId);
      if (A) {
        const pa = portPos(A, linkDrag.fromSide || 'r');
        const off = 50;
        svg += `<path class="edge" style="opacity:.5;stroke-dasharray:5 4" d="M ${pa.x} ${pa.y} C ${pa.x + pa.dx * off} ${pa.y + pa.dy * off}, ${linkDrag.x2} ${linkDrag.y2}, ${linkDrag.x2} ${linkDrag.y2}"/>`;
      }
    }
    osintEdges.innerHTML = svg;
  }
  function osintRemoveLink(id) { const i = osintLinks.findIndex(l => l.id === id); if (i >= 0) { osintLinks.splice(i, 1); osintRender(); } }

  /* ============ MUSIC PLAYER ============ */
  let musicReady = false, mAudio = null, mTracks = [], mIndex = -1, mStorageOK = true, mPrevVol = 1;
  const ICON = {
    play: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M8 5.5v13a1 1 0 0 0 1.5.87l10.5-6.5a1 1 0 0 0 0-1.74L9.5 4.63A1 1 0 0 0 8 5.5z"/></svg>',
    pause: '<svg viewBox="0 0 24 24" fill="currentColor"><rect x="6.5" y="5" width="3.6" height="14" rx="1.2"/><rect x="13.9" y="5" width="3.6" height="14" rx="1.2"/></svg>',
    prev: '<svg viewBox="0 0 24 24" fill="currentColor"><rect x="6" y="5" width="2.6" height="14" rx="1"/><path d="M20 5.6v12.8a1 1 0 0 1-1.55.83l-9-6.4a1 1 0 0 1 0-1.66l9-6.4A1 1 0 0 1 20 5.6z"/></svg>',
    next: '<svg viewBox="0 0 24 24" fill="currentColor"><rect x="15.4" y="5" width="2.6" height="14" rx="1"/><path d="M4 5.6v12.8a1 1 0 0 0 1.55.83l9-6.4a1 1 0 0 0 0-1.66l-9-6.4A1 1 0 0 0 4 5.6z"/></svg>',
    vol: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 9.5v5h3.5L13 19V5L7.5 9.5z" fill="currentColor" stroke="none"/><path d="M16.5 8.5a4.5 4.5 0 0 1 0 7"/></svg>',
    mute: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 9.5v5h3.5L13 19V5L7.5 9.5z" fill="currentColor" stroke="none"/><path d="M16.5 9.5l5 5M21.5 9.5l-5 5"/></svg>',
    note: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"><path d="M9 17.5V5.5l10-2v10"/><circle cx="6.4" cy="17.5" r="2.6" fill="currentColor" stroke="none"/><circle cx="16.4" cy="15.5" r="2.6" fill="currentColor" stroke="none"/></svg>'
  };

  function musicUser() {
    try { const u = window.netlifyIdentity && netlifyIdentity.currentUser(); return (u && u.email) || 'guest'; }
    catch (e) { return 'guest'; }
  }

  // ---- audio-reactive background ----
  let mAudioCtx = null, mAnalyser = null, mFreqData = null, mLevel = 0, mBurst = 0, mPrevAvg = 0;
  window.__reactiveOn = (function () { try { return localStorage.getItem('trace_reactive') !== '0'; } catch (e) { return true; } })();
  window.__getAudioLevel = function () { return mLevel; };
  window.__getBurst = function () { return mBurst; };
  function musicSetupAnalyser() {
    if (mAnalyser || !mAudio) return;
    try {
      const AC = window.AudioContext || window.webkitAudioContext;
      if (!AC) return;
      mAudioCtx = new AC();
      const src = mAudioCtx.createMediaElementSource(mAudio);
      mAnalyser = mAudioCtx.createAnalyser();
      mAnalyser.fftSize = 256;
      mAnalyser.smoothingTimeConstant = 0.65;
      mFreqData = new Uint8Array(mAnalyser.frequencyBinCount);
      src.connect(mAnalyser);
      mAnalyser.connect(mAudioCtx.destination);
      function tick() {
        if (mAnalyser) {
          mAnalyser.getByteFrequencyData(mFreqData);
          // overall level (for the gentle glow)
          let sum = 0;
          for (let i = 0; i < mFreqData.length; i++) sum += mFreqData[i];
          const avg = sum / mFreqData.length / 255;
          const target = mAudio.paused ? 0 : Math.min(1, avg * 1.6);
          mLevel += (target - mLevel) * 0.18;
          // BASS energy: average just the lowest frequency bins
          const bassBins = 8;
          let bsum = 0;
          for (let i = 0; i < bassBins; i++) bsum += mFreqData[i];
          const bass = mAudio.paused ? 0 : (bsum / bassBins / 255);   // 0..1
          // smoothly ease the burst toward the bass energy (no sudden jump)
          const want = Math.max(0, bass - 0.12) * 1.4;                // soft floor, scaled
          const k = want > mBurst ? 0.22 : 0.06;                      // rise quicker than it falls
          mBurst += (Math.min(1, want) - mBurst) * k;
          if (mBurst < 0.0008) mBurst = 0;
        }
        requestAnimationFrame(tick);
      }
      tick();
    } catch (e) { /* analyser unavailable — background just won't react */ }
  }

  // ---- IndexedDB (best-effort persistence; never blocks playback) ----
  function withTimeout(promise, ms) {
    return Promise.race([promise, new Promise((_, rej) => setTimeout(() => rej(new Error('storage timeout')), ms))]);
  }
  function mOpenDB() {
    return new Promise((res, rej) => {
      let req;
      try { req = indexedDB.open('trace-music', 1); }
      catch (e) { rej(e); return; }
      req.onupgradeneeded = (e) => {
        const db = e.target.result;
        if (!db.objectStoreNames.contains('tracks')) db.createObjectStore('tracks', { keyPath: 'id' });
      };
      req.onsuccess = () => res(req.result);
      req.onerror = () => rej(req.error);
      req.onblocked = () => rej(new Error('storage blocked'));
    });
  }
  async function mGetTracks(user) {
    const db = await withTimeout(mOpenDB(), 4000);
    return new Promise((res, rej) => {
      const out = [];
      const cur = db.transaction('tracks', 'readonly').objectStore('tracks').openCursor();
      cur.onsuccess = (e) => { const c = e.target.result; if (c) { if (c.value.user === user) out.push(c.value); c.continue(); } else res(out); };
      cur.onerror = () => rej(cur.error);
    });
  }
  async function mPut(t) { const db = await withTimeout(mOpenDB(), 4000); return new Promise((res, rej) => { const tx = db.transaction('tracks', 'readwrite'); tx.objectStore('tracks').put(t); tx.oncomplete = res; tx.onerror = () => rej(tx.error); }); }
  async function mDelete(id) { const db = await withTimeout(mOpenDB(), 4000); return new Promise((res, rej) => { const tx = db.transaction('tracks', 'readwrite'); tx.objectStore('tracks').delete(id); tx.oncomplete = res; tx.onerror = () => rej(tx.error); }); }

  // fire-and-forget save; failure just means "session only", playback already works
  function musicPersist(t) {
    if (!mStorageOK) return;
    mPut(t).catch(() => {
      mStorageOK = false;
      const h = document.getElementById('musicHint');
      if (h) h.textContent = 'Heads up: songs will play this session but can\u2019t be saved in this browser context.';
    });
  }

  async function musicInit() {
    if (musicReady) return;
    musicReady = true; window.__musicReady = true;
    mAudio = new Audio();
    mAudio.volume = 1;
    mAudio.addEventListener('timeupdate', musicOnTime);
    mAudio.addEventListener('loadedmetadata', musicOnTime);
    mAudio.addEventListener('ended', musicNext);
    mAudio.addEventListener('play', musicSyncPlayIcon);
    mAudio.addEventListener('pause', musicSyncPlayIcon);

    document.getElementById('musicFile').addEventListener('change', musicOnFiles);
    // inject SVG icons into static controls
    document.getElementById('prevBtn').innerHTML = ICON.prev;
    document.getElementById('nextBtn').innerHTML = ICON.next;
    document.querySelectorAll('[data-icon="prev"]').forEach(el => el.innerHTML = ICON.prev);
    document.querySelectorAll('[data-icon="next"]').forEach(el => el.innerHTML = ICON.next);
    musicSyncPlayIcon(); musicSyncMuteIcon();
    updateNpArt();
    const miniArt = document.getElementById('miniArt'); if (miniArt) miniArt.innerHTML = ICON.note;
    const rt = document.getElementById('reactiveToggle');
    if (rt) rt.checked = window.__reactiveOn !== false;
    document.getElementById('seek').addEventListener('input', (e) => {
      if (mAudio.duration) mAudio.currentTime = (e.target.value / 1000) * mAudio.duration;
    });
    const onVol = (val) => {
      mAudio.volume = val / 100; mAudio.muted = false; musicSyncMuteIcon();
      const v = document.getElementById('vol'); if (v) v.value = val;
      const mv = document.getElementById('miniVol'); if (mv) mv.value = val;
    };
    document.getElementById('vol').addEventListener('input', (e) => onVol(+e.target.value));
    const miniVol = document.getElementById('miniVol');
    if (miniVol) miniVol.addEventListener('input', (e) => onVol(+e.target.value));

    // load this account's saved songs (best-effort; never blocks the UI)
    musicRenderList();
    try {
      const saved = await mGetTracks(musicUser());
      if (saved.length) {
        const existing = new Set(mTracks.map(t => t.id));
        saved.forEach(t => { if (!existing.has(t.id)) mTracks.push({ ...t, name: cleanTrackName(t.name), url: URL.createObjectURL(t.blob), coverUrl: t.cover ? URL.createObjectURL(t.cover) : null }); });
        musicRenderList();
      }
    } catch (e) {
      mStorageOK = false;
      document.getElementById('musicHint').textContent = 'Songs will play this session — saved playback isn\u2019t available in this browser context.';
    }
  }

  function musicPickFiles() { document.getElementById('musicFile').click(); }

  // re-read ID3 tags for saved tracks (their stored names may be old/dirty)
  async function musicRefreshSavedMeta() {
    for (const t of mTracks) {
      if (t.metaDone || !t.blob) continue;
      try {
        const changed = await loadMeta(t, t.blob);
        t.metaDone = true;
        if (changed && mStorageOK) {
          mPut({ id: t.id, user: t.user, name: t.name, type: t.type, blob: t.blob, cover: t.cover, metaDone: true }).catch(() => {});
        }
      } catch (e) { t.metaDone = true; }
    }
    musicRenderList(); updateMiniPlayer(); updateNpArt();
  }

  // strip download-site noise from filenames -> clean song title
  function cleanTrackName(raw) {
    let s = String(raw || '').replace(/\.[^.]+$/, '');            // drop extension
    s = s.replace(/_+\d*/g, ' ');                                 // underscores / "__3" -> space FIRST (so glued site names separate)
    const SITES = 'spotidownloader|spotdownloader|spotdownload|spotdown|y2mate|ytmp3|yt1s|tubidy|savefrom|musicpapa|mp3juices?|9convert|320kbps|flvto|onlymp3|snaptube';
    s = s.replace(new RegExp('\\b(?:' + SITES + ')(?:\\.(?:org|com|net|io|co|to|app))?', 'gi'), '');
    s = s.replace(/\s{2,}/g, ' ').trim();                         // collapse spaces
    s = s.replace(/^[\s\-–|·•]+|[\s\-–|·•]+$/g, '').trim();        // trim only EDGE separators (keep internal dashes)
    s = s.replace(/\s*([-–|])\s*(?:[-–|]\s*)+/g, ' $1 ');         // collapse runs like " - - " to " - "
    s = s.replace(/\s{2,}/g, ' ').trim();
    return s || String(raw || '').replace(/\.[^.]+$/, '');        // fallback if emptied
  }

  // extract embedded cover art AND title/artist tags from ID3 (mp3)
  function parseID3(buf) {
    const out = { cover: null, mime: null, title: '', artist: '' };
    const u8 = new Uint8Array(buf);
    if (u8.length < 10 || u8[0] !== 0x49 || u8[1] !== 0x44 || u8[2] !== 0x33) return out; // "ID3"
    const major = u8[3];
    const tagSize = (u8[6] << 21) | (u8[7] << 14) | (u8[8] << 7) | u8[9];
    const end = Math.min(10 + tagSize, u8.length);
    let pos = 10;
    function decodeText(start, len) {
      if (len <= 0) return '';
      const enc = u8[start];
      const body = u8.subarray(start + 1, start + len);
      try {
        if (enc === 1 || enc === 2) {                            // UTF-16
          return new TextDecoder('utf-16').decode(body).replace(/\0+$/, '').trim();
        }
        if (enc === 3) return new TextDecoder('utf-8').decode(body).replace(/\0+$/, '').trim();
        // 0 = ISO-8859-1
        let s = ''; for (let i = 0; i < body.length; i++) { if (body[i] === 0) break; s += String.fromCharCode(body[i]); }
        return s.trim();
      } catch (e) { return ''; }
    }
    while (pos + 10 <= end) {
      if (major === 2) {
        const id = String.fromCharCode(u8[pos], u8[pos + 1], u8[pos + 2]);
        const size = (u8[pos + 3] << 16) | (u8[pos + 4] << 8) | u8[pos + 5];
        if (size <= 0 || !/^[A-Z0-9]{3}$/.test(id)) break;
        const dstart = pos + 6;
        if (id === 'TT2') out.title = decodeText(dstart, size);
        else if (id === 'TP1') out.artist = decodeText(dstart, size);
        else if (id === 'PIC') {
          let p = dstart + 1;
          const fmt = String.fromCharCode(u8[p], u8[p + 1], u8[p + 2]); p += 3;
          p += 1; while (p < dstart + size && u8[p] !== 0) p++; p++;
          out.mime = fmt.toLowerCase().indexOf('png') >= 0 ? 'image/png' : 'image/jpeg';
          out.coverBytes = u8.slice(p, dstart + size);
        }
        pos = dstart + size;
      } else {
        const id = String.fromCharCode(u8[pos], u8[pos + 1], u8[pos + 2], u8[pos + 3]);
        const size = major === 4
          ? ((u8[pos + 4] << 21) | (u8[pos + 5] << 14) | (u8[pos + 6] << 7) | u8[pos + 7])
          : ((u8[pos + 4] << 24) | (u8[pos + 5] << 16) | (u8[pos + 6] << 8) | u8[pos + 7]);
        if (size <= 0 || !/^[A-Z0-9]{4}$/.test(id)) break;
        const dstart = pos + 10;
        if (id === 'TIT2') out.title = decodeText(dstart, size);
        else if (id === 'TPE1') out.artist = decodeText(dstart, size);
        else if (id === 'APIC') {
          let p = dstart;
          const enc = u8[p]; p++;
          let mime = '';
          while (p < dstart + size && u8[p] !== 0) { mime += String.fromCharCode(u8[p]); p++; }
          p++; p++;
          if (enc === 1 || enc === 2) { while (p + 1 < dstart + size && !(u8[p] === 0 && u8[p + 1] === 0)) p += 2; p += 2; }
          else { while (p < dstart + size && u8[p] !== 0) p++; p++; }
          out.mime = mime || 'image/jpeg';
          out.coverBytes = u8.slice(p, dstart + size);
        }
        pos = dstart + size;
      }
    }
    return out;
  }
  async function loadMeta(track, fileOrBlob) {
    let changed = false;
    try {
      const buf = await fileOrBlob.arrayBuffer();
      const m = parseID3(buf);
      // cover
      if (m.coverBytes && m.coverBytes.length > 100) {
        track.cover = new Blob([m.coverBytes], { type: m.mime });
        track.coverUrl = URL.createObjectURL(track.cover);
        changed = true;
      }
      // real title from tags (cleaned of any site-name junk too)
      const tagTitle = cleanTrackName(m.title);
      if (tagTitle && tagTitle.length > 1) {
        const artist = cleanTrackName(m.artist);
        track.name = artist && artist.length > 1 ? `${artist} - ${tagTitle}` : tagTitle;
        changed = true;
      }
    } catch (e) {}
    return changed;
  }
  function artHtml(t) {
    return t && t.coverUrl ? `<img src="${t.coverUrl}" alt="">` : ICON.note;
  }

  function toggleReactive(cb) {
    window.__reactiveOn = cb.checked;
    try { localStorage.setItem('trace_reactive', cb.checked ? '1' : '0'); } catch (e) {}
  }

  async function musicReloadForUser() {
    if (!musicReady) return;
    if (mAudio) { mAudio.pause(); mAudio.removeAttribute('src'); }
    mTracks.forEach(t => { if (t.url) URL.revokeObjectURL(t.url); });
    mTracks = []; mIndex = -1;
    const npt = document.getElementById('npTitle'); if (npt) npt.textContent = 'Nothing playing';
    try {
      const saved = await mGetTracks(musicUser());
      mTracks = saved.map(t => ({ ...t, name: cleanTrackName(t.name), url: URL.createObjectURL(t.blob), coverUrl: t.cover ? URL.createObjectURL(t.cover) : null }));
    } catch (e) {}
    musicRenderList();
  }

  async function musicOnFiles(e) {
    const files = Array.from(e.target.files || []);
    const user = musicUser();
    const wasEmpty = mTracks.length === 0;
    for (const f of files) {
      const t = { id: 'trk-' + Date.now() + '-' + Math.random().toString(36).slice(2, 7), user, name: cleanTrackName(f.name), type: f.type, blob: f };
      mTracks.push({ ...t, url: URL.createObjectURL(f) });  // playable immediately
      const ref = mTracks[mTracks.length - 1];
      loadMeta(ref, f).then(changed => {                     // read real title + cover in background
        if (changed) {
          t.name = ref.name; t.cover = ref.cover;            // persist corrected name + art
          musicRenderList(); updateMiniPlayer(); updateNpArt();
          const np = document.getElementById('npTitle');
          if (np && mIndex >= 0 && mTracks[mIndex] === ref) np.textContent = ref.name;
        }
        musicPersist(t);
      });
    }
    e.target.value = '';
    musicRenderList();
    if (wasEmpty && mTracks.length) musicPlay(0);            // start playing the first added
  }

  function musicRenderList() {
    const list = document.getElementById('playlist');
    if (!mTracks.length) {
      list.innerHTML = `<div class="music-empty" id="musicEmpty">No songs yet. Hit “Add songs” to load audio files from your device.</div>`;
      return;
    }
    list.innerHTML = mTracks.map((t, i) => `
      <div class="track ${i === mIndex ? 'active' : ''}" onclick="musicPlay(${i})">
        <span class="${t.coverUrl ? 'track-art' : 'track-eq'}">${t.coverUrl ? `<img src="${t.coverUrl}" alt="">` : (i === mIndex ? '' : ICON.note)}</span>
        <span class="track-name">${esc(t.name)}</span>
        <button class="track-del" title="remove" onclick="event.stopPropagation();musicRemove(${i})">×</button>
      </div>`).join('');
  }

  function musicPlay(i) {
    if (i < 0 || i >= mTracks.length) return;
    mIndex = i;
    musicSetupAnalyser();
    if (mAudioCtx && mAudioCtx.state === 'suspended') mAudioCtx.resume();
    mAudio.src = mTracks[i].url;
    mAudio.play().catch(() => {});
    document.getElementById('npTitle').textContent = mTracks[i].name;
    musicRenderList();
    updateMiniPlayer();
    updateNpArt();
  }
  function musicTogglePlay() {
    if (mIndex < 0 && mTracks.length) { musicPlay(0); return; }
    if (!mAudio.src) return;
    musicSetupAnalyser();
    if (mAudioCtx && mAudioCtx.state === 'suspended') mAudioCtx.resume();
    if (mAudio.paused) mAudio.play().catch(() => {}); else mAudio.pause();
  }
  function musicNext() { if (mTracks.length) musicPlay((mIndex + 1) % mTracks.length); }
  function musicPrev() {
    if (!mTracks.length) return;
    if (mAudio.currentTime > 3) { mAudio.currentTime = 0; return; }
    musicPlay((mIndex - 1 + mTracks.length) % mTracks.length);
  }
  async function musicRemove(i) {
    const t = mTracks[i]; if (!t) return;
    try { if (mStorageOK) await mDelete(t.id); } catch (e) {}
    if (t.url) URL.revokeObjectURL(t.url);
    mTracks.splice(i, 1);
    if (i === mIndex) { mAudio.pause(); mAudio.removeAttribute('src'); mIndex = -1; document.getElementById('npTitle').textContent = 'Nothing playing'; }
    else if (i < mIndex) mIndex--;
    musicRenderList();
  }
  function musicToggleMute() {
    if (!mAudio) return;
    mAudio.muted = !mAudio.muted;
    musicSyncMuteIcon();
  }
  function musicSyncMuteIcon() {
    const icon = (mAudio.muted || mAudio.volume === 0) ? ICON.mute : ICON.vol;
    const b = document.getElementById('muteBtn'); if (b) b.innerHTML = icon;
    const m = document.getElementById('miniMute'); if (m) m.innerHTML = icon;
  }
  function musicSyncPlayIcon() {
    const icon = (mAudio && !mAudio.paused) ? ICON.pause : ICON.play;
    const b = document.getElementById('playBtn'); if (b) b.innerHTML = icon;
    const m = document.getElementById('miniPlay'); if (m) m.innerHTML = icon;
    updateMiniPlayer();
  }
  function updateNpArt() {
    const el = document.getElementById('npArt');
    if (!el) return;
    const t = (mIndex >= 0) ? mTracks[mIndex] : null;
    el.innerHTML = artHtml(t);
  }
  function updateMiniPlayer() {
    const mp = document.getElementById('miniPlayer');
    if (!mp) return;
    const hasTrack = (typeof mIndex !== 'undefined') && mIndex >= 0 && mTracks[mIndex];
    const show = hasTrack && currentTab !== 'music';
    mp.style.display = show ? 'flex' : 'none';
    if (show) {
      document.getElementById('miniTitle').textContent = mTracks[mIndex].name;
      document.getElementById('miniArt').innerHTML = artHtml(mTracks[mIndex]);
      const mv = document.getElementById('miniVol');
      if (mv && mAudio) mv.value = Math.round(mAudio.volume * 100);
    }
  }
  function fmtTime(s) { if (!s || isNaN(s)) return '0:00'; const m = Math.floor(s / 60), ss = Math.floor(s % 60); return `${m}:${ss < 10 ? '0' : ''}${ss}`; }
  function musicOnTime() {
    document.getElementById('curTime').textContent = fmtTime(mAudio.currentTime);
    document.getElementById('durTime').textContent = fmtTime(mAudio.duration);
    const seek = document.getElementById('seek');
    seek.value = mAudio.duration ? Math.round((mAudio.currentTime / mAudio.duration) * 1000) : 0;
  }
</script>
  <a class="discord-link" href="https://discord.gg/tracercodes" target="_blank" rel="noopener" title="Join our Discord">
    <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M20.317 4.369A19.79 19.79 0 0 0 16.558 3.2a.074.074 0 0 0-.079.037c-.34.607-.719 1.4-.984 2.022a18.27 18.27 0 0 0-5.487 0 12.6 12.6 0 0 0-.997-2.022.077.077 0 0 0-.079-.037A19.74 19.74 0 0 0 3.677 4.369a.07.07 0 0 0-.032.027C1.255 7.99.59 11.522.916 15.01a.082.082 0 0 0 .031.057 19.9 19.9 0 0 0 5.993 3.03.078.078 0 0 0 .084-.028c.462-.63.874-1.295 1.226-1.994a.076.076 0 0 0-.041-.106 13.1 13.1 0 0 1-1.872-.892.077.077 0 0 1-.008-.128c.126-.094.252-.192.372-.291a.074.074 0 0 1 .077-.01c3.928 1.793 8.18 1.793 12.062 0a.074.074 0 0 1 .078.009c.12.099.246.198.373.292a.077.077 0 0 1-.006.127 12.3 12.3 0 0 1-1.873.892.077.077 0 0 0-.041.107c.36.698.772 1.362 1.225 1.993a.076.076 0 0 0 .084.028 19.84 19.84 0 0 0 6.002-3.03.077.077 0 0 0 .032-.056c.5-4.094-.838-7.598-3.549-10.614a.061.061 0 0 0-.031-.028zM8.02 12.89c-1.182 0-2.157-1.085-2.157-2.419 0-1.333.956-2.418 2.157-2.418 1.21 0 2.176 1.094 2.157 2.418 0 1.334-.956 2.419-2.157 2.419zm7.975 0c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.955-2.418 2.157-2.418 1.21 0 2.176 1.094 2.157 2.418 0 1.334-.946 2.419-2.157 2.419z"/></svg>
    <span>discord.gg/tracercodes</span>
  </a>
</body>
</html>
