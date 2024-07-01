import litellm
from typing import List, Dict, Any

class LLMAgent:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
    
    def preprocessing(self, messages: List[Dict[str, Any]]):
        raise NotImplementedError()
    
    def postprocessing(self, messages: List[Dict[str, Any]]):
        raise NotImplementedError()
    
    def completion(self, message: List[Dict[str, Any]]):
        raise NotImplementedError()