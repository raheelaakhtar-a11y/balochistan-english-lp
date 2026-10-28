# Rules and history (decided with the user, 2026-10-19 to 28)

## Standing rules

1. **Never overwrite.** Every revision is a new `_vN` file in `Desktop\Level 1 Maths Day 1\`. Only delete a version when the user asks.
2. **Maths-native activities, English design.** "It is as if I have just switched the subject": same structure and look, activities from the SLO and the book.
3. **Not a replica of the sample maths LP** (the Pindi sample). The user rejected a copy ("I don't want exact replication").
4. **A picture shows exactly what the text names.** Enforced by asserts (see SKILL.md).
5. **Never repeat information to fill space.** Rebalance with spacing and zoom.
6. **Do only what is asked this round.** "Don't give me the Prep Pack and the Worksheet as yet" means Lesson Plan only.
7. Spell-check printed words. Answers come from one data block.

## Version history (Day 1)

| Ver | Date | What changed |
|---|---|---|
| v1 | 19 Oct | English-design base; counting only; Kie capped, so SVG only |
| v2 | 19 to 20 Oct | first copied the sample (rejected: "looks like Pindi", deleted); then Taleemabad-brand look (kept, unused) |
| v3 | 20 Oct | English look plus counting train; user: English activities were ported, not wanted |
| v4 | 20 Oct | maths-native lesson in English design (Silly Counter, Count and Swap, Ten Boxes, Number Chart) |
| v5 | 28 Oct | new planner: Days 1 to 2 only, rows or small groups, no scatter above 9 |
| v6 | 28 Oct | stones drawn as stones; Kie characters replace drawn people; asserts added |
| v7 | 28 Oct | Lesson Plan only: removed "By the end of today..." and "Counting only"; Today's Goal under outcome; added a glance grid |
| v8 | 28 Oct | Lesson Plan only: removed the glance grid (it repeated the minutes); page 1 rebalanced by spacing and zoom 1.07 |

Prep Pack and Worksheet: current is v6.

## Decisions the user can reverse

- Book has no page counting to 20: the plan cites p.5 and p.18 and states it.
- Day 1 is counting only; writing numerals starts Day 3.
- Hook "The Secret Stones" became "Guess, Then Count" with 14 stones in two rows of seven.
- We Do uses piles in cups; Count and Swap fills the Ten Box Mat to count each pile.

## Errors seen, and the fix

| Error | Fix |
|---|---|
| Kie 433 (daily cap) | stop, never loop; reuse scenes; retry another day |
| "fishs" | `pl()` helper |
| Call-sheet "use" column invisible | `--grey` is a background colour; use `--mid` |
| `NameError: name 'margin' is not defined` | double the braces in an f-string `<style>` |
| PDF copied while overflowing | check `overflow=OK` and look at every PNG before copying |
| Bash build wrote no PDF | build from PowerShell |
