from app.core.bus_tracking import find_best_bus
from app.adapters.bus_data.mock import MockBusDataProvider


def test_find_best_bus():
    provider = MockBusDataProvider()

    available_buses = [
        {
            "bus_number": "111",
            "source": "saravanampatti",
            "destination": "kct"
        }
    ]

    result = find_best_bus(
        available_buses,
        provider,
        11.0900,
        76.9950
    )

    assert result is not None
    assert result["bus_number"] == "111"
    assert result["eta_minutes"] >= 0


def test_no_live_bus():
    provider = MockBusDataProvider()

    available_buses = [
        {
            "bus_number": "999",
            "source": "saravanampatti",
            "destination": "kct"
        }
    ]

    result = find_best_bus(
        available_buses,
        provider,
        11.0900,
        76.9950
    )

    assert result is None


def test_empty_bus_list():
    provider = MockBusDataProvider()

    result = find_best_bus(
        [],
        provider,
        11.0900,
        76.9950
    )

    assert result is None


def test_api_find_bus():
    from app.main import app

    client = app.test_client()

    response = client.post(
        "/api/find-bus",
        json={
            "source": "saravanampatti",
            "destination": "kumaraguru"
        }
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "success"
    assert data["bus"]["bus_number"] == "111"
    assert data["bus"]["eta_minutes"] >= 0


def test_api_invalid_source():
    from app.main import app

    client = app.test_client()

    response = client.post(
        "/api/find-bus",
        json={
            "source": "unknown place xyz",
            "destination": "kumaraguru"
        }
    )

    assert response.status_code == 400

    data = response.get_json()

    assert data["status"] == "error"
    assert data["message"] == "Source location not recognized"


def test_api_missing_input():
    from app.main import app

    client = app.test_client()

    response = client.post(
        "/api/find-bus",
        json={
            "source": "saravanampatti"
        }
    )

    assert response.status_code == 400

    data = response.get_json()

    assert data["status"] == "error"
    assert data["message"] == "Source and destination are required"


def test_api_tamil():
    from app.main import app

    client = app.test_client()

    response = client.post(
        "/api/find-bus",
        json={
            "language": "2",
            "source": "saravanampatti",
            "destination": "kumaraguru"
        }
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "success"
    assert data["language"] == "ta"
    assert data["bus"]["bus_number"] == "111"


def test_api_hindi():
    from app.main import app

    client = app.test_client()

    response = client.post(
        "/api/find-bus",
        json={
            "language": "3",
            "source": "saravanampatti",
            "destination": "kumaraguru"
        }
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "success"
    assert data["language"] == "hi"
    assert data["bus"]["bus_number"] == "111"


def test_api_invalid_language():
    from app.main import app

    client = app.test_client()

    response = client.post(
        "/api/find-bus",
        json={
            "language": "5",
            "source": "saravanampatti",
            "destination": "kumaraguru"
        }
    )

    assert response.status_code == 400

    data = response.get_json()

    assert data["status"] == "error"


def test_api_invalid_source():
    from app.main import app

    client = app.test_client()

    response = client.post(
        "/api/find-bus",
        json={
            "language": "1",
            "source": "unknownplace",
            "destination": "kumaraguru"
        }
    )

    assert response.status_code == 400

    data = response.get_json()

    assert data["status"] == "error"


def test_api_invalid_destination():
    from app.main import app

    client = app.test_client()

    response = client.post(
        "/api/find-bus",
        json={
            "language": "1",
            "source": "saravanampatti",
            "destination": "unknownplace"
        }
    )

    assert response.status_code == 400

    data = response.get_json()

    assert data["status"] == "error"

def test_conversation_api():
    from app.main import app

    client = app.test_client()

    response = client.post(
        "/api/conversation",
        json={
            "language": "1",
            "source": "saravanampatti",
            "destination": "kumaraguru"
        }
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "success"
    assert data["language"] == "en"
    assert data["source"] == "Saravanampatti"
    assert data["destination"] == "Kumaraguru College of Technology"
    assert data["bus_number"] == "111"
    assert data["eta_minutes"] >= 0


def test_conversation_api_tamil():
    from app.main import app

    client = app.test_client()

    response = client.post(
        "/api/conversation",
        json={
            "language": "2",
            "source": "saravanampatti",
            "destination": "kumaraguru"
        }
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "success"
    assert data["language"] == "ta"


def test_conversation_api_hindi():
    from app.main import app

    client = app.test_client()

    response = client.post(
        "/api/conversation",
        json={
            "language": "3",
            "source": "saravanampatti",
            "destination": "kumaraguru"
        }
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "success"
    assert data["language"] == "hi"