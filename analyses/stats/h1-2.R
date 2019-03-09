library(here)
# NOTE: this will load {magrittr}, {here}, {conflicted} and {tidyverse}. also,
# `conflict_prefer`s filter from {dplyr}
# furthermore, it loads 3 data.frames: (1) `dat` which contains the pooled data run
# through `2-wrangling-main.R`, (2) `datHard` which is `dat` with all the hard
# exclusion criteria applied (as described in `analysis-plan.md`), and (3)
# `datSoft` which is `datHard` with the soft exclusion criteria applied (as
# described in `analysis-plan.md`)
source(here('wrangling', '3-exclusion-criteria.R'))

# import MVN library for outlier detection and testing normality assumptions, and other libs
library(MVN)
library(haven)
library(psych)


# ANALYSIS on sample with hard exclusion criteria

# recode condition into new variable, and subset data
datHard$ConditionRecoded <- datHard$condition
datHard$ConditionRecoded[datHard$condition == 'rereading'] <- 1
datHard$ConditionRecoded[datHard$condition == 'general_noFeedback'] <- 2
datHard$ConditionRecoded[datHard$condition == 'content_noFeedback'] <- 3
datHard$ConditionRecoded[datHard$condition == 'general_feedback'] <- 4
datHard$ConditionRecoded[datHard$condition == 'content_feedback'] <- 5

data <- subset(datHard, ConditionRecoded == 2 | ConditionRecoded == 3 | ConditionRecoded == 4 | ConditionRecoded == 5)


# select dependent variables
DVs <- select(datHard, totalCorrect, totalIntrusors)
groups_DVs <- select(datHard, ConditionRecoded, totalCorrect, totalIntrusors)
Dvs_are <- c("totalCorrect", "totalIntrusors")

## CHECK UNIVARIATE AND MULTIVARIATE NORMALITY ASSUMPTION AND OUTLIERS

# check for univariate and multivariate normality and outliers for rereading group
this_group <- filter(groups_DVs, ConditionRecoded == 1)
this_group_DVs <- this_group[Dvs_are]
data_rereading <- mvn(this_group_DVs, mvnTest = "hz", covariance = TRUE, tol = 1e-25, alpha = 0.5, desc = TRUE, transform = "none",
    univariateTest = c("SW"), univariatePlot = "histogram", multivariatePlot = "qq",
    multivariateOutlierMethod = "quan", showOutliers = TRUE, showNewData = TRUE)
  # -> for the rereading group, the data was found to be normal at the univariate and multivariate levels, and no outliers were found


# check for univariate and multivariate normality and outliers for general_noFeedback group
this_group <- filter(groups_DVs, ConditionRecoded == 2)
this_group_DVs <- this_group[Dvs_are]
data_general <- mvn(this_group_DVs, mvnTest = "hz", covariance = TRUE, tol = 1e-25, alpha = 0.5, desc = TRUE, transform = "none",
    univariateTest = c("SW"), univariatePlot = "histogram", multivariatePlot = "qq",
    multivariateOutlierMethod = "quan", showOutliers = TRUE, showNewData = TRUE)
  # for the general_noFeedback group, the data was found to be normal at the univariate and multivariate levels, and 2 outliers were found
  # based on the robust squared mahalanobis distance


# check for univariate and multivariate normality and outliers for content_noFeedback group
this_group <- filter(groups_DVs, ConditionRecoded == 3)
this_group_DVs <- this_group[Dvs_are]
data_content <- mvn(this_group_DVs, mvnTest = "hz", covariance = TRUE, tol = 1e-25, alpha = 0.5, desc = TRUE, transform = "none",
    univariateTest = c("SW"), univariatePlot = "histogram", multivariatePlot = "qq",
    multivariateOutlierMethod = "quan", showOutliers = TRUE, showNewData = TRUE)
  # for the content_noFeedback group, the data was found to be normal at the multivariate level, however the distribution of the variable 
  # totalIntrusors was found to be significantly different from the one expected under the normality assumption


# check for univariate and multivariate normality and outliers for general_feedback group
this_group <- filter(groups_DVs, ConditionRecoded == 4)
this_group_DVs <- this_group[Dvs_are]
data_generalFeed <- mvn(this_group_DVs, mvnTest = "hz", covariance = TRUE, tol = 1e-25, alpha = 0.5, desc = TRUE, transform = "none",
                    univariateTest = c("SW"), univariatePlot = "histogram", multivariatePlot = "qq",
                    multivariateOutlierMethod = "quan", showOutliers = TRUE, showNewData = TRUE)


# check for univariate and multivariate normality and outliers for content_feedback group
this_group <- filter(groups_DVs, ConditionRecoded == 5)
this_group_DVs <- this_group[Dvs_are]
data_contentFeed <- mvn(this_group_DVs, mvnTest = "hz", covariance = TRUE, tol = 1e-25, alpha = 0.5, desc = TRUE, transform = "none",
                        univariateTest = c("SW"), univariatePlot = "histogram", multivariatePlot = "qq",
                        multivariateOutlierMethod = "quan", showOutliers = TRUE, showNewData = TRUE)

