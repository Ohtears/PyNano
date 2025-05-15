# PyNano: A Modular Command-Based Text Editor

PyNano is a simple, modular, command-based text editor designed as part of a teaching assistant's work to demonstrate key software engineering concepts and design patterns. The project showcases the use of decorators, the command design pattern, exception handling, permission handling, the factory design pattern, and file registries.

## Features

- **Command-Based Interface**: Navigate directories, create, delete, and edit files using commands.
- **Text Editor**: A curses-based text editor with undo/redo functionality.
- **User Management**: Role-based access control with permissions for actions like file creation, deletion, and user management.
- **File Registry**: Dynamically register and handle different file types.
- **Admin Panel**: Manage users and their roles through an admin interface.

## Design Patterns and Concepts

1. **Command Design Pattern**:
   - Commands like `cd`, `ls`, `create`, `del`, and `nano` are implemented as separate classes and registered in a central `CommandRegistry`.

2. **Decorator Pattern**:
   - Permissions are enforced using the `@has_permission` decorator, ensuring only authorized users can perform specific actions.

3. **Factory Design Pattern**:
   - File types are dynamically registered and instantiated using a file registry and the `@register_file_type` decorator.
   - **Plugin Architecture**:
     - The `file_registry.py` module implements a plugin architecture for registering file extensions.
     - Developers can extend the application by creating new file handlers and registering them with the registry, enabling support for additional file types without modifying the core code.
     - Example:
       ```python
       # filepath: PyNano/Models/python_handler.py
       from Core.file_registry import register_file_type

       @register_file_type('.py')
       class PythonFileHandler:
           def open(self, filename):
               with open(filename, 'r') as file:
                   return file.read()

           def save(self, filename, content):
               with open(filename, 'w') as file:
                   file.write(content)
       ```
       - In this example, a new file handler for `.py` files is created by overriding the `open` and `save` methods. The `@register_file_type('.py')` decorator registers this handler with the file registry.

4. **Exception Handling**:
   - Custom exceptions like `UserAlreadyExistsError`, `UserNotFoundError`, and `IncorrectPasswordError` are used for robust error handling.

5. **Role-Based Access Control**:
   - Users are assigned roles (`root`, `admin`, `editor`, `guest`) with predefined permissions.

6. **Memento Pattern**:
   - Undo/redo functionality in the text editor is implemented using the memento pattern to save and restore editor states.

7. **Modular Programming**:
   - The project is organized into modules for commands, models, core functionality, and the user interface, promoting reusability and maintainability.
   - The folder structure is as follows:
     - **Models**: Contains class definitions for users, files, and file types.
     - **Interface**: Handles the user interface components, such as the session manager and text editor.
     - **Commands**: Implements the command classes (e.g., `cd`, `ls`, `nano`) used in the command-based interface.
     - **Core**: Includes core functionality such as error handling, undo/redo and initialization logic.

## Commands

- **File and Directory Operations**:
  - `cd <directory>`: Change the current directory.
  - `ls`: List files and directories.
  - `pwd`: Display the current directory.
  - `create <filename>`: Create a new file.
  - `del <filename>`: Delete a file.
  - `nano <filename>`: Open a file in the text editor.

- **User Management**:
  - `login <username>`: Log in as a user.
  - `register`: Register a new user.
  - `logout`: Log out of the current session.
  - `admin`: Access the admin panel (requires appropriate permissions).

- **Text Editor Shortcuts**:
  - `Ctrl+O`: Save the file.
  - `Ctrl+X`: Exit the editor.
  - `Ctrl+U`: Undo the last change.
  - `Ctrl+R`: Redo the last undone change.

## How to Run

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd PyNano
   ```

2. Install dependencies (if any are added to `requirements.txt`):
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the `user.json` file:
   - The `user.json` file is located under the `User/` directory and contains user data for the application.
   - By default, it includes the following users:
     ```json
     [
       {
         "username": "root",
         "password": "rootpass",
         "role": "root"
       },
       {
         "username": "admin",
         "password": "adminpass",
         "role": "admin"
       },
       {
         "username": "editor",
         "password": "editorpass",
         "role": "editor"
       },
       {
         "username": "guest",
         "password": "guestpass",
         "role": "guest"
       }
     ]
     ```
   - You can modify this file to add or remove users as needed.

4. Run the application:
   ```bash
   python main.py
   ```

## Future Improvements

- Add support for more file types.
- Enhance the text editor with features like search, copy-paste, and syntax highlighting.
- Improve the admin panel with more user management options.
- Add unit tests for better reliability.
- Implement autosave functionality to prevent data loss.
- Hide passwords when inputting for better security.

---
**Author**: Ashkan Marali
