from fastapi.testclient import TestClient
import pytest

from app import main

client = TestClient(main)


def test_process_message():
    # Test valid message
    valid_message = {
        "customerId": 1,
        "type": "A",
        "amount": "0.012",
        "uuid": "a596b362-08be-419f-8070-9c3055566e7c"
    }
    response = client.post("/messages", json=valid_message)
    assert response.status_code == 200
    assert response.json() == {"message": "Message processed successfully"}

    # Test missing required field
    missing_field_message = {
        "customerId": 1,
        "type": "A",
        "amount": "0.012"
    }
    response = client.post("/messages", json=missing_field_message)
    assert response.status_code == 422


def test_get_stats():
    # Add sample messages to the database
    sample_messages = [
        {
            "customerId": 1,
            "type": "A",
            "amount": "0.012",
            "uuid": "a596b362-08be-419f-8070-9c3055566e7c"
        },
        {
            "customerId": 1,
            "type": "B",
            "amount": "0.01",
            "uuid": "b346aad6-7f67-4322-b012-eb5f1690bb47"
        },
        {
            "customerId": 2,
            "type": "A",
            "amount": "0.015",
            "uuid": "c5f9d2d2-9f02-4d5b-8f24-8be6c4493a1e"
        }
    ]
    client.post("/messages", json=sample_messages[0])
    client.post("/messages", json=sample_messages[1])
    client.post("/messages", json=sample_messages[2])

    response = client.get("/stats")
    assert response.status_code == 200
    assert response.json() == {
        "stats": [
            {
                "customerId": 1,
                "type": "A",
                "count": 1,
                "totalAmount": "0.012"
            },
            {
                "customerId": 1,
                "type": "B",
                "count": 1,
                "totalAmount": "0.01"
            },
            {
                "customerId": 2,
                "type": "A",
                "count": 1,
                "totalAmount": "0.015"
            }
        ]
    }


# Run tests with pytest
if __name__ == "__main__":
    pytest.main()
