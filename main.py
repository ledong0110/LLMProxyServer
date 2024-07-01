
import os 
import traceback
import json, time
from dotenv import load_dotenv
load_dotenv()
from utils.utils import getenv, set_env_variables

from fastapi import FastAPI, Request, status, HTTPException, Depends
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware

from agents.responseAgent import ResponseAgent
from handlers.msgHandlers import msg_handler

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


######## CHAT COMPLETIONS ################

# for streaming
def data_generator(response):
    for chunk in response:
        # print(f"chunk: {chunk}")
        yield f"data: {json.dumps(chunk.json())}\n\n"

# for completion
@app.post("/chat/completions")
async def completion(request: Request):
    data = await request.json()
    print(f"received request data: {data}")
    set_env_variables(data)
    data = msg_handler(data)
    response_agent = ResponseAgent(config=data)
    # handle how users send streaming
    if 'stream' in data:
        if type(data['stream']) == str: # if users send stream as str convert to bool
            # convert to bool
            if data['stream'].lower() == "true":
                data['stream'] = True # convert to boolean
    
    response = response_agent.generate(**data)
    if 'stream' in data and data['stream'] == True: # use generate_responses to stream responses
            return StreamingResponse(data_generator(response), media_type='text/event-stream')
    return response


@app.get("/health")
async def health():
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=getenv("PORT", 8080))