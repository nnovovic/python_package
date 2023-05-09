import os

from python_package import __version__


def test_shell(client):
    r = client.get('/shell')
    assert r.json and r.json['error']

    r = client.get('/shell?command=echo 1')
    assert r.json and not r.json['error'] and r.json['stdout'] == f'1{os.linesep}'

    r = client.post('/shell')
    assert r.json and r.json['error']

    r = client.post('/shell', data={'command': 'echo 1'})
    assert r.json and not r.json['error'] and r.json['stdout'] == f'1{os.linesep}'

    r = client.post('/shell', data='{}', headers={'Content-Type': 'application/json'})
    assert r.json and r.json['error']

    r = client.post('/shell', data='{"command": "echo 1"}', headers={'Content-Type': 'application/json'})
    assert r.json and not r.json['error'] and r.json['stdout'] == f'1{os.linesep}'


def test_info(client):
    r = client.get('/info')

    assert r.is_json and r.json['version'] == __version__
