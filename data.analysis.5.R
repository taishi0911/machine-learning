d<-read.csv("/Users/okanotaishi/Downloads/data3a.csv")
fit2$deviance
d
d$y.rnd <- rpois(100, lambda = mean(d$y))
mean(d$y)
d$y.rnd

fit1 <- glm(y.rnd ~ 1, data = d, family = poisson)
fit2 <- glm(y.rnd ~ x, data = d, family = poisson)
fit1$deviance - fit2$deviance

get.dd<-function(d)
{
  n.sample<-nrow(d)
  y.mean<-mean(d$y)
  d$y.rnd<-rpois(n.sample, lambda=y.mean)
  fit1<-glm(y.rnd~1, data=d, family=poisson)
  fit2<-glm(y.rnd~x, data=d, family=poisson)
  fit1$deviance - fit2$deviance
}

pb <- function(d, n.bootstrap)
{
  replicate(n.bootstrap, get.dd(d))
}

dd12<- pb(d, n.bootstrap = 1000)
summary(dd12)
hist(dd12,100)
abline(v=4.5)
sum(dd12>=4.5)
quantile(dd12,0.95)


fit1<-glm(y~1, data=d, family=poisson)
fit2<-glm(y~x, data=d, family=poisson)
anova(fit1, fit2, test="Chisq")

