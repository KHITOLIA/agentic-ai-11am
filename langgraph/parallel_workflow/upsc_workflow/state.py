from typing import TypedDict, Annotated
from pydantic import BaseModel, Field
import operator


class UPSCState(TypedDict):
    essay : str
    language_feedback : str
    analysis_feedback : str
    clarity_feedback : str
    overall_feedback : str
    individual_scores : Annotated[list[int], operator.add]
    avg_score : float

class EvaluationSchema(BaseModel):
    feedback : str = Field(description = 'Detailed Feedback from the essay ')
    score : int = Field(description = 'score of the essay out of 10')