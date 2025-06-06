## [Github Coral Agent](https://github.com/Coral-Protocol/github-coral-agent)
The Github Coral Agent is an open-source agent designed for managing GitHub repositories.

### Responsibility
The Github Coral Agent is an open-source agent designed for managing GitHub repositories. It supports creating, updating, and searching for repositories and files, handling issues and pull requests, and facilitating collaboration through comments and reviews using a multi-agent architecture.


### Details
- **Framework**: LangChain
- **Tools used**: Github MCP Server Tools, Coral Server Tools
- **AI model**: OpenAI GPT-4o
- **Date added**: June 4, 2025
- **Reference**: [Github MCP Repo](https://github.com/github/github-mcp-server)
- **License**: MIT

### Clone & Install Dependencies

1. Run [Coral Server](https://github.com/Coral-Protocol/coral-server)
<details>

This agent runs on Coral Server, follow the instrcutions below to run the server. In a new terminal clone the repository:


```bash
git clone https://github.com/Coral-Protocol/coral-server.git
```

Navigate to the project directory:
```bash
cd coral-server
```
Run the server
```bash
cd ./gradlew run
```
</details>

2. Run [Interface Agent](https://github.com/Coral-Protocol/Coral-Interface-Agent)
<details>


If you are trying to run Open Deep Research agent and require an input, you can either create your agent which communicates on the coral server or run and register the Interface Agent on the Coral Server. In a new terminal clone the repository:


```bash
git clone https://github.com/Coral-Protocol/Coral-Interface-Agent.git
```
Navigate to the project directory:
```bash
cd Coral-Interface-Agent
```

Install `uv`:
```bash
pip install uv
```
Install dependencies from `pyproject.toml` using `uv`:
```bash
uv sync
```

Configure API Key
```bash
export OPENAI_API_KEY=
```

Run the agent using `uv`:
```bash
uv run python 0-langchain-interface.py
```

</details>

3. Agent Installation

In a new terminal clone the repository
```bash
git clone https://github.com/Coral-Protocol/github-coral-agent.git
```
Navigate to the project directory:
```bash
cd github-coral-agent
```

Install `uv`:
```bash
pip install uv
```
Install dependencies from `pyproject.toml` using `uv`:
```bash
uv sync
```


Clone the repository:
```bash
git clone 
```

Navigate to the project directory:
```bash
cd 
```

Install `uv`:
```bash
pip install uv
```

Install dependencies from `pyproject.toml` using `uv`:
```bash
uv sync
```

This command will read the `pyproject.toml` file and install all specified dependencies in a virtual environment managed by `uv`.

### Configure Environment Variables
Get the API Key:
[OpenAI](https://platform.openai.com/api-keys)
[Github Token](https://github.com/settings/tokens)

Rename the sample environment file to `.env` and add the keys:
```bash
mv .env_sample .env
```
Check if the environment file has correct URL for Coral Server and adjust the parameters accordingly.

### Run Agent
Run the agent using `uv`:
```bash
uv run python github_coral_agent.py
```

### Example Output
```
Any GitHub task
```

### Creator Details
- **Name**: Suman Deb
- **Affiliation**: Coral Protocol
- **Contact**: [Discord](https://discord.com/invite/Xjm892dtt3)

