from abc import ABC

import car_model

class Component(car_model, ABC):
    
    def GetInfo(self, id1):
        # get info of component_id using id from database
        return True

    def AddNew(self, id1, **details):
        comp_id = id1
        for key, value in details.values():
            comp_name = key
            service_criteria = value
        
        # Add service_criteria and component in the database using id
        return True

    def ChangeExisting(self, id1, **details):
        comp_id = id1
        for key, value in details.values():
            comp_name = key
            service_criteria = value
        # Change service criteria using id
        return True
