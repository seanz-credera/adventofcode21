library(dplyr)
{
paperCo <- read.table("input13.txt", sep = ",")
# Coordinates are indexed at 0
paper <- matrix(0, max(paperCo$V2) + 1, max(paperCo$V1) + 1)
# Adding coordinates
for (i in 1:nrow(paperCo)){
  # row, column means y, x
  paper[paperCo$V2[i] + 1, paperCo$V1[i] + 1] <- 1
}
}

foldThis <- function(thisPaper, thisDirection, thisVal){
  if (thisDirection == "x"){
    left <- thisPaper[, c(1:(thisVal))]
    right <- thisPaper[, c(ncol(thisPaper):(thisVal + 2))]
    if (ncol(right) > ncol(left)) {
      left <- cbind(
        matrix(0, nrow(left), ncol(right) - ncol(left)),
        left)
    } else {
      right <- cbind(
        matrix(0, nrow(right), ncol(left) - ncol(right)),
        right)
    }
    finalp <- left + right
    return(finalp)
  } else {
    top <- thisPaper[c(1:(thisVal)),]
    bot <- thisPaper[c(nrow(thisPaper):(thisVal + 2)),]
    if (nrow(top) > nrow(bot)) {
      bot <- rbind(
        matrix(0, nrow(top) - nrow(bot), ncol(bot)),
        bot)
    } else {
      top <- rbind(
        matrix(0, nrow(bot) - nrow(top), ncol(top)),
        top)
    }
    finalp <- top + bot
    return(finalp)
  }
}
# test <- foldThis(paper, "y", 7)

# fold along x=655
# fold along y=447
# fold along x=327
# fold along y=223
# fold along x=163
# fold along y=111
# fold along x=81
# fold along y=55
# fold along x=40
# fold along y=27
# fold along y=13
# fold along y=6

folded <- foldThis(paper, "x", 655) %>% 
  foldThis("y", 447) %>% 
  foldThis("x", 327) %>% 
  foldThis("y", 223) %>% 
  foldThis("x", 163) %>% 
  foldThis("y", 111) %>% 
  foldThis("x", 81) %>% 
  foldThis("y", 55) %>% 
  foldThis("x", 40) %>% 
  foldThis("y", 27) %>% 
  foldThis("y", 13) %>% 
  foldThis("y", 6) 

folded[folded > 0] <- 1
library(plot.matrix)
plot(folded, ylab = "", xlab = "", main = "")
