# FractalJS

A JavaScript HTML5 canvas-based fractal-drawing app that lets you zoom up to any level of precision (or at least as far as JavaScript's floating point precision goes :-). It uses a complex number class to calculate the Mandelbrot set for each pixel in the canvas and colors the points outside the set using a color-smoothing algorithm. 

<hr />

## example

Starting with a simple canvas that has a width and height declared:

<pre>
&lt;canvas id="mycanvas" width="300" height="300"&gt;&lt;/canvas&gt;
</pre>

To initialize the plugin, you run this code:

<pre>
$('#mycanvas').fractaljs();
</pre>

<em>For a full list of options and callback methods, see below</em>.

This simple code will create a rendering of the Mandelbrot set and add "zoom in" and "zoom out" buttons. If you supply width and height values into the options, the canvas's width and height will be overridden by them. The rendered canvas will look something like this:

<img src="https://github.com/janhartigan/FractalJS/raw/master/example/mandelbrot300x300_50maxit_minzoom.png" />

If you want to do something after the fractal is rendered, you have access to an afterDraw() method that is fired on completion of the drawing. The zoom object (which contains width, height, x, and y information for the rendered set) is passed as a parameter to this function.

It's also important to keep in mind that FractalJS doesn't have the capacity for infinite zoom. This is because of the limits of floating point precision in JavaScript. As floating point numbers (e.g. 0.0000005 or 1.4242455353294) get more precise, they approach the bit limits. This means that beyond a certain limit, floating point numbers will usually round to some less precise number. Watch what happens as we zoom into some deep level of a 148x148 Mandelbrot set:

<img src="https://github.com/janhartigan/FractalJS/raw/master/example/pixelation.png" />

## options

These are the settings and callback functions available for the plugin:

<pre>
{	
	/* Determines whether or not to draw the control bar below the fractal's canvas.
	 * If you choose not to use this, you could use the afterDraw callback to display 
	 * the fractal data to your users, and you should also make use of the zoomButton 
	 * options to let your users perform actions on the fractal.
	 * 
	 * @type Bool
	 */
	useControlBar: true,
	
	/* The maximum number of iterations to perform the operation before assuming a point to be in the set
	 * In an ideal world, we'd set this as high as possible, but since we have limited resources, we have to choose some limit
	 * 
	 * @type Int
	 */
	maxIterations: 300,
	
	/* The color range multiplier. This number represents the number of times the color spectrum repeats itself.
	 * 
	 * @type Int
	 */
	colorRangeRepeats: 7,
	
	/* If this is not 0 (i.e. if it has been set as an option), it will be the new width of the canvas
	 * 
	 * @type Int
	 */
	width: 0,
	
	/* If this is not 0 (i.e. if it has been set as an option), it will be the new height of the canvas
	 * 
	 * @type Int
	 */
	height: 0,
	
	/**
	 * This callback fires after the fractal has been drawn
	 * 
	 * @param Object	zoom ==> {x, y, width, height}
	 */
	afterDraw: function(zoom) {}
}
</pre>

## exposed methods

FractalJS exposes a few methods on the jQuery object. For now, these just allow you to create, destroy, and get access to the fractal object being used for the supplied canvas element.

### fractaljs()

This method is the one into which you pass the options object. You can use this to create a new fractal or re-render a canvas that has already been initialized with FractalJS. It is used like this:

<pre>
$('#mycanvas').fractaljs();
</pre>

After you have initialized the fractal, you can reset certain options by resupplying a new options object. Note that FractalJS automatically figures out the size of your canvas before each drawing, so you can tinker with this outside of FractalJS and everything should work well.

### fractaljsDestroy()

This method will destroy the fractal object associated with the canvas and clear the canvas. It is used like this:

<pre>
$('#mycanvas').fractaljsDestroy();
</pre>

### fractaljsObject()

This method will return the the fractal object associated with the supplied canvas or false if none are found. This will give you access to the methods and properties for that particular fractal object. It is used like this:

<pre>
$('#mycanvas').fractaljsObject();
</pre>