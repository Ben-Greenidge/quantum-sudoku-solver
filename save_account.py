import os
from dotenv import load_dotenv

from qiskit_ibm_runtime import QiskitRuntimeService

load_dotenv()

QiskitRuntimeService.save_account(
    token=os.environ["api_key"],
    instance=os.environ["crn"],
)
