from jinja2 import Template

name = "Peter"
age = 34

tm = Template("my name is {{ name }} and I am {{ age }}")
msg = tm.render(name=name, age=age)

print(msg)
