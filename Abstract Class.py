from abc import ABC, abstractmethod


class Employee(ABC):
    def init(self, job_band, employee_name, basic_salary, qualification):
        self._job_band = job_band
        self.employee_name = employee_name
        self.__basic_salary = basic_salary
        self.__qualification = qualification

    def get_job_band(self):
        pass

    def get_employee_name(self):
        pass

    def get_basic_salary(self):
        pass

    def get_qualification(self):
        pass

    @abstractmethod
    def validate_job_band(self):
        pass

    def validate_basic_salary(self):
        pass

    def validate_qualification(self):
        pass

    @abstractmethod
    def calculate_gross_salary(self):
        pass


class Graduate(Employee):
    def __init(self, job_band, employee_name, basic_salary, qualification, cgpa):
        super().init()
        self.cgpa = cgpa

    def get_cgpa(self):
        pass

    def validate_job_band(self):
        pass

    def calculate_gross_salary(self):
        pass


def Lateral(Employee):
    def __init(self, job_band, employee_name, basic_salary, qualification, skill_set):
        self.__skill_set = skill_set

    def get_skill_set(self):
        pass

    def validate_job_band(self):
        pass

    def calculate_gross_salary(self):
        pass
