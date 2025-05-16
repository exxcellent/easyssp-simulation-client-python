![easyssp-logo-light](https://raw.githubusercontent.com/exxcellent/easyssp-auth-client-python/refs/heads/master/images/logo-light.png#gh-light-mode-only)
![easyssp-logo-dark](https://raw.githubusercontent.com/exxcellent/easyssp-auth-client-python/refs/heads/master/images/logo-dark.png#gh-dark-mode-only)

# easySSP Simulation Python Client

This is the official Python client for the **Simulation API** of the easySSP. It provides an easy-to-use interface for
interacting with simulation endpoints — including launching, monitoring, and managing simulations programmatically.

---

## 🚀 Features

- 📋 Retrieve available simulation options and current simulation credits
- 🎯 Launch and control simulations
- 🔍 Monitor simulation progress and access results
- 🗂️ Manage and organize executed simulations

---

## 📦 Installation

```bash
pip install easyssp-simulation-client
```

Or clone and install from source:

```bash
git clone https://github.com/exxcellent/easyssp-simulation-client-python.git
cd easyssp-simulation-client-python
pip install -e .
```

## Tests

Execute `pytest` or `python -m pytest` to run the tests.

## 📁 Project Structure

```bash
easyssp_simulation/
├── __init__.py
├── client/
│   ├── __init__.py
│   └── simulation_client.py                         # Simulating SSP models with integrated FMI components in easySSP
│
├── models/
│   ├── __init__.py
│   ├── hardware_option.py                           # The available hardware configuration options for simulations
│   ├── run.py                                       # The different runs the Simulation consists of
│   ├── simulation.py                                # The created/started simulation
│   ├── simulation_info.py                           # Info about the simulation
│   ├── simulation_started.py                        # Info about the started simulation
│   ├── start_simulation_configuration.py            # The configuration for the simulation runs
│   ├── start_simulation_run_configuration.py        # Specifies configurations for simulation runs to execute on the given .ssp-file
│   └── step.py                                      # Each simulation run is split into two steps. The 'generate' step will generate a simulator. The 'simulate' step will use that simulator to perform the simulation with the given configurations
```

## 📖 API Reference

This client is built against the official **Simulation API** specification, available as an OpenAPI (Swagger) document.

You can explore the full API documentation here:  
👉 [**Simulation API**](https://apps.exxcellent.de/easy-ssp/docs/integration-api/v1/simulation/index.html)
or in the `docs` directory in this project.

## 📚 Examples Repository & Extended Documentation

Looking for working demos? Check out the Simulation Client Examples Repository here:  
👉 [**Simulation Client Examples Repository**](https://github.com/exxcellent/easyssp-simulation-examples-python)

It includes:

- Real-world examples for running and managing simulations
- Usage patterns for authentication and error handling

It's the best place to explore how the client works in action and how to integrate it into your own workflows.

## 🛠️ Requirements

- Python 3.11+
- easyssp Pro Edition Account

Install dependencies using uv:

```bash
pip install uv
uv sync
```

## 🤝 Contributing

This module is maintained as part of the easySSP ecosystem. If you find issues or want to suggest improvements, please
open an issue or submit a pull request.

## 📄 License

This project is licensed under the MIT License.
