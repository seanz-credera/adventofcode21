#target area: x=201..230, y=-99..-65

# PART 1
# max y is 98, reaches -99
# choose(98 + 1, 2) for max height


# PART 2
# for some y, x has y*2 + 2 steps
# x has to be 20, it will be at 210 (choose 20 + 1, 2) in 21 steps
# x can be from 19 to 230
# y can be from 98 to -99


totalSum <- 0
pos <- c(0,0)
vel <- c(NA, NA)
rm(i, j)
for (i in 19:230){
  for (j in 98:-99){
    # print(c(i,j))
    pos <<- c(0,0)
    vel <<- c(i, j)
    repeat{
      pos <<- pos + vel
      vel <<- c(ifelse((vel[1] - 1 ) < 0, 0, vel[1] - 1), 
                vel[2] - 1)
      if (pos[1] >= 201 & pos[1] <=230 & 
          pos[2] >= -99 & pos[2] <= -65) {
        totalSum <<- totalSum + 1
        break
      }
      if (pos[1] > 230 | pos[2] < -99){
        break
      }
    }
  }
}