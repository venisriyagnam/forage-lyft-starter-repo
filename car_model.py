from abc import ABC, abstractmethod
import datetime

class CarModel(ABC):

    @abstractmethod
    def GetInfo(id1):
        return True

    @abstractmethod
    def ChangeExisting(id1, **details):
        return True

    @abstractmethod
    def AddNew(**details):
        return True

    def CheckServiceCriteria(self, component, current_measure, previous_measure):
        # We donot need to write seperate classes for everything, we can generalize it as component
        # Everytime when a new component is added just add a few lines of code
        # I dont really think there is any difference in the new class diagram and existing one.

        if component == 'engine':
            self.service_criteria = self.service_criteria if self.service_criteria else 30000
            previous_measure = previous_measure if previous_measure else 0
            if current_measure - previous_measure >= self.service_criteria:
                # update last service mileage in database for next use
                return True

        if component == 'Battery':
            self.service_criteria = self.service_criteria if self.service_criteria else 3
            if current_measure.year - self.last_service_date.year >= self.service_criteria:
                # update last service date in database for next use
                return True

