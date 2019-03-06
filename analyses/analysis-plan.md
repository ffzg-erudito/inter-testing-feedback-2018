# Tests

## H1 + H2

We plan to conduct a one-way MANOVA with interpolated activity as the independent variable, and the number 
of correct answers on the final test and the number of chosen intrusive distractors. We will perform this 
analysis only on the subset of participants not receiving feedback.

Furthermore, after conducting the omnibus analysis to assess the impact of interpolated activity on the 
combination of DVs, in order to assess the importance of each dependent variable, since we expect our DVs 
to be correlated (which makes assessing their importance through univariate ANOVAs problematic), we will 
use Roy-Bargmann stepdown analysis, in which the highest-priority dependent variable is tested in univariate 
ANOVA (with appropriate alpha adjustment), and the remaining dependent variables are assessed separately each 
in ANCOVA, where the higher-priority dependent variables (e.g. the dependent variable considered causally 
prior) are entered as covariates (Tabachnick & Fidell, 2013).

According to our theoretical position, the dependent variable with higher priority in our study is the 
total number of correct answers a participant gives. Thus, if we obtain a significant omnibus test statistic 
for the effect of interpolated activity, we will conduct one post hoc ANCOVA, entering the total number 
of correct answers as the covariate, to assess the effect of interpolated activity on the number of 
chosen intrusive distractors. In our case, if the observed significant differences are completely 
accounted for by the effects of the inteprolated activity on the number of correct answers given (i.e. 
the more important DV), then the ANCOVA will show that there is no significant impact of interpolated 
activity on the number of chosen intrusive distractors. Finally, to supplement the Roy-Bargmann procedure,
we will also consider using discriminant analysis, where we will use the otput loading matrix containing
correlations between the individual DVs and the linear combination of DVs that maximises the treatment 
differences.

In case of a statistically significant Wilks' lambda (or other appropriate omnibus test statistic), and if 
a particular DV is found to be important to the main effect, we will proceed with assessing planned contrasts
analysis. We aim to compare the two test groups with the rereading group. Tabachnick and Fidell (2013) suggest 
that, in the case of post hoc comparisons, an extension of the Scheffé procedure be used to protect against 
inflated Type I error due to multiple tests. This conservative procedure allows for an unlimited number of 
comparisons.


We plotted the power obtained with our sample size (N = 125) and the roughly estimated sample size
we expect to work with after our exclusion criteria have been applied (N = 110), as a function of a
range of effect sizes, depicted in the images below. 

![alt text](https://github.com/ffzg-erudito/inter-testing-feedback-2018/blob/master/analyses/images/H1-H2_power_plot_N125.png)

![alt text](https://github.com/ffzg-erudito/inter-testing-feedback-2018/blob/master/analyses/images/H1-H2_power_plot_N110.png)

As can be seen from the images, with our effective sample size we expect to obtain power of about .8
to detect effects deemed by Cohen (1988) to be somewhere in the range between small and medium (around .06).

Furthermore, in order to investigate whether there is no difference between the two test groups, we will
conduct a two-one-sided t-tests (TOST) procedure, as well as a Bayesian t-test.

### TOST

The smallest effect size of interest (SEOSI) we would like to detect is Cohen's d = 0.25. This SESOI
was chosen because:
a) it falls within Cohen's proposed "small" effect size range
b) according to the Chan et al. meta-analysis, if the effect exists, it should probably be larger
c) it represents a 57% probability of superiority of one group over the other (calculated through
`https://rpsychologist.com/d3/cohend/`). Fifty seven per cent was practically chosen aribtrarily,
but it represent a just-above-chance probability.

Still, we think this SESOI is quite conservative.

### Bayesian t-test

## H3 to H6

To test these hypotheses, we also plan to conduct a two-way MANOVA with feedback and interpolated 
activity as the independent variables, and the number of correct answers on the final test and the
number of chosen intrusive distractors as the dependent variables. We will exclude the rereading 
group from this analysis. In line with the hypotheses, we will be looking at the main effect of 
feedback on the combination of DVs, the main effect of interpolated activity on the combination of 
DVs, and the interaction effect of the IVs on the combination of DVs.

To follow up on the omnibus analysis, we will employ the same general procedure used for testing the first
two hypotheses, which was outlined above. We will assess the importance of the individual DVs for each 
of the hypothesised effects through Roy-Bargmann stepdown analysis: first, we will conduct a two-way 
ANOVA on the number of correct answers, after which we will conduct a two-way ANCOVA with the number of 
correct answers entered as a covariate. We will consider reinforcing this with a discriminant analysis.

We plotted the power obtained with our sample size (N = 166) and the roughly estimated sample size
we expect to work with after our exclusion criteria have been applied (N = 145) as a function of a 
range of effect sizes, depicted in the images below.

![alt text](https://github.com/ffzg-erudito/inter-testing-feedback-2018/blob/master/analyses/images/H3-H6_power_plot_N166.png)

![alt text](https://github.com/ffzg-erudito/inter-testing-feedback-2018/blob/master/analyses/images/H3-H6_power_plot_N145.png)

As can be seen from the images, with our effective sample size we expect to obtain power of about .8
to detect effects deemed by Cohen (1988) to be somewhere in the range between small and medium (around .05).


# Exclusion criteria

We have identified several potential exclusion criteria.

The "hard" ones are:
- if a participant's training text reading time is below 90 seconds, that
    participant will be excluded. The training text is appx. 700 words long, and
    it's (a) unlikely that a person would be able to carefully read it in such a
    short time, and (b) even if someone were able to read the text carefully and
    with comprehension in that short amount of time, the person would probably
    differ from the general population on various characteristics.
- people scoring 0 on the final test will be excluded. The final test has 20
    questions, so we'd expect participants to have at least a few correct
    answers by chance alone.
- there were two questions regarding reading difficulties/impairments. One asked
    participants whether they had any reading impairments, for example dyslexia.
    Participants answered with yes/no, and were asked to state what kind of
    difficulty they had, if any. The free-text answers of those who have
    answered "yes" to these questions will be examined, and an exclusion
    decision made.

The "soft" criteria:
- The second question regarding reading difficulties was only whether they've had any
    reading difficulties during this research, but not what kind of
    difficulties. Hence, the answer to this question may not have the same
    gravity as the answer to the previous one. Therefore, the answer to this
    question will be used as a criterion for a robustness check exclusion.
- Participants were asked how many times they've read each of the three texts.
    The answer was indicated on an ordinal scale comprising the following
    options:
    - in the rereading condition:
        - the whole text once
        - the whole text once and some key points
        - approximately one and a half times
        - appx. two times
        - appx. two and a half times
        - three or more times
    - in the remaining conditions:
        - I haven't managed to read the text at least once or I had to increase
            my reading speed in order to read it
        - the whole text once
        - the whole text once and some key points
        - appx. one and a half times
        - between one and one and a half times
        - between one and a half and two times
        - two or more times.

    Since this isn't a precise measure, we will use this criterion only as a
    robustness check. For the check, we will only retain participants who've
    read the text once/one and a half times/once + key points if they're in the
    test conditions and twice/two and a half times if they're in the rereading
    condition.

We will perform a robustness check of the obtained results by applying the established
"soft" exclusion criteria to our sample and repeating the described analyses on the 
resultant sample.
