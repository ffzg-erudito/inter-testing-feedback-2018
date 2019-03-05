# Tests

## H1 + H2

We plan to conduct a MANOVA with interpolated activity as a dependent variable, and the number of
correct answers on the final test and the proportion of chosen intrusive distractors among
incorrect answers. We will perform this analysis only on the subset of participants not receiving feedback.

In case of a statistically significant Wilks' lambda, we will proceed with assessing planned contrasts analysis.
We aim to compare the two test groups with the rereading group.

We plotted the power obtained with our sample size (N = 125) and the sample size we expect to work with after 
our exclusion criteria have been applied (N = 110) as a function of a range of effect sizes, depicted in
the images below. 
![alt text](https://github.com/ffzg-erudito/inter-testing-feedback-2018/blob/master/analyses/images/H1-H2_power_plot_N125.png)

![alt text](https://github.com/ffzg-erudito/inter-testing-feedback-2018/blob/master/analyses/images/H1-H2_power_plot_N110.png)

As can be seen from the images, with our effective sample size we expect to have .8 power to detect an effect
size in the medium range. 

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

To test these hypotheses, we also plan to conduct a MANOVA with feedback and interpolated activity
as the independent variables and the number of correct answers on the final test and the proportion 
of chosen intrusive distractors among incorrect answers. In line with the hypotheses, we will be 
looking at the main effect of feedback on 


We plotted the power obtained with our sample size (N = 166) and the sample size we expect to work with after 
our exclusion criteria have been applied (N = 145) as a function of a range of effect sizes, depicted in
the images below. 
![alt text](https://github.com/ffzg-erudito/inter-testing-feedback-2018/blob/master/analyses/images/H3-H6_power_plot_N166.png)

![alt text](https://github.com/ffzg-erudito/inter-testing-feedback-2018/blob/master/analyses/images/H3-H6_power_plot_N145.png)

As can be seen from the images, with our effective sample size we expect to have .8 power to detect an effect
size in the lower medium range. 


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
