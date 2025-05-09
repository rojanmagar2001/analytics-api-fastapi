from fastapi import APIRouter
from .schemas import EventSchema, EventsListSchema, EventCreateSchema, EventUpdateSchema

router = APIRouter()


# Get all events
# GET /api/events/
@router.get("/")
def read_events() -> EventsListSchema:
    return {"results": [{"id": 1}, {"id": 2}, {"id": 3}], "count": 3}


# Create a new event
# POST /api/events/
@router.post("/")
def create_event(payload: EventCreateSchema) -> EventSchema:
    print(payload.page)
    data = payload.model_dump()  # payload -> dict
    return {"id": 1, **data}


# Get a specific event
# GET /api/events/{event_id}
@router.get("/{event_id}")
def get_event(event_id: int) -> EventSchema:
    return {"id": event_id}


# Update event
# PUT /api/events/{event_id}
@router.put("/{event_id}")
def update_event(event_id: int, payload: EventUpdateSchema) -> EventSchema:
    print(payload.description)
    data = payload.model_dump()
    return {"id": event_id, **data}
