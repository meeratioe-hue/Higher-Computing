

from dataclasses import dataclass

@dataclass
class person():
  height : float = 0.0
  weight : float = 0.0
  bmi : float = 0.0

people = [person() for index in range(5)]
