from abc import ABC

import car_model

class Car(car_model, ABC):
    
    def GetInfo(self, id1):
        # get info of car using id from database
        return True

    def AddNew(self, id1, **details):
        car_id = id1
        parts = {}
        for key, value in details.values():
            parts[key] = value
        
        # Add parts dictionary in the database using id
        return True

    def ChangeExisting(self, id1, **details):
        car_id = id1
        # Get the list of all parts using id and change according to the details dictionary
        return True
