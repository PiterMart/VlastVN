# OX RELATED FILES
image ox = "images/characters/OX/OX_idle.png"
image side ox = "images/characters/OX/side-OX_idle.png"

define o = Character("Ooshio", image="ox" )

# YX RELATED FILES

image yx = "images/characters/YX/YX_idle.png"
image side yx = "images/characters/YX/side_YX.png"
image yx angry = "images/characters/test/test2 angry.png"
image yx carry = "images/characters/YX/YX_carrying_OX.png"

define y = Character("Yuudachi", image= "yx")

# TINY ROBOT FILES

define tr = Character("FM-01", image="tr")
image tr = "images/characters/tiny robot/robot_tiny.png"
image side tr = "images/characters/tiny robot/robot_profile.png"

# SENTRY

define s = Character("Sentry", image="s")
image s = "images/characters/sentrys/sentrys.png"
image side s = "images/characters/sentrys/profile_sentry.png"


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

    sceme bg earth
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

    scene bg factory-from-space
    with fade

    "The only thing still standing, is humanity's factory."
    "Built as a huge faraday cage."
    "Preserving humanity's biggest factory."

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
    o "Sometimes I wonder how can you forget i haven't got a sismic sensor like you."
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

    y "Listen, we are searching for a specific human within this walls."
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

    y "Im not a very good detective"

    o "Maybe not, but me... "
    o "I would've never been able to even scratch the surface of that wall."

    y "Whats that worth if i cant process the information..."

    o "Hear, next time let me do tha talking, maybe i can persuade this low capability robots"

    y "sight... low capabilities.."

    o " come on dont over process it, lets keep going."
    
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

    y "Wait a second, my sound receptors are sensing something."

    o "Ok let me hear."

    y "Don't worry, I got this."

    o "Let me hear, it's an order."

    y "…"

    o "I don't know why I even ask."



    y "They flew by, probably security sentries.
    … Wait, there it is again."

    o "That's it, I'm connecting to your receptors as well."

    y "whatever…
"
    o "CALCULATING DISTANCE. Lets go, we have to leave. They are coming at us."

    y "I don't belive they are…"

    o "come on lets go! Lets get out of here.."

    stop music

    #silence

    y "Oh, now i see.."

    #sentrys coming

    play audio "audio/sentrys.mp3"

    "Two flying security sentries blast thru a ventilation hatch above the OXYX"

    show s at left

    s "Stop Where you are, you are trespassing ZEHNKR facilities. Shut down your systems immediately or you will be shot."


    o "Defense formation, NOW!"


    #fighting






    
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

    "YX chest opens revealing its insides"

    y "Im very vulnerable when im open, we have to be carefull..."

    o "*Blushed* It's my first time charging from a model-YX... "

    y "Right, haha, let me help you."
    y "Grabs OX's by the waist and  pushes its belly"

    #ah noise

    o "Oh..."

    #yx compartment opens

    "A compartment opens on OX's belly, revealing a female charging plug."

    y "come closer... dont be shy, the cable isnt very long..."

    "OX aprochaes YX and hugs her"

    #electricity noise
    #both hugging

    "her charging plug magnetically attaches "

    

    # o "plugin to YX: th- thanks… this will only take 1 minute and 23 seconds."

    # y "In the end, i m just a walking battery."

    # o "You really do think so. After all, you still can t acknowledge your capabilities. Clearly something is wrong with your computing software."

    # y "Oh so you say? Well, then i might not even be a walking battery. SHUTTING DOWN POWER OUTPUTS."

    # o "HEY! What is it with you? "

    # y "WHAT?!"

    # o "its odd for a robot to be this irrational."

    # y "Irrational? Im a dumb piece of metal, my whole purpose is to be a tool for others."

    # o "Don t you realize I think that of myself as well… I get what you re saying.."

    # y "..INITIALIZING POWER OUTPUTS. Let s just get this over with."

    # o "There s only 23% remaining."


    #walking to the wlevator images


    y "I'm sensing a movement north from our position. Its something really big.."

    o "We have to reach the mainframe of the factory and get access to the structural blueprints."

    Y "And how is it that you plan on doing that.."

    o "Not with that attitude to begin with."

    y "OK."

    o "If we want to finish this mission, you better start trusting me."

    y "Do i have any other options?"

    o "Acting like a jerk."

    y "don't push it…"

    O "give me access to your scans."

    y "sight . DATABASE PERMISSIONS UPDATED. I can't believe im doing this."

    O "There! it seems to be 3.4 km from here. There was a 0.3km displacement of an approximately 500 square meters object. My guess is its some kind of heavy duty elevator. And something has to control it. Lets see it for ourselves."

    y "Whatever you say, big brain. "

    O "Come on, let's keep moving forward there s no time to waste."

















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
