from .base import LLMAgent
import litellm

class ResponseAgent(LLMAgent):

    def __init__(self, config):
        super().__init__(config)

    def completion(self, messages):
        return litellm.completion(model=config.model, messages=messages, stream=config.stream)
    
    def generate(self, **kwargs):
        return litellm.completion(**kwargs)