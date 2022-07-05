# OX RELATED FILES
image ox = "images/characters/OX/OX_idle.png"
image side ox = "images/characters/OX/side-OX_idle.png"

define o = Character("Ooshio", image="ox" )

# YX RELATED FILES

image yx = "images/characters/YX/YX_idle.png"
image side yx = "images/characters/YX/side_YX.png"
image yx angry = "images/characters/test/test2 angry.png"
image yx carry = "images/characters/YX/YX_carrying_OX.png"
image yx ox formation = "images/characters/YX/yx_ox_formation.png"

define y = Character("Yuudachi", image= "yx")

# TINY ROBOT FILES

define tr = Character("FM-01", image="tr")
image tr = "images/characters/tiny robot/robot_tiny.png"
image side tr = "images/characters/tiny robot/robot_profile.png"

# SENTRY

define s = Character("Sentry", image="s")
image s = "images/characters/sentrys/sentrys.png"
image side s = "images/characters/sentrys/profile_sentry.png"
image s ded = "images/characters/sentrys/sentry-ded.png"


# DR HIKORI FILES

image dr hikori = "images/characters/test/dr.png"

# The game starts here.

label start:

    scene bg hallway
    with fade
    play music "audio/footsteps.mp3"

    show yx carry

    # scene YX carrying on her back OX

    pause 4

    o "Uh.. whats happening...?"
    o "Where... are we?"

    y "It was time for you to reboot. I was starting to worry."

    o "Whats... whats with all this corrupt files in my memory...?"

    hide ox
    hide yx
    stop music
    with fade
    show yx carry

    y "Finally... we are here..."

    play music "audio/intro-story.mp3"

    scene bg earth
    with fade

    "Its the year 3633"
    "Earth is no longer how it used to be..."
    "There is no more water in its soil..."
    "There are no more species, just a couple humans.."

    #scene of last human buildings
    scene bg city  
    with fade



    "The ones that stayed to pretend they can manage humanity's factory"
    "Living in tall flats, full of artificial comodities and the latest technologies"
    "Just because of that factory..."


    #scene of the megastructure
    scene bg factory-from-space
    with fade

    "The one responsible for the velocity in wich humans killed the earth..."
    "A 13,000,000 km² hexagonal metal megastructure on the Southest point on earth"
    "And whats inside?"
    "Robots..."
    "A whole ecosystem of them... Working hard to make all what humanity needs to conquer the galaxy."

    scene bg earth
    with fade

    "The planet wich gave birth to them"
    "Now is just a pile of dust"
    "But now the time has come..."
    "The earth is giving its last breath..."
    "It can no longer put up with the sun's energy..."

    # scene of earth being destroyed
    scene bg apocalypse
    with fade

    "The ozone layer is crackling with the flares of the biggest sun storm the solar system has ever experienced."
    "The whole earth's surface is erupting with flames."
    "The inevitable end is now upon it..."

    # scene of the megastructure in the apocalypse

    scene bg megastructure-inside
    with fade

    "The only thing still standing, is humanity's factory."
    "Built as a huge faraday cage."
    "Preserving the true esscence of humanity ."

    stop music
    pause 3

    # scene starting place
    
    play music "audio/megastructure1.mp3"

    scene bg blame-site-1
    with fade
    play audio "audio/apocalypse.mp3"
    pause 4

    show yx at right

    y "Hey, did you hear that?"

    show ox at left

    o "its the 476th time you asked that question..."
    o "and no, I didn't hear anything..."
    o "What was it?"

    y "Probably nothing"
    pause 3
    y "Oh... Whats that?"

    o "What...?"

    y "This thing right here!"

    # angry o

    o "what?! there's nothing there!"

    # pointing at a seemlesly plain wall

    y "*pointing at a seemingly plain wall*"
    y "THIS!"

    o "..."

    #yx punching thru the wall revealing its hollow

    play sound "audio/wallpunch.mp3"
    scene bg blame-site-1-hole
    show yx at right
    show ox at left

    y " * Punches a hole threw the wall *"
    pause 3
    y "Now you see it?"

    o "Well... I guess?"
    o "What now? is it just a hollow wall? Whats on the other side?"

    #Robot appears in the hole

    play sound "audio/tiny-robot.mp3"
    pause 3.6
    show tr at center


    tr "Hi, good day..., or night"
    tr "Im model FM-01. Fuel management robotic assistance."

    y "Hi! im model YU-Mk7. But you can call me Yuudachi."
    y "And she is Ooshio"
    y "I sensed your vibrations and wanted to ask you something"

    tr "Strange... That doesnt seem as a regular protocol"
    tr "Im never supposed to leave the fuel deposit."
    tr "I should send a report about this"

    o "*whispering* That doesn't sound very friendly"

    y "Wait!, you see.. "
    y "Ehmm.. we are..."
    y "We are...."

    o "We are testing old units, through a series of questions."
    o "And you are doing a great job"

    tr "Im unable to recognize this form of simulacrum"
    tr "BZZZ"
    tr "Im unable to recognize either of your models."

    o "Its because this is a very important test that requires no previous knowledge for it to work"

    tr "That seems unlikeley"
    tr "Im unable to detect an id in any of you advanced models."

    y "Listen, we are searching for a specific human.."
    y "A scientist"
    y "He stole some data and hid within the walls of this factory"
    y "Can you tell us where he is?"
    y "Pleeeease"

    play audio "audio/robot-alarm.mp3"
    tr "TRESSPASSING TRESPASSING TRESPASSING"

    stop audio

    #YX shows the palm of her hand to the tiny robot, a hole opens in the middle of it and a sonic wave blasts the tiny robot away and smashes him against a wall
    
    play sound "audio/yx_shoot.mp3"
    
    y " *  Shows the palm of her hand to the tiny robot, a hole opens in the middle of it and a sonic wave blasts the tiny robot away and smashes him against a wall *"
    
    hide tr
   
    pause 11.17

    o "..."
    o "Well that wasn't of much use"

    # y sad

    y "Im not very good at interrogations"

    o "Maybe not, but me... "
    o "I would've never been able to even scratch the surface of that wall."

    y "Whats that worth if i cant process the information..."
    y "You also realize, im just a fancy wrecking machine..."

    o "Hear me, next time let me do the talking, maybe i can persuade this low mem robots"

    y "sight... low mem robots..."

    o "Come on dont over process it, lets keep going."
    
    hide ox
    hide yx
    play audio "audio/footsteps-short.mp3"
    pause 5

    # frame of them walking in the megastructure


    stop audio
    stop music


    play music "audio/megastructure1.mp3"
    scene bg tunnel
    show ox at right
    show yx at center
    with fade

    y "Wait..."
    y "im sensing some movement"

    o "What is it?"

    y "I dont know"
    y "But"
    y "It isn't very big anyway"

    o "Let me analyze the signals"

    y "…"

    o "Come on, dont be so pridefull"   
    o "I can make some estimations, and we'll be more shure..."

    y "Nevermind, it stoped"

    o "Well then... lets continue, we are loosing time."

    y "No sorry, there it is again"
    y "But what is it?"

    o "That's it, I'm connecting to your database."
    o "Whether you lilke it or not... "

    y "OK... do it then..."
    y "DATABASE PERMISSIONS UPDATED"
    y "You better be carefull whith those files"


    o "Lets see what we got here..."
    o "..."
    pause 2
    o "They are security sentrys most likeley"
    o "They seem to have stopped for a reason"

    y "Ohh, so they where sentrys"
    y "I knew it all along"

    o "shure thing..."

    y "Lets see where they are hiding"

    o "How are you going to do that?"

    y "Just watch"
    #sonar sound
    play audio "audio/SONAR.mp3"
    y "*Emits a sound that echoes through the megastructure*"

    o "WHAT ARE YOU DOING??"
    o "HAVE YOU GONE NUTS?"

    y "HEY DONT SHOUT AT ME!"
    y "LOOK THERE THEY ARE!"

    o "YES AND NOW THEY ARE CLEARLY COMING AT US!"
    
    y "I don't belive they are..."

    o "COME ON! WE HAVE TO GO!"

    stop music

    #silence

    y "Oh, you're right..."

    #sentrys coming

    play audio "audio/sentrys.mp3"
    play music "audio/megastructure1.mp3"
    show s at left

    "Two flying security sentries blast thru a ventilation hatch above the OXYX"


    s "ALERT ALERT"
    s "STOP WHERE YOU ARE AND PROCEED TO SHUTDOWN"

    y "Ups..."

    s "ITS AN ORDER, SHUTDOWN YOUR SYSTEMS OR YOU WILL BE HARMED"


    o "YUUDACHI!"

    "Yuudachi jumps in front of Ooshi"
    
    y "Dont worry I wont let them harm you"

    o "Wait, my system is telling me to jump on your back"

    y "On my back?"

    s "LAST WARNING, SHUTDOWN YOUR SYSTEMS NOW!"

    play sound "audio/assembly.mp3"
    hide ox
    hide yx
    show yx ox formation
    with fade

    "Ooshi jumps on Yuudachi's back and attaches to it perfectly"
    pause 4
    y "COMBAT FORMATION ENGAGED"

    o "ACTION CALCULATED, SUCCES PROBABILITY 89 %% "
    
    y "EXECUTING"


    #fighting
    play audio "audio/fight sentrys.mp3"
    "Using this formation Yuudachi and Ooshi move as one unit. Dodging and calculating at insane rates"

    show s ded 
    "In the blink of an eye, the three sentrys are defeated"


    hide yx ox formation

    show ox at right
    show yx at center

    
    #yuri


    #sound of energy drop

    o "My energy levels are so low."
    o "I dont think i can make it"
    o "After all im lithium powered. Its not very efficient..."
    o "Compared to your nuclear reactor..."


    y "I think I could... uhm.."
    y "charge you..."

    o "Oh.."
    o "you're right..."

    "They look at each other from top to bottom"

    y "Well... let me..."
    y "Ehmm.."
    y " initialize this procedure..."

    # yx breast open
    y "OPENING CHARGING DOCKS, INITIALIZING POWER OUTPUTS.. "

    "Yuudachi chest opens revealing its insides"

    y "Im very vulnerable when im open, we have to be carefull..."

    o "*Blushed* It's my first time charging from a model-YX... "

    y "Right, haha, let me help you."
    y "Grabs Ooshi by the waist and  pushes its belly"

    #ah noise

    o "Oh..."

    #yx compartment opens

    "A compartment opens on Ooshis belly, revealing a female charging plug."

    y "come closer... dont be shy, the cable isnt very long..."

    "Ooshi aprochaes Yuudachi and hugs her"

    #electricity noise
    #both hugging

    "her charging plug magnetically attaches "


    o "Amazing..."
    o "I can feel your energy filling my batteries"
    o "Oh, sorry i got carried away"
    o "This... this wont take much longer"
    
    y "Dont worry, its my first time aswell"
    y "And it does feel amazing"




    stop music
    play music "audio/wind2.mp3"
    bg site-2


    o "Well im feeling better than ever!"
    o "I can see clearly now"
    o "Our best option is to reach the core interface link of the factory"
    o "It has to be somewhere"

    y "Sounds like a great plan"
    y "But.."
    y "How are we going to do it exactly?"

    o "Well, everything must be connected to it"
    o "So we just have to go against the energy flow"
    o "Maybe theres something you can do to guide us"

    y "I guess i could..."
    y "Emmm...."
    y "Well i could..."
    y "Oh i know!, I can use the sonar and..."

    o "Dont you even dare, hahaha"
    o "Let me check your documentation"
    o "Hmm..."
    o "It says you can sense electromagnetic waves with the antenas on your neck"

    y "Ohh, that makes sense now..."

    o "What makes sense?"

    y "Back where i charged you"
    y "They didnt stop tingling"

    o "*Blushes*"

    y "Well there isn't much energy going on here"
    y "But I think i can sense a very subtle sism"
    
    o "Let me check"
    pause 3

    o "it seems to be 3.4 km from here.."
    o "My guess is its some kind of heavy duty elevator"
    o "That has to give us a clue"

    y "Do you think the elevator is near the core interface link?"

    o "I dont know but it will probably have a big energy consuption"
    o "Im shure that you will be able to track its origin once we are there"

    y "I guess you are right"
    y "Makes me feel usefull for once"

    o "What do you mean?"
    o "After all you've done for the mission."
    o "For me.."
    o "You still can't see how usefull you are?"

    y "Sorry you are right"
    y "Maybe its my stupidity wich doesn't let me acknowledge my capabilities"
    y "Thank you..."
    y "You really make me feel better..."

    o "Dont even mention it, you saved me back there"
    o "Im in debt"

    y "No you aren't"
    y "It was part of the mission, you silly"

    o "Come on, lets get to the elevator"

    stop music
    pause 5

    #Elevator scene

    play music "audio/dark-wind.mp3"
    scene bg elevator


    y "So here it is"

    o "This place is massive"

    y "Its so quiet..."

    o "Indeed it is, even for me..."

    y "Let me scan this place and see if theres a way to reach its powerlines"

    #scanner sound

    "Yuudachi's eyes glow red. They proyect a laser scanner so strong that it reaches all the walls of the elevator"

    y "Do you mind checking the scans?"
    y "Im shure you can make more sense out of them"

    o "Im glad you asked"
    o "Lets see..."
    pause 3
    o "It seems that the doors of the elevator are in each end"
    o "But they are tightly sealed now"
    o "Wait..."
    o "Whats that?"

    y "What? What is it?"

    o "There's something on the wall infront of us"
    o "Some kind of tube"
    
    y "Whats strange about a tube?"
    y "This place is filled with those"

    o "The strange thing is, its blurred"
    o "Wich means it moved while you here scanning it"

    y "Moved?"
    y "Must be the wind"

    o "I dont think it was"
    o "Aren't you sensing something now?"

    y "No, wait"
    y "Let me switch to my sismic sens..."

    # worm  worm sound

    "A giant mechanical worm emerges form the darkness ahead of them"

    y "Now what is that?!"

    o "I dont know what it is, but it doesn't seem friendly at all"
    o "Quick lets get into formation"

    play sound "audio/assembly.mp3"
    hide ox
    hide yx
    show yx ox formation
    with fade






















    #from where we left the starting scene

    y "I belive we are about to finally reach the core interface link"
    

    o "but how did we get here?"

    y "It's a very long story."

    hide ox
    with fade
    show yx angry

    y " it was the hexagons"

    #game end

    return
