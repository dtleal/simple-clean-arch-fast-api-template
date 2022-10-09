from domain.use_case.first_example.ports import FirstExampleInputPort, FirstExampleOutputPort
from typing import Dict


class FirstExampleUseCase():
    
    def __init__(self) -> None:
        ...
    
    async def __call__(self, input_port: FirstExampleInputPort) -> None:
        _body = {
            "_id": input_port._id,
            "name": input_port.name,
            "active": input_port.active,
            "response": "May the force be with you!"
        }
        return FirstExampleOutputPort(
            code=200, 
            body=Dict(_body)
        )
