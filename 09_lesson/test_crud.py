import pytest
from sqlalchemy.orm import Session
from models import Student
from config import get_db, Base, engine


@pytest.fixture(scope="function")
def db_session():
    Base.metadata.create_all(bind=engine)
    db = next(get_db())

    try:
        yield db
    finally:
        db.rollback()
        Base.metadata.drop_all(bind=engine)
        db.close()


def test_create_student(db_session: Session):
    """Тест на создание студента."""
    student = Student(name="Иван Иванов", email="ivan@example.com")
    db_session.add(student)
    db_session.commit()
    db_session.refresh(student)

    assert student.id is not None
    assert student.name == "Иван Иванов"
    assert student.email == "ivan@example.com"
    assert student.is_deleted is False


def test_update_student(db_session: Session):
    """Тест на обновление студента."""
    student = Student(name="Петр Петров", email="petr@example.com")
    db_session.add(student)
    db_session.commit()
    db_session.refresh(student)

    student.name = "Петр Сидоров"
    student.email = "sidorov@example.com"
    db_session.commit()
    db_session.refresh(student)

    assert student.name == "Петр Сидоров"
    assert student.email == "sidorov@example.com"


def test_soft_delete_student(db_session: Session):
    """Тест на мягкое удаление студента."""
    student = Student(name="Анна Сергеева", email="anna@example.com")
    db_session.add(student)
    db_session.commit()
    db_session.refresh(student)

    student.is_deleted = True
    db_session.commit()
    db_session.refresh(student)

    assert student.is_deleted is True
    student_in_db = db_session.query(Student).filter(
        Student.id == student.id
    ).first()
    assert student_in_db is not None
    assert student_in_db.is_deleted is True
