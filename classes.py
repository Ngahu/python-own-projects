1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
< !doctype
html >
Flaskr
< div


class ="page" >

< h1 > Flaskr < / h1 >
< div


class ="metanav" > {% if user.email %}

< a
href = "{{ url_for('logout') }}" > log
out < / a >
{ % else %}
< a
href = "{{ url_for('login') }}" > log in < / a >
{ % endif %} < / div >
{ %
for message in get_flashed_messages() %}
< div


class ="flash" > {{message}} < / div >


{ % endfor %}
{ % block
body %}{ % endblock %}

< / div >