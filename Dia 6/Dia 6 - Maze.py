# Dia 6 - 100DaysOfCodeChallenge
# Maze
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
'''
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def wall_on_left():
    turn_left()
    if wall_on_front():
        return True
    else:
        return False

while not at_goal():
    if not wall_on_right():
        turn_right()
        move()
    elif not wall_in_front():
        move()
    else:
        turn_left()
'''