# The script of the game goes in this file.

#IMAGES
image forest = "bg room.jpg"
image chick = "chick.png"
image birb = "birb.png"


#CHARACTER
define c = Character("Chick")
define b = Character("Birb")

# >>>>>>>>>>The game starts here.<<<<<<<<<<
#NOTES
        #want to add music? play music "exactfilename.exacttype" .... stop music
label start:
    #POINTS
    $ chickPoints = 0
    $ birbPoints = 0

    #STORY
    scene forest
    show chick at left
    show birb at right
    "This is Chick and Birb, They are the realest birds in the universe"
    hide chick
    hide birb
    show chick 
    c "Hi dudes my name is Chick the Chicken"
    c "I like to eat chicken nuggets from Mcdonalds. Someone said thats something called 'can ball ism' but I don't know that sounds like a basketball philosphy"
    hide chick
    show birb
    b "Yo wasssuuuup my birbs. Its ya boi Birb the Bird"
    b "Imma spill some tea here. I think Chick the Chicken is the dumbest bird alive a disgrace to all birbs in the universe. Ya didn't hear this from me."
   
    menu:
        "Hey Birb. You lookin extra real fine todayyy":
            jump happybirb
        "Hey Birb I heard that you dumb boi":
             jump annoyedbirb

    label happybirb:
        b "ayy back atchu my boi. you my boi 4evaaa"
        jump gameintro
    label annoyedbirb:
        b "wtf u dumb too. *slaps Chick* this dumb boi can't fit anything inside his brain look who's talkin smack"
        "Birb leaves the chat"
        jump gameintro

    label gameintro:
        c "Hey birb wanna play a game?"
        b "Sure whats it called"
        c "Don't ask me dumb questions and just play the game"
        "Do you want to play?"
        menu:
            "Yes":
                jump game
            "No":
                jump home
    
    label game:
        "Great lets play"
    label home:
        "You suck boi"
# This ends the game.

    return
