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
16
17
18
19
20
21
22
{ % extends
"layout.html" %}
{ % block
body %}
{ % if user.email %}

< form


class ="add-entry" action="{{ url_for('add_post') }}" method="post" >

< dl >
< dt > Title: < / dt >
< dd > < input
size = "30"
type = "text" / > < / dd >
< dt > Text: < / dt >
< dd > < textarea
cols = "40"
name = "text"
rows = "5" > < / textarea > < / dd >
< dd > < input
type = "submit"
value = "Share" / > < / dd >
< / dl >
< / form > { % endif %}
< ul


class ="entries" > {% for post in posts %}

< li >
< h2 > {{post['title']}} < / h2 >
{{post['text'] | safe}}
{ % else %} < / li >
< li > < em > Unbelievable.No
posts
here
so
far! < / em >
{ % endfor %} < / li >
< / ul >
{ % endblock %}