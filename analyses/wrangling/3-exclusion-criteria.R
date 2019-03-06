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
dat %>% filter(., readingTime > 90) %>%
    filter(., totalCorrect > 0) %>% nrow(.)
# [1] 206

dat %>% filter(., readingDeficits == 'DA') %>% nrow(.)
# [1] 3

dat %>% filter(., readingDeficits == 'DA') %>% select(., which)
# # A tibble: 3 x 1
#   which             
#   <chr>             
# 1 slabovidnost      
# 2 brzopletost       
# 3 OKP (ako se broji)

# apply hard criteria to data
datHard <- dat %>% filter(., readingTime > 90 & totalCorrect > 0 &
                          !which %in% c('slabovidnost', 'brzopletost'))

# soft exclusion criteria
datHard %>% filter(., readingDifficultiesThisExp == 'NE') %>% nrow
# [1] 196

readFilter <- function(condition, timesRead) {
    readGenCont <- c('jednom cijeli tekst',
                     'jednom cijeli tekst i preletjeti "ključne" dijelove',
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

dat %>% select(., activityFactor, kolikoProcitaoText1) %>%
    map2(.)

map2_lgl(dat$activityFactor, dat$kolikoProcitaoText1, .f = readFilter)

datHard %>% filter(., (kolikoProcitaoText1 %in% readGenCont &
                       activityFactor %in% c('general', 'content')) |
                   ())
