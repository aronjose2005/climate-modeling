import pytest
from src.policy_recommendation import recommend_policy

def test_recommend_policy():
    climate_data = {"future_temperature": 26.5}
    analysis = {"sentiment": "negative"}
    policy = recommend_policy(climate_data, analysis)
    assert isinstance(policy, str)
    assert len(policy) > 0
