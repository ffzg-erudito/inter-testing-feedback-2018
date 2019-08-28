![](https://i.creativecommons.org/l/by/4.0/88x31.png "Creative Commons Attribution 4.0 International")
![](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0 1.0 Universal")
![](https://www.gnu.org/graphics/gplv3-127x51.png "GNU General Public License v3")

All datasets (.csv files in the folder /analyses/data/ and subfolders) are licensed under CC0 1.0 Universal.
The license can be found here - https://creativecommons.org/publicdomain/zero/1.0/legalcode.

The manuscript and related materials (.tex and .pdf files in /paper/ and subfolders; .pdf, .Rmd, .tex, .odg in
/analyses/ and subfolders; .md files in the root directory) are licensed under CC-BY 4.0 license
(https://creativecommons.org/licenses/by/4.0/legalcode).

The rest of the materials is licensed under the GPLv3 license (https://www.gnu.org/licenses/gpl-3.0.txt).

# Interpolated testing and feedback

October 2018


This repository contains `Python` scripts and ancillary files for running an 
experiment designed for investigating the forward testing effect, as well as the
analyses scripts (`R`), and a manuscript (`LaTex`).

# Contents

`design.md` contains short description of design, and has the write up of the
hypothses.

## `analyses`

This folder contains the data (`data/`), data preparation (`wrangling/`) and
analyses scripts (`stats/`). `images/` and `helpers/` contain auxiliary files.
The analysis plan is written up in `analysis-plan.md`. It also contains power
curves for the study, with final sample size and predicted sample size after
exclusion cirteria are applied.

### `data`

`results.csv` is the main data file.

`for-bayes/` contains filtered datasets used in JASP. Same data as used in the
first and second MANOVA.

## `informed-consent`

The informed consent forms files.

## `paper`

Files for compiling the article.

## `scripts`

### `exp-application`

The `oTree` app. Too deep to explain further.

### `misc`

Miscellaneous scripts used for various randomizations.

## `texts`

The texts used in the study.
