from unittest.mock import Mock

from easyssp_utils.client import ApiClient
from easyssp_utils.client.api_response import ApiResponse
from easyssp_utils.client.rest import RESTResponse
import pytest

from easyssp_simulation.client import SimulationClient
from easyssp_simulation.models import (
    Simulation,
    SimulationInfo,
    SimulationStarted,
    StartSimulationConfiguration,
)


@pytest.fixture
def mock_api_client():
    return Mock(spec=ApiClient)


@pytest.fixture
def simulation_client(mock_api_client):
    return SimulationClient(api_client=mock_api_client, username="test_user", password="test_pass")


# test list simulations
def test_get_simulation_successful(simulation_client, mock_api_client):
    mock_response = Mock(spec=RESTResponse)
    mock_response.data = Simulation(id="123", name="Test Simulation", runs=[])
    headers = {"Custom-Header": "HeaderValue"}
    mock_api_client.param_serialize.return_value = [None, None, headers, None, None]
    mock_api_client.response_deserialize.return_value = mock_response

    _request_timeout = (1.0, 2.0)
    simulation = simulation_client.get_simulation(simulation_id="123", _request_timeout=_request_timeout).data

    assert simulation.id == "123"
    assert simulation.name == "Test Simulation"
    mock_api_client.call_api.assert_called_once()
    args, kwargs = mock_api_client.call_api.call_args
    assert kwargs["_request_timeout"] == _request_timeout
    assert args[2] == {"Custom-Header": "HeaderValue"}
    mock_api_client.call_api.assert_called_once()


def test_get_simulations_successful(simulation_client, mock_api_client):
    mock_response = Mock()
    mock_response.data = [
        Simulation(id="123", name="Simulation One", runs=[]),
        Simulation(id="456", name="Simulation Two", runs=[]),
    ]
    headers = {"Custom-Header": "CustomValue"}
    mock_api_client.param_serialize.return_value = [None, None, headers, None, None]
    mock_api_client.response_deserialize.return_value = mock_response

    _request_timeout = (1.0, 2.0)
    simulations = simulation_client.get_simulations(_request_timeout=_request_timeout).data

    assert len(simulations) == 2
    assert simulations[0].id == "123"
    assert simulations[0].name == "Simulation One"
    assert simulations[1].id == "456"
    assert simulations[1].name == "Simulation Two"
    args, kwargs = mock_api_client.call_api.call_args
    assert kwargs["_request_timeout"] == _request_timeout
    assert args[2] == {"Custom-Header": "CustomValue"}
    mock_api_client.call_api.assert_called_once()


def test_get_simulation_not_found(simulation_client, mock_api_client):
    mock_api_client.call_api.side_effect = Exception("404 Not Found")
    mock_api_client.param_serialize.return_value = []

    with pytest.raises(Exception, match="404 Not Found"):
        simulation_client.get_simulation(simulation_id="invalid-id")


def test_get_simulations_empty(simulation_client, mock_api_client):
    mock_response = Mock()
    mock_response.data = []
    mock_api_client.response_deserialize.return_value = mock_response
    mock_api_client.param_serialize.return_value = []

    simulations = simulation_client.get_simulations().data

    assert len(simulations) == 0


# test delete simulations
def test_delete_simulation_successful(simulation_client, mock_api_client):
    mock_rest_response = Mock(spec=RESTResponse)
    mock_rest_response.data = None
    mock_api_response = Mock(spec=ApiResponse)
    mock_api_response.data = None
    mock_api_client.call_api.return_value = mock_rest_response
    mock_api_client.response_deserialize.return_value = mock_api_response
    mock_api_client.param_serialize.return_value = []

    simulation_client.delete_simulation(simulation_id="123")
    mock_api_client.call_api.assert_called_once()


def test_delete_simulation_not_found(simulation_client, mock_api_client):
    mock_api_client.call_api.side_effect = Exception("404 Not Found")
    mock_api_client.param_serialize.return_value = []

    with pytest.raises(Exception):
        simulation_client.delete_simulation(simulation_id="nonexistent_id")
    mock_api_client.call_api.assert_called_once()


def test_delete_simulation_run_success(simulation_client, mock_api_client):
    mock_rest_response = Mock(spec=RESTResponse)
    mock_rest_response.data = None
    mock_api_client.param_serialize.return_value = []

    mock_api_client.call_api.return_value = mock_rest_response
    simulation_client.delete_simulation_run(run_id="run_001")
    mock_api_client.call_api.assert_called_once()


def test_delete_simulation_run_not_found(simulation_client, mock_api_client):
    mock_api_client.call_api.side_effect = Exception("404 Not Found")
    mock_api_client.param_serialize.return_value = []

    with pytest.raises(Exception) as exc:
        simulation_client.delete_simulation_run(run_id="invalid_run_id")
    assert "404 Not Found" in str(exc.value)
    mock_api_client.call_api.assert_called_once()


# test get intermediate results
def test_get_simulation_result_sample_success(simulation_client, mock_api_client):
    mock_result = bytearray(b"sampled_simulation_result")
    mock_api_response = Mock(spec=ApiResponse)
    mock_api_response.data = mock_result
    mock_rest_response = Mock(spec=RESTResponse)
    mock_api_client.call_api.return_value = mock_rest_response
    mock_api_client.response_deserialize.return_value = mock_api_response
    mock_api_client.param_serialize.return_value = []

    _request_timeout = (1.0, 2.0)
    result = simulation_client.get_simulation_result_sample(run_id="valid_run_id",
                                                                                     _request_timeout=_request_timeout).data

    mock_api_client.call_api.assert_called_once()
    assert result == mock_result
    args, kwargs = mock_api_client.call_api.call_args
    assert kwargs["_request_timeout"] == _request_timeout
    mock_api_client.call_api.assert_called_once()


def test_get_simulation_result_sample_invalid_id(simulation_client, mock_api_client):
    mock_api_client.call_api.side_effect = RuntimeError("404 Not Found")
    mock_api_client.param_serialize.return_value = []

    with pytest.raises(RuntimeError, match="404 Not Found"):
        simulation_client.get_simulation_result_sample(run_id="invalid_run_id")

    mock_api_client.call_api.assert_called_once()


# test simulation info
def test_simulation_info_successful(simulation_client, mock_api_client):
    mock_simulation_info = Mock(spec=SimulationInfo)
    mock_api_response = Mock(spec=ApiResponse)
    mock_api_response.data = mock_simulation_info
    mock_rest_response = Mock(spec=RESTResponse)
    mock_api_client.call_api.return_value = mock_rest_response
    mock_api_client.response_deserialize.return_value = mock_api_response
    mock_api_client.param_serialize.return_value = []

    result = simulation_client.get_simulation_info().data

    mock_api_client.call_api.assert_called_once()
    assert result == mock_simulation_info

def test_simulation_info_failed_call(simulation_client, mock_api_client):
    mock_api_client.call_api.side_effect = Exception("API call failed")
    mock_api_client.param_serialize.return_value = []

    with pytest.raises(Exception, match="API call failed"):
        simulation_client.get_simulation_info()

    mock_api_client.call_api.assert_called_once()


# test get simulation log
def test_get_simulation_log_successful(simulation_client, mock_api_client):
    mock_bytearray = b"Simulation log data"
    mock_api_response = Mock(spec=ApiResponse)
    mock_api_response.data = mock_bytearray
    mock_rest_response = Mock(spec=RESTResponse)
    mock_api_client.call_api.return_value = mock_rest_response
    mock_api_client.response_deserialize.return_value = mock_api_response
    mock_api_client.param_serialize.return_value = []

    step_id = "12345"
    result = simulation_client.get_simulation_log(step_id=step_id).data

    mock_api_client.call_api.assert_called_once()
    assert result == mock_bytearray


def test_get_simulation_log_with_invalid_step_id(simulation_client, mock_api_client):
    mock_api_client.call_api.side_effect = Exception("404 Not Found")
    mock_api_client.param_serialize.return_value = []

    step_id = "invalid_step_id"
    with pytest.raises(Exception, match="404 Not Found"):
        simulation_client.get_simulation_log(step_id=step_id)
    mock_api_client.call_api.assert_called_once()


# test get simulation results
def test_get_simulation_result_successful(simulation_client, mock_api_client):
    mock_response_data = Mock(spec=bytearray)
    mock_api_response = Mock(spec=ApiResponse)
    mock_api_response.data = mock_response_data
    mock_rest_response = Mock(spec=RESTResponse)
    mock_api_client.call_api.return_value = mock_rest_response
    mock_api_client.response_deserialize.return_value = mock_api_response
    mock_api_client.param_serialize.return_value = []
    run_id = "test_run_id"

    result = simulation_client.get_simulation_result(run_id=run_id).data

    mock_api_client.call_api.assert_called_once()
    assert result == mock_response_data


def test_get_simulation_result_404_error(simulation_client, mock_api_client):
    mock_rest_response = Mock(spec=RESTResponse)
    mock_api_client.call_api.return_value = mock_rest_response
    mock_api_client.response_deserialize.side_effect = Exception("Not Found")
    mock_api_client.param_serialize.return_value = []
    run_id = "invalid_run_id"

    with pytest.raises(Exception, match="Not Found"):
        simulation_client.get_simulation_result(run_id=run_id)

    mock_api_client.call_api.assert_called_once()


# test start simulation
def test_start_simulation_successful(simulation_client, mock_api_client):
    mock_configuration = Mock(spec=StartSimulationConfiguration)
    mock_simulation_started = Mock(spec=SimulationStarted)
    mock_api_response = Mock(spec=ApiResponse)
    mock_api_response.data = mock_simulation_started
    mock_rest_response = Mock(spec=RESTResponse)
    mock_api_client.call_api.return_value = mock_rest_response
    mock_api_client.response_deserialize.return_value = mock_api_response
    mock_api_client.param_serialize.return_value = []

    result = simulation_client.start_simulation(
        configuration=mock_configuration,
        ssp_file=b"mock_ssp_file_data",
        stimuli_file=[b"stimuli_file_data_1", b"stimuli_file_data_2"]
    ).data

    mock_api_client.call_api.assert_called_once()
    assert result == mock_simulation_started


def test_start_simulation_invalid_response(simulation_client, mock_api_client):
    mock_configuration = Mock(spec=StartSimulationConfiguration)
    mock_api_client.call_api.return_value = None
    mock_api_client.param_serialize.return_value = []

    with pytest.raises(AttributeError):
        simulation_client.start_simulation(
            configuration=mock_configuration,
            ssp_file=b"mock_ssp_file_data"
        )

    mock_api_client.call_api.assert_called_once()


# test stop simulation
def test_stop_simulation_successful(simulation_client, mock_api_client):
    simulation_id = "test_simulation"
    mock_api_response = Mock(spec=ApiResponse)
    mock_api_response.data = "test data"
    mock_rest_response = Mock(spec=RESTResponse)
    mock_api_client.call_api.return_value = mock_rest_response
    mock_api_client.response_deserialize.return_value = mock_api_response
    mock_api_client.param_serialize.return_value = []

    _request_timeout = (5.0, 10.0)
    simulation_client.stop_simulation(simulation_id=simulation_id, _request_timeout=_request_timeout)

    mock_api_client.call_api.assert_called_once()
    args, kwargs = mock_api_client.call_api.call_args
    assert kwargs["_request_timeout"] == _request_timeout
    mock_api_client.call_api.assert_called_once()


def test_stop_simulation_not_found(simulation_client, mock_api_client):
    simulation_id = "invalid_id"
    mock_api_client.call_api.side_effect = Exception("404 Not Found")
    mock_api_client.param_serialize.return_value = []

    with pytest.raises(Exception) as exc_info:
        simulation_client.stop_simulation(simulation_id=simulation_id)

    mock_api_client.call_api.assert_called_once()
    assert "404" in str(exc_info.value)


def test_stop_simulation_run_successful(simulation_client, mock_api_client):
    run_id = "test_simulation_run"
    mock_api_response = Mock(spec=ApiResponse)
    mock_api_response.data = "test data"
    mock_rest_response = Mock(spec=RESTResponse)
    mock_api_client.call_api.return_value = mock_rest_response
    mock_api_client.response_deserialize.return_value = mock_api_response
    mock_api_client.param_serialize.return_value = []

    _request_timeout = (5.0, 10.0)
    simulation_client.stop_simulation_run(run_id=run_id, _request_timeout=_request_timeout)

    mock_api_client.call_api.assert_called_once()
    args, kwargs = mock_api_client.call_api.call_args
    assert kwargs["_request_timeout"] == _request_timeout
    mock_api_client.call_api.assert_called_once()


def test_stop_simulation_run_not_found(simulation_client, mock_api_client):
    run_id = "invalid_id"
    mock_api_client.call_api.side_effect = Exception("404 Not Found")
    mock_api_client.param_serialize.return_value = []

    with pytest.raises(Exception) as exc_info:
        simulation_client.stop_simulation_run(run_id=run_id)

    mock_api_client.call_api.assert_called_once()
    assert "404" in str(exc_info.value)
