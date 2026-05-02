from fastapi import APIRouter, Depends
from database.models.models import User, Expense
from database.models.using_models import ExpenseCreate, ExpenseRead, ExpenseUpdate
from securety import get_current_user
from sqlmodel import Session, select
from database.conection import get_session

router = APIRouter()


@router.get("/expenses/")
def get_expenses(current_user: User = Depends(get_current_user), session: Session = Depends(get_session)):
    statement = select(Expense).where(Expense.user_id == current_user.id)
    expenses = session.exec(statement).all()
    expenses = [ExpenseRead.from_orm(expense) for expense in expenses]
    return expenses


@router.post("/expenses/")
def create_expense(
    expense_in: ExpenseCreate,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    db_expense = Expense.model_validate(expense_in, update={"user_id": current_user.id})
    
    session.add(db_expense)
    session.commit()
    session.refresh(db_expense)
    
    return {
        "message": "Expense created successfully",
        "expense_id": db_expense.id
    }


@router.put("/expenses/{expense_id}")
def update_expense(
    expense_id: int,
    updated_expense: ExpenseUpdate,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    statement = select(Expense).where(Expense.id == expense_id, Expense.user_id == current_user.id)
    expense_item = session.exec(statement).first()
    if not expense_item:
        return {"error": "Expense not found"}
    
    if updated_expense.name is not None:
        expense_item.name = updated_expense.name
    if updated_expense.amount is not None:
        expense_item.amount = updated_expense.amount
    if updated_expense.category is not None:
        expense_item.category = updated_expense.category
    if updated_expense.date is not None:
        expense_item.date = updated_expense.date
    
    session.add(expense_item)
    session.commit()
    session.refresh(expense_item)
    
    return {
        "message": "Expense updated successfully",
        "expense_id": expense_item.id
    }


@router.delete("/expenses/{expense_id}")
def delete_expense(
    expense_id: int,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    statement = select(Expense).where(Expense.id == expense_id, Expense.user_id == current_user.id)
    expense_item = session.exec(statement).first()
    if not expense_item:
        return {"error": "Expense not found"}
    
    session.delete(expense_item)
    session.commit()
    
    return {
        "message": "Expense deleted successfully",
        "expense_id": expense_id
    }
