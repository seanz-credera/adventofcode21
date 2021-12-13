library(dplyr)

sm <- read.csv("input11test.txt", colClasses = c("character"),
               header = F)

oct <- sm$V1 %>% strsplit("") %>% 
  unlist %>% matrix(ncol = 10, byrow = TRUE) %>% 
  apply(c(1,2), as.integer)

flashThis <- function(thisMat){
  # only on first
  if (sum(thisMat == 9) == 0) return(thisMat)
  
  addThis <- matrix(0, 10, 10)
  addThis[thisMat == 9] <- 1
  flashed <- thisMat + 
    cbind(addThis[, c(2:10)], rep(0, 10)) + 
    cbind(rep(0, 10), addThis[, c(1:9)]) +
    rbind(addThis[c(1:9), ], rep(0, 10)) +
    rbind(rep(0, 10), addThis[c(2:10), ])
  if (sum(flashed == 9) > 0){
    return(flashThis(flashed))
  } else {
    return(flashed)
  }
}

flashThis(oct+1)

stepThis <- oct
flashes <- 0
for (steps in 1:1) {
  oct <- oct + 1
  stepThis <<- flashThis(oct)
  flashes <<- flashes + sum(stepThis > 9)
  stepThis[stepThis > 9] <- 0
}
