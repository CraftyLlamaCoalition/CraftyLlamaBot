"""
This module provides a class `PassManager` for managing passwords using the 'pass' command line utility.

The `PassManager` class provides methods for adding, updating, retrieving, and deleting passwords.

Example usage:
    pm = PassManager()
    print(pm.add_password('new_pass', 'mypassword'))  # Add a new password
    print(pm.get_password('new_pass'))  # Get password for 'example'
    print(pm.delete_password('new_pass'))  # Delete the password
"""

import subprocess


class PassManager:
    def __init__(self):
        self.pass_command = "pass"

    def get_password(self, name: str) -> str:
        """
        This method retrieves the password for a given name using a subprocess command.
        If the subprocess command fails, it rasies a CalledProcessError.

        Parameters:
        name (str): The name for which the password is to be retrieved.

        Returns:
        str: The password if the subprocess command is successful
        """
        output = subprocess.check_output(
            [self.pass_command, "show", name], stderr=subprocess.STDOUT
        )
        return output.decode("utf-8").strip()

    def update_password(self, name, new_password):
        """
        This method updates an existing password in the password store.

        It uses the 'pass' command line utility to update the password associated with the given name.
        The '--force' option is used to ensure the password is updated without prompting for confirmation.

        Parameters:
        name (str): The name associated with the password to be updated.
        new_password (str): The new password to be set.

        Returns:
        str: The output from the 'pass' command or an error message if the command fails.
        """
        try:
            process = subprocess.Popen(
                [self.pass_command, "insert", "--force", name],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            process.communicate(
                input=f"{new_password}\n{new_password}\n".encode("utf-8")
            )
            if process.returncode == 0:
                return "Password updated successfully"
            else:
                return "Error updating password"
        except Exception as e:
            return f"Error: {str(e)}"

    def add_password(self, name, password):
        """
        This method adds a new password to the password store.

        Parameters:
        name (str): The name associated with the password.
        password (str): The password to be added.

        Returns:
        str: A message indicating the success or failure of the operation.
        """
        try:
            process = subprocess.Popen(
                [self.pass_command, "insert", "--force", name],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            process.communicate(input=f"{password}\n{password}\n".encode("utf-8"))
            if process.returncode == 0:
                return "Password added successfully"
            else:
                return "Error adding password"
        except Exception as e:
            return f"Error: {str(e)}"

    def delete_password(self, name):
        """
        This method deletes a password from the password store.

        It uses the 'pass' command line utility to delete the password associated with the given name.
        The '--force' option is used to ensure the password is deleted without prompting for confirmation.

        Parameters:
        name (str): The name associated with the password to be deleted.

        Returns:
        str: The output from the 'pass' command or an error message if the command fails.
        """
        try:
            output = subprocess.check_output(
                [self.pass_command, "rm", "--force", name], stderr=subprocess.STDOUT
            )
            return output.decode("utf-8").strip()
        except subprocess.CalledProcessError as e:
            return f"Error: {e.output.decode('utf-8').strip()}"


# Example usage
if __name__ == "__main__":
    pm = PassManager()
    print(pm.add_password("new_pass", "mypassword"))  # Add a new password
    print(pm.get_password("new_pass"))  # Get password for 'example'
    print(pm.delete_password("new_pass"))  # Delete the password
