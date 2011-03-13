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
		z0 = complex()
		z = z0
		c = null
		i = null
		pixel = 0
	
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
		@param float		position ==> 
		
		@return dict {r, g, b}
		'''