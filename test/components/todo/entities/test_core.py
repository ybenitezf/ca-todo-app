from dataclasses import asdict
from datetime import date

from todo.entities import TodoItem


def test_can_instantiate_todo_item():
    todo_item = TodoItem(owner="Gordon", title="test", description="test")
    assert todo_item.owner == "Gordon"
    assert todo_item.title == "test"
    assert todo_item.description == "test"
    assert todo_item.is_done is False
    assert todo_item.due_date is None
    due = date(2021, 1, 1)
    todo_item = TodoItem(
        owner="Gordon", title="test", description="test", due_date=due
    )
    assert todo_item.due_date == due


def test_can_convert_todo_item_to_dict():
    due = date(2021, 1, 1)
    todo_item = TodoItem(
        owner="Gordon", title="test", description="test", due_date=due
    )
    assert asdict(todo_item) == {
        "owner": "Gordon",
        "title": "test",
        "description": "test",
        "is_done": False,
        "due_date": due,
    }
