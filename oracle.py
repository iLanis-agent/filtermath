import json, math

def pos(x): return isinstance(x,(int,float)) and math.isfinite(x) and x>0
def jround(x): return math.floor(x+0.5)
def jsnum(x):
    if isinstance(x,float) and x==int(x): return str(int(x))
    return str(x)
def r1(x): return jround(x*10)/10
def r2(x): return jround(x*100)/100
def money(x): return f"{r2(x):.2f}"

def life_plan(ratedGal,galPerDay):
    if not pos(ratedGal) or not pos(galPerDay): return {"error":"gallons must both be above zero"}
    days=ratedGal/galPerDay
    if days<45: verdict="faster than the sticker: your glasses drink the filter early"
    elif days<=75: verdict="about the sticker's pace"
    else: verdict="slower than the sticker: change by taste and flow, not the calendar"
    return {"days":r1(days),"verdict":verdict}

def gal(x): return jsnum(x)+(" gallon" if x==1 else " gallons")
def render_life(r,ratedGal,galPerDay):
    return ("Your "+jsnum(ratedGal)+" gallon filter at "+gal(galPerDay)+" a day figures "
            +jsnum(r["days"])+" days - "+r["verdict"]+".")

def cost_plan(filterPrice,ratedGal,bottledGal):
    if not pos(filterPrice) or not pos(ratedGal) or not pos(bottledGal):
        return {"error":"price, gallons and bottle cost must all be above zero"}
    perGal=filterPrice/ratedGal
    save=bottledGal-perGal
    return {"perGal":r2(perGal),"save":r2(save),"life":r2(save*ratedGal),"wins":save>0}

def render_cost(r,filterPrice,ratedGal,bottledGal):
    if not r["wins"]:
        return ("Your $"+money(filterPrice)+" filter over "+jsnum(ratedGal)+" gallons costs $"
                +money(r["perGal"])+" a gallon - more than the $"+money(bottledGal)+" bottle; check the numbers.")
    return ("Your $"+money(filterPrice)+" filter over "+jsnum(ratedGal)+" gallons costs $"+money(r["perGal"])
            +" a gallon - $"+money(r["save"])+" under the $"+money(bottledGal)+" bottle, saving $"
            +money(r["life"])+" over the filter's life.")

def refill_plan(galPerDay,cups):
    if not pos(galPerDay) or not pos(cups): return {"error":"gallons a day and pitcher cups must both be above zero"}
    refills=galPerDay/(cups/16)
    verdict="a faucet mount stops being a luxury" if refills>4 else "a pitcher keeps up"
    return {"refills":r1(refills),"verdict":verdict}

def render_refill(r,galPerDay,cups):
    return ("At "+gal(galPerDay)+" a day your "+jsnum(cups)+"-cup pitcher means about "
            +jsnum(r["refills"])+" refills - "+r["verdict"]+".")

cases=[]
def add(tool,args):
    if tool=="life": r=life_plan(*args); fn=render_life
    elif tool=="cost": r=cost_plan(*args); fn=render_cost
    else: r=refill_plan(*args); fn=render_refill
    case={"tool":tool,"args":args,"result":r}
    if "error" not in r: case["render"]=fn(r,*args)
    cases.append(case)

for a in [(40,2),(40,0.8),(40,1),(120,1.5),(100,2),(40,0.5),(120,1.6),(60,1.3)]:
    add("life",a)
for a in [(8,40,1.2),(35,120,1.0),(10,40,0.8),(15,100,1.5),(30,120,0.9),(8,40,0.15),(12,60,1.1)]:
    add("cost",a)
for a in [(2.5,10),(1,10),(3,10),(0.8,7),(2,6),(4,12),(1.5,5)]:
    add("refill",a)
add("life",[0,2]); add("life",[40,0]); add("cost",[0,40,1.2]); add("refill",[0,10])

json.dump(cases,open("expected.json","w"),separators=(",",":"))
print(len(cases),"cases")
