import uiautomator2 as u2

d = u2.connect()

xml = d.dump_hierarchy()

with open("layout.xml", "w") as f:
    f.write(xml)

print("Hierarchy berhasil disimpan.")
