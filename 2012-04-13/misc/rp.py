from rpy2.robjects import r
r('x <- rnorm(100)')  # generate x at R
r('y <- x + rnorm(100,sd=0.5)')  # generate y at R
r('plot(x,y)')  # have R plot them
r('lmout <- lm(y~x)')  # run the regression
r('print(lmout)')  # print from R
loclmout = r('lmout') # download lmout from R to Python
print loclmout  # print locally
