from fastapi import APIRouter

from interface_adapters.api.v1.controllers.first_controller_example import FirstrExampleController
from interface_adapters.api.v1.dtos.first_example_dto import (
    FirstExampleInputDTO, FirstExampleOutputDTO
)
from domain.use_case.first_example.first_example import FirstExampleUseCase
from frameworks.requests.manager import RequestsManager


router = APIRouter()

@router.post(
    "/first-example",
    response_model=FirstExampleOutputDTO,
)
async def first_example_route(
    input_dto: FirstExampleInputDTO,
) -> FirstExampleOutputDTO:
    """"""
    requests_manager = RequestsManager()
    first_example_use_case = FirstExampleUseCase(http_requests=requests_manager)
    controller = FirstrExampleController(first_example_use_case=first_example_use_case)
    return await controller.control(input_dto)
