from abc import ABC, abstractmethod
from typing import Generic, TypeVar

InputDTO = TypeVar('InputDTO')
OutputDTO = TypeVar('OutputDTO')

class UseCase(Generic[InputDTO, OutputDTO], ABC):
    """Interface base para Use Cases"""
    
    @abstractmethod
    def execute(self, input_dto: InputDTO) -> OutputDTO:
        pass