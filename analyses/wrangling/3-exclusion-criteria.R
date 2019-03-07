# this file contains the code used to apply the "hard" and "soft" exclusion
# criteria described in `analysis-plan.md`
library(tidyverse)
library(here)
library(conflicted)
library(magrittr)
conflict_prefer('filter', 'dplyr')

# created by data-pooling.R
dat <- read_csv(here('data', 'results.csv'))

# hard exclusion criteria
# dat %>% filter(., readingTime > 90) %>%
#     filter(., totalCorrect > 0) %>% nrow(.)
# [1] 206

# dat %>% filter(., readingDeficits == 'DA') %>% nrow(.)
# [1] 3

# dat %>% filter(., readingDeficits == 'DA') %>% select(., which)
# # A tibble: 3 x 1
#   which             
#   <chr>             
# 1 slabovidnost      
# 2 brzopletost       
# 3 OKP (ako se broji)
# there are only 3 participants who've answerd YES to the reading difficulties
# question. their free-text answers are "weak vision", "OCD" and appx.
# "proneness to errors due to lack of vigilance". since each of these COULD
# impact the participant's performance, and since there's only three of them,
# we've decided to exclude them all, to be on the safe side

# apply hard criteria to data
datHard <- dat %>% filter(., readingTime > 90 & totalCorrect > 0 &
                          readingDeficits == 'NE')

# soft exclusion criteria
# datHard %>% filter(., readingDifficultiesThisExp == 'NE') %>% nrow
# [1] 196

# function to filter those who've read the text once, one and a half times or
# once + key points (if in the general or content condition) | those who've read
# the text twice or two and a half times (if in the rereading condition)
readFilter <- function(condition, timesRead) {
    readGenCont <- c('jednom cijeli tekst',
                     'jednom cijeli tekst i preletjeti ključne dijelove',
                     'oko jedan i pola puta')

    rereadCont <- c('oko dva i pola puta', 'oko dva puta')

    if (condition %in% c('general', 'content')) {
        if (timesRead %in% readGenCont) return(T)
        else return(F)
    } else {
        if (timesRead %in% rereadCont) return(T)
        else return(F)
    }
}

# applying filter to data, storing as variable
datHard$timesReadFilter1 <- map2_lgl(datHard$activityFactor,
                                     datHard$kolikoProcitaoText1,
                                     readFilter)
datHard$timesReadFilter2 <- map2_lgl(datHard$activityFactor,
                                     datHard$kolikoProcitaoText2,
                                     readFilter)
datHard$timesReadFilter3 <- map2_lgl(datHard$activityFactor,
                                     datHard$kolikoProcitaoText3,
                                     readFilter)

datSoft <- datHard %>% select(., matches('Filter')) %>% rowSums(.) %>%
    {which(. >= 2)} %>% {datHard[., ]} %>%
    filter(., readingDifficultiesThisExp == 'NE')
