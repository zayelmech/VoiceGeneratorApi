
## First Time Cloning Repository 

1. Create a virtual environment:

```powershell CMD
    python -m venv venv
```

2. Activate the virtual environment:

- Windows
```powershell CMD
    
    venv\Scripts\activate
```
- For macOS and Linux:
```powershell CMD
    
   source venv/bin/activate
```

3. Install the dependencies inside the virtual environment:

```powershell CMD
    pip install fastapi starlette pyttsx3 pydantic uvicorn
```

4. Install ffmpeg:

    For Windows: You can download a static build of ffmpeg from the official website (https://ffmpeg.org/) and add the ffmpeg executable to your system's PATH.
    For macOS: You can install ffmpeg using Homebrew by running brew install ffmpeg in the terminal.
    For Linux: You can install ffmpeg using the package manager specific to your distribution (e.g., apt, yum, dnf).

5. Start the FastAPI application using Uvicorn:
```powershell CMD
    uvicorn main:app --reload
```


## Run with venv ready

1. Activate the virtual environment:

- Windows
```powershell CMD
    
    venv\Scripts\activate
```
- For macOS and Linux:
```powershell CMD
    
   source venv/bin/activate
```

2. Start the FastAPI application using Uvicorn:
```powershell CMD
    uvicorn main:app --reload
```
