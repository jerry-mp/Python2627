# Unit 2 Project: Text Monster Game
# Overview:
'''The Unit 2 Project is a text-based adventure game! In this game you will navigate a character through a 'dungeon', collecting items along the way to defeat the main monster.
    The purpose of this project is to bring together concepts that you have learned so far: lists, conditionals, and the while loop.
    You will want to pay careful attention to the requirements below; there may be multiple lists that are needed, and multiple while loops, to make this game possible!'''

#Objectives:
#1. Use lists to store data during the game play
#2. Use conditionals to control to the flow of the game game based on user-inputs
#3. Use a while loop to keep the game active while the player is still alive/the game has not yet been won
#4. Be able to terminate the game given conditions of either the player dying, the player quitting, or the game being won.

#Requirements
#1. Map
    #a. the map of the game is three floors, stored in a list
    #b. each floor has 3-5 rooms (be consistent with your choice across the three floors for now!)
    #c. the player should always start in the same place within the game

#2. Room contents
    #a. Rooms should contain "something". This could be an item the player picks up ("sword"), it could be an empty room ("empty room"), or it could be a monster ("name of monster") that guards that particular room
    #b. if there is an item the player can pick up in the room, the room becomes "empty" after the player grabs it
    #c. if a monster is killed, then the room becomes "empty"
    #d. some rooms may contain stairs

#3. Movement
    #a. the player can move room-to-room using commands such as 'left', 'right', 'up', 'down'
    #b. the player can only move up or down in rooms where there are stairs to do so
    #c. if the player tries to move left or right beyond the length of the floor, that movement should be prevented (think of list index issues!)

#4. Inventory
    #a. the player has an inventory that starts out empty at the beginning of the game
    #b. the player can add items to the inventory that they find in rooms (swords, etc.)
    #c. in order to fight a monster in game, the player must have a sword in their inventory
    #d. you should be prevented from being able to pick up items in a room that would not normally be placed in an inventory, such as monsters, stairs, etc.

#5. Monsters
    #a. there must be 2-3 monsters distributed throughout the map; one of those monsters should be the main monster/final boss
    #b. the player must have some weapon to fight and defeat a monster
    #c. to defeat the final boss, you must have a sword and a secondary special item in the player's inventory

#6. Win/Lose Conditions

#The following condition must be true in order for the player to win the game:
    #a. The player defeats the main monster and grabs the prize the main monster was holding

#The following conditions result in the game ending and needing to be restarted
    #a. The player fights a monster without the required weapon/items
    #b. the player tries to go past a monster in a room
    #c. the player chooses the command to stop/quit the game

#Helpful Starting Considerations:
#1. Consider making your gameboard three separate lists for each floor, for now.
#2. Keep track of the player's position using two variables: 
    #player_room = 0
    #player_floor = floor_1
#3. Create an empty list for the inventory
#4. Consider storing all known actions the player can make in a list itself, to help with flow of control!

#What is next?
# Create a new file called unit2_project_lastName.py
# Work systematically! Create your known variables, lists, etc. before tackling the while loop
# Pseudocode: create a basic template for thinking about how the game is played, how to deal with player movement, adding items to an inventory, etc.



