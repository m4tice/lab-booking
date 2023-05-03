"""dummy"""


from fastapi import FastAPI


def addition(first_number: int, second_number: int):
    """
    addtion of first number and second number
    """
    return first_number + second_number


DEVICES = ["device_01", "device_02", "device_03"]

PCS = {"PC01" : "HP001",
       "PC02" : "HP002",
       "PC03" : "HP003"}

app = FastAPI()


@app.get("/devices")
async def get_devices():
    """
    get all devices
    """
    return DEVICES

@app.get("/pcs/{pcid}")
async def get_pc_by_id(pcid: str):
    """
    return PC by id
    """

    return PCS[pcid]
