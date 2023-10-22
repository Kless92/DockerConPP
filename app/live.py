from flask import url_for
import pytest

@pytest.mark.usefixtures('live_server')
class TestLiveServer:
    def test_server_is_up(self):
        res = urllib2.urlopen(url_for('index', _external=True))
        assert b'OK' in res.read()
        assert res.code == 200