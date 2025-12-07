###########
#LIBRARIES#
###########

import math
from typing import Optional

######################
#CONVERSION FUNCTIONS#
######################

def ConvertDToR(V):
    hpi = math.pi / 180
    cal = V * hpi
    return cal

def ConvertRToD(V):
    hpi = 180 / math.pi
    cal = V * hpi
    return cal


#####
#SAN#
#####

def calculate(inp):
    radians = ConvertDToR(inp)

    sin = math.sin(radians)

    if inp == 90 :

        tan = "Math Error"
        out = "Math Error"
    else :

        tan = math.tan(radians)
        added = sin + tan
        out = added / 2
    
    return out

#############
#SAN INVERSE#
#############

def _quartic_f(t: float, y: float) -> float:
    return (y * (t**4)) + 2.0 * t - y

def _find_root_signed(y: float, sign: int, max_expand=1<<30) -> Optional[float]:
    if y == 0.0:
        return 0.0

    a = 0.0
    b = 0.1 * sign
    fa = _quartic_f(a, y)
    fb = _quartic_f(b, y)

    if abs(fb) < 1e-15:
        return b

    expand = 1.0
    limit = 1e12
    steps = 0
    while fa * fb > 0 and abs(b) < limit and steps < 200:
        expand *= 2.0
        b = (0.1 * expand) * sign
        fb = _quartic_f(b, y)
        steps += 1

    if fa * fb > 0:
        lo, hi = 0.0, 1.0
        for _ in range(200):
            flo = _quartic_f(lo, y)
            fhi = _quartic_f(hi, y)
            if flo * fhi <= 0:
                a, b = lo, hi
                fa, fb = flo, fhi
                break
            lo = hi
            hi *= 2.0
        else:
            return None

    lo, hi = a, b
    flo, fhi = fa, fb
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        fmid = _quartic_f(mid, y)
        if abs(fmid) < 1e-14:
            return mid
        if flo * fmid <= 0:
            hi = mid
            fhi = fmid
        else:
            lo = mid
            flo = fmid
    return 0.5 * (lo + hi)

def CalculateInv(y: float, k: int = 0) -> float:
    if abs(y) < 1e-15:
        return 0.0

    sign = 1 if y > 0 else -1

    t = _find_root_signed(y, sign)
    if t is None:
        t = _find_root_signed(y, 1) or _find_root_signed(y, -1)
        if t is None:
            raise ValueError(f"Could not find real root for y={y}")

    xr = 2.0 * math.atan(t) + 2.0 * k * math.pi
    xd = math.degrees(xr)
    xd = ((xd + 180.0) % 360.0) - 180.0
    return xd