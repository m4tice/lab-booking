"""Main Application"""

from fastapi import FastAPI


PCS = ["PC_01", "PC_02", "PC_03", "PC_04", "PC_05", "PC_06"]
DEVICES = ["Device_01", "Device_02", "Device_03"]

lb_app = FastAPI()


@lb_app.get("/pcs")
async def get_pcs():
    """
    Get all PCs
    :return: PCS
    """
    return PCS


@lb_app.get("/devices")
async def get_devices():
    """
    Get all devices
    :return: DEVICES
    """
    return DEVICES
