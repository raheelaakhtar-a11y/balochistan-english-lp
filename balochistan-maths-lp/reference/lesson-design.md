# Lesson design (Beginner Day 1, M-B-01 Count objects up to 20)

Design rule: the **page design** is the English plan's; the **activities** are maths-native, built from the SLO and the book.
Concrete, then pictorial, then abstract. Each I Do stage runs Model, Together, Try.

## Minutes (fixed)

| Part | Min |
|---|---|
| Warm-up | 5 |
| Hook | 5 |
| I Do | 20 |
| We Do | 12 |
| You Do | 8 |
| Exit check | 10 |

`doc_lp_m8.py` asserts the bar sums to 60. Shown once, on page 1.

## Page 1: roadmap and outcomes

Header 46 mm. Day ribbon (Days 1 to 2 gold, Days 31 to 33 green). Then, in order:

1. Today box: `1-20 Count Objects up to 20` (the planner code and sentence verbatim)
2. Learning outcome (sky, full width)
3. Today's Goal (teal), directly after
4. THE 60 MINUTES bar
5. Student book row + "Your three documents" row
6. To prepare box

## Page 2: warm-up and hook

- **Warm-up, Fingers and Counting** (book pp.2 to 3): count on fingers, then count as far as you can.
- **Hook, Guess, Then Count**: 14 stones in two rows of seven. Children guess, then count.
- Write on the Board box.

## Page 3: I Do (20 min), four stages

| Stage | Material | Idea |
|---|---|---|
| 1 | real stones | touch and tick, one number per stone |
| 2 | Picture Cards A to D | count pictures (6 apples scatter, 9 balls in a row, 13 fish in a row, 17 stars in a row) |
| 3 | stones + Ten Box | make ten (book p.14: 9 candies + 1) |
| 4 | stones + two Ten Boxes | past ten (book p.18, numbers 11 to 20) |

Stages 1, 3, 4 use stones; their pictures draw stones (asserted).

## Page 4: We Do (12 min)

- **Silly Counter**: the teacher makes three counting mistakes and children catch them (skips a number, counts one twice, misses one). Table with real stones.
- **Count and Swap**: six piles `[12, 13, 15, 17, 18, 20]` in cups, counted into the Ten Box Mat, then swapped to check reliability. Number Chart for support.
- **Check the Book**: p.5 rows 6 pumpkins, 8 doughnuts, 9 oranges.

## Page 5: Your Turn and exit

- Your Turn answers (from the data block).
- **Exit Check**: Part A 8 written items (6 count-and-circle + 2 draw-dots), Part B oral "count out 12, 16, 19".
- Score and decide: On track / Practise / Re-teach. **No pass-mark line** (`[PENDING]`).
- Key facts to remember, At home.

## Prep Pack (7 pages)

Number Chart 1 to 20, Call Sheet, four Picture Cards (A to D), Ten Box Mats x8, tally. Materials: about 100 stones/caps and 6 cups.

## Student Worksheet (2 pages)

Page 1 You Do: worked example (4 stars), four count-and-circle items `[7, 12, 15, 18]`, three draw-dots items `[8, 13, 17]` (example 5), dot-to-dot 1 to 20 (ten-pointed star).
Page 2: the 8-item exit check: `("c", 9 ball scatter)`, `("d", 6)`, `("c", 14 kite)`, `("c", 11 fish)`, `("d", 10)`, `("c", 19 pencil)`, `("c", 16 apple)`, `("c", 20 star)`.

## Where the data lives

`common_m5.py` holds: `HOOK_N`, `PILES`, `SILLY`, `BOOK_ROWS`, `CARDS_M`, `CARD_USE`, `ORAL_GIVE`, `T1_EX`, `T1`, `T2_EX`, `T2`, `T3_N`, `EXIT`. Change a number there and the Lesson Plan, Prep Pack and Worksheet all follow. Never type a count into a `doc_*.py`.
