

from dataclasses import dataclass

@dataclass
class person():
  height : float = 0.0
  weight : float = 0.0
  bmi : float = 0.
  
  BMIdetails = ???

  BMIrecord[1].height = 1.75
  BMIrecord[1].weight = 70.5
  BMIrecord[1].bmi = BMIrecord[1].weight / BMIrecord[1].height **2 