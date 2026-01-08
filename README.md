This is a simple FastAPI link-shortener project.

## How to Use (with a virtual environment)

1. Access the project folder:
   ```bash
   cd C:\{project_folder}
   ```

2. [Skip if done the first time] Create a virtual environment:

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

# Using the API:
Once the server is running, use the address 
```
localhost:{your_host}/shorten?url={url_address_you_want_to_shorten}
```
You will receive the shortened link.

## TODO

* Integrate the project with a PostgreSQL database (using Docker)

## Note

* So far the project hasn't been integrated to the database => the docker-compose file is pretty much useless (don't use it)