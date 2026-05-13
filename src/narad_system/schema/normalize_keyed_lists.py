from pathlib import Path
import re

path = Path('/home/dianam/projects/NARAD-DataServices/src/narad/schema/narad_UITF_instance.yaml')
text = path.read_text(encoding='utf-8')
pattern = re.compile(r'^(\s*)-\s+([A-Za-z_][A-Za-z0-9_]*)\s*:\s*$', re.MULTILINE)
new_text, count = pattern.subn(r'\1- name: \2', text)
path.write_text(new_text, encoding='utf-8')
print(count)
