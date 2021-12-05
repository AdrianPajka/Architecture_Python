from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass(frozen=True)
class OrderLine:
    """ Representation of single order
    
    Args: 
    
    order_id : id of order
    sku      : stock-keeping-unit
    qty      : quantity 
    
    """
    order_id: str
    sku: str
    qty: int


@dataclass
class Batch:
    ref: str
    sku: str
    available_quantity: int
    eta: Optional[date]

    def allocate(self, line: OrderLine):
        self.available_quantity -= line.qty
    
    def can_allocate(self, line: OrderLine) -> bool:
        return self.sku == line.sku and self.available_quantity >= line.qty
        
        


