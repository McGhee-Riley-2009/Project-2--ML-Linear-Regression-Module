# Project-2--ML-Linear-Regression-Module
This program is my second project for data science progression. I applied a basic linear regression model that finds a more exact line than the equation we typically use. (y=Ax+B is an approximation). This model produces exact results and graphs them in red. Our approximation is graphed in green, and data points are blue.
I know that this model was technically a non-iterable algorithm, but I transformed it into a _somewhat_ iterable system that shows more exact lines when more data points are provided. I thought that this was really interesting to make and it taught me that tools are only as good as what _you_ use them for.

What Was New/What I Learned:
 - 
  - I used sklearn for the first time (specifically thier linear regression model)

  - I also learned that you can label the lines and data points and create a legend. Small, but useful.

  - I found the creation of the random data very difficult, because I could not fathom a way to make anything but completely scattered data. I learned y=mx+b early on in school, so that was a little obvious but with my random number generator it would spit out a line that just had spaces. Then I thought of "noise". I made a much smaller variable that multiplies the y values, making them negative or positive, while also making sure they were almost **never** the exact value
