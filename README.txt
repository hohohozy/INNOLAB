# Flask A* Pathfinding Service (For Thunkable)

## Deployment Guide (Render.com)

1. Upload this project to a GitHub repository.
2. Log in to https://render.com and click "New Web Service".
3. Connect your GitHub account and select this project repository.
4. Choose Python as the environment and set `main.py` as the entry file.
5. Wait for Render to deploy the application automatically.
6. Once deployed, you will receive a URL like:
   https://your-app-name.onrender.com/get_path

## API Usage
Send a POST request to `/get_path` with the following JSON body:

{
  "grid": [
    [0,0,0],
    [0,1,0],
    [0,0,0]
  ],
  "start": [0,0],
  "end": [2,2]
}

The response will contain a list of coordinates representing the path, which can be used to visualize the escape route.
