# Word choice (simple but academic)

Adapted from Imbad0202/academic-research-skills (writing_quality_check.md) and Orchestra-Research
ml-paper-writing (Lipton, Steinhardt, Perez). These are prompts for judgment, not hard bans. Keep a word when it
is the most precise term. Standard robotics terms are exempt ("robust control", "robustness to perturbations").

## Prefer the plain academic word

| Avoid | Use |
|---|---|
| leverage, utilize | use |
| showcase | show, demonstrate |
| delve into | examine, study |
| facilitate | enable, help |
| endeavor, embark on | aim, begin |
| pivotal, crucial (as filler) | important, key, or delete |
| underscore | show, highlight |
| a plethora of, a myriad of | many |
| commence | start, begin |
| in order to | to |
| due to the fact that | because |
| is capable of | can |
| has the ability to | can |
| a large number of | many (or the number) |
| cutting-edge, groundbreaking | state-of-the-art, or delete |
| tapestry, landscape, realm, paradigm (figurative) | field, area, or delete |
| holistic, multifaceted, synergy | state the specific property |

## Vague → specific (Steinhardt)

| Vague | Specific |
|---|---|
| performance | success rate, return, latency, smoothness |
| improves | raises the success rate from 50% to 80% |
| fast | 3.5 ms per action, 4× faster |
| large dataset | 50 demonstrations per task, 22.8 hours |
| good results | 95.0% success over 3 seeds |

## Delete

- Intensifiers: very, really, quite, extremely, highly, remarkably, significantly (unless a statistical test).
- Fillers: actually, basically, essentially, fortunately, unfortunately.
- Throat-clearing: "It is worth noting that", "It should be noted that", "It is important to note that",
  "In the realm of", "When it comes to". Start with the subject.
- Meta-commentary inside sections ("This section will discuss ..."). A roadmap sentence at the end of the
  introduction is fine.
- Generic openers that fit any paper ("In recent years, deep learning has achieved remarkable success").

## Nominalization → verb

"We performed an analysis of" → "We analyzed". "achieves a reduction of" → "reduces".
"provides an improvement in" → "improves".

## Pronouns

Use "this"/"these" with a noun: "This result shows", not "This shows".

## Structure smells

- Padding lists to three items. Use as many points as the evidence supports.
- Synonym cycling for one concept. Keep one term.
