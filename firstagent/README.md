# Prompt Agent Quick Start

A minimal Python console app that runs a **prompt agent** hosted in [Microsoft Foundry](https://ai.azure.com/) using the [Microsoft Agent Framework SDK](https://github.com/microsoft/agent-framework).

## Architecture Overview

This project connects to a **pre-configured prompt agent** in Microsoft Foundry. The agent's instruction, tools, and model configuration are all managed server-side in the Foundry portal — none of that logic lives in this codebase. The code simply authenticates, connects to the agent by name, sends user messages, and streams back responses (including any tool call outputs).

```
+------------------------+              +----------------------------------+
|                        |    HTTP      |  Microsoft Foundry               |
|  run_agent.py          | -----------> |                                  |
|  (console app)         | <----------- |  +----------------------------+  |
|                        |   Stream     |  |     Prompt Agent           |  |
|  - FoundryAgent        |              |  |                            |  |
|                        |              |  |  - Instructions            |  |
+-----------------------+               |  |  - Tools                   |  |
                                        |  |  - Model deployment        |  |
                                        |  +----------------------------+  |
                                        +----------------------------------+
```

### Key concepts

- **`FoundryAgent`** — A high-level abstraction from the Agent Framework that connects to an existing PromptAgent or HostedAgent in Foundry and handles the conversation loop and streaming.

## Prerequisites

- **Python 3.10+**
- **Azure authentication** — This project authenticates using [DefaultAzureCredential](https://aka.ms/azsdk/python/identity/credential-chains#usage-guidance-for-defaultazurecredential). Ensure your environment provides credentials via one of the supported sources:
  - Azure CLI (`az login`)
  - Visual Studio Code account sign-in
  - Visual Studio account sign-in

  Confirm authentication locally (e.g., `az account show`) before running the script.
- **Access** to the Microsoft Foundry project and the prompt agent referenced in the code

## Quick Start

```text
# 1. Create and activate a Python virtual environment
python -m venv .venv

# On Windows:
.venv\Scripts\activate

# On macOS/Linux:
source .venv/bin/activate

# 2. Install dependencies (--pre is required for prerelease SDK packages)
pip install --pre -r requirements.txt

# 3. Run the agent
python run_agent.py
```

## Project Structure

```
├── run_agent.py        # Entry point — authenticates, connects to agent, streams responses
├── requirements.txt    # Python dependencies (Agent Framework SDK packages)
└── README.md
```

There is only one source file. All agent behavior (instructions, tools, model config) is managed in the Foundry portal, not in code.

## Next Steps

This quick start is intentionally minimal — a starting point for further development. Use GitHub Copilot to help you with any of the following:

- Add OpenTelemetry tracing — Instrument the agent for observability into runs, tool calls, and latency.
- Integrate into an existing application — Extract the agent logic into a web server (e.g., FastAPI, Flask) or other application host.

## Additional Resources

- [Microsoft Agent Framework](https://learn.microsoft.com/agent-framework/overview/agent-framework-overview)
