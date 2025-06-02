import pytest
from src.climate_modeling import model_climate

def test_model_climate():
    data = [{"temperature": 25.0, "co2": 400}, {"temperature": 26.0, "co2": 410}]
    prediction = model_climate(data)
    assert "future_temperature" in prediction
    assert "future_co2" in prediction
    assert prediction["future_temperature"] > 25.0
