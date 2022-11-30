import re
file = "R13.rst"
pattern = r'R([0-9]+).rst'
suffix='C'
group = fr"{suffix}\g<1>"
replaced = re.sub(pattern, group, file)
print(replaced)
