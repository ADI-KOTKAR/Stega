def test_index(app, client):
    del app
    res = client.get('/working')
    assert res.status_code == 200
    print(res)