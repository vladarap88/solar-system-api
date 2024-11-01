def test_get_all_planets_with_no_records(client):
    #Act
    response = client.get("/planets")
    response_body = response.get_json()

    #Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_one_planet_succeeds(client, two_saved_planets):
    response = client.get("planets/1")
    response_body= response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name":"Mercury",
        "description": "The smallest and closest planet to the Sun",
        "distance_from_sun": 36
    }

# def test_nonexistent_planet_return_404(client, two_saved_planets):
#     response = client.get("planets/1")
#     response_body= response.get_json()

#     assert response.status_code == 404


def test_create_one_planet_in_empty_db(client):
    response = client.post("/planets", json={
        "name":"Pluto",
        "description": "Previously our 9th planet, is now classified as a dwarf planet.",
        "distance_from_sun": 3700
    })
    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body == {
        "id": 1,
        "name":"Pluto",
        "description": "Previously our 9th planet, is now classified as a dwarf planet.",
        "distance_from_sun": 3700
    }