from app import create_app

app = create_app()

if __name__ == "__main__":
    import uvicorn
    import os
    # Get port from environment variable for Cloud Run
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)