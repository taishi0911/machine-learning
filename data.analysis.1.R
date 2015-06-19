load("/Users/okanotaishi/Downloads/data.RData")
plant.seed<-data
length(plant.seed)
sd(plant.seed)
# sd = standard deviation
sqrt(var(plant.seed))
table(plant.seed)
par(mfrow=c(2,2)) # separating right below window
hist(plant.seed, breaks = seq(-0.5, 9.5, 1.0))
hist(plant.seed)
# -0.5-0.5, 0.5-1.5, ...following ; progression ; making histgram
# rough figure ; functions are length(),sd(),summary()...

# below; poisson distibution
y <- 0:9
prob1 <- dpois(y, lambda=3.56)
# hist(prob, breaks = seq(-0.5,10.5,1.0))
plot(y, prob1, type="b", lty=2)
prob2 <- ppois(y, lambda=3.56)
plot(y, prob2, type="b", lty=2)
# prob3 <- qpois(y, lambda=3.56)
# make histgram and prob in one figure
# first, make histgram. second, drow line of prob.
hist(plant.seed)
lines(y, 50*prob, type="b", lty=2)

prob<-dpois(y, lambda=3.56)
lambda<-seq(2.0,5.0,0.1)
logL<-function(m)sum(dpois(data,m,log=TRUE))

plot(lambda, sapply(lambda,logL), type="l")
prob4 <- rpois(50,3.5)
# plot(prob4)
prob4
hist(prob4)
mean(prob4)

# the mean of lambda
y<-0
n=1000
for(i in 1:n){
  x <- mean(rpois(50,3.56))
  y <- y + x
}
lambda.hut = y/n
lambda.hut

y1 <- NULL
n=1000
for(i in 1:n){
  x <- mean(rpois(50,3.56))
  y1 <- append(y1,x)
}
hist(y1)

load("/Users/okanotaishi/Downloads/data.RData")
data
summary(data)
table(data)
hist(data)
hist(data, breaks=seq(-0.5,9.5,1))
var(data)
seq(1,9,1)
hist(data, breaks={0,1,2,3,4,5,6,7,8,9})
y<-0:9
prob<-dpois(y,lambda=3.56)
plot(y,prob,type="b",lty=2)
cbind(y,prob)
hist(data)
hist(data, breaks=seq(-0.5,9.5,1))
lines(y, 50*prob)
logL<-function(m)sum(dpois(data,m,log=TRUE))
lambda<-seq(2,5,0.1)
plot(lambda,sapply(lambda,logL))
random<-rpois(50,3.5)

