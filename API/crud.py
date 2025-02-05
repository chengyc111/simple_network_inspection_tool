from sqlalchemy.orm import Session
from sqlalchemy import func
from API import models, schemas


def create_device(db: Session, device: schemas.DeviceIn):
    db_device = models.DeviceInfo(**device.dict())
    db.add(db_device)
    db.commit()
    db.refresh(db_device)
    return db_device


def get_dev(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.DeviceInfo).offset(skip).limit(limit).all()


def get_dev_all(db: Session):
    return db.query(models.DeviceInfo).all()


def get_device_info(db: Session, ip_add: str):
    dev = db.query(models.DeviceInfo).filter(models.DeviceInfo.ip_add == ip_add).first()
    return dev


def update_device_info(db: Session, device_info: schemas.DeviceIn):
    dev = db.query(models.DeviceInfo).filter(models.DeviceInfo.id == device_info.id).first()
    dev.hostname = device_info.hostname
    dev.device_type = device_info.device_type
    dev.port = device_info.port
    dev.protocol = device_info.protocol
    dev.super_pw = device_info.super_pw
    dev.password = device_info.password
    dev.username = device_info.username
    db.commit()
    db.refresh(dev)
    return dev


def delete_device_info(db: Session, id_name: int):
    dev = db.query(models.DeviceInfo).filter(models.DeviceInfo.id == id_name).first()
    db.delete(dev)
    db.commit()


def get_hostname(db: Session, hostname: str):
    dev = db.query(models.DeviceInfo).filter(models.DeviceInfo.hostname == hostname).first()
    return dev


def get_count(db: Session):
    count = db.query(func.count(models.DeviceInfo.id)).scalar()
    return count
