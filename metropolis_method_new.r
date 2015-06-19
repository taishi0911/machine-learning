loglik <- function(q) {
  ans <- 0
  for (i in 1:length(data)) {
    ans <- ans + ( data[i] * log(q) + (8 - data[i]) * log(1-q) )
  }
  return(ans)
}

lik <- function(q) {
  return( exp(loglik(q)) )
}

#####ここまではオッケー

metropolis <- function(time_steps, default) {
  q <- default
  delta <- 0.01           # step size
  history <- c(default)   # history of q value

  for (i in 1:time_steps) {

    ###### condition at boundary value
    if(q == 0){
      q <- q + delta
      history <- c(history, q)

    }else if(q == 1){
      q <- q - delta
      history <- c(history, q)
    #####

    }else{
        if(runif(1) < 0.5){ #1/2の確率でqを大きくする
          if( lik(q) < lik(q + delta) ){ #尤度が大きくなる＝当てはまりが良くなる時
              q <- q + delta #qの値を新たにする
          history <- c(history, q)

          }else{ #尤度が小さくなる＝当てはまりが悪くなる時
          r <- lik(q + delta) / lik(q) # rに尤度比を代入して

          if(runif(1) < r){ #rの確率でqはq+deltaに移動する
            q <- q + delta
            history <- c(history, q)

          }else{
            history <- c(history, q)
          }
        }

      }else{　#1/2の確率でqを小さくする
        if( lik(q) < lik(q - delta) ){
          q <- q - delta
          history <- c(history, q)

        }else{
          r <- lik(q - delta) / lik(q)

          if(runif(1) < r){
            q <- q - delta
            history <- c(history, q)
          }else{
            history <- c(history, q)
          }
        }
      }

    }
  }

  return(history)
}