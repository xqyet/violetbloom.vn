define j = Character("Kase", color="#7af5b8")

image bg darkalley = "darkalley.png"
image bg bathroom = "bathroom.jpg"
image jecka = "kase.png"



label start:

    scene bg darkalley 

    play music "audio/ambience/Exterior_Ambience.mp3"

    show kase
    j "It's too quiet here tonight..."

    show kase 
    j "Something feels off."

    show kase
    j "Wait—did I hear footsteps?"

    show kase 
    j "Ugh. Maybe I'm just being paranoid."

    show kase
    j "Still, it's kind of exciting to sneak out like this."

    menu:
        "Go Home.":
            jump go_home

        "Go for a walk.":
            jump go_walk

# === Branch: Go Home ===
label go_home:

    

    show kase 
    j "I better not take any chances."
    scene bg bathroom
    show kase
    j "Back to my room it is."

    

    stop music fadeout 1.0
    return

# === Branch: Go for a Walk ===
label go_walk:

    show kase 
    j "A short walk won’t hurt."

    show kase 
    j "Although... I should stay alert just in case."

    return
