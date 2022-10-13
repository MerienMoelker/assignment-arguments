# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

# 1
def greet(name, greeting='Hello, <name>!'):
    greeting = greeting.replace('<name>', name)
    return print(greeting)


# 2
gravity = {
    'sun': 274.0,
    'jupiter': 24.9,
    'neptune': 11.2,
    'saturn': 10.4,
    'earth': 9.8,
    'uranus': 8.9,
    'venus': 8.9,
    'mars': 3.7,
    'mecury': 3.7,
    'moon': 1.6,
    'pluto': 0.6
}
def force(mass, body='earth'):
    f = mass * gravity[body]
    return print(f)


# 3
G = 6.674 * 10**-11
def pull(m1, m2, d):
    f = G * ((m1 * m2) / d**2)
    return print(f)


greet('Doc')
greet('Bob', "What's up, <name>!")
force(80.5)
pull(800, 1500,3)
