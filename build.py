# Builds the installable web app (index.html) from the shared app body.
import pathlib,re
root=pathlib.Path(__file__).parent
body=(root/'app-body.html').read_text()
head='''<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#EDF0F5" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0B1019" media="(prefers-color-scheme: dark)">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="apple-mobile-web-app-title" content="Calisthenics">
<meta name="description" content="Your 8-week home calisthenics plan with daily workouts, form guides and progress tracking.">
<link rel="manifest" href="manifest.webmanifest">
<link rel="apple-touch-icon" href="icons/apple-touch-icon.png">
<link rel="icon" type="image/png" href="icons/icon-192.png">
<style>:root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0;font-size:14px;font-family:system-ui,sans-serif}img{max-width:100%}[hidden]{display:none!important}</style>
</head><body>
'''
tail='''
<script>if('serviceWorker' in navigator){window.addEventListener('load',()=>{navigator.serviceWorker.register('sw.js').catch(()=>{});});}</script>
</body></html>
'''
(root/'index.html').write_text(head+body+tail)
print('built index.html',len(head+body+tail),'bytes')
