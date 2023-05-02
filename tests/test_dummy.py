"""Test dummy"""

from fastapi.testclient import TestClient
import dummy


def test_addition():
    """
    Test dummy::addition
    """
    assert dummy.addition(1, 2) == 3


client = TestClient(dummy.app)


def test_get_device():
    """
    test get devices
    """
    response = client.get("/devices")
    print("guu8hc::guu8hc", response.json)
    assert response.status_code == 200
    assert response.json() == ["device_01","device_02","device_03"]


def test_get_pc_by_id():
    """
    test get pc by id
    """
    pcid = 'PC02'
    response = client.get(f"pcs/{pcid}")
    print("guu8hc::", response.json)
    assert response.status_code == 200
    assert response.json() == 'HP002'
