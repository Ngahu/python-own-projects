{ % extends
"layout.html" %}
{ % block
body %}
< h2 > Login < / h2 >
{ % if error %}
< p


class ="error" > < strong > Error:<

    / strong > {{error}}
{ % endif %} < / p >

< form
action = "{{ url_for('login') }}"
method = "post" >
< dl >
< dt > Email: < / dt >
< / dl >
< / form > < input
name = "email"
type = "text" / >

Password:

< input
name = "password"
type = "password" / >

< input
type = "submit"
value = "Login" / >

{ % endblock %}
