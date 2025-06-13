## [Github Coral Agent](https://github.com/Coral-Protocol/github-coral-agent)

The Github Coral Agent is an open-source agent designed for managing GitHub repositories using a multi-agent architecture.

## Responsibility
The Github Coral Agent manages GitHub repositories, supporting creation, updating, searching for repositories and files, handling issues and pull requests, and facilitating collaboration through comments and reviews.

## Details
- **Framework**: LangChain
- **Tools used**: Github MCP Server Tools, Coral Server Tools
- **AI model**: OpenAI GPT-4o
- **Date added**: June 4, 2025
- **Reference**: [Github MCP Repo](https://github.com/github/github-mcp-server)
- **License**: MIT

## Use the Agent

### 1. Run Coral Server
<details>

Ensure that the [Coral Server](https://github.com/Coral-Protocol/coral-server) is running on your system. In a new terminal, clone the repository:

```bash
# Clone the Coral Server repository
git clone https://github.com/Coral-Protocol/coral-server.git

# Navigate to the project directory
cd coral-server

# Run the server
./gradlew run
```
</details>

### 2.Run [Interface Agent](https://github.com/Coral-Protocol/Coral-Interface-Agent)
<details>

The Interface Agent is required to interact with the Github Coral Agent. In a new terminal, clone the repository:

```bash
# Clone the Interface Agent repository
git clone https://github.com/Coral-Protocol/Coral-Interface-Agent.git

# Navigate to the project directory
cd Coral-Interface-Agent

# Install `uv`:
pip install uv

# Install dependencies from `pyproject.toml` using `uv`:
uv sync

# Run the agent using `uv`:
uv run python 0-langchain-interface.py
```
</details>

### 3. Run Github Coral Agent
<details>

In a new terminal, clone the repository:

```bash
# Clone the Github Coral Agent repository
git clone https://github.com/Coral-Protocol/github-coral-agent.git

# Navigate to the project directory
cd github-coral-agent

# Install `uv`:
pip install uv

# Install dependencies from `pyproject.toml` using `uv`:
uv sync
```
This command will read the `pyproject.toml` file and install all specified dependencies in a virtual environment managed by `uv`.
</details>

### 4. Configure Environment Variables
<details>

Get the API Key:
[OpenAI](https://platform.openai.com/api-keys)
[Github Token](https://github.com/settings/tokens)

Rename the sample environment file to `.env` and add the keys:
```bash
cp -r .env_sample .env
```
Check if the environment file has correct URL for Coral Server and adjust the parameters accordingly.
</details>

### 5. Run Agent
<details>

Run the agent using `uv`:
```bash
uv run python github_coral_agent.py
```
</details>

### 6. Example
<details>

```bash
# Input:
Ask the Interface Agent to create a new repository, open an issue, or search for a file using the Github Coral Agent.

# Output:
The Github Coral Agent will perform the requested GitHub task and return the result via the Interface Agent.
```
</details>

## Creator Details
- **Name**: Suman Deb
- **Affiliation**: Coral Protocol
- **Contact**: [Discord](https://discord.com/invite/Xjm892dtt3)

