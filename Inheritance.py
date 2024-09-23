#Single Inheritance
'''class parents:
    mobile="Redmi note11"
class child(parents):
    laptop="Infinix"
pb=child()
print(pb.mobile)
print(pb.laptop)'''
class student:
    name="pooja"
class english(student):
    eg=99
class science(english):
    sc=98
class python(science):
    py=100
class java(python):
    jv=101
pb=java()
print(pb.name)
print(pb.eg)
print(pb.py)
#multiple Inheritance
"""
class parents:
    mobile="Redmi note11"
class child(parents):
    laptop="Infinix"
class subchild(child):
    pass
pb=subchild()
print(pb.mobile)
print(pb.laptop)"""
