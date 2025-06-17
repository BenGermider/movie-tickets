
from pydantic import BaseModel, Field

class PaymentMethod(BaseModel):
    card_number: str = Field(..., example="53261234567891011121")
    cvc: str = Field(..., example="123")
    expiration_date: str = Field(..., example="12/33")
    id: str

class Reservation(BaseModel):
    email: str = Field(..., example="hello@gmail.com")
    payment_method: PaymentMethod
