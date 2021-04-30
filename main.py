# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
# Part 1

# Create a variable for every player that scored
scorer_name_0 = 'Ruud Gullit'
scorer_name_1 = 'Marco van Basten'

# Create a variable for each minute of the match that a goal was scored in
goal_0 = 32
goal_1 = 54

# Using the +-operator, create a string that reports on who scored when
scorers = scorer_name_0 + ' ' + str(goal_0) + ', ' + scorer_name_1 + ' ' + str(goal_1)
print(scorers) 

#Use f-strings or the +-operator to create a single string with information about who scored
report = f'{scorer_name_0} scored in the {goal_0}nd minute\n{scorer_name_1} scored in the {goal_1}th minute'
print(report)

# Part 2
# Choose a player that played in the soccer match and store his name as a string in the variable player
player = 'Ronaldje Koeman'

# first_name: use slicing and the find-method (help) to isolate and store the player's first name.
first_name_loc = player.find('Ronaldje')
print(first_name_loc)
first_name = player[0:8]
print(first_name)

# last_name_len: use find, slicing and len to isolate and store the length of their last name.
last_name_pos = player.find(' ')
print(last_name_pos)
# last_name_len = len(player[last_name_pos:len(player)])
last_name_len = len(player[player.find(' ') + 1:])
print('last name length' ,last_name_len)

# name_short: isolate and store the player's name
name_short = player[0] + '.' + player[last_name_pos:len(player)]
print(name_short)

#chant
chant_times = 'Ronaldje! ' * 8
chant = chant_times.strip() 
print(chant)
    
#good_chant
good_chant = chant_times[10:] !='Ronald'
print(good_chant)

    
