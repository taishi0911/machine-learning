x<-0
for(i in 1:5){
  x=x+1}
x

x<-1:5
for(i in x){
  x<-append(x,i)
}
x

x<-0
while(x<=5){
  x<-x+1
}
x

x<-0
for(i in 1:5){
  x<-x+1
  if(x==3)break
}
x

x<-0
repeat{
  if(x<=5)x<-x+1
  else break
}
x

y<-0
for(i in 1:100){
  x <- mean(rpois(50,3.5))
  y <- y + x
}
lambda.hut = y/100
lambda.hut

x<-mean(rpois(50,3.5))
x
