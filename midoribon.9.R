update.packages()
install.packages("rjags", dep = TRUE)
library(rjags)
load("?/desktop/programing/midoribon/kubobook2012/chapter09/d.RData")

data_list<-list(N=nrow(d),Y=d$y,X=d$x,Mean.X=mean(d$x))
inits<-list(beta1=0,beta2=0)

m<-jags.model(file="?/Desktop/programing/midoribon/jags.bugs.txt",
              data=data_list,
              inits=list(inits,inits,inits),
              n.chain=3
              )
update(m,1000) #beta‚ª‚¨
result<-coda.samples(m,c("beta1",beta2),thin=3,n.iter=3000)
