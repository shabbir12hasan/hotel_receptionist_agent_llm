# Hotel Receptionist Agent
Author: Shabbir Hasan
Date: 2025-08-15

## Project Overview
This project is a hotel receptionist agent designed to assist users by performing these main tasks:
1. Answering hotel-specific questions.
2. Providing the best food recommendations near the station.
3. Provide weather updates

---

## Features
- **Hotel-Specific Q&A**: Offers accurate and prompt answers to questions related to the hotel, such as amenities, check-in/check-out times, and room availability.
- **Food Recommendations**: Suggests top-rated food options near the station based on user preferences and proximity.
- **Weather Update**: Provie weather update from the live APIs

---

## Installation Instructions

To set up the environment for the hotel receptionist agent, follow these steps:

1. **Clone the Repository**:

2. **Create a Virtual Environment**:
    For Python projects, it's recommended to use a virtual environment. You can create one using:
    ```bash
    python3 -m venv venv
    ```
3. **Activate the Virtual Environment**:
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```

4. **Install Poetry**:
    You can install Poetry using pip with the following command:
    ```bash
    pip install poetry
    ```

5. **Add Poetry to Your Path**:
    After installation, ensure that Poetry is added to your system's PATH. You can do this by adding the following line to your shell configuration file (e.g., `.bashrc`, `.zshrc`):
    ```bash
    export PATH="$HOME/.local/bin:$PATH"
    ```

6. **Verify the Installation**:
    To confirm that Poetry has been installed successfully, run:
    ```bash
    poetry --version

7. **Set the PYTHONPATH**:
    To ensure your project can be found by Python, add the project path to your PYTHONPATH environment variable. You can do this by adding the following line to your shell configuration file:
    ```bash
    export PYTHONPATH=$PYTHONPATH:/path/to/your/project/root
    ```
