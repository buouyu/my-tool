import re as reg
import pyperclip as clip

clipboard_content = clip.paste()
res = clipboard_content
replaceMap = [[r'\s+', ''], [r'\[', '[\n'], [r'\]', '\n]\n'], [r'{', '{\n'], [r'}', '\n}\n'], [r',', ',\n'], [r'\n,\n$', ''], [r'\n$', '']]
for it in replaceMap:
    res = reg.sub(it[0], it[1], res)
print(res)
clip.copy(res)