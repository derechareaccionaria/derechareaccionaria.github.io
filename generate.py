import os
import json

from jinja2 import Template

t = Template("""
<body>
<h1>Derecha reaccionaria</h1>

<h3>Mirror</h3>

source <a href="https://web.archive.org/web/20210613200617js_/https://reaccionconservadora.net">Web archive</a>

{% for x in data %}
 <h4><b>Nombre: {{ x["nombre"] }}</b> </h4>
 <p><b>Bio</b>{{ x["bio"] }} </p>
 <p><b>provincia </b> {{ x["provincia"] }}</p>
 <p><b>antiderechos </b> {{ x["antiDerechos"] }}</p>
 <img src="{{ x["imagen"]}}" alt="Italian Trulli">
<hr>
<p></p>
{% endfor %}

</body>

""")


with open("nodes.json", "r") as f:
    data = f.read()

    jdata = json.loads(data)

    print(jdata)

index = t.render(data=jdata)
with open("index.html", 'w') as f:
    f.write(index)
