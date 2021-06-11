"""
Fan utils.
Bruce Wernick
10 June 2021
"""

__all__ = ['refrho', 'refspeed', 'refpole', 'pole2sync', 'pole2speed',
  'loose_speed2pole', 'get_pole', 'fancode', 'toSPL', 'toSWL',
  'SWL_pole', 'approx_SWL']

from math import log10, pi

refrho = 1.2 # standard air density

# ref motor, 4-pole 50 Hz
refspeed = 1440.0 # rpm
refpole = 4.0 #

def pole2sync(p, f=50.0):
  "given the motor poles return synchronous speed [rpm]"
  return f*(2.0/p)*60.0

def pole2speed(p, f=50.0):
  "return actual speed [rpm] of motor"
  return refspeed*(4.0/p)*(50.0/f)

def approx_speed2pole(n):
  "approximate conversion of speed to pole"
  if n <= 500: return 12
  if n <= 600: return 10
  if n <= 750: return 8
  if n <= 1000: return 6
  if n <= 1500: return 4
  if n <= 3000: return 2
  return None

def get_pole(dia,hub,blade):
  "given (dia,hub,blade), get the valid motor poles"
  if(dia>=800)|((dia==560)&(blade==14))|((630<=dia<=710)&(hub==150)):
    return [4,6]
  return [2,4,6]

def fancode(code):
  "split code into (dia,hub,blade)"
  dia,hub,blade=list(map(int,code.split('/')))
  return (dia,hub,blade)

def toSPL(swl, Q=4.0, r=3.0):
  "sound power level to sound pressure level"
  return swl - abs(10.0 * log10(Q/(4.0*pi*r**2)))

def toSWL(spl, Q=4.0, r=3.0):
  "sound pressure level to sound power level"
  return spl + abs(10.0 * log10(Q/(4.0*pi*r**2)))

def SWL_pole(swl, pole=4):
  "Adjust SWL for pole, ref pole=4"
  pole=float(pole)
  return swl + 50.0*log10(refpole/pole)

def approx_SWL(**kwargs):
  """you need to specify at least two of
  mw = motor power [kW]
  pt = total pressure [Pa]
  qa = air volume [m3/s]"""
  if 'wm' in kwargs and 'pt' in kwargs:
    wm = kwargs['wm']
    pt = kwargs['pt']
    return round(67.0+10.0*log10(wm)+10.0*log10(pt), 1)
  if 'qa' in kwargs and 'pt' in kwargs:
    qa = kwargs['qa']
    pt = kwargs['pt']
    return round(40.0+10.0*log10(qa)+20.0*log10(pt), 1)
  if 'wm' in kwargs and 'qa' in kwargs:
    wm = kwargs['wm']
    qa = kwargs['qa']
    return round(94.0+20.0*log10(wm)-10.0*log10(qa), 1)
  return None


# ---------------------------------------------------------------------

if __name__=='__main__':

  print(approx_SWL(pt=300, qa=1.0))
