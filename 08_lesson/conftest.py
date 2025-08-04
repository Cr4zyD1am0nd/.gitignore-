import pytest
import uuid


@pytest.fixture
def random_project_name():
    return f"Test Project {uuid.uuid4()}"
