from fastapi import FastAPI, Body
from transformer_model import TransformerModel
from models import CONSTANTS, Argument, Arguments, ArgumentResponse, ArgumentsResponse

"""
    API'ımızın çalışacağı adresin sonuna /docs eklediğimizde, hazır bir dokümantasyon göreceğiz.
    API'ımız hakkında temel bilgileri bu dokümantasyonda gösterebilmek için app  nesnemizi 
    tanımlarken bu bilgileri parametre olarak giriyorum. Örneğin tags_metadata sorgularımızı
    dokümantasyonda gruplamak için kullanılacak.
"""

tags_metadata = [
    {
        "name": "Status",
    },
    {
        "name": "Evaluations",
        "description": "Operations to label Turkish text.",
    }
]

app = FastAPI(
    title= "caseAPI",
    version="1.0",
    description="A simple API for a transformer model",
    openapi_tags=tags_metadata
)


@app.get('/', include_in_schema = False, tags=["Status"])
async def status_check():
    return "This is CaseAPI!"


@app.get('/status', tags=["Status"])
async def status_check():
    return CONSTANTS["statusResponse"]


@app.post('/argument', summary = "Evaluate an argument", status_code = 200, tags=["Evaluations"])
async def evaluate_argument(argument: Argument = Body(..., example = CONSTANTS["argumentExample"])):
    """
    Evaluate an argument's label using a transformer model
    - **body**: Arguments must have a string type body

    Response will have a body and evaluation parameter
    - **body**: Input Argument's body
    - **evaluation**: The evaluation of the argument. Has label and score information
    """
    model = TransformerModel()
    evaluation = model.analyse(argument.body)
    response = ArgumentResponse(body = argument.body, evaluation = evaluation)
    return response


@app.post('/arguments', summary = "Evaluate a list of arguments separately", status_code = 200, tags=["Evaluations"])
async def evaluate_arguments(arguments: Arguments = Body(..., example = CONSTANTS["argumentsExample"])):
    """
    Evaluate a list of argument's labels using a transformer model
    - **argList**: A list of Arguments

    Response will be a list of evaluations

    - **evaluations**: List of evaluations, structured as:
        1. **body**: Input Argument's body
        2. **evaluation**: The evaluation of the argument. Has label and score information
    """
    model, evaluations = TransformerModel(), list()
    for arg in arguments.argList:
        evaluation = model.analyse(arg.body)
        evaluations.append(ArgumentResponse(body = arg.body, evaluation = evaluation))
    response = ArgumentsResponse(evaluations = evaluations)
    return response
