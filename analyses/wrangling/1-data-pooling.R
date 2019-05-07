library(tidyverse)
library(here)

fileList <- list.files(here('data'), pattern="*.csv", full.names = T)

datfr <- map_dfr(fileList, read_csv)

write_csv(datfr, here('data', 'results.csv'))
