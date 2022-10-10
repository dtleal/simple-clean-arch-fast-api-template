from domain.use_case.first_example.ports import FirstExampleInputPort, FirstExampleOutputPort


class FirstExampleUseCase():
    
    def __init__(self) -> None:
        ...
    
    async def __call__(self, input_port: FirstExampleInputPort) -> FirstExampleOutputPort:
        return FirstExampleOutputPort(
            code=200, 
            body={
                "name": input_port.name,
                "active": input_port.active,
                "response": "May the force be with you!"
            }
        )
