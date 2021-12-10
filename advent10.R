library(dplyr)

nav <- read.table("input10.txt")
points <- c(3, 57, 1197, 25137)
names(points) <- c(")", "]", "}", ">")
reverse <- c(")", "]", "}", ">")
names(reverse) <- c("(", "[", "{", "<")

getPoints <- function(x){
  xlist <- x %>% strsplit("") %>% {.[[1]]}
  closingList <- c()
  for (i in xlist){
    # print(i)
    if (i %in% c("(", "[", "{", "<")){
      closingList <- c(closingList, reverse[i])
      
    } else {
      if (i != closingList[length(closingList)]) {
        return(unname(points[i]))
      } else {
        closingList <- closingList[1: (length(closingList) - 1)]
      }
    }
  }
  return(0)
}

sapply(nav$V1, getPoints) %>% unname %>% sum

# Part 2  
incomplete <- nav$V1[which(sapply(nav$V1, getPoints) == 0)]

points <- c(1:4)
names(points) <- c(")", "]", "}", ">")
reverse <- c(")", "]", "}", ">")
names(reverse) <- c("(", "[", "{", "<")

getPoints <- function(x){
  xlist <- x %>% strsplit("") %>% {.[[1]]}
  closingList <- c()
  for (i in xlist){s
    if (i %in% c("(", "[", "{", "<")){
      closingList <- c(closingList, unname(reverse[i]))
    } else {
      closingList <- closingList[1: (length(closingList) - 1)]
    }
  }
  clr <- rev(closingList)
  totalScore <- 0
  for (i in clr){
    totalScore <- (totalScore * 5) + points[i]
  }
  return(totalScore)
}

sapply(incomplete, getPoints) %>% unname %>% median
# 2802519786
