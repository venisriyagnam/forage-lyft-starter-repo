from abc import ABC, abstractmethod
import datetime

class CarModel(ABC):

    @abstractmethod
    def GetInfo(id1):
        pass

    @abstractmethod
    def ChangeExisting(id1, **details):
        pass

    @abstractmethod
    def AddNew(**details):
        pass

    def CheckServiceCriteria(self, component, current_measure):
        # We donot need to write seperate classes for everything, we can generalize it as component
        # Everytime when a new component is added just add a few lines of code
        # I dont really think there is any difference in the new class diagram and existing one.

        if component == 'engine':
            if current_measure - self.last_service_mileage >= self.service_criteria:
                # update last service mileage in database for next use
                return True

        if component == 'Battery':
            if current_measure.year - self.last_service_date.year >= self.service_criteria:
                # update last service date in database for next use
                return True

