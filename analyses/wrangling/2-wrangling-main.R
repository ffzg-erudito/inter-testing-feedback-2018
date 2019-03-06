library(tidyverse)
library(here)
library(conflicted)
library(magrittr)
conflict_prefer('filter', 'dplyr')

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

dat$activityFactor <- dat %>% pull(., condition) %>%
    str_replace(., regex('_(no)?Feedback', ignore_case = T), '')

# standardizing colnames to camelCase
dat %<>% rename_at(., vars(contains('_')), funs(gsub),
                  pattern = '_([[:alpha:]])',
                  replacement = '\\U\\1',
                  perl = T)

# clean times read variables of excess quotation marks
dat %<>% mutate_at(., vars(matches('kolikoProc')),
                  .funs = str_replace_all, pattern = '\\"',
                  replacement = '')

write_csv(dat, here('data', 'results.csv'))
