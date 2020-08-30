# # Package # #
from db.database import collection
from models import Employee

__all__ = ("EmployeeRepository",)


class EmployeeRepository:

    @staticmethod
    def create(create: Employee):
        """Create an Employee and return its Read object"""
        document = create.dict()
        # The time and id could be inserted as a model's Field default factory,
        # but would require having another model for Repository only to implement it

        result = collection.insert_one(document)
        assert result.acknowledged
