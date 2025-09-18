# # # testing.py
# # import os
# # from github import Github
# # from dotenv import load_dotenv  # <-- Import this new library
# #
# # # 1. Load environment variables from the .env file
# # load_dotenv()  # <-- This is the crucial line you were missing
# #
# # # 2. Now you can get the token from the .env file
# # token = os.getenv('GITHUB_PERSONAL_ACCESS_TOKEN')
# #
# # # 3. Print the token to debug (Optional, but very helpful)
# # # If this prints 'None', your .env file is not set up correctly.
# # print(f"Token: {token}")
# #
# # # 4. Check if the token was actually found
# # if token is None:
# #     print("ERROR: Could not find 'GITHUB_PERSONAL_ACCESS_TOKEN' in the .env file.")
# #     exit(1)
# #
# # # 5. Now try to authenticate
# # g = Github(token)
# #
# # # 6. Test a simple function: List your repositories
# # print("Attempting to list your repositories...")
# # try:
# #     for repo in g.get_user().get_repos():
# #         print(f"-> {repo.name}")
# #     print("Success! GitHub authentication is working.")
# # except Exception as e:
# #     print(f"Failed to list repos. Error: {e}")
#
# # github_manager.py
# import os
# from github import Github, GithubException
# from dotenv import load_dotenv
#
# # Load environment variables
# load_dotenv()
#
#
# class GitHubManager:
#     """A clean, standalone manager for GitHub operations."""
#
#     def __init__(self, access_token: str = None):
#         self.access_token = access_token or os.getenv('GITHUB_PERSONAL_ACCESS_TOKEN')
#         if not self.access_token:
#             raise ValueError("GitHub Personal Access Token not provided and not found in .env file")
#         self.g = Github(self.access_token)
#         self.user = self.g.get_user()
#         print("GitHub Manager initialized successfully.")
#
#     def list_repos(self):
#         """List all repositories for the authenticated user."""
#         try:
#             repos = []
#             # This is the correct way to list repos - just get them, don't modify anything
#             for repo in self.user.get_repos():
#                 repos.append({"name": repo.name, "url": repo.html_url})
#             return {"status": "success", "repositories": repos}
#         except GithubException as e:
#             return {"status": "error", "message": f"Failed to list repositories: {e}"}
#
#     def backup_folder_to_github(self, repo_name, folder_path, commit_message="Auto-backup"):
#         """
#         Backup a local folder to a GitHub repository.
#         Creates the repo if it doesn't exist, then uploads all files.
#         """
#         try:
#             # FIXED: Better repository handling
#             try:
#                 repo = self.user.get_repo(repo_name)
#             except GithubException:
#                 # Create repo if it doesn't exist
#                 create_result = self.create_repo(repo_name, description="Auto-backed up repository")
#                 if create_result["status"] == "error":
#                     return create_result  # Return the error immediately
#                 repo = self.user.get_repo(repo_name)  # Now get the newly created repo
#
#             # ... rest of the method remains the same
#     # def list_repos(self):
#     #     """List all repositories for the authenticated user."""
#     #     try:
#     #         repos = []
#     #         for repo in self.user.get_repos():
#     #             repos.append({"name": repo.name, "url": repo.html_url})
#     #         return {"status": "success", "repositories": repos}
#     #     except GithubException as e:
#     #         return {"status": "error", "message": f"Failed to list repositories: {e}"}
#
#     def create_repo(self, name, description="", private=False):
#         """Create a new repository."""
#         try:
#             repo = self.user.create_repo(name, description=description, private=private)
#             return {"status": "success", "message": f"Repository '{name}' created.", "url": repo.html_url}
#         except GithubException as e:
#             return {"status": "error", "message": f"Failed to create repository: {e}"}
#
#     def create_file(self, repo_name, file_path, file_content, commit_message):
#         """Create a new file in a repository."""
#         try:
#             repo = self.user.get_repo(repo_name)
#             result = repo.create_file(file_path, commit_message, file_content)
#             return {"status": "success", "message": f"File '{file_path}' created in '{repo_name}'.",
#                     "commit_sha": result['commit'].sha}
#         except GithubException as e:
#             return {"status": "error", "message": f"Failed to create file: {e}"}
#
#     def get_file_content(self, repo_name, file_path):
#         """Get the content of a file from a repository."""
#         try:
#             repo = self.user.get_repo(repo_name)
#             file = repo.get_contents(file_path)
#             return {"status": "success", "content": file.decoded_content.decode('utf-8'), "sha": file.sha}
#         except GithubException as e:
#             return {"status": "error", "message": f"Failed to get file content: {e}"}
#
#     def update_file(self, repo_name, file_path, new_content, commit_message, sha=None):
#         """Update a file in a repository."""
#         try:
#             repo = self.user.get_repo(repo_name)
#             if not sha:
#                 # Get the current file SHA if not provided
#                 file = repo.get_contents(file_path)
#                 sha = file.sha
#             result = repo.update_file(file_path, commit_message, new_content, sha)
#             return {"status": "success", "message": f"File '{file_path}' updated in '{repo_name}'.",
#                     "commit_sha": result['commit'].sha}
#         except GithubException as e:
#             return {"status": "error", "message": f"Failed to update file: {e}"}
#
#     def backup_folder_to_github(self, repo_name, folder_path, commit_message="Auto-backup"):
#         """
#         Backup a local folder to a GitHub repository.
#         Creates the repo if it doesn't exist, then uploads all files.
#         """
#         try:
#             # Create repo if it doesn't exist
#             try:
#                 repo = self.user.get_repo(repo_name)
#             except GithubException:
#                 repo = self.create_repo(repo_name, description="Auto-backed up repository")
#                 if repo["status"] == "error":
#                     return repo
#                 repo = self.user.get_repo(repo_name)
#
#             # Walk through folder and upload files
#             for root, dirs, files in os.walk(folder_path):
#                 for file in files:
#                     local_file_path = os.path.join(root, file)
#                     # Create relative path for GitHub
#                     relative_path = os.path.relpath(local_file_path, folder_path)
#
#                     with open(local_file_path, 'r', encoding='utf-8') as f:
#                         content = f.read()
#
#                     # Try to create file, update if it exists
#                     result = self.create_file(repo_name, relative_path, content, commit_message)
#                     if result["status"] == "error" and "already exists" in result["message"].lower():
#                         # File exists, try to update
#                         file_info = self.get_file_content(repo_name, relative_path)
#                         if file_info["status"] == "success":
#                             result = self.update_file(repo_name, relative_path, content, commit_message,
#                                                       file_info["sha"])
#
#                     if result["status"] == "error":
#                         print(f"Failed to process {relative_path}: {result['message']}")
#
#             return {"status": "success", "message": f"Folder '{folder_path}' backed up to '{repo_name}'"}
#
#         except Exception as e:
#             return {"status": "error", "message": f"Failed to backup folder: {e}"}
#
#
# # Simple test function
# def main():
#     """Test the GitHub manager functions."""
#     manager = GitHubManager()
#
#     # Test listing repos
#     print("Listing repositories:")
#     result = manager.create_file('MyTestFile','https://github.com/AyeshaIjazTabassum/MyTestingRepo.git','This is test file','Done')
#     print(result)
#
#     # Test creating a file (optional - uncomment to test)
#     # print("\nCreating test file:")
#     # result = manager.create_file("test-repo", "README.md", "# Test File", "Initial commit")
#     # print(result)
#
#
# if __name__ == "__main__":
#     main()


# standalone_github_agent.py
import os
import time
from dotenv import load_dotenv
from github import Github, GithubException
import json

# Load environment variables
load_dotenv()


class GitHubAgent:
    """Standalone GitHub agent that can perform operations without Langchain/Coral"""

    def __init__(self):
        self.access_token = os.getenv('GITHUB_PERSONAL_ACCESS_TOKEN')
        if not self.access_token:
            raise ValueError("GitHub Personal Access Token not found in .env file")

        self.g = Github(self.access_token)
        self.user = self.g.get_user()
        self.agent_id = os.getenv('AGENT_ID', 'github_standalone_agent')
        print(f"GitHub Agent '{self.agent_id}' initialized successfully")

    def get_available_tools(self):
        """Return list of available tools with their schemas"""
        return [
            {
                "name": "list_repos",
                "description": "List all repositories for the authenticated user",
                "args": {}
            },
            {
                "name": "create_repo",
                "description": "Create a new repository",
                "args": {
                    "name": "string",
                    "description": "string",
                    "private": "boolean"
                }
            },
            {
                "name": "create_file",
                "description": "Create a new file in a repository",
                "args": {
                    "repo_name": "string",
                    "file_path": "string",
                    "file_content": "string",
                    "commit_message": "string"
                }
            },
            {
                "name": "get_file_content",
                "description": "Get content of a file from repository",
                "args": {
                    "repo_name": "string",
                    "file_path": "string"
                }
            }
        ]

    def list_repos(self):
        """List all repositories"""
        try:
            repos = []
            for repo in self.user.get_repos():
                repos.append({
                    "name": repo.name,
                    "url": repo.html_url,
                    "description": repo.description,
                    "private": repo.private
                })
            return {"status": "success", "repositories": repos}
        except GithubException as e:
            return {"status": "error", "message": f"Failed to list repositories: {e}"}

    def create_repo(self, name, description="", private=False):
        """Create a new repository"""
        try:
            repo = self.user.create_repo(name, description=description, private=private)
            return {
                "status": "success",
                "message": f"Repository '{name}' created",
                "url": repo.html_url
            }
        except GithubException as e:
            return {"status": "error", "message": f"Failed to create repository: {e}"}

    def create_file(self, repo_name, file_path, file_content, commit_message):
        """Create a new file in repository"""
        try:
            repo = self.user.get_repo(repo_name)
            result = repo.create_file(file_path, commit_message, file_content)
            return {
                "status": "success",
                "message": f"File '{file_path}' created in '{repo_name}'",
                "commit_sha": result['commit'].sha
            }
        except GithubException as e:
            return {"status": "error", "message": f"Failed to create file: {e}"}

    def get_file_content(self, repo_name, file_path):
        """Get file content from repository"""
        try:
            repo = self.user.get_repo(repo_name)
            file = repo.get_contents(file_path)
            return {
                "status": "success",
                "content": file.decoded_content.decode('utf-8'),
                "sha": file.sha
            }
        except GithubException as e:
            return {"status": "error", "message": f"Failed to get file content: {e}"}

    def execute_tool(self, tool_name, **kwargs):
        """Execute a tool by name with provided arguments"""
        tool_methods = {
            "list_repos": self.list_repos,
            "create_repo": self.create_repo,
            "create_file": self.create_file,
            "get_file_content": self.get_file_content
        }

        if tool_name not in tool_methods:
            return {"status": "error", "message": f"Unknown tool: {tool_name}"}

        return tool_methods[tool_name](**kwargs)

    def process_instruction(self, instruction):
        """
        Process a natural language instruction and execute appropriate tools
        Simple version of the AI planning from the original code
        """
        instruction = instruction.lower()

        # Simple instruction parsing - this is where you could add more AI logic
        if "list" in instruction and ("repo" in instruction or "repository" in instruction):
            return self.list_repos()

        elif "create" in instruction and "repo" in instruction:
            # Simple extraction - in real scenario you'd use better NLP
            repo_name = "new_repository"  # Default
            if "called" in instruction:
                repo_name = instruction.split("called")[1].strip().split()[0]
            return self.create_repo(repo_name)

        elif "create" in instruction and "file" in instruction:
            # Simple pattern matching
            return {"status": "info", "message": "Need more details for file creation"}

        else:
            return {
                "status": "error",
                "message": "Instruction not understood. Available commands: list repos, create repo, create file"
            }

    def run_agent_loop(self):
        """Main agent loop that processes instructions"""
        print(f"Agent {self.agent_id} started. Waiting for instructions...")
        print("Available tools:", [tool["name"] for tool in self.get_available_tools()])

        while True:
            try:
                # Simulate receiving an instruction (replace this with your actual input method)
                instruction = input("\nEnter instruction (or 'quit' to exit): ").strip()

                if instruction.lower() == 'quit':
                    break

                if not instruction:
                    continue

                print(f"\nProcessing instruction: {instruction}")

                # Process the instruction
                result = self.process_instruction(instruction)

                # Display result
                print("Result:", json.dumps(result, indent=2))

                # Simulate waiting between operations
                time.sleep(1)

            except KeyboardInterrupt:
                print("\nAgent stopped by user")
                break
            except Exception as e:
                print(f"Error in agent loop: {e}")
                time.sleep(2)


def main():
    """Test all GitHub agent functions sequentially"""
    try:
        # Initialize the agent
        print("Initializing GitHub Agent...")
        agent = GitHubAgent()
        print("✅ Agent initialized successfully\n")

        time.sleep(1)

        # Test 1: List available tools
        print("1. Testing get_available_tools()...")
        tools = agent.get_available_tools()
        print("✅ Available tools:")
        for tool in tools:
            print(f"   - {tool['name']}: {tool['description']}")
        print()

        time.sleep(1)

        # Test 2: List repositories
        print("2. Testing list_repos()...")
        repo_result = agent.list_repos()
        if repo_result["status"] == "success":
            print("✅ Repositories found:")
            for repo in repo_result["repositories"][:3]:  # Show first 3 to avoid too much output
                print(f"   - {repo['name']} ({'private' if repo['private'] else 'public'})")
            if len(repo_result["repositories"]) > 3:
                print(f"   ... and {len(repo_result['repositories']) - 3} more")
        else:
            print("❌ Failed to list repositories:", repo_result["message"])
        print()

        time.sleep(1)

        # Test 3: Create a test repository
        print("3. Testing create_repo()...")
        test_repo_name = f"test-repo-{int(time.time())}"  # Unique name using timestamp
        create_result = agent.create_repo(
            name=test_repo_name,
            description="Test repository created by GitHub Agent",
            private=False
        )
        if create_result["status"] == "success":
            print(f"✅ Repository '{test_repo_name}' created successfully!")
            print(f"   URL: {create_result['url']}")
        else:
            print("❌ Failed to create repository:", create_result["message"])
        print()

        time.sleep(2)  # Wait a bit for GitHub to process

        # Test 4: Create a file in the test repository
        print("4. Testing create_file()...")
        file_content = """# Test File
This file was created by the GitHub Agent automated test.
Timestamp: {time.time()}
"""
        file_result = agent.create_file(
            repo_name=test_repo_name,
            file_path="README.md",
            file_content=file_content,
            commit_message="Initial commit - automated test"
        )
        if file_result["status"] == "success":
            print("✅ File created successfully!")
            print(f"   Commit SHA: {file_result['commit_sha']}")
        else:
            print("❌ Failed to create file:", file_result["message"])
        print()

        time.sleep(2)  # Wait a bit for GitHub to process

        # Test 5: Get file content
        print("5. Testing get_file_content()...")
        content_result = agent.get_file_content(
            repo_name=test_repo_name,
            file_path="README.md"
        )
        if content_result["status"] == "success":
            print("✅ File content retrieved successfully!")
            print("   Content preview:")
            print("   " + "-" * 40)
            # Show first 3 lines of content
            lines = content_result["content"].split('\n')[:3]
            for line in lines:
                print(f"   | {line}")
            print("   " + "-" * 40)
            print(f"   File SHA: {content_result['sha']}")
        else:
            print("❌ Failed to get file content:", content_result["message"])
        print()

        time.sleep(1)

        # Test 6: Test execute_tool method
        print("6. Testing execute_tool() with list_repos...")
        tool_result = agent.execute_tool("list_repos")
        if tool_result["status"] == "success":
            print("✅ execute_tool worked for list_repos!")
            print(f"   Found {len(tool_result['repositories'])} repositories")
        else:
            print("❌ execute_tool failed:", tool_result["message"])
        print()

        time.sleep(1)

        # Test 7: Test process_instruction method
        print("7. Testing process_instruction()...")
        instructions_to_test = [
            "list all repositories",
            "create a new repository",
            "show me my repos"
        ]

        for instruction in instructions_to_test:
            print(f"   Testing instruction: '{instruction}'")
            instruction_result = agent.process_instruction(instruction)
            print(f"   Result: {instruction_result['status']} - {instruction_result['message']}")
            time.sleep(0.5)
        print()

        # Final summary
        print("🎉 All tests completed!")
        print(f"\nTest repository '{test_repo_name}' was created for testing.")
        print("You can delete it manually on GitHub if you don't need it.")

        # Optionally start the interactive loop
        print("\n" + "=" * 50)
        start_interactive = input("Start interactive mode? (y/n): ").lower().strip()
        if start_interactive == 'y':
            agent.run_agent_loop()
        else:
            print("Testing completed. Exiting.")

    except Exception as e:
        print(f"❌ Critical error in main: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()