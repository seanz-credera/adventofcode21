library(dplyr)

sm <- read.csv("input9.txt", colClasses = c("character"),
               header = F)

smat <- sm$V1 %>% strsplit("") %>% 
  unlist %>% matrix(ncol = 100, byrow = TRUE) %>% 
  apply(c(1,2), as.integer)

# Part 1
lowpt <- c()
for (i in 1:100){
  for (j in 1:100){
    lookx <- c(i-1, i+1)
    lookx <- lookx[lookx <= 100 & lookx > 0]
    looky <- c(j-1, j+1)
    looky <- looky[looky <= 100 & looky > 0 ]
    
    if (smat[i,j] < 
        min(min(smat[lookx, j]), min(smat[i, looky]))){
      print(c(i,j))
      lowpt <- c(lowpt, smat[i,j])
    }
  }
}

(lowpt + 1)%>% sum

# Part 2  
seenList <- c()

getSize <- function(i, j){
  #print(c(i,j))
  seenList <<- c(seenList, toString(c(i,j)))
  if (smat[i,j] == 9) return(0)
  lookx <- c(i-1, i+1)
  lookx <- lookx[lookx <= 100 & lookx > 0]
  looky <- c(j-1, j+1)
  looky <- looky[looky <= 100 & looky > 0 ]

  neighborsize <- 0
  for (x in lookx){
    if (!(toString(c(x,j)) %in% seenList)){
      neighborsize <- neighborsize + getSize(x, j)
    }
  }
  
  for (y in looky) {
    if (!(toString(c(i,y)) %in% seenList)){
      neighborsize <- neighborsize + getSize(i, y)
    }
  }
  
  return(1 + neighborsize)
}

getSize(1,1)
seenList <- c()
sizes <- c()
for (i in 1:100){
  for (j in 1:100){
    if (smat[i,j] == 9) next
    if (toString(c(i,j)) %in% seenList) next
    sizes <- c(sizes, getSize(i,j))
    
  }
}

sizes %>% sort(decreasing = TRUE) %>% {.[1:3]} %>% prod
