from kasm_python.kasm import Kasm


def test_can_initialise_kasm_instance():
    assert Kasm(url="https://localhost.com", api_key="abc", api_key_secret="abcd1234")


def test_can_initialise_kasm_without_protocol():
    kasm = Kasm(url="localhost.com", api_key="abc", api_key_secret="abcd1234")
    assert kasm.base_url == "https://localhost.com"
