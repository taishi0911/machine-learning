load("/Users/okanotaishi/Downloads/data (2).RData")
load("/Users/okanotaishi/Downloads/")
logLik(fit)
fit.null<-glm(formula=y~1,family=poisson,data=d)
logLik(fit.null)
fit.null
fit.f<-glm(formula=y~x,family=poisson,data=d)
logLik(fit.f)
fit.f
fit.xf<-glm(formula=y~x+f,family=poisson,data=d)
fit.xf
fit.xf<-glm(formula=y~x+f,family=poisson,data=d)
