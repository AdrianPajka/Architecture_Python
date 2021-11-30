import pytest


class NoQuantityAvailable(Exception):
    pass


class TestQuantity:
    """Test allocation cases of products."""

    def availability(self, ordered: int, available: int):
        left = available - ordered
        if left > 0:
            return left
        else:
            raise NoQuantityAvailable

    def test_available_products(self):
        assert self.availability(2, 20) == 18

    def test_not_enough_products(self):
        with pytest.raises(NoQuantityAvailable):
            assert self.availability(ordered=5, available=2)
            
