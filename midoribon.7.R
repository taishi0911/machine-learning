library("glmmML")
d <- read.csv("~/Desktop/programing/midoribon/kubobook2012/chapter07/data.csv")
summary(d)
hist(d$y)
hist(d$x)
glmmML(cbind(y, N-y)~x, data = d, family = binomial, cluster = id, method= "ghq")

d1 <- read.csv("~/Desktop/programing/midoribon/kubobook2012/chapter07/birth.csv")
summary(d1)
tgt = d1[d1$age==23,]
#http://cse.naro.affrc.go.jp/takezawa/r-tips/r/13.html
tgt
summary(tgt)
glm(bwt~age,data=d1,family=poisson)
glmmML(bwt~age, data = d1, family = poisson, cluster = id, method= "ghq")
plot(d1)
plot(d1$bwt,d1$age)
#http://cse.naro.affrc.go.jp/takezawa/r-tips/r/70.html