from datetime import date
import pytest
from typing import Tuple

from model import Batch, OrderLine


class NoQuantityAvailable(Exception):
    pass


class TestQuantity:
    """Test allocation cases of products."""

    def make_batch_and_line(self, sku, batch_qty, line_qty) -> Tuple[Batch, OrderLine]:
        """Return Batch and OrderLine objects. 

        Args:
            sku       (str): name of product e.g. chair, lamp et.c
            batch_qty (int): max quantity in batch 
            line_qty  (int):  ordered quantity

        """
        return (
                Batch('batch-001', sku, batch_qty, eta=date.today()),
                OrderLine('order-123', sku, line_qty)
                )

    def test_greater_allocation(self):
        large_batch, small_line = self.make_batch_and_line("Lamp", 20, 2)
        assert large_batch.can_allocate(small_line)
        
    def test_allocation_if_available_smaller_than_required(self):
        small_batch, large_line = self.make_batch_and_line("Lamp", 2, 20)
        assert not small_batch.can_allocate(large_line)
        
    def test_allocation_if_available_equal_to_required(self):
        batch, line = self.make_batch_and_line("Lamp", 2, 2)
        assert batch.can_allocate(line)
        
    def test_allocation_if_skus_dont_match(self):
        batch = Batch('batch-001', 'Lamp', 20, eta = date.today())
        line = OrderLine("order123", "Not a lamp", 10)
        assert not batch.can_allocate(line)


    
