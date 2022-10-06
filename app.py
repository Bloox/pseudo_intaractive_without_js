import sys

from importlib.machinery import SourceFileLoader
choices_patch=sys.argv[1]
# imports the module from the given path
output=choices_patch.split(".")[0]
print(choices_patch)

file = SourceFileLoader("Odin",f"{choices_patch}").load_module()

#print(dir(choice))
f=open(f"{output}.html",'w',encoding="utf-8")
#import choice as file
head="""
<!--Automoticly Generated-->
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Fira+Code&family=Noto+Emoji&display=swap');
    {0}
    
    select{
        color:#fff;
        background-color: #0000;
        border:none;
    }
    h1 {
        color:var(--fg0)
    }
    html {
        background-color:var(--bg);
        color:var(--fg1);
        width:800px;
        border:1px solid var(--fg0);
        font-family: 'Fira Code','Noto Emoji', monospace;
    }
    .choice{ 
        margin:20px 0;
    }
    .choice:has(:checked) > .choic {
        display:none;
        
    }
    .choice:has(:checked){
        font-style: italic;
        color:var(--fg0);
    }
    .choice:has(:checked):before{
        content:">";
        padding-right:20px;;
    }
    {1}
    </style>
    <title>Document</title>
</head>\n"""

body="""<body>"""


body+='\n\t'+file.config['theme']+"<select>"
for i in file.data:
    body+=f'\n\t\t<option value="{i["name"][1]}">{i["name"][0]}</option>'
body+='\n\t</select><br><br>'
n=0
c=0
choice_style=""
max_choices=0
for i in file.struct:
    if i[0]=="text":
        text=i[1]
        for j in file.props:
            if f"{'{'}{j}{'}'}" in i[1]:
                text=text.replace(f"{'{'}{j}{'}'}",f'<i class="ins-{j}"></i>')
        text=text.replace("\n",'<br>')
        body+=text+"\n"
    elif i[0]=='choice':
        text=f'<div class="choice" id="c{c}">\n'
        text+='<div class="choic">'
        o=0
        for j in i[1]:
            text+='\n'+f'{j}:<input type="checkbox" name="{j}" class="cc-{o}">'
            o+=1
        text+='\n</div>'
        text+='\n</div>'
        
        body+=text
        choice_style+=f"#c{c}"+"{\n"
        for j in range(len(i[1])):
            choice_style+=f'\t--cc-{j}:var(--o{c}-{j});\n'
        choice_style+="}\n"
        if len(i[1])>max_choices:max_choices=len(i[1])
        c+=1
    n+=1
o=0
for i in range(max_choices):
    choice_style+=f".choice:has(.choic>.cc-{o}:checked)::after"+"{\n\t"
    choice_style+=f'content:"\\a" var(--cc-{o});\n'+"}\n"
    o+=1
style=""
for i in file.data:
    style+=f':root:has([value="{i["name"][1]}"]:checked){"{"}\n'
    print(i)
    for j in i['style']:
        style+=f'\t--{j}:{i["style"][j]};\n'
    for j in i['props']:
        style+=f'\t--p-{j}:"{i["props"][j]}";\n'
    o=0
    ss="\""
    st="\\\""
    for j in i['tree']:
        l=0
        for k in j:
            style+=f'\t--o{o}-{l}:"{k.replace(ss,st)}";\n'
            l+=1
        o+=1
    style+="\n}\n"
for i in file.props:
    style+=f".ins-{i}::after"+"{\n"
    style+=f"\tcolor:var(--fg0);\n"
    style+=f"\tcontent:var(--p-{i});"+"\n}\n"

head=head.replace("{0}",style)
head=head.replace("{1}",choice_style)
body+='\n</body>'
print(head+body)
f.write(head+body)
f.close()