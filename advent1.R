library(tidyr)
library(dplyr)
library(zoo)

sub <- read.table("input.txt")

sub$V1 %>% diff %>% {. > 0} %>% sum()


sub$V1 %>% rollapply(3, sum) %>% diff %>% {. > 0} %>% sum

# 1538