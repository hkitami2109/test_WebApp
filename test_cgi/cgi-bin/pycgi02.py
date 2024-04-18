#!/usr/bin/python3
# -*- coding: utf-8 -*-
import cgi
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
print("[Python CGI Test 02]",file=sys.stderr)
print('Content-Type: text/html; charset=UTF-8\n')
html_body = """
<h1>[Python3 CGI test 02]</h1>
<h2>area01 = "%s"</h2>
<h2>area02 = "%s"</h2>
"""
form = cgi.FieldStorage()
area01 = form.getvalue('area01', '')
area02 = form.getvalue('area02', '')
print(html_body % (area01, area02))
