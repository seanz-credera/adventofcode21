library(tidyr)
library(dplyr)

sb <- read.table("input3.txt", 
                 colClasses = c("character"))
sbm <- sb$V1 %>% strsplit(.,"") %>% unlist %>% 
  sapply(as.integer) %>% 
  matrix(ncol = 12, byrow = TRUE)

apply(sbm, 2, median)

# 010111100100 - 1508, 2587
# 101000011011

sbdf <-  data.frame(sbm)

#oxygen
consider <- sbdf
for (i in 1:12){
  consider <- consider %>% 
    filter(consider[, i] == 
             ifelse(mean(consider[,i]) >= 0.5, 1, 0))
}
consider
# 011001100111 - 1639

#c02
consider <- sbdf
for (i in 1:12){
  consider <- consider %>% 
    filter(consider[, i] == 
             ifelse(mean(consider[,i]) >= 0.5, 0, 1))
  if (nrow(consider) == 1) break
}
consider
# 101010000100 - 2692