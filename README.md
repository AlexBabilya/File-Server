# FastAPI File Upload Example

This FastAPI application provides a simple endpoint to upload files. It utilizes the `fastapi` library for creating a web API and allows users to upload files via the `/file/` endpoint.

##  Installation

### Step 1: Clone this repository

```bash
git clone https://github.com/AlexBabilya/file-server.git
cd file-erver
```

To ensure a clean and isolated environment for your FastAPI project, it's recommended to use a virtual environment. Here are the steps to create a new virtual environment, activate it, and install packages from a `requirements.txt` file:

### Step 2: Create a Virtual Environment

```bash
# On Windows
python -m venv venv

# On macOS and Linux
python3 -m venv venv
```

This will create a new directory named `venv` containing the virtual environment.

### Step 3: Activate the Virtual Environment

#### On Windows:

```bash
venv\Scripts\activate
```

#### On macOS and Linux:

```bash
source venv/bin/activate
```

After activation, your command prompt or terminal should now show the virtual environment name, indicating that you are working within the virtual environment.

### Step 4: Install Dependencies from `requirements.txt`

Install the dependencies using `pip`:

```bash
pip install -r requirements.txt
```

This will install the specified packages along with their dependencies in your virtual environment.

### Step 5: Deactivate the Virtual Environment

When you're done working in your virtual environment, you can deactivate it:

```bash
deactivate
```

The `--reload` flag enables automatic code reloading during development.

## Usage

### Step 1: Run the FastAPI application:

After activating virtual environment and installing dependencies, you can run server: 

```bash
uvicorn main:app --reload
```

The `--reload` flag enables automatic code reloading during development.

### Uploading a File

Send a POST request to the `/file/` endpoint with the file attached. The server will store the file in the specified `UPLOAD_DIRECTORY`.

Example using [curl](https://curl.se/):

```bash
curl -X POST "http://127.0.0.1:8000/file/" -H "accept: application/json" -H "Content-Type: multipart/form-data" -F "file=@/path/to/your/file.txt"
```

### Response

If the file upload is successful, you will receive a JSON response:

```json
{
  "message": "File uploaded successfully"
}
```

If there is an error during the file upload process, an error message will be returned with a status code of 500.

```json
{
  "message": "Error: <error_message>"
}
```

## Configuration

You can modify the `UPLOAD_DIRECTORY` variable in the `main.py` file to change the directory where the uploaded files will be stored.

```python
UPLOAD_DIRECTORY = "./"
```

Make sure that the specified directory exists and the application has the necessary permissions to write to it.
