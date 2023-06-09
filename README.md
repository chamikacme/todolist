# To-Do List App

The To-Do List App is a simple application built with Tkinter and MongoDB that allows you to manage your tasks effectively.

## Features

- Add new tasks to your to-do list.
- Mark tasks as complete or incomplete.
- Delete tasks from your list.
- Tasks are stored in a MongoDB database for persistence.

## Installation

1. Clone the repository: `git clone https://github.com/your-username/to-do-list-app.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Set up MongoDB:
   - Create a MongoDB Atlas account.
   - Set up a cluster and obtain the connection string.
   - Update the `connection_string` variable in `database_functions.py` with your connection string.
4. Run the application: `python main.py`

## Usage

- Enter a task in the input field and click the "Add" button to add it to your to-do list.
- Click on a task in the list to mark it as complete or incomplete.
- Select a task and click the "Delete" button to remove it from the list.

## Contributing

Contributions are welcome! If you have any ideas, improvements, or bug fixes, please submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

