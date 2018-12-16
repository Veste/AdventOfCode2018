from collections import deque
from enum import Enum
import sys


class Facing(Enum):
	UP = 1
	RIGHT = 2
	DOWN = 3
	LEFT = 4
# end Facing


class Cart:
	def __init__(self, facing, location):
		self.facing = facing
		self.x = location[0]
		self.y = location[1]
		self.intersection_i = 0
	# end __init__

	def __str__(self):
		return "Cart({}: [{},{}])".format(self.facing, self.x, self.y)
	# end __str__

	INTERSECTION_MAP = {
		Facing.UP: {0: Facing.LEFT, 1: Facing.UP, 2: Facing.RIGHT},
		Facing.DOWN: {0: Facing.RIGHT, 1: Facing.DOWN, 2: Facing.LEFT},
		Facing.LEFT: {0: Facing.DOWN, 1: Facing.LEFT, 2: Facing.UP},
		Facing.RIGHT: {0: Facing.UP, 1: Facing.RIGHT, 2: Facing.DOWN},
	}

	TURN_CHANGE_MAP = {
		'/': {
			Facing.UP: Facing.RIGHT,
			Facing.RIGHT: Facing.UP,
			Facing.LEFT: Facing.DOWN,
			Facing.DOWN: Facing.LEFT
		},
		'\\': {
			Facing.UP: Facing.LEFT,
			Facing.RIGHT: Facing.DOWN,
			Facing.LEFT: Facing.UP,
			Facing.DOWN: Facing.RIGHT
		}
	}

	def get_next_intersection_dir(self):
		next_dir = Cart.INTERSECTION_MAP[self.facing][self.intersection_i]
		self.intersection_i = (self.intersection_i + 1) % 3
		return next_dir
	# end intersection_direction
# end Cart


turn_locations = {}
carts = []

w,h = 0,0

inf_name = 'input'
if len(sys.argv) > 1:
	inf_name = sys.argv[1]
with open(inf_name) as in_file:
	for y, line in enumerate(in_file):
		h += 1
		w = len(line)
		#print(y, line)
		for x, c in enumerate(line):
			# Looking for turns
			if c == '/':
				turn_locations[x, y] = '/'
			elif c == '\\':
				turn_locations[x, y] = '\\'
			elif c == '+':
				turn_locations[x, y] = '+'
			# end if

			# Looking for carts
			if c == '<':
				carts.append(Cart(Facing.LEFT, (x, y)))
				#print("LEFT, {},{},  {}".format(x, y, c))
			elif c == '>':
				carts.append(Cart(Facing.RIGHT, (x, y)))
				#print("RIGHT, {},{},  {}".format(x, y, c))
			elif c == '^':
				carts.append(Cart(Facing.UP, (x, y)))
				#print("UP, {},{},  {}".format(x, y, c))
			elif c == 'v':
				carts.append(Cart(Facing.DOWN, (x, y)))
				#print("DOWN, {},{},  {}".format(x, y, c))
			# end if
		# end for
	# end for
# end with

'''
for tl, tt in turn_locations.items():
	print("{}: {}".format(tl, tt))
# end for

print()
'''

carts.sort(key=lambda c: c.x)
carts.sort(key=lambda c: c.y)
for cart in carts:
	#print(cart)
	print("{}:{}".format(cart.y, cart.x))
# end for

crashx, crashy = -1, -1
crashed = False
loop_count = 0
while not crashed:
	loop_count += 1

	'''
	for y in range(h):
		for x in range(w):
			cxy = False
			for cart in carts:
				if cart.x == x and cart.y == y:
					ch = 'X'
					if cart.facing == Facing.UP:
						ch = '^'
					elif cart.facing == Facing.DOWN:
						ch = 'v'
					elif cart.facing == Facing.LEFT:
						ch = '<'
					elif cart.facing == Facing.RIGHT:
						ch = '>'
					# end if
					print(ch, end="")
					cxy = True
					break
			# end for

			if not cxy:
				ch = ' '
				#if (x, y) in turn_locations:
				#	ch = turn_locations[x, y]
				print(ch, end="")
		# end for
		print()
	# end for
	'''
	

	for ci, cart in enumerate(carts):
		if cart.facing == Facing.UP:
			cart.y -= 1
		elif cart.facing == Facing.DOWN:
			cart.y += 1
		elif cart.facing == Facing.LEFT:
			cart.x -= 1
		elif cart.facing == Facing.RIGHT:
			cart.x += 1
		# end facing test

		if (cart.x, cart.y) in turn_locations:
			turn_type = turn_locations[cart.x, cart.y]
			if turn_type == '+':
				cart.facing = cart.get_next_intersection_dir()
			else:
				cart.facing = Cart.TURN_CHANGE_MAP[turn_type][cart.facing]
			# end if
		# end if

		c_locs = [(c.x, c.y) for c in carts]
		if len(carts) > len(set(c_locs)):
			for coi, other_cart in enumerate(carts):
				if coi != ci and cart.x == other_cart.x and cart.y == other_cart.y:
					crashx, crashy = cart.x, cart.y
					crashed = True
					print(loop_count)
					break
				# end if
			# end for
		# end if
	# end for

	carts.sort(key=lambda c: c.x)
	carts.sort(key=lambda c: c.y)
	'''
	if loop_count > 330:
		for y in range(h):
			for x in range(w):
				cxy = False
				for cart in carts:
					if cart.x == x and cart.y == y:
						if cxy:
							ch = 'X'
						elif cart.facing == Facing.UP:
							ch = '^'
						elif cart.facing == Facing.DOWN:
							ch = 'v'
						elif cart.facing == Facing.LEFT:
							ch = '<'
						elif cart.facing == Facing.RIGHT:
							ch = '>'
						# end if
						print(ch, end="")
						cxy = True
				# end for

				if not cxy:
					ch = '-'
					#if (x, y) in turn_locations:
					#	ch = turn_locations[x, y]
					print(ch, end="")
			# end for
			print()
		# end for
		print()
		in_wait = input("waiting")
	# end if
	
	#print('looping')
	'''
# end while

print("{},{}".format(crashx, crashy))

