from unittest import mock
from frakkcomm.ejjelifeny import Ejjelifeny

class TestFrakkComm:

    def test_program_running(self, mocker, monkeypatch):

        ejjelifeny = Ejjelifeny("127.0.0.1", 8023, 1, "feny1", 0, 255)

        # TODO: replace this with mocker
        monkeypatch.setattr(ejjelifeny, "TCPSendData", lambda message: None)

        control_light = ejjelifeny.controlLight({"blue": True, "white": True}, 100, 1)
        ejjelifeny.turnOffLight()
        ejjelifeny.turnOnBlueLight(50)
        ejjelifeny.turnOnWhiteLight(50)

        assert control_light

    def test_blue_color_turns_on(self, mocker, monkeypatch):

        ejjelifeny = Ejjelifeny("127.0.0.1", 8023, 1, "feny1", 0, 255)

        # TODO: replace this with mocker
        monkeypatch.setattr(ejjelifeny, "TCPSendData", lambda message: None)

        control_light = ejjelifeny.controlLight({"blue": True, "white": False}, 100, 1)
        assert control_light == "5509ff00f45601816472"

        # TODO: finish tests
