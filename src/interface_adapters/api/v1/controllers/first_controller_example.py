from domain.use_case.first_example.first_example import FirstExampleUseCase
from interface_adapters.api.v1.dtos.first_example_dto import (
    FirstExampleInputDTO, FirstExampleOutputDTO
)
from domain.use_case.first_example.ports import FirstExampleInputPort


class FirstrExampleController():
    
    def __init__(
        self,
        first_example_use_case: FirstExampleUseCase
    ) -> None:
        """"""
        self._first_example_use_case = first_example_use_case

    async def control(self, input_dto: FirstExampleInputDTO) -> FirstExampleOutputDTO:
        """"""
        input_port = FirstExampleInputPort(
            _id = input_dto._id,
            name = input_dto._id,
            active = input_dto._id,
        )
        return self._first_example_use_case(input_port=input_port)
