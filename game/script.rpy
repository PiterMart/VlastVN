# OX RELATED FILES
image ox = "images/characters/OX/OX_idle.png"
image side ox = "images/characters/OX/side-OX_idle.png"

define o = Character("OX", image="ox" )

# YX RELATED FILES

image yx = "images/characters/YX/YX_idle.png"
image side yx = "images/characters/YX/side_YX.png"
image yx angry = "images/characters/test/test2 angry.png"
image yx carry = "images/characters/YX/YX_carrying_OX.png"

define y = Character("YX", image= "yx")

#TINY ROBOT FILES

define tr = Character("Tiny Robot")
image tr = "images/characters/tiny robot/robot_tiny.png"

# DR HIKORI FILES

image dr hikori = "images/characters/test/dr.png"

# The game starts here.

label start:

    scene bg blame-site
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
    show yx at center
    show ox at right

    y "Finally... we are here..."

    play music "audio/intro-story.mp3"

    scene bg world-scene
    with fade

    "Its the year 3633"
    "Earth is no longer how it used to be..."
    "Now its just a big dessert and a couple ponds of salty water"

    #scene of last human buildings

    "Very few humans remain... The ones that stayed to pretend they can manage humanity's factory"

    #scene of the megastructure

    "A 13,000,000 km² hexagonal metal megastructure on the Southest point on earth"
    "Inside, theres only robots. A whole ecosystem of them, Fabricating all human desires."
    # scene of earth being destroyed

    "The ozone layer cant wistand the flares of the biggest sun storm the solar system has ever experienced."
    "The whole earth's surface erupts in flames, all whatever was left, dead or alive is finally erased from it."
    # scene of the megastructure in the apocalypse

    "The only thing still standing, is humanity's factory"

    stop music

    # scene starting place
    
    play music "audio/megastructure1.mp3"

    scene bg wall-megastructure
    with fade
    play audio "audio/apocalypse.mp3"
    pause 4
    # stop music
    # play music "audio/megastructure1.mp3"
    # pause 2

    show yx at right

    y "Did you hear that?"

    show ox at left

    o "No, what did you hear?"

    y "It was probably nothing"
    y "And whats that?"

    o "What?"

    y "This"

    # angry o
    o "what?! there's nothing there!"

    # pointing at a seemlesly plain wall

    y "THIS!"

    o "..."

    #yx punching thru the wall revealing its hollow
    play sound "audio/wallpunch.mp3"
    pause 3

    y "Now you see?"

    o "Well... Now I do... Certainly."
    o "Sometimes I wonder how can you forget i haven't got a sismic sensor like you."
    o "What now? is it just a hollow wall? Whats on the other side?"

    #Robot appears in the hole
    play sound "audio/tiny-robot.mp3"
    pause 3.6
    show tr at center
    tr "Hi, good day, or night."

    o "Hi..."

    tr "I dont recognize you, well.. I dont recognize most things. I never left this fuel deposit. Why did you break the wall?"

    y "We are searching for a scientist hiding within the walls of the factory. Did you happen to see him?"

    tr "I belive i should be the one making questions. I cant detect any certifications in any of you. It seems like you are trespassing"

    #robot eyes start to blink red

    #YX shows the palm of her hand to the tiny robot, a hole opens in the middle of it and a sonic wave blasts the tiny robot away and smashes him against a wall
    play sound "audio/yx_shoot.mp3"
    pause 11.17
    hide tr
    y "Well that wasn't of much use"

    # y sad

    y "Im not a very good detective"

    o ""















    #from where we left the starting scene

    y "I belive we are about to finally reach the core interface link"
    

    o "but how did we get here?"

    y "It's a very long story."

    hide ox
    with fade
    show yx angry

    y " it was the hexagons"

# game end

    return
