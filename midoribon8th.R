data <- c(4,3,4,5,5,2,3,1,4,0,1,5,5,6,5,4,4,5,3,4)

logL<-0
L <- function(q){
  for (i in 1:length(data))
  logL <- logL + (data[i]*log(q)+(8-data[i])*log(1-q))
  L <- exp(logL)
  return(L)
}

q <- 0.1
L(q)
