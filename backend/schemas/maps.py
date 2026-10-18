from pydantic import BaseModel

"""
    Schema pra instanciação das rotas e decodificação de polilinha futuramente.
"""

class Polyline(BaseModel): 
    encodedPolyline: str

class GoogleMapsRoute(BaseModel):
    distanceMeters: int
    duration: str
    polyline: Polyline

class GoogleMapsRouteResponse(BaseModel):
    routes: list[GoogleMapsRoute]
    
