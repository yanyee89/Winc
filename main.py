# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

#Greet template
def greet(name,greeting= 'Hello, <name>!'):
    return greeting.replace('<name>', name)

#force
def force(mass, body = 'earth'):
    planet_gravity={
        'sun': 274,
        'jupiter': 24.9,
        'neptune': 11.2,
        'saturn': 10.4,
        'earth': 9.8,
        'uranus': 8.9,
        'venus': 8.9,
        'mars': 3.7,
        'mercury': 3.7,
        'moon': 1.6,
        'pluto': 0.6
        }
    output = (mass * planet_gravity[body])
    return output

#gravity
def pull(m1, m2, d):
    G = 0.00000000006674
    f = G*((m1 * m2)/d**2)    
    return f

#print(pull(22,5,5))



print(greet('steve', 'hello and welcome <name>'))

