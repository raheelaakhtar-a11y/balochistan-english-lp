# Layout rules (decided with the user, 2026-10-27/28)

Fixed A4 pages. `.content` is absolutely positioned (left/right 10 mm, top 30 mm, bottom 15 mm, overflow hidden). `.foot` sits at bottom 5 mm.

## Page 1
- Learning outcomes box (sky), then immediately the **Today's Goal** teal box.
- No "By the end of today" box. Today's Goal does not repeat on page 2.

## Page 2 (start, I Do)
- Zoom wrapper 1.2, height 210.0 mm, blocks spread with `space-between`.

## Page 4 (You Do)
- Zoom 1.08 (Beginner) / 1.12 (Intermediate).
- The check row is **last**: "CHECK BEFORE MOVING ON" (cfu) and the gold "While you walk around" box, pushed to the bottom of the page.

## Page 5 (exit check)
- Content `bottom:70mm`, zoom wrapper (1.2 Beginner, 1.05 Intermediate).
- **Footer band** pinned at bottom 12.5 mm, gold top rule, zoom .9, in this order: Score and decide (mint) + Key facts to remember (navy), then **At home (optional)** underneath. At home must come after the boxes, not above them.
- At home text: Beginner "Say A, B, C, D and the words ant, bed, cat, dog to someone at home."; Intermediate "Read the words clap, drum, ship and phone to someone at home."
- Footer band CSS: `.ftb .box{padding:2mm 3.2mm;margin-bottom:0}.ftb .box h2{font-size:10pt;margin-bottom:1mm}.ftb .row{gap:3mm;margin-bottom:0}` (doubled braces in f-strings).

## Content rules
- Exit check: Part A written items (names and sounds never mixed in one item), Part B hear 4 to 5 children.
- Tracker: On track / Practise / Re-teach. No pass-mark line.
- Beginner Day 1: letters A B C D by name, sound, write capital and small (E-B-01..03, E-B-04 folded in). Picture words ant, bed, cat, dog.
- Intermediate Day 1: E-I-01 with E-I-06 folded in, builds on E-B-07. Blends cl bl dr br, digraphs ch sh th ph, 2 to 3 word phrases, 3 to 5 letter words. Planner says avoid st, tr, wh and long vowels (the 28 Oct planner now allows `st`; phone and photo accepted by the user despite the long-vowel rule).

## Version history convention
Every change is a new `_vN` file in the Desktop day folder (`Level 1 English Day 1 (final planner)`, `Level 2 English Day 1 (final planner)`). Never overwrite.
