library(tidyr)
library(dplyr)
library(crayon)

mp <- read.table(text = gsub(",", "\t", 
                             readLines("input5.txt")))
# Part 1
mp1 <- mp %>% filter(V1 == V4 | V2 == V5)
lines <- as.matrix(mp1[, c(1,2,4,5)])
getCords <- function(x) {
  return(c(as.character(x[1]:x[3]) %+% "," %+%
             as.character(x[2]:x[4])))
}

coords <- apply(lines, 1, getCords)
coords %>% unlist %>% table %>% {.>=2} %>% sum

# Part 2
lines <- as.matrix(mp[, c(1,2,4,5)])
coords <- apply(lines, 1, getCords)
coords %>% unlist %>% table %>% {.>=2} %>% sum