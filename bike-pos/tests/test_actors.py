import unittest
from bikeshop.actors import Staff, Customer, PrivilegeException


class TestBikeShopActors(unittest.TestCase):
    def test_if_staff_is_staff(self):
        staff = Staff(1, "John", 30, 52000, "Manager")
        assert isinstance(staff, Staff)

    def test_if_staff_id_is_always_a_string(self):
        staff = Staff(1, "John", 30, 52000, "Manager")
        assert isinstance(staff.id, str)

    def test_customer_does_not_have_salary(self):
        customer = Customer(1, "Benjamin", 16)
        assert hasattr(customer, "salary") is False

    def test_getting_salary_matches_input_salary(self):
        staff = Staff(1, "John", 30, 52000, "Customer Service Representative")
        assert staff.get_salary() == staff.salary

    def test_accessing_manager_salary_raises_exception(self):
        staff = Staff(1, "John", 30, 52000, "Manager")
        self.assertRaises(PrivilegeException, staff.get_salary)