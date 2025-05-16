from typing import Annotated, Any

from easyssp_utils.client import ApiClient, ApiResponse
from easyssp_utils.client.api_client import RequestSerialized
from pydantic import Field, StrictBytes, StrictFloat, StrictInt, StrictStr, validate_call

from easyssp_simulation import models
from easyssp_simulation.models import (
    Simulation,
    SimulationInfo,
    SimulationStarted,
    StartSimulationConfiguration,
)


class SimulationClient:

    def __init__(self, username: str, password: str, api_client=None, user_agent=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default(username=username, password=password, client_id="simulation-api", user_agent=user_agent)
        self.api_client = api_client

    # list simulations
    @validate_call
    def get_simulation(
            self,
            simulation_id: Annotated[
                StrictStr, Field(description="The id of the simulation started with the Simulation-API.")],
            _request_timeout: None | Annotated[StrictFloat, Field(gt=0)] | tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]] = None,
            _request_auth: dict[StrictStr, Any] | None = None,
            _content_type: StrictStr | None = None,
            _headers: dict[StrictStr, Any] | None = None,
            _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[Simulation]:
        """Request the simulation with the given id.

        Returns a general overview of the simulation with the given id. Gives insight to the configuration and status for each run and for each simulation step inside the runs. Also includes the ids of runs and steps to make further requests.

        :param simulation_id: The id of the simulation started with the Simulation-API. (required)
        :type simulation_id: str
        :param _request_timeout: timeout setting for this request. If one
                                  number is provided, it will be a total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """

        _param = self._get_simulation_serialize(
            simulation_id=simulation_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: dict[str, str | None] = {
            "200": "Simulation",
            "404": "LocalizedErrorMessage",
            "500": "ErrorMessage",
            "401": "ErrorMessage",
            "403": "ErrorMessage",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
            custom_models=models
        )

    def _get_simulation_serialize(
            self,
            simulation_id,
            _request_auth,
            _content_type,
            _headers,
            _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: dict[str, str] = {
        }

        _path_params: dict[str, str] = {}
        _query_params: list[tuple[str, str]] = []
        _header_params: dict[str, str | None] = _headers or {}
        _form_params: list[tuple[str, str]] = []
        _files: dict[
            str, str | bytes | list[str] | list[bytes] | list[tuple[str, bytes]]
        ] = {}
        _body_params: bytes | None = None

        # process the path parameters
        if simulation_id is not None:
            _path_params["simulationId"] = simulation_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter

        # set the HTTP header `Accept`
        if "Accept" not in _header_params:
            _header_params["Accept"] = self.api_client.select_header_accept(
                [
                    "application/json"
                ]
            )

        # authentication setting
        _auth_settings: list[str] = [
        ]

        return self.api_client.param_serialize(
            method="GET",
            resource_path="/integration/api/v1/simulation/{simulationId}",
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )

    @validate_call
    def get_simulations(
            self,
            _request_timeout: None | Annotated[StrictFloat, Field(gt=0)] | tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]] = None,
            _request_auth: dict[StrictStr, Any] | None = None,
            _content_type: StrictStr | None = None,
            _headers: dict[StrictStr, Any] | None = None,
            _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[list[Simulation]]:
        """Request all available simulations.

        Returns all simulations of the current user. Gives insight to the configuration and status for each run and for each simulation step inside the runs. Also includes the ids of runs and steps to make further requests.

        :param _request_timeout: timeout setting for this request. If one
                                  number is provided, it will be a total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """

        _param = self._get_simulations_serialize(
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: dict[str, str | None] = {
            "200": "List[Simulation]",
            "500": "ErrorMessage",
            "401": "ErrorMessage",
            "403": "ErrorMessage",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
            custom_models=models
        )

    def _get_simulations_serialize(
            self,
            _request_auth,
            _content_type,
            _headers,
            _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: dict[str, str] = {
        }

        _path_params: dict[str, str] = {}
        _query_params: list[tuple[str, str]] = []
        _header_params: dict[str, str | None] = _headers or {}
        _form_params: list[tuple[str, str]] = []
        _files: dict[
            str, str | bytes | list[str] | list[bytes] | list[tuple[str, bytes]]
        ] = {}
        _body_params: bytes | None = None

        # process the path parameters
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter

        # set the HTTP header `Accept`
        if "Accept" not in _header_params:
            _header_params["Accept"] = self.api_client.select_header_accept(
                [
                    "application/json"
                ]
            )

        # authentication setting
        _auth_settings: list[str] = [
        ]

        return self.api_client.param_serialize(
            method="GET",
            resource_path="/integration/api/v1/simulation",
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )

    # delete simulation
    @validate_call
    def delete_simulation(
            self,
            simulation_id: Annotated[
                StrictStr, Field(description="The id of the simulation started with the Simulation-API.")],
            _request_timeout: None | Annotated[StrictFloat, Field(gt=0)] | tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]] = None,
            _request_auth: dict[StrictStr, Any] | None = None,
            _content_type: StrictStr | None = None,
            _headers: dict[StrictStr, Any] | None = None,
            _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Deletes the given simulation.

        Deletes the simulation with the given id and all its runs with all associated data (Logs, Results, Configuration, Status). A simulation can only be deleted if all simulation runs are finished (done, time_out, stopped or error state).

        :param simulation_id: The id of the simulation started with the Simulation-API. (required)
        :type simulation_id: str
        :param _request_timeout: timeout setting for this request. If one
                                  number is provided, it will be a total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """

        _param = self._delete_simulation_serialize(
            simulation_id=simulation_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: dict[str, str | None] = {
            "204": None,
            "400": "LocalizedErrorMessage",
            "404": "LocalizedErrorMessage",
            "500": "ErrorMessage",
            "401": "ErrorMessage",
            "403": "ErrorMessage",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
            custom_models=models
        )

    def _delete_simulation_serialize(
            self,
            simulation_id,
            _request_auth,
            _content_type,
            _headers,
            _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: dict[str, str] = {
        }

        _path_params: dict[str, str] = {}
        _query_params: list[tuple[str, str]] = []
        _header_params: dict[str, str | None] = _headers or {}
        _form_params: list[tuple[str, str]] = []
        _files: dict[
            str, str | bytes | list[str] | list[bytes] | list[tuple[str, bytes]]
        ] = {}
        _body_params: bytes | None = None

        # process the path parameters
        if simulation_id is not None:
            _path_params["simulationId"] = simulation_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter

        # set the HTTP header `Accept`
        if "Accept" not in _header_params:
            _header_params["Accept"] = self.api_client.select_header_accept(
                [
                    "application/json"
                ]
            )

        # authentication setting
        _auth_settings: list[str] = [
        ]

        return self.api_client.param_serialize(
            method="DELETE",
            resource_path="/integration/api/v1/simulation/{simulationId}",
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )

    @validate_call
    def delete_simulation_run(
            self,
            run_id: Annotated[StrictStr, Field(description="The id of the simulation run.")],
            _request_timeout: None | Annotated[StrictFloat, Field(gt=0)] | tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]] = None,
            _request_auth: dict[StrictStr, Any] | None = None,
            _content_type: StrictStr | None = None,
            _headers: dict[StrictStr, Any] | None = None,
            _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Deletes the given simulation run.

        Deletes the simulation run with the given id with all associated data (Logs, Results, Configuration, Status). If the simulation run was the only run in the simulation, the simulation is deleted as well. A simulation run can only be deleted if the run is finished (done, time_out, stopped or error state).

        :param run_id: The id of the simulation run. (required)
        :type run_id: str
        :param _request_timeout: timeout setting for this request. If one
                                  number is provided, it will be a total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """

        _param = self._delete_simulation_run_serialize(
            run_id=run_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: dict[str, str | None] = {
            "204": None,
            "400": "LocalizedErrorMessage",
            "404": "LocalizedErrorMessage",
            "500": "ErrorMessage",
            "401": "ErrorMessage",
            "403": "ErrorMessage",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
            custom_models=models
        )

    def _delete_simulation_run_serialize(
            self,
            run_id,
            _request_auth,
            _content_type,
            _headers,
            _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: dict[str, str] = {
        }

        _path_params: dict[str, str] = {}
        _query_params: list[tuple[str, str]] = []
        _header_params: dict[str, str | None] = _headers or {}
        _form_params: list[tuple[str, str]] = []
        _files: dict[
            str, str | bytes | list[str] | list[bytes] | list[tuple[str, bytes]]
        ] = {}
        _body_params: bytes | None = None

        # process the path parameters
        if run_id is not None:
            _path_params["runId"] = run_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter

        # set the HTTP header `Accept`
        if "Accept" not in _header_params:
            _header_params["Accept"] = self.api_client.select_header_accept(
                [
                    "application/json"
                ]
            )

        # authentication setting
        _auth_settings: list[str] = [
        ]

        return self.api_client.param_serialize(
            method="DELETE",
            resource_path="/integration/api/v1/simulation/run/{runId}",
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )

    # get intermediate simulation results
    @validate_call
    def get_simulation_result_sample(
            self,
            run_id: Annotated[StrictStr, Field(description="The id of the simulation run.")],
            _request_timeout: None | Annotated[StrictFloat, Field(gt=0)] | tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]] = None,
            _request_auth: dict[StrictStr, Any] | None = None,
            _content_type: StrictStr | None = None,
            _headers: dict[StrictStr, Any] | None = None,
            _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[bytearray]:
        """Request the sampled results of a simulation run.

        Delivers the results of a simulation run with the given id in a reduced size. Can be used to fetch the current results during a ***running*** simulation, or to get a reduced preview of the results for performance purposes. The sample size is limited to 10000 data points. Each data point is evenly distributed across all currently simulated data points, representing a sup sampling of the actual results.

        :param run_id: The id of the simulation run. (required)
        :type run_id: str
        :param _request_timeout: timeout setting for this request. If one
                                  number is provided, it will be a total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """

        _param = self._get_simulation_result_sample_serialize(
            run_id=run_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: dict[str, str | None] = {
            "200": "bytearray",
            "404": "LocalizedErrorMessage",
            "500": "ErrorMessage",
            "401": "ErrorMessage",
            "403": "ErrorMessage",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
            custom_models=models
        )

    def _get_simulation_result_sample_serialize(
            self,
            run_id,
            _request_auth,
            _content_type,
            _headers,
            _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: dict[str, str] = {
        }

        _path_params: dict[str, str] = {}
        _query_params: list[tuple[str, str]] = []
        _header_params: dict[str, str | None] = _headers or {}
        _form_params: list[tuple[str, str]] = []
        _files: dict[
            str, str | bytes | list[str] | list[bytes] | list[tuple[str, bytes]]
        ] = {}
        _body_params: bytes | None = None

        # process the path parameters
        if run_id is not None:
            _path_params["runId"] = run_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter

        # set the HTTP header `Accept`
        if "Accept" not in _header_params:
            _header_params["Accept"] = self.api_client.select_header_accept(
                [
                    "text/csv"
                ]
            )

        # authentication setting
        _auth_settings: list[str] = [
        ]

        return self.api_client.param_serialize(
            method="GET",
            resource_path="/integration/api/v1/simulation/run/{runId}/result/sample",
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )

    # get simulation info
    @validate_call
    def get_simulation_info(
            self,
            _request_timeout: None | Annotated[StrictFloat, Field(gt=0)] | tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]] = None,
            _request_auth: dict[StrictStr, Any] | None = None,
            _content_type: StrictStr | None = None,
            _headers: dict[StrictStr, Any] | None = None,
            _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[SimulationInfo]:
        """Receive Available Credits and Simulation Options.

        Returns various general information required to interact with this API: - A list of currently available hardware configurations, with their identifier, credit cost per minute and actually hardware sizes - A list of available target execution platforms to run the simulation in. - The current credit amount the user has. - The general fix costs of a simulation.

        :param _request_timeout: timeout setting for this request. If one
                                  number is provided, it will be a total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """

        _param = self._simulation_info_serialize(
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: dict[str, str | None] = {
            "200": "SimulationInfo",
            "500": "ErrorMessage",
            "401": "ErrorMessage",
            "403": "ErrorMessage",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
            custom_models=models
        )

    def _simulation_info_serialize(
            self,
            _request_auth,
            _content_type,
            _headers,
            _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: dict[str, str] = {
        }

        _path_params: dict[str, str] = {}
        _query_params: list[tuple[str, str]] = []
        _header_params: dict[str, str | None] = _headers or {}
        _form_params: list[tuple[str, str]] = []
        _files: dict[
            str, str | bytes | list[str] | list[bytes] | list[tuple[str, bytes]]
        ] = {}
        _body_params: bytes | None = None

        # process the path parameters
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter

        # set the HTTP header `Accept`
        if "Accept" not in _header_params:
            _header_params["Accept"] = self.api_client.select_header_accept(
                [
                    "application/json"
                ]
            )

        # authentication setting
        _auth_settings: list[str] = [
        ]

        return self.api_client.param_serialize(
            method="GET",
            resource_path="/integration/api/v1/simulation/info",
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )

    # get simulation log
    @validate_call
    def get_simulation_log(
            self,
            step_id: Annotated[StrictStr, Field(description="The id of the simulation step.")],
            _request_timeout: None | Annotated[StrictFloat, Field(gt=0)] | tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]] = None,
            _request_auth: dict[StrictStr, Any] | None = None,
            _content_type: StrictStr | None = None,
            _headers: dict[StrictStr, Any] | None = None,
            _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[bytearray]:
        """Request the log of a simulation step.

        Delivers the simulation log output created by the step.

        :param step_id: The id of the simulation step. (required)
        :type step_id: str
        :param _request_timeout: timeout setting for this request. If one
                                  number is provided, it will be a total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """

        _param = self._get_simulation_log_serialize(
            step_id=step_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: dict[str, str | None] = {
            "200": "bytearray",
            "404": "LocalizedErrorMessage",
            "500": "ErrorMessage",
            "401": "ErrorMessage",
            "403": "ErrorMessage",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
            custom_models=models
        )

    def _get_simulation_log_serialize(
            self,
            step_id,
            _request_auth,
            _content_type,
            _headers,
            _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: dict[str, str] = {
        }

        _path_params: dict[str, str] = {}
        _query_params: list[tuple[str, str]] = []
        _header_params: dict[str, str | None] = _headers or {}
        _form_params: list[tuple[str, str]] = []
        _files: dict[
            str, str | bytes | list[str] | list[bytes] | list[tuple[str, bytes]]
        ] = {}
        _body_params: bytes | None = None

        # process the path parameters
        if step_id is not None:
            _path_params["stepId"] = step_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter

        # set the HTTP header `Accept`
        if "Accept" not in _header_params:
            _header_params["Accept"] = self.api_client.select_header_accept(
                [
                    "text/plain"
                ]
            )

        # authentication setting
        _auth_settings: list[str] = [
        ]

        return self.api_client.param_serialize(
            method="GET",
            resource_path="/integration/api/v1/simulation/step/{stepId}/log",
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )

    # get simulation results
    @validate_call
    def get_simulation_result(
            self,
            run_id: Annotated[StrictStr, Field(description="The id of the simulation run.")],
            _request_timeout: None | Annotated[StrictFloat, Field(gt=0)] | tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]] = None,
            _request_auth: dict[StrictStr, Any] | None = None,
            _content_type: StrictStr | None = None,
            _headers: dict[StrictStr, Any] | None = None,
            _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[bytearray]:
        """Request the results of a simulation run.

        Delivers the final results of a ***finished*** simulation run with the given id. The results can only be requested once the simulation is finished and will have the full resolution of all data points.

        :param run_id: The id of the simulation run. (required)
        :type run_id: str
        :param _request_timeout: timeout setting for this request. If one
                                  number is provided, it will be a total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """

        _param = self._get_simulation_result_serialize(
            run_id=run_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: dict[str, str | None] = {
            "200": "bytearray",
            "404": "LocalizedErrorMessage",
            "500": "ErrorMessage",
            "401": "ErrorMessage",
            "403": "ErrorMessage",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
            custom_models=models
        )

    def _get_simulation_result_serialize(
            self,
            run_id,
            _request_auth,
            _content_type,
            _headers,
            _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: dict[str, str] = {
        }

        _path_params: dict[str, str] = {}
        _query_params: list[tuple[str, str]] = []
        _header_params: dict[str, str | None] = _headers or {}
        _form_params: list[tuple[str, str]] = []
        _files: dict[
            str, str | bytes | list[str] | list[bytes] | list[tuple[str, bytes]]
        ] = {}
        _body_params: bytes | None = None

        # process the path parameters
        if run_id is not None:
            _path_params["runId"] = run_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter

        # set the HTTP header `Accept`
        if "Accept" not in _header_params:
            _header_params["Accept"] = self.api_client.select_header_accept(
                [
                    "text/csv"
                ]
            )

        # authentication setting
        _auth_settings: list[str] = [
        ]

        return self.api_client.param_serialize(
            method="GET",
            resource_path="/integration/api/v1/simulation/run/{runId}/result",
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )

    # start simulation
    @validate_call
    def start_simulation(
            self,
            configuration: StartSimulationConfiguration,
            ssp_file: Annotated[StrictBytes | StrictStr | tuple[StrictStr, StrictBytes], Field(
                description="The ssp file to simulate.")],
            stimuli_file: Annotated[list[StrictBytes | StrictStr | tuple[StrictStr, StrictBytes]] | None, Field(
                description="Optional Stimuli-Files to be used by the defined simulation runs. Each stimuli Needs to be referenced by a run.")] = None,
            _request_timeout: None | Annotated[StrictFloat, Field(gt=0)] | tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]] = None,
            _request_auth: dict[StrictStr, Any] | None = None,
            _content_type: StrictStr | None = None,
            _headers: dict[StrictStr, Any] | None = None,
            _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[SimulationStarted]:
        """Starts a simulation for a given SSP.

        Starts a simulation for the given .ssp-file with included FMI 2.0 components. The request is a Multipart-Upload with the following components:
            - configuration: A Json-Object specifying the configuration of the simulation
            - ssp: The .ssp-file to simulate with.
            - stimuli: Optional, any number of .csv-files to stimulate the different runs with. Files that are not referenced in a run will be ignored.  When successful, the API returns the status model for the created simulation, the remaining credits of the user and a URL that can be used to open the simulation view of easySSP. Note that we do not validate the given ssp files nor the stimuli beforehand.

        :param configuration: (required)
        :type configuration: StartSimulationConfiguration
        :param ssp_file: The ssp file to simulate. (required)
        :type ssp_file: bytearray
        :param stimuli_file: Optional Stimuli-Files to be used by the defined simulation runs. Each stimulus Needs to be referenced by a run.
        :type stimuli_file: List[bytearray]
        :param _request_timeout: timeout setting for this request. If one
                                  number is provided, it will be a total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """

        _param = self._start_simulation_serialize(
            configuration=configuration,
            ssp_file=ssp_file,
            stimuli_file=stimuli_file,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: dict[str, str | None] = {
            "200": "SimulationStarted",
            "400": "LocalizedErrorMessage",
            "500": "ErrorMessage",
            "401": "ErrorMessage",
            "417": "LocalizedErrorMessage",
            "403": "ErrorMessage",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
            custom_models=models
        )

    def _start_simulation_serialize(
            self,
            configuration,
            ssp_file,
            stimuli_file,
            _request_auth,
            _content_type,
            _headers,
            _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: dict[str, str] = {
            "stimuli": "multi",
            "configuration": "application/json",
            "ssp": "application/x-ssp-package"
        }

        _path_params: dict[str, str] = {}
        _query_params: list[tuple[str, str]] = []
        _header_params: dict[str, str | None] = _headers or {}
        _form_params: list[tuple[str, str]] = []
        _files: dict[
            str, str | bytes | list[str] | list[bytes] | list[tuple[str, bytes]]
        ] = {}
        _body_params: bytes | None = None

        # process the path parameters
        # process the query parameters
        # process the header parameters
        # process the form parameters
        if configuration is not None:
            _form_params.append(("configuration", configuration.to_json()))
        if ssp_file is not None:
            _files["ssp"] = ssp_file
        if stimuli_file is not None:
            _files["stimuli"] = stimuli_file
        # process the body parameter

        # set the HTTP header `Accept`
        if "Accept" not in _header_params:
            _header_params["Accept"] = self.api_client.select_header_accept(
                [
                    "application/json"
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params["Content-Type"] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        "multipart/form-data"
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params["Content-Type"] = _default_content_type

        # authentication setting
        _auth_settings: list[str] = [
        ]

        return self.api_client.param_serialize(
            method="POST",
            resource_path="/integration/api/v1/simulation",
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )

    # stop simulation run
    @validate_call
    def stop_simulation(
            self,
            simulation_id: Annotated[
                StrictStr, Field(description="The id of the simulation started with the Simulation-API.")],
            _request_timeout: None | Annotated[StrictFloat, Field(gt=0)] | tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]] = None,
            _request_auth: dict[StrictStr, Any] | None = None,
            _content_type: StrictStr | None = None,
            _headers: dict[StrictStr, Any] | None = None,
            _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Stops the given simulation.

        Requests to stop the simulation with the given id by setting all its runs to a stop_pending state. It may take a while for the infrastructure to react and actually stop the simulations.

        :param simulation_id: The id of the simulation started with the Simulation-API. (required)
        :type simulation_id: str
        :param _request_timeout: timeout setting for this request. If one
                                  number is provided, it will be a total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """

        _param = self._stop_simulation_serialize(
            simulation_id=simulation_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: dict[str, str | None] = {
            "204": None,
            "404": "LocalizedErrorMessage",
            "500": "ErrorMessage",
            "401": "ErrorMessage",
            "403": "ErrorMessage",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
            custom_models=models
        )

    def _stop_simulation_serialize(
            self,
            simulation_id,
            _request_auth,
            _content_type,
            _headers,
            _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: dict[str, str] = {
        }

        _path_params: dict[str, str] = {}
        _query_params: list[tuple[str, str]] = []
        _header_params: dict[str, str | None] = _headers or {}
        _form_params: list[tuple[str, str]] = []
        _files: dict[
            str, str | bytes | list[str] | list[bytes] | list[tuple[str, bytes]]
        ] = {}
        _body_params: bytes | None = None

        # process the path parameters
        if simulation_id is not None:
            _path_params["simulationId"] = simulation_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter

        # set the HTTP header `Accept`
        if "Accept" not in _header_params:
            _header_params["Accept"] = self.api_client.select_header_accept(
                [
                    "application/json"
                ]
            )

        # authentication setting
        _auth_settings: list[str] = [
        ]

        return self.api_client.param_serialize(
            method="POST",
            resource_path="/integration/api/v1/simulation/{simulationId}/stop",
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )

    @validate_call
    def stop_simulation_run(
            self,
            run_id: Annotated[StrictStr, Field(description="The id of the simulation run.")],
            _request_timeout: None | Annotated[StrictFloat, Field(gt=0)] | tuple[
                Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]] = None,
            _request_auth: dict[StrictStr, Any] | None = None,
            _content_type: StrictStr | None = None,
            _headers: dict[StrictStr, Any] | None = None,
            _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Stops the given simulation run.

        Requests to stop the simulation run with the given id. The run status will change to stop_pending.It may take a while for the infrastructure to react.

        :param run_id: The id of the simulation run. (required)
        :type run_id: str
        :param _request_timeout: timeout setting for this request. If one
                                  number is provided, it will be a total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """

        _param = self._stop_simulation_run_serialize(
            run_id=run_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: dict[str, str | None] = {
            "204": None,
            "404": "LocalizedErrorMessage",
            "500": "ErrorMessage",
            "401": "ErrorMessage",
            "403": "ErrorMessage",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
            custom_models=models
        )

    def _stop_simulation_run_serialize(
            self,
            run_id,
            _request_auth,
            _content_type,
            _headers,
            _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: dict[str, str] = {
        }

        _path_params: dict[str, str] = {}
        _query_params: list[tuple[str, str]] = []
        _header_params: dict[str, str | None] = _headers or {}
        _form_params: list[tuple[str, str]] = []
        _files: dict[
            str, str | bytes | list[str] | list[bytes] | list[tuple[str, bytes]]
        ] = {}
        _body_params: bytes | None = None

        # process the path parameters
        if run_id is not None:
            _path_params["runId"] = run_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter

        # set the HTTP header `Accept`
        if "Accept" not in _header_params:
            _header_params["Accept"] = self.api_client.select_header_accept(
                [
                    "application/json"
                ]
            )

        # authentication setting
        _auth_settings: list[str] = [
        ]

        return self.api_client.param_serialize(
            method="POST",
            resource_path="/integration/api/v1/simulation/run/{runId}/stop",
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )
