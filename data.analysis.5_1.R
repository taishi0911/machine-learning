d<-read.csv("~/downloads/data3a.csv")
fit1<-glm(y~1, data=d, family=poisson)
fit2<-glm(y~x, data=d, family=poisson)
D12=fit1$deviance-fit2$deviance
D12

fit1
  # coef = cor(fit1$y, fit1$1)
  # d$rnd<-rpois(100, lambda=(coef))
d$rnd<-rpois(100, lambda=(2.058))
fit3<-glm(rnd~1, data=d, family=poisson)
fit4<-glm(rnd~x, data=d, family=poisson)
D34=fit3$deviance-fit4$deviance
D34

source("~/Desktop/programing/midoribon/chapter05/pb.R")
dd12<-pb(d, n.bootstrap=100)
hist(dd12,100)
abline(v=D12)
sum(dd12>=D12)

fit5<-glm(y~x, data=d, family=poisson)
fit6<-glm(y~f+x, data=d, family=poisson)
D56=fit5$deviance-fit6$deviance
D56
fit6

source("~/Desktop/programing/midoribon/chapter05/pb2.R")
dd56<-pb2(d, n.bootstrap=1000)
hist(dd56,100)
abline(v=D56)
sum(dd56>=D56)
quantile(dd56, 0.95)

anova(fit5, fit6, test="Chisq")
