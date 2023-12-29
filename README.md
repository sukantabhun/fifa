# FIFA 2026 World Cup Prediction Website

## Overview

This project is part of the IBM Data Science and Machine Learning Training. The FIFA 2026 World Cup Prediction Website allows users to explore and predict outcomes for the upcoming FIFA 2026 World Cup matches.

## Technologies Used

- **HTML**
- **CSS**
- **JavaScript**
- **Python**
- **Django**
- **Jupyter Notebook**

## Project Structure

The project is organized as follows:

- **fifa-1.1.2/**: Root directory of the project.
  - **fifa/**: Django project folder.
  - **static/**: Contains static files such as CSS and JavaScript.
  - **templates/**: HTML templates for the Django app.
  - **venv/**: Virtual environment for Python dependencies.
  - **manage.py**: Django management script.
  - **requirements.txt**: List of Python dependencies.

## Setting Up the Environment

1. Open a terminal and navigate to the project directory:

    ```bash
    cd ...\fifa-1.1.2\fifa-1.1.2
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    venv\Scripts\activate   # On Windows
    source venv/bin/activate # On Unix or MacOS
    ```

3. Install project dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Running the Development Server

1. Make sure you are in the project root directory:

    ```bash
    cd ...\fifa-1.1.2\fifa-1.1.2
    ```

2. Run the Django development server:

    ```bash
    python manage.py runserver
    ```

3. Open a web browser and navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to view the FIFA 2026 World Cup Prediction Website.

## Additional Information

- The machine learning models and data analysis notebooks can be found in the `notebooks/` directory.

- For development, it is recommended to use Visual Studio Code as the integrated development environment (IDE).

