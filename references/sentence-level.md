# Sentence-level principles

From Gopen & Swan, "The Science of Scientific Writing" (1990), via Orchestra-Research ml-paper-writing.
These support the user's rule of simple sentences (SKILL.md §2.3).

1. **Subject and verb close together.** Move long modifiers after the verb or into a new sentence.
   Weak: "The policy, which was trained on 50 demonstrations per task with three seeds, reaches 95.0%."
   Strong: "The policy reaches 95.0%. We train it on 50 demonstrations per task with three random seeds."
2. **Stress position.** Put the new or important item at the end of the sentence.
   "With the contractive perturbation, the success rate rises to $95.0\%$."
3. **Topic position.** Start with whose story the sentence tells, usually "we" or the method.
4. **Old before new.** Open with what the reader already knows, then add the new information. This links
   sentences without extra connectives.
5. **One unit, one function.** One idea per sentence, one message per paragraph.
6. **Action in the verb.** "We compare", not "We make a comparison".
7. **Context before new information.** State the purpose before the equation or figure.
   "To bound the error, we require ... (Eq. 3)".

## When a complex sentence is allowed

Keep a subordinate clause when it carries a causal or logical relation that would break if split:
- cause and effect: "Because the encoder runs at every step, $H=1$ needs $3.5$\,ms per action."
- condition: "If the chunk is too long, the policy cannot react to perturbations."
- contrast inside one claim: "Diffusion policy needs $10$ denoising steps, whereas ours needs one."

Split everything else, especially chains such as "X, and Y, which Z, while W".

## Active voice

- "We train the policy", not "The policy is trained".
- "Fig. 3 shows", not "It is shown in Fig. 3".
- Passive is fine only when the actor is unknown or does not matter
  ("The objects are placed at random positions").
