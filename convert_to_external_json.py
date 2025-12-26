import re

# Read the original HTML
with open('intox8000_Anomalies/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find and remove the embeddedData definition (line with const embeddedData = {...};)
# This is a large JSON object on a single line
pattern = r'const embeddedData = \{.*?\};'
content = re.sub(pattern, '// Data loaded from external JSON file', content, flags=re.DOTALL)

# Replace the loadData function to use fetch
old_load = 'allData = embeddedData;'
new_load = '''const response = await fetch('intox8000-data.json');
                if (!response.ok) throw new Error('Failed to load data');
                allData = await response.json();'''

content = content.replace(old_load, new_load)

# Write the new HTML
with open('intox8000_Anomalies/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Converted to external JSON loading")
