#example
struct = [ #here is structure of you file
    #index 0:type("text|choice") index 1:[look at the comments]
    ["text","Welcome {icon}! do you like it?"], #type:str text, you can use {name} to insert thing declaret in props
    ['choice',["yes","no"]],                    #type:list (name for ever choice, any number of them)
    ["text","<b>Text in bold<b/>"], #you can use html!
    ['choice',["0","1","2","3","4"]], #any amout of args!   
]
config = {
    'title':"food!",      #not used at the moment
    'theme':"choose food:"#before variant chosen
}
props = [
    "icon" #list of names of potential props!
]

data=[
    {
        "name":["red",'[none]'], #0 visable(any characters) 1 sytem(ascii only (don't use space))
        "props":{"icon":"🍓"},   #dictionary, {prop_name:prop_value}
        "tree":[
            ['True',"False"],    #output for given choice
            ['2','4','8','16','32']
        ],
        "style":{'fg0':"red",'fg1':"#888","bg":"black"} #style for your html for given variant
    }, #(0) Defult selected
    {
        "name":["blue",'blue'], #0 visable(any characters) 1 sytem(ascii only (nmo space))
        "props":{"icon":"🫐","name":"berry"},
        "tree":[
            ['False',"True"], #each variant has it owen outputs!,
            ['22','44','88','1616','322'] #yes i did't follow any pattern
        ],
        "style":{'fg0':"blue",'fg1':"#888","bg":"black"}
    } #(1) not defult selected
] #supported is any amout of variants