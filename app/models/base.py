from sqlalchemy import Column, Boolean, DateTime, func
from datetime import datetime

class TimestampMixin:
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

class SoftDeleteMixin:
    is_deleted = Column(Boolean, default=False)

class BaseModelMixin(TimestampMixin, SoftDeleteMixin):
    pass
