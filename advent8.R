library(dplyr)

sd <- read.table("input8.txt")

# Part 1
sd %>% select(V12, V13, V14, V15) %>% as.matrix %>% 
  apply(c(1,2), nchar) %>% {. %in% c(2,3,4,7)} %>% sum

# Part 2
# 0(6), @1(2), 2(5), 3(5), @4(4), 
# 5(5), 6(6), @7(3), @8(7), 9(6)

# 6 - 0, 6, 9
# 5 - 2, 3, 5

# get 1, 4, 7, 8, 
# CHECK NCHAR
# 3 (shares 2 letters with 1)
# 9 (shares 5 letters with 3)

# 5 (shares 3 letters with 4)
# 6 (shares 3 letters with 4)
# last 5 letter is 2
# last 6 letter is 0

whatShares <- function(number, xlist, numlist){
  checkThis <- xlist[which(numlist == number)][1] %>% strsplit("") %>% {.[[1]]}
  sapply(xlist, 
                function(y) length(intersect(strsplit(y, "")[[1]], checkThis))) %>% 
    unname %>% return
}

# x <- sd[1, -11] %>% unname %>% unlist
getNum <- function(x){
  numList <- rep(NA, 14)
  numList[which(nchar(x) == 2)] <- 1
  numList[which(nchar(x) == 3)] <- 7
  numList[which(nchar(x) == 4)] <- 4
  numList[which(nchar(x) == 7)] <- 8
  
  numList[(nchar(x) == 5) & 
            (whatShares(1, x, numList) == 2) & 
            is.na(numList)] <- 3
  
  numList[(nchar(x) == 6) & 
            (whatShares(3, x, numList) == 5) & 
            is.na(numList)] <- 9
  
  numList[(nchar(x) == 5) & 
            (whatShares(4, x, numList) == 3) & 
            is.na(numList)] <- 5
  
  numList[(nchar(x) == 6) & 
            (whatShares(5, x, numList) == 5) & 
            is.na(numList)] <- 6

  numList[(nchar(x) == 5) & is.na(numList)] <- 2
  numList[(nchar(x) == 6) & is.na(numList)] <- 0
  return(numList)
}

sd[, -11] %>% apply(1, getNum) %>% {.[c(11:14), ]} %>% 
  apply(1, sum) %>% 
  {.[1] * 1000 + .[2] * 100 + .[3] * 10 + .[4]}

