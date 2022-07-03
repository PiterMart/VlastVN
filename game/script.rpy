# OX RELATED FILES
image ox = "images/characters/OX/OX_idle.png"

define o = Character("OX" )

# YX RELATED FILES

image yx = "images/characters/test/test2.png"
image yx angry = "images/characters/test/test2 angry.png"

define y = Character("YX")

# DR HIKORI FILES

image dr hikori = "images/characters/test/dr.png"

# The game starts here.

label start:

    scene bg blame-site
    # play music "audio/04. Sorry about my face - I mustn't forget to delete this.flac"

   
    show ox 


    # scene YX carrying on her back OX

    o "Uh.. whats happening...?"
    o "Where... are we?"

    show yx at left

    y "It was time for you to reboot. I was starting to worry."

    o "Whats... whats with all this corrupt files in my memory...?"

    hide ox
    hide yx
    with fade
    show yx at center

    y "Here we are, finally..."

    scene bg world-scene

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

    # scene starting place

    scene bg wall-megastructure

    show ox at right

    y "Did you hear that?"

    show yx at left

    o "No, what did you hear?"

    y "It was probably nothing"













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
