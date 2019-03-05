library(tidyverse)
library(here)
library(conflicted)
library(magrittr)

# created by data-pooling.R
dat <- read_csv(here('data', 'results.csv'))

# create total test score, i.e. DV1
dat$totalCorrect <- dat %>% select(., matches('content_3_')) %>%
    rowSums(.)

# create DV2 - total number of intrusors chosen
dat$totalIntrusors <- dat %>% select(., matches('isIntrusor_3_')) %>%
    rowSums(.)

# dropping demographics and participant code
dat %<>% select(., -c(participant_code, spol, dob))

write_csv(dat, here('data', 'results.csv'))
