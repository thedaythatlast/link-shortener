This is a simple FastAPI link-shortener project.

## How to Use (with a virtual environment)

1. Access the project folder:
   ```bash
   cd C:\{project_folder}
   ```

2. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

3. Activate the virtual environment (Windows):

   ```bash
   .\.venv\Scripts\activate
   ```

4. Run the development server:

   ```bash
   fastapi dev main.py
   ```

## TODO

* Integrate the project with a PostgreSQL database (using Docker)
* Validity check for the URL

## Note

* So far the project hasn't been integrated to the database => the docker-compose file is pretty much useless (don't use it)