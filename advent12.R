library(dplyr)
{
cave <- read.table(text = gsub("-", "\t", 
                             readLines("input12.txt")))
colnames(cave) <- c("from", "to")
cave <- cave %>% 
  {rbind(cave, data.frame("from" = .$to, "to" = .$from))} %>% 
  filter(!(from %in% c("end")), !(to %in% c("start")))
}

# Part 1
pathsFrom <- function(startNode, visited){
  if(startNode == "end") return(1)
  visited <- c(visited, startNode)
  toLook <- cave[which(cave$from == startNode), "to"]
  toLook <- toLook[!(substr(toLook,1,1) %in% letters & 
                       toLook %in% visited)]
  sapply(toLook, pathsFrom, visited) %>% unlist %>% sum %>% return
  
}

visited <- c()
pathsFrom("start", visited)

# Part 2
pathsFrom2 <- function(startNode, visited){
  if(startNode == "end") return(1)
  visited <- c(visited, startNode)
  visitedtwice <- table(visited)[which(table(visited) > 1)] %>% 
    names %>% {.[substr(., 1, 1) %in% letters]}
  if (length(visitedtwice) < 1) {
    # if haven't visited anything twice, allow all tolooks
    listCheck <- FALSE
  } else {
    listCheck <- visited
  }
  toLook <- cave[which(cave$from == startNode), "to"]
  toLook <- toLook[!(substr(toLook,1,1) %in% letters & 
                       toLook %in% listCheck)]
  sapply(toLook, pathsFrom2, visited) %>% unlist %>% sum %>% return
}

visited <- c()
# slightly larger - 103
pathsFrom2("start", visited) 
