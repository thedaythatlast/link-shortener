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

4. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Run the development server:

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
* The link shortener automatically adds "https://" to any link that doesn't contain "http://" or "https://" by default. This makes the link shortener not useable for sites that can't be accessed with "https://".