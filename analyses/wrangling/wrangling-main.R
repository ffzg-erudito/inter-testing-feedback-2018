library(tidyverse)
library(here)
library(conflicted)
library(magrittr)

dat <- read_csv(here('data', 'results.csv'))

# constructing intrusors DV as proportion of chosen intrusive distractors on
# incorrectly answered questions

getIntrusors <- function(x) {
    x %<>% bind_rows(.)
    propIntrusors <- x[which(x == 0)] %>% colnames(.) %>%
        str_subset(., 'content') %>% str_extract(., '\\d{1,2}$') %>%
        paste0('isIntrusor_3_', .) %>% {select(x, one_of(.))} %>%
        rowMeans(.)

    return(propIntrusors)
}

dat %>% select(., matches('content_3_|isIntrusor_3_')) %>%
  apply(., getIntrusors, MARGIN = 1) -> dat$propIntrusors

# dropping demographics and participant code
dat %<>% select(., -c(participant_code, spol, dob))
