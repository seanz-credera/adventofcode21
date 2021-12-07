library(dplyr)

crab <- readLines("input7.txt") %>% 
  strsplit(",") %>% unlist %>% sapply(as.integer) %>% unname

# Part 1
(crab - median(crab)) %>% abs %>% sum

# Part 2
(crab - floor(mean(crab))) %>%
  abs %>% sapply(bigsum) %>% sum