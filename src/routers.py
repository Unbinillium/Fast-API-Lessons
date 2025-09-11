from fastapi.routing import APIRouter

BASE_ROUTE_PATH = "/tictonic-plates"
router = APIRouter(prefix=BASE_ROUTE_PATH)


standart_dataset = [
 {
    "plate": "yz",
    "lat": 24.052,
    "lon": 107.132
  },
  {
    "plate": "yz",
    "lat": 23.456,
    "lon": 107.681
  },
  {
    "plate": "yz",
    "lat": 23.141,
    "lon": 108.561
  },
  {
    "plate": "yz",
    "lat": 22.82,
    "lon": 109.436
  },
  {
    "plate": "yz",
    "lat": 22.495,
    "lon": 110.308
  },
  {
    "plate": "yz",
    "lat": 22.165,
    "lon": 111.175
  },
  {
    "plate": "yz",
    "lat": 21.831,
    "lon": 112.038
  },
  {
    "plate": "yz",
    "lat": 21.408,
    "lon": 112.288
  },
  {
    "plate": "yz",
    "lat": 20.985,
    "lon": 112.537
  },
  {
    "plate": "yz",
    "lat": 20.561,
    "lon": 112.784
  },
  {
    "plate": "yz",
    "lat": 20.137,
    "lon": 113.03
  },
  {
    "plate": "yz",
    "lat": 19.713,
    "lon": 113.274
  },
  {
    "plate": "yz",
    "lat": 19.288,
    "lon": 113.517
  },
  {
    "plate": "yz",
    "lat": 18.863,
    "lon": 113.759
  },
  {
    "plate": "yz",
    "lat": 18.438,
    "lon": 114
  },
  {
    "plate": "yz",
    "lat": 18.438,
    "lon": 114
  }
]

@router.get('/get-dataset')
def get_dataset():
    return standart_dataset
