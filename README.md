# GetStego
A Multimedia Steganography Tool for encoding hidden messages within images, audio, and video files.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/ShreeMaiya/GetStego.git
    ```
2. Navigate to the project directory:
    ```sh
    cd GetStego
    ```
3. Create a virtual environment:
    ```sh
    python -m venv venv
    ```
4. Activate the virtual environment:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```sh
        source venv/bin/activate
        ```
5. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Apply migrations:
    ```sh
    python manage.py migrate
    ```
2. Run the development server:
    ```sh
    python manage.py runserver
    ```
3. Open your web browser and go to `http://127.0.0.1:8000/` to access the application.
4. Follow the on-screen instructions to encode or decode messages within multimedia files.

## Requirements

- Python 3.x
- Required Python packages (listed in `requirements.txt`)

