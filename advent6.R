library(dplyr)

fish <- readLines("input6.txt") %>% 
  strsplit(",") %>% unlist %>% sapply(as.integer)

fish1 <- c("0" = 0, table(fish), "6" = 0, "7" = 0, "8" = 0)
for (i in 1:256){
  newfish <- fish1["0"]
  names(fish1) <- names(fish1)[c(9, 1:8)]
  fish1["6"] <- fish1["6"] + newfish
  fish1["8"] <- newfish
}

fish1 %>% sum %>% print(digits = 16)