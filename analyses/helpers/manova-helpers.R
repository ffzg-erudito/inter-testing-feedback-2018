covMatrixRatio <- function(rowi, coli, matrixList) {
  # extract variance/covariance at specified indices
  variances <- map_dbl(matrixList, function(x) {x[rowi, coli]})
  ratio <- max(variances) / min(variances)
  return(ratio)
}

omegaSquared <- function(n, lambda, dfh) {
  omSq <- 1 - ((n * lambda) / (n - dfh - 1 + lambda))
  return(omSq)
}

manovaStats <- function(manovaModel, statistic = 'test', effect,
                        type = '3', test = 'Pillai') {
  # specify effect as regex targeting the name of the effect in the `Anova`
  # output table
  Anova(manovaModel, type = type, test = test) %>% capture.output(.) %>%
    str_subset(., effect) %>% str_extract_all(., '\\d+\\.?\\d*') %>%
    pluck(1) -> results
  
  if (statistic == 'test') return(results[2] %>% as.numeric(.))
  else if (statistic == 'df') return(results[1] %>% as.numeric(.))
  else if (statistic == 'p') return(results[6] %>% as.numeric(.))
  else print('unrecognized statistic requested. try "p", "df" or "test".')
  }