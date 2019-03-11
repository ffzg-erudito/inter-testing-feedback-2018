covMatrixRatio <- function(rowi, coli, matrixList) {
  # extract variance/covariance at specified indices
  variances <- map_dbl(matrixList, function(x) {x[rowi, coli]})
  ratio <- max(variances) / min(variances)
  return(ratio)
  }