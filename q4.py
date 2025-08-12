from typing import Self

class Date:
    def __init__(self, day: int, month: int, year: int):
        pass

    def __str__(self) -> str:
        pass

    def add_date(self, other: Self) -> Self:
        """Returns the sum of this date and the other date.
        Adds together the years, months, and days, respectively.
        The resulting date is a real date (e.g., not December 40th).
        Does not modify the existing Date.

        Parameters
        ----------
        other : Date
            The other date to add this one to
        
        Returns
        -------
        Date
            The result of adding these two dates

        Example: Date(1, 2, 2025).add_date(Date(1, 0, 0)) returns Date(2, 2, 2025)
        Example: Date(31, 12, 1999).add_date(Date(366, 0, 0)) returns Date(31, 12, 2000)
        (Don't forget about leap years!)
        """
