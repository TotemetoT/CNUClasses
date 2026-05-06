*****
Copyright 2024 Christopher Newport University.

All rights reserved.

For the private use of CNU students currently enrolled in CPSC 250L.
Not for posting on any site other than internal student-gitlab.pcs server.

*****

# Lab11 - Cool Curves

For this lab, you will need to use `numpy` and `matplotlib` to plot some cool curves.

You need to write a class that defines some default parameters
 (e.g., `A`, `a`, and `b`) as attributes,
a `plot_curve` method that generates the curve given parameter values,
and a `set_parameters` method that allows you to update parameter values.

The `plot_curve` method should include some parameters to set line properties such as color.

Define a main method that creates an instance of your class, calls `set_parameters`,
defines a `matplotlib` figure, calls `plot_curve`, then saves figure and  `plt.show()`.

Generate plots for at least 3 different sets of parameters
that show variety of plots, and submit screenshots to Scholar.
Include proper labeling and title with your name.

Each figure should include a title and legend, where each curve
should be labeled with the parameter values in legend and title should have
curve name and your `(first.last.yy)`.

> Hint: Use f-strings to create the required string to use as labels and titles.
> e.g. `plt.plot(x, y, 'r', label=f'a={a_value:6.3f} b={b_value:3d}')`
> You must change formatting as appropriate.

Choose one of the following nine plots:

> Note: The equations are written in a basic text form, and are not executable Python.
> You make look them up online to see a prettier form of equation.

Some of these, the `x, y` values depend on a third variable like time `t` or angle `theta`,
and may require conversion from polar (radius and angle) to Cartesian (x, y) coordinates.

You will need to define the range of the dependent variable (e.g. `t` or `x` or `theta`)
and the spacing of points to give a pleasing curve.

Use `numpy` for all of these calculations.


### 1. **Lissajous Curves**

  https://mathworld.wolfram.com/LissajousCurve.html

   - Defined by the parametric equations:

     `x = A sin(a t + \delta)`

     `y = B sin(b t)`

   - Where `A`, `B`, `a`, and `b` control the amplitude and frequency, and `\delta` is the phase shift.
   - These curves produce intricate looping patterns depending on the frequency ratio `a/b`.

### 2. **Epicycloids and Hypocycloids**

  - Epicycloid:

  Created by tracing a point on the circumference of a circle rolling around the outside of another circle.

  https://mathworld.wolfram.com/Epicycloid.html

  ` x = (R + r) cos(t) - r cos((R + r)/r t)`

  ` y = (R + r) sin(t) - r sin((R + r)/r t)`

  - Hypocycloid:

  Similar to the epicycloid but with the circle rolling inside another circle.

  https://mathworld.wolfram.com/Hypocycloid.html

   - These can generate star-like or flower patterns depending on the ratio between `R` and `r`.

### 3. **Butterfly Curve**

  https://mathworld.wolfram.com/ButterflyCurve.html

  - A famous and aesthetically pleasing curve with the equation:

  ` x = sin(t) (e^{cos(t)} - 2 cos(4t) - sin^5((t)/12))`

  ` y = cos(t) (e^{cos(t)} - 2 cos(4t) - sin^5((t)/12))`

   - This curve resembles butterfly wings and is a beautiful example of a parametric plot.

### 4. **Fermat's Spiral**

  https://mathworld.wolfram.com/FermatsSpiral.html

  - A type of spiral with the polar equation:

  `r = \pm \sqrt{a theta}`

  - As `theta` increases, the curve spirals outwards.

  Changing `a` can modify the tightness of the spiral.

  > Note: This is in *polar* coordinates, so you need to change to *Cartesian* (x,y) to plot!

### 5. **Lemniscate of Bernoulli**

  https://mathworld.wolfram.com/Lemniscate.html

  - A figure-eight shaped curve with the polar equation:

  ` r^2 = a^2 cos(2 theta)`

  - This creates a smooth, symmetric, infinity-symbol shape.

  > Note: This is in *polar* coordinates, so you need to change to *Cartesian* (x,y) to plot!

### 6. **Logarithmic Spiral**

  https://mathworld.wolfram.com/LogarithmicSpiral.html

  - A self-similar spiral defined by:

  ` r = a e^{b theta}`

  - This spiral appears in nature (e.g., nautilus shells, galaxies) and expands with each turn, unlike Fermat's Spiral.

  > Note: This is in *polar* coordinates, so you need to change to *Cartesian* (x,y) to plot!

### 7. **Viviani’s Curve**

  This is a 3D curve, so it requires special set up for Matplotlib.
  
  As an example, consider another curve:

  https://matplotlib.org/stable/gallery/mplot3d/lines3d.html#sphx-glr-gallery-mplot3d-lines3d-py

  ```
  import matplotlib.pyplot as plt
  import numpy as np

  fig = plt.figure()
  ax = fig.add_subplot(projection='3d')

  ...

  ax.plot(x, y, z, label='parametric curve')
  ```

  - A 3D curve that is the intersection of a sphere and a cylinder.

  In parametric form:

  `x = a (1 + cos(t))`

  `y = a sin(t)`

  `z = 2a sin(t/2)`

  https://mathworld.wolfram.com/VivianisCurve.html

  - It creates a double-looped path that’s visually appealing in 3D.

### 8. **Cardioid and Limacon**

  https://mathworld.wolfram.com/Limacon.html

  - Limacon of Pascal has a general form:

  `r = a + b cos(theta)`

  - When `a = b`, it becomes a cardioid (heart-shaped curve).

  Varying `a` and `b` changes the shape, creating dimples, loops, or circles.

### 9. **Tschirnhausen Cubic**

  https://mathworld.wolfram.com/TschirnhausenCubic.html


  `r = a sec^3( 1/3 theta)`

  - This curve has a distinctive loop and can create interesting spiraling shapes.

  Numpy does not define an `np.sec` function, so you need to recall that `secant = 1/cosine`

  But you cannot have cosine = 0.0, so your theta domain will need to be adjusted accordingly to keep in bounds.

  Use a domain from negative to positive values.

----

For equations with `sin`, `cos` based on angle `theta` you will need to experiment
to define the proper range to get a closed curve.  It might be more or less than 2 pi.

Likewise some parameter values may give meaningless plots.

You *ARE* allowed to look up references online if you have difficulty finding reasonable parameter values.

Experimenting with these formulas by varying their parameters can lead
to a wide range of visually compelling shapes.

Your domains should give range values that are real, so no divide by zero `1/0` or imaginary `sqrt(-1)` values.

You should generate a plot with at least three distinct plots representing different
parameter values.

* Zybooks
* https://student-gitlab.pcs.cnu.edu   - your personal CS250 repo's only
* You *are* allowed to reference your prior projects
* https://web-cat.cs.vt.edu    - your webcat submissions
* https://docs.python.org/3/

> You are expected to show incremental progress throughout the lab.
> Accessing prior semester solutions of your own or anyone else's, including online tutoring sites such as
> (but not limited to) Chegg, Docsity, StackOverflow or other is strictly forbidden and warrants a CHECS referral.

> Reference to StackOverflow for general questions (e.g. how to format a string) is allowed.

> You are only allowed to have general discussions (e.g. how to format a string) under empty hands rules.
> The design and implementation should be your own work.

> You *MAY* refer to ChatGPT for specific questions (e.g. how to plot on map), but not for the overall design.

> You *MAY* refer to online sources for information about the curves, e.g. https://mathworld.wolfram.com/TschirnhausenCubic.html


Before you can leave early, you need to implement at least two different curves with multiple parameter values.
Otherwise, you forfeit the "significant progress" points.

You must implement two different curves for full credit.

You must finish this lab before the start of class next week as we will build on this lab.

## Grading

  * Final Grading (100 points)
    * 20 points: Significant progress during the lab
    * 20 points: Class defined with require attributes and methods
    * 20 points: At least one plot generated for curve
    * 20 points: Correct plot generated for variety of parameter values
    * 10 points: Implementing two or more different curves
    * 10 points: Style and efficiency points defined by instructor

Implementing one curve successfully gives you a max of 90 points.

Implement two or more different curves for full credit.

Follow your instructor's directions for submitting the generated plot figures.
