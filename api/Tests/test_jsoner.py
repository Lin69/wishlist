import sys
import os
sys.path.append(os.path.join(sys.path[0], '../'))
import json_handler
import pytest
def test_status400():
    response = {
        'status':400,
        'text':'Bad Request'
    }
    assert response == json_handler.jsoner(status=400)

def test_status403():
    response = {
        'status':403,
        'text':'Forbidden'
    }
    assert response == json_handler.jsoner(status=403)

def test_status200_noargs():
    response = {
        'status':200,
        'text':'OK'
    }
    assert response == json_handler.jsoner(status=200)

def test_func_noargs():
    
    with pytest.raises(KeyError):
        json_handler.jsoner()
