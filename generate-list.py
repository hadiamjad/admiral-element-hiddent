input_file = 'easylist_general_hide.txt'
output_file = 'easylist_ids.js'

easylist_ids = set()

with open(input_file, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if line.startswith('###'):
            selector = line[3:]
            if selector and not selector.startswith('.') and not selector.startswith(':') and ' ' not in selector:
                easylist_ids.add(selector)

# Generate JavaScript Set syntax
js_set_lines = ['const easylistSelectors = new Set([']
for item in sorted(easylist_ids):
    js_set_lines.append(f'  "{item}",')
js_set_lines.append(']);')

# Write to file or print
with open(output_file, 'w', encoding='utf-8') as f:
    f.write('\n'.join(js_set_lines))

print(f'JavaScript Set written to: {output_file}')
