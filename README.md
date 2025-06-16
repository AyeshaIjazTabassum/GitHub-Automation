## [Github Coral Agent](https://github.com/Coral-Protocol/github-coral-agent)

The Github Coral Agent is an open-source agent designed for managing GitHub repositories.

## Responsibility
The Github Coral Agent is an open-source agent designed for managing GitHub repositories. It supports creating, updating, and searching for repositories and files, handling issues and pull requests, and facilitating collaboration through comments and reviews using a multi-agent architecture.


## Details
- **Framework**: LangChain
- **Tools used**: Github MCP Server Tools, Coral Server Tools
- **AI model**: OpenAI GPT-4o
- **Date added**: June 4, 2025
- **Reference**: [Github MCP Repo](https://github.com/github/github-mcp-server)
- **License**: MIT

## Use the Agent

### 1. Clone & Install Dependencies

<details>

Ensure that the [Coral Server](https://github.com/Coral-Protocol/coral-server) is running on your system. If you are trying to run Open Deep Research agent and require an input, you can either create your agent which communicates on the coral server or run and register the [Interface Agent](https://github.com/Coral-Protocol/Coral-Interface-Agent) on the Coral Server.  


```bash
# In a new terminal clone the repository:
git clone https://github.com/Coral-Protocol/github-coral-agent.git

# Navigate to the project directory:
cd github-coral-agent

# Install `uv`:
pip install uv

# Install dependencies from `pyproject.toml` using `uv`:
uv sync
```

</details>

### 2. Configure Environment Variables

<details>

Get the API Key:
[OpenAI](https://platform.openai.com/api-keys) || 
[Github Token](https://github.com/settings/tokens)

```bash
# Create .env file in project root
cp -r .env_sample .env
```

Check if the .env file has correct URL for Coral Server and adjust the parameters accordingly.

</details>

### 3. Run Agent

<details>

```bash
# Run the agent using `uv`:
uv run python github_coral_agent.py
```
</details>

### 4. Example

<details>

```bash
# Input:
GitHub MCP instruction

#Output:
The desired output from the Github MCP execution
```

</details>

### Creator Details
- **Name**: Suman Deb
- **Affiliation**: Coral Protocol
- **Contact**: [Discord](https://discord.com/invite/Xjm892dtt3)

