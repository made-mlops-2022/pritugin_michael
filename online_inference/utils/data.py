from pydantic import BaseModel, validator


class HeartRequest(BaseModel):
    age: int
    sex: int
    cp: int
    trestbps: int
    chol: int
    fbs: int
    restecg: int
    thalach: int
    exang: int
    oldpeak: float
    slope: int
    ca: int
    thal: int

    @validator("age")
    def age_validator(cls, v):
        if v < 0:
            raise ValueError("Age less than 0")
        if v > 100:
            raise ValueError("Age over 100")

        return v

    @validator("sex")
    def sex_validator(cls, v):
        if v not in [0, 1]:
            raise ValueError("Sex must be 0 or 1")

        return v

    @validator("cp")
    def cp_validator(cls, v):
        if v < 0 or v > 3:
            raise ValueError("cp must be 0, 1, 2, 3")

        return v

    @validator("trestbps")
    def trestbps_validator(cls, v):
        if v < 0:
            raise ValueError("trestbps must be positive")

        return v

    @validator("chol")
    def chol_validator(cls, v):
        if v < 0:
            raise ValueError("chol must be positive")

        return v

    @validator("fbs")
    def fbs_validator(cls, v):
        if v not in [0, 1]:
            raise ValueError("fbs must be 0 or 1")

        return v

    @validator("restecg")
    def restecg_validator(cls, v):
        if v not in [0, 1, 2]:
            raise ValueError("restecg must be 0 or 1 or 2")

        return v

    @validator("thalach")
    def thalach_validator(cls, v):
        if v < 0:
            raise ValueError("thalach must be positive")

        return v

    @validator("exang")
    def exang_validator(cls, v):
        if v not in [0, 1]:
            raise ValueError("exang must be 0 or 1")

        return v

    @validator("oldpeak")
    def oldpeak_validator(cls, v):
        if v < 0:
            raise ValueError("oldpeak must be positive")

        return v

    @validator("slope")
    def slope_validator(cls, v):
        if v not in [0, 1, 2]:
            raise ValueError("slope must be 0 or 1 or 2")

        return v

    @validator("ca")
    def ca_validator(cls, v):
        if v < 0 or v > 4:
            raise ValueError("ca must be 0, 1, 2, 3, 4")

        return v

    @validator("thal")
    def thal_validator(cls, v):
        if v not in [0, 1, 2]:
            raise ValueError("thal must be 0 or 1 or 2")

        return v
