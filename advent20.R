library(dplyr)
filename <- "input20.txt"
matsize <- 100

ikey <- readLines(filename, n = 1) %>% strsplit("") %>% unlist

img <- read.csv(filename, colClasses = c("character"),
               header = F, skip = 1)

imat <- img$V1 %>% strsplit("") %>% 
  unlist %>% matrix(ncol = matsize, byrow = TRUE)

padThis <- function(inputMat, thisChar){
  cbind(rep(thisChar, nrow(inputMat)), 
        inputMat, 
        rep(thisChar, nrow(inputMat))) %>% {
          rbind(rep(thisChar, ncol(.)), 
                .,
                rep(thisChar, ncol(.)))
        } %>% return
}
# strtoi("00000001001100110000010110110111", base = 2)

padMany <- function(inputMat, thisChar){
  return(inputMat %>% padThis(thisChar) %>% 
           padThis(thisChar) %>% padThis(thisChar) %>% 
           padThis(thisChar) %>% padThis(thisChar) %>% 
           padThis(thisChar))
}

# Part 1
pimat <- imat %>% padMany(".")
omat <- matrix(NA, nrow(pimat), ncol(pimat))
for (i in 2:(nrow(pimat) - 1)){
  for (j in 2:(ncol(pimat) - 1)){
    # print(c(i,j))
    tobin <- c(pimat[i - 1, c((j-1):(j + 1))],
               pimat[i, c((j-1):(j + 1))],
               pimat[i + 1, c((j-1):(j + 1))])
    omat[i,j] <- ifelse(tobin == ".", 0, 1) %>% 
      paste0(collapse = "") %>% 
      strtoi(base = 2) %>% 
      {ikey[(. + 1)]}
  }
}
fmat <- omat[c(5:(nrow(omat) - 4)), c(5:(ncol(omat) - 4))]
sum(fmat == "#")
# 5570 is too hight
pimat <- fmat %>% padMany(fmat[1,1])


# Part 2
pimat <- imat %>% padMany(".")
for (i in 1:50){
  print(i)
  omat <- matrix(NA, nrow(pimat), ncol(pimat))
  for (i in 2:(nrow(pimat) - 1)){
    for (j in 2:(ncol(pimat) - 1)){
      # print(c(i,j))
      tobin <- c(pimat[i - 1, c((j-1):(j + 1))],
                 pimat[i, c((j-1):(j + 1))],
                 pimat[i + 1, c((j-1):(j + 1))])
      omat[i,j] <- ifelse(tobin == ".", 0, 1) %>% 
        paste0(collapse = "") %>% 
        strtoi(base = 2) %>% 
        {ikey[(. + 1)]}
    }
  }
  fmat <- omat[c(5:(nrow(omat) - 4)), c(5:(ncol(omat) - 4))]
  pimat <- fmat %>% padMany(fmat[1,1])
}
sum(fmat == "#")


