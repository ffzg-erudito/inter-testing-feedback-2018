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