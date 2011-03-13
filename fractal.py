from math import log, sqrt

class fractal:
	'''iterator that manages the creation of a fractal image'''
	
	options = {
		'width': 590,	#width in pixels of the fractal area
		'height': 380,	#height in pixels of the fractal area
		'max_iterations': 300,	#maximum number of iterations to perform for each point
		'color_range_repeats': 7	#the amount of times to repeat the color pattern
	}
	
	zoom = {
		'x': -2.3,
		'y': 1.5,
		'width': 3,
		'height': 3
	}
	
	image = []
	
	
	def __init__(self, options):
		'''init function sets up the options'''
		self.options.update(options)
	
	def change_options(self, options):
		'''overrides current options with the newly-supplied set'''
		self.options.update(options)
	
	def draw_fractal(self):
		'''this draws the fractal and returns the image list'''
		z = complex()
		c = complex()
		i = 0
		pixel = 0
		x = 0
		y = 0
		itminus = 0
		colors = {'r':0, 'g':0, 'b':0}
		over_iterated = false
		iteration_divider = self.options['max_iterations'] / self.options['color_range_repeats']
		orig_zoom_height = self.zoom['height']
		
		self.image = []  #reset the image array
		
		#adjust for non-square viewports
		self.zoom['height'] = self.zoom['width'] * (self.options['height'] / self.options['width'])
		self.zoom['y'] = self.zoom['y'] - (orig_zoom_height - self.zoom['height'])/2
		
		#for each vertical row in the viewport
		for y in range(self.options['height']):
			#for each horizontal pixel in the row
			for x in range(self.options['width']):
				z = complex()
				c = self.convert_pixel_to_point(x, y)
				i = 0
				over_iterated = false
				
				while abs(z) < 4 and not over_iterated:
					z = z**2 + c
					i += 1
					
					if i > self.options['max_iterations']:
						#if abs(z) is still less than 4 and we're past our max_iterations counter, assume the point is in the set and color it black
						i = 0
						self.image.extend([0, 0, 0, 255])
						pixel += 4
						
						over_iterated = true
				
				if not over_iterated:
					#if the point is outside the set, color it
					itminus = log(log(sqrt(z.real**2 + z.imag**2), 2), 2)
					colors = self.rainbow_color((i - itminus) / iteration_divider)
					
					self.image.extend([colors['r'], colors['g'], colors['b'], 255])
					pixel += 4
					
		return self.image
		
	
	def convert_pixel_to_point(self, x, y):
		'''takes an x and a y position and converts it to a complex point
		@param int		x
		@param int		y
		
		@return complex
		'''
		stepx = self.zoom['width'] / self.options['width']
		stepy = self.zoom['height'] / self.options['height']
		
		return complex(self.zoom['x'] + x * stepx, self.zoom['y'] - y * stepy)
	
	def rainbow_color(self, position):
		'''takes a value calculated from the coloring algorithm and assigns an r, g, b value to it depending on how high it is
		@param float		position
		
		@return dict {r, g, b}
		'''
		cols = []
		nbars = 6   #number of color bars
		position_int = int(position)
		position_frac = position - position_int
		m = nbars * position_frac
		n = int(m)   #integer portion of m
		f = m - n    #fraction portion of m
		t = int(f * 255)
		color_vals = {
			0: {'r':255, 'g': t, 'b': 0},
			1: {'r':255 - t, 'g': 255, 'b': 0},
			2: {'r':0, 'g': 255, 'b': t},
			3: {'r':0, 'g': 255 - t, 'b': 255},
			4: {'r':t, 'g': 0, 'b': 255},
			5: {'r':255, 'g': 0, 'b': 255 - t}
		}
		
		return color_vals[n]