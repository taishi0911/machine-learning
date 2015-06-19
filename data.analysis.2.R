par(mfrow=c(2,2))

d<-read.csv("/Users/okanotaishi/Downloads/data3a.csv")
d<-read.csv(file.choose())

d
d$x
d$y
d$f

# What class the data object belong to (data.frame, numetric, integer, factor ... )
class(d)
class(d$x)
class(d$y)
class(d$f)

summary(d)

plot(d$x, d$y, pch=c(4,19)[d$f])
# plot(d$x, d$y, pch=c(21,19)[d$f])
legend("topleft", legend = c("C","T"), pch = c(4,19))

# below is making box-whisker plot
plot(d$f,d$y)

dfit<-glm(y~x, data=d, family=poisson)
fit
logLik(fit)
(7508+19590)+26424
161424+(350806-53522)
