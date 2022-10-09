from fastapi import FastAPI
from frameworks.fast_api.manager import FastApiManager


def initialize() -> FastAPI:
    try:
        app = FastApiManager(app=FastAPI())
        app.initialize_cors()
        app.initialize_limiter()
        app.initialize_routers()
        return app.get_instance()
    except Exception as error:
        raise("An excepetion has ocurred trying to initialize FastApi: ", error)
