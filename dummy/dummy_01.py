from fastapi import FastAPI, Body


PCS = ["PC_01", "PC_02", "PC_03", "PC_04", "PC_05", "PC_06"]
DEVICES = ["Device_01", "Device_02", "Device_03"]

lb_app = FastAPI()


@lb_app.get("/pcs")
async def get_pcs():
    return PCS


@lb_app.get("/devices")
async def get_devices():
    return DEVICES

