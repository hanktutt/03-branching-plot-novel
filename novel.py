#!/usr/bin/python3

import sys

assert sys.version_info >= (3,4), 'This script requires at least Python 3.4'

def show_location(location):
    ''' Displays the description, displays a list of options, accepts and returns user input '''
    description = location["description"]
    options = location["options"]
    print(description)
    if len(options) == 0:
        return "quit"
    while True:
        for o in options:
            print('[' + o["option"] + '] ' + o["display"])
        print('[q] to quit')
        choice = input("What do you choose? ")
        if choice.lower() == 'q':
            return "quit"
        for o in options:
            if choice.lower() == o["option"].lower():
                return o["result"]
            print("Please choose one of the options:")



world = {
"start":{
"description":"You are an astronaut on a lunar space mission. You start your mission after you have just landed."
,"options":[
{
"display":"You can exit the spacecraft"
,"option":"1"
,"result":"lunar landing base"
}
,{
"display":"You can stay until ready"
,"option":"2"
,"result":"start"
}
]
}
,"lunar landing base":{
"description":"You are at the base"
,"options":[
{
"display":"You can leave to explore"
,"option":"1"
,"result":"outskirts of base"
},
{
"display":"You can gather supplies"
,"option":"2"
,"result": "depot"
},
{
"display":"You can go back to ship"
,"option":"3"
,"result":"start"
}
]
}
,"depot": {
"description":"You have just gathered supplies. Press 1 to retrun to base."
,"options":[
{
"display":"return to base"
,"option":"1"
,"result":"lunar landing base"
}
]
}
,"outskirts of base":{
"description":"You just left the base. Now where?"
,"options":[
{
"display":"you can go to a crater"
,"option":"1"
,"result":"crater"
}
,{
"display":"you can go to a cave"
,"option":"2"
,"result":"cave"
}
,{
"display": "you can go back to base"
,"option":"3"
,"result":"lunar landing base"
}
]
}
,"crater":{
"description":"You jumped down into a crater to take a look."
,"options":[
{
"display":"You can look behind a strange rock"
,"option":"1"
,"result":"rock"
},
{
"display":"You can look into a hole"
,"option":"2"
,"result": "cave depths"
},
{
"display":"You can go back to outskirts of base"
,"option":"3"
,"result":"outskirts of base"
}
]
}
,"rock":{
"description":"You have found some alien treasure!"
,"options":[
{
"display":"You can take it!"
,"option":"1"
,"result":"alien attack"
},
{
"display":"You can leave it."
,"option":"2"
,"result": "crater"
},
]
}
,"alien attack":{
"description":"The Aliens tracked you down after you stole their treasure!"
,"options":[
{
"display":"You can try to run to base"
,"option":"1"
,"result":"death"
},
{
"display":"You can try to fight back"
,"option":"2"
,"result": "death"
},
{
"display":"You can try to hide in a cave"
,"option":"3"
,"result":"cave"
}
]
}
,"cave":{
"description":"You are safely hidden inside a cave!"
,"options":[
{
"display":"You can explore a hole"
,"option":"1"
,"result":"cave depths"
},
{
"display":"You can climb up into a tunnel"
,"option":"2"
,"result": "cave tunnel"
},
{
"display":"You can go back to the outskirts of the base"
,"option":"3"
,"result":"outskirts of base"
}
]
}
,"cave tunnel":{
"description":"You are going deeper and deeper into the cave"
,"options":[
{
"display":"You can explore a hole"
,"option":"1"
,"result":"cave depths"
},
{
"display":"You can climb out of tunnel through opening"
,"option":"2"
,"result": "dark side of the moon"
},
{
"display":"You can go back to the way you came"
,"option":"3"
,"result":"cave"
}
]
}
,"dark side of the moon":{
"description":"You have found the dark side of the Moon! You have won the game!"
,"options":[]
}
,"death":{
"description":"You have been eliminated by the Aliens :( "
,"options":[]
}
,"cave depths":{
"description":"You have fallen down a hole in the Cave and there is no way out!"
,"options":[]
}

}


location = "start"
while location != "quit":
    location = show_location(world[location])