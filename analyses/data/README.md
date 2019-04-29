# `results.csv`

This is the file which contains the raw data used in the analyses.

Variables are:
- `when` - timestamp
- `giveFeedback` - whether the participant received feedback on the interpolated
    test or not
- `condition` - experimental condition
- `timerStart` - auxiliary
- `readingTime` - the time the participant spent reading the practice text
- `readingTimeEstimate` - the reading time available for reading the main text
    parts, based on the time they have spent reading the practice text
- `kolikoProcitaoText<N>` - participants' estimates of how many times they've
    read each part of the text. Important: participants in the rereading
    condition had a different set of options than the rest, to account for the
    extra time they have had for reading. Options are:
    - jednom cijeli tekst - the whole text once
    - oko dva puta - around two times
    - jednom cijeli tekst i preletjeti ključne dijelove - the whole text once
        and skim the key parts
    - više od jedan i pola puta, ali manje od dva puta - more than one and a
        half times, but less than two times
    - više nego jednom, ali nešto manje od jedan i pola puta - more than once,
        but somewhat less than one and a half times
    - oko dva i pola puta - around two and a half times
    - nisam uspjela/uspio pročitati do kraja ili sam žurila/žurio da bih
        pročitala/pročitao - I haven't managed to read the whole text or I had
        to speed up to be able to read it
    - tri ili više puta	- three or more times
- `readingDeficits` - whether they have reading deficits: YES/NO
- `which` - if so, which? question was mandatory ( :( ), so a lot of "no/none"
    options
- `readingDifficultiesThisExp` - whether they've had reading difficulties in
    this experiment particularly
- `practiceForActivity_<N>` | `practiceForFinal_<N>` - answers to practice Qs
    for the interpolated activity and final test, respectively
- `genKnowledge_<N>_<M>` - answers to general knowledge questions;
    correct/incorrect (1/0)
- `content_<N>_<M>` - same as above but for content related questions.
    `content_3_<M>` are the final test questions.
- `isIntrusor_<N>_<M>` - whether the chosen option is an intrusive distractor or
    not
- `totalCorrect` - total number of correct answers
- `totalIntrusors` - total number of intrusive distractors chosen
- `activityFactor` - which interpolated activity the participant engaged in
