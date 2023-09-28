import pytest
from app import app, entries


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_add_entry_with_happiness(client):
    initial_entries_count = len(entries)
    content = "Test Entry Content"
    happiness = "😃"

    response = client.post(
        "/add_entry", data={"content": content, "happiness": happiness}
    )

    assert response.status_code == 302
    assert response.headers["Location"] == "/"

    entry = entries[0]
    assert entry is not None
    assert entry.content == "Test Entry Content"
    assert entry.happiness == "😃"
