from pydantic import BaseModel

from infrastructure.constants import Day, Part, Year


class InputId(BaseModel):
    year: Year
    day: Day

    class Config:
        extra = 'ignore'
        frozen = True


class SolutionId(BaseModel):
    year: Year
    day: Day
    part: Part

    @property
    def input_id(self) -> InputId:
        return InputId(year=self.year, day=self.day)

    class Config:
        extra = 'ignore'
        frozen = True
