define j = Character("Jecka", color="#7af5b8")

image bg darkalley = "darkalley.png"
image bg bathroom = "bathroom.jpg"
image jecka = "jecka.png"
image jecka smile = "jecka_smile.png"
image jecka smoke = "jecka_smoke.png"
image jecka surprised = "jecka_surprised.png"
image jecka worried = "jecka_worried.png"

label start:

    scene bg darkalley 

    play music "audio/ambience/Exterior_Ambience.mp3"

    show jecka
    j "It's too quiet here tonight..."

    show jecka 
    j "Something feels off."

    show jecka 
    j "Wait—did I hear footsteps?"

    show jecka 
    j "Ugh. Maybe I'm just being paranoid."

    show jecka 
    j "Still, it's kind of exciting to sneak out like this."

    menu:
        "Go Home.":
            jump go_home

        "Go for a walk.":
            jump go_walk

# === Branch: Go Home ===
label go_home:

    

    show jecka 
    j "I better not take any chances."
    scene bg bathroom
    show jecka
    j "Back to my room it is."

    

    stop music fadeout 1.0
    return

# === Branch: Go for a Walk ===
label go_walk:

    show jecka 
    j "A short walk won’t hurt."

    show jecka 
    j "Although... I should stay alert just in case."

    return
