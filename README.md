# Filter math

The sticker names the months, the gallons name the truth, and the bottle names the price.

The pitcher box says "change every 2 months" while rating the cartridge in gallons. Only one survives your kitchen: a two-gallon-a-day household spends a 40-gallon filter in three weeks, and a glass-at-dinner household can ignore the calendar.

## The three tools

- **Life plan** - rated gallons over your daily draw, banded unrounded against the sticker's pace (under 45 days, about the sticker, slower than the sticker).
- **Cost plan** - cartridge price over rated gallons becomes the honest cost per gallon, the savings against bottled, and the lifetime savings of one filter. Judged unrounded: if the filter loses to the bottle, it says so.
- **Refill plan** - daily draw against pitcher cups (16 cups to the gallon, a labeled norm) becomes refills a day; past 4, a faucet mount stops being a luxury.

## Honesty notes

Illustrative planning arithmetic only. Certifications name what a filter reduces: look for the NSF/ANSI listing on the cartridge, not the box art. A filter that runs slow, smells or tastes off is done regardless of the calendar, and fridge filters follow the same gallon truth as pitchers.

## Files

- `index.html` - the pitch
- `app.html` - the calculators
- `engine.js` - the arithmetic (browser and node)
- `oracle.py` - the same arithmetic, float-for-float, writing `expected.json`
- `test.js` - runs every case in `expected.json` through `engine.js` and compares results and renders exactly

Run the check:

```
python3 oracle.py && node test.js
```
