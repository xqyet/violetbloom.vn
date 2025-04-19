define k = Character("Kase", color="#7af5b8")
define h = Character("Hannah", color="#7af5b8")

image bg darkalley = "darkalley.png"
image bg bathroom = "bathroom.jpg"
image kase = "kase.png"
image hannah = "hannah.png"



label start:

    scene bg darkalley 

    play music "audio/ambience/Exterior_Ambience.mp3"

    show kase
    k "It's too quiet here tonight..."
    
    show hannah
    h "testing!"

    show kase 
    k "Something feels off."

    show kase
    k "Wait—did I hear footsteps?"

    show kase 
    k "Ugh. Maybe I'm just being paranoid."

    show kase
    k "Still, it's kind of exciting to sneak out like this."

    menu:
        "Go Home.":
            jump go_home

        "Go for a walk.":
            jump go_walk

# === Branch: Go Home ===
label go_home:

    

    show kase 
    k "I better not take any chances."
    scene bg bathroom
    show kase
    k "Back to my room it is."


    

    stop music fadeout 1.0
    return

# === Branch: Go for a Walk ===
label go_walk:

    show kase 
    k "A short walk won’t hurt."

    show kase 
    k "Although... I should stay alert just in case."

    return
