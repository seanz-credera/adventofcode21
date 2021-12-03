library(tidyr)
library(dplyr)

sb <- read.table("input2.txt")
# Horiz
a <- sb %>% filter(V1 == "forward") %>% select(V2) %>% sum
# Depth
b <- sb %>% filter(V1 == "down") %>% select(V2) %>% sum - 
  sb %>% filter(V1 == "up") %>% select(V2) %>% sum
a*b

horiz <- 0
depth <- 0
aim <- 0

for (i in 1:nrow(sb)){
  direct <- sb$V1[i]
  mag <- sb$V2[i]
  if (direct == "forward"){
    horiz <- horiz + mag
    depth <- depth + (mag * aim)
  }
  if (direct == "down"){
    #depth <- depth + mag
    aim <- aim + mag
  } 
  if (direct == "up")
  {
    #depth <- depth - mag
    aim <- aim - mag
  }
}
horiz * depth
