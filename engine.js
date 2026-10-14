// Filter math - water filter pitcher honesty.
// The sticker says two months; the filter is rated in gallons. Your glasses
// decide which one is telling the truth. Verdicts judge the unrounded figure;
// rounding is for display only.
var FilterMath = (function () {
  function pos(x) { return typeof x === "number" && isFinite(x) && x > 0; }
  function r1(x) { return Math.round(x * 10) / 10; }
  function r2(x) { return Math.round(x * 100) / 100; }
  function money(x) { return r2(x).toFixed(2); }

  function lifePlan(ratedGal, galPerDay) {
    if (!pos(ratedGal) || !pos(galPerDay)) return { error: "gallons must both be above zero" };
    var days = ratedGal / galPerDay;
    var verdict;
    if (days < 45) verdict = "faster than the sticker: your glasses drink the filter early";
    else if (days <= 75) verdict = "about the sticker's pace";
    else verdict = "slower than the sticker: change by taste and flow, not the calendar";
    return { days: r1(days), verdict: verdict };
  }

  function gal(x) { return x + (x === 1 ? " gallon" : " gallons"); }
  function renderLife(r, ratedGal, galPerDay) {
    return "Your " + ratedGal + " gallon filter at " + gal(galPerDay) + " a day figures "
      + r.days + " days - " + r.verdict + ".";
  }

  function costPlan(filterPrice, ratedGal, bottledGal) {
    if (!pos(filterPrice) || !pos(ratedGal) || !pos(bottledGal)) return { error: "price, gallons and bottle cost must all be above zero" };
    var perGal = filterPrice / ratedGal;
    var save = bottledGal - perGal;
    return { perGal: r2(perGal), save: r2(save), life: r2(save * ratedGal), wins: save > 0 };
  }

  function renderCost(r, filterPrice, ratedGal, bottledGal) {
    if (!r.wins) return "Your $" + money(filterPrice) + " filter over " + ratedGal + " gallons costs $"
      + money(r.perGal) + " a gallon - more than the $" + money(bottledGal) + " bottle; check the numbers.";
    return "Your $" + money(filterPrice) + " filter over " + ratedGal + " gallons costs $" + money(r.perGal)
      + " a gallon - $" + money(r.save) + " under the $" + money(bottledGal) + " bottle, saving $"
      + money(r.life) + " over the filter's life.";
  }

  // Labeled norm: a "cup" in pitcher sizing is 8 fl oz, so 16 cups to the gallon.
  function refillPlan(galPerDay, cups) {
    if (!pos(galPerDay) || !pos(cups)) return { error: "gallons a day and pitcher cups must both be above zero" };
    var refills = galPerDay / (cups / 16);
    var verdict = refills > 4 ? "a faucet mount stops being a luxury" : "a pitcher keeps up";
    return { refills: r1(refills), verdict: verdict };
  }

  function renderRefill(r, galPerDay, cups) {
    return "At " + gal(galPerDay) + " a day your " + cups + "-cup pitcher means about "
      + r.refills + " refills - " + r.verdict + ".";
  }

  return {
    lifePlan: lifePlan, renderLife: renderLife,
    costPlan: costPlan, renderCost: renderCost,
    refillPlan: refillPlan, renderRefill: renderRefill
  };
})();
if (typeof module !== "undefined") module.exports = FilterMath;
