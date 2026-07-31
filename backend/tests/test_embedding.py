from unittest.mock import patch, MagicMock

from backend.services.embedding import (
    calculate_similarity,
    get_model,
)


@patch("backend.services.embedding.SentenceTransformer")
def test_get_model_loads_once(mock_model):
    fake_model = MagicMock()

    mock_model.return_value = fake_model

    # Reset cached model
    import backend.services.embedding as embedding

    embedding.model = None

    model1 = get_model()
    model2 = get_model()

    assert model1 == fake_model
    assert model2 == fake_model

    mock_model.assert_called_once_with(
        "all-MiniLM-L6-v2"
    )


@patch("backend.services.embedding.cosine_similarity")
@patch("backend.services.embedding.get_model")
def test_calculate_similarity(
    mock_get_model,
    mock_cosine_similarity,
):
    fake_model = MagicMock()

    fake_model.encode.side_effect = [
        [[0.1, 0.2, 0.3]],
        [[0.2, 0.3, 0.4]],
    ]

    mock_get_model.return_value = fake_model

    mock_cosine_similarity.return_value = [[0.875]]

    score = calculate_similarity(
        "Java Resume",
        "Java Job Description",
    )

    assert score == 87.5

    assert fake_model.encode.call_count == 2

    mock_cosine_similarity.assert_called_once()


@patch("backend.services.embedding.cosine_similarity")
@patch("backend.services.embedding.get_model")
def test_calculate_similarity_zero(
    mock_get_model,
    mock_cosine_similarity,
):
    fake_model = MagicMock()

    fake_model.encode.side_effect = [
        [[1, 2]],
        [[3, 4]],
    ]

    mock_get_model.return_value = fake_model

    mock_cosine_similarity.return_value = [[0.0]]

    score = calculate_similarity(
        "Resume",
        "Job",
    )

    assert score == 0.0


@patch("backend.services.embedding.cosine_similarity")
@patch("backend.services.embedding.get_model")
def test_calculate_similarity_hundred(
    mock_get_model,
    mock_cosine_similarity,
):
    fake_model = MagicMock()

    fake_model.encode.side_effect = [
        [[1, 2]],
        [[1, 2]],
    ]

    mock_get_model.return_value = fake_model

    mock_cosine_similarity.return_value = [[1.0]]

    score = calculate_similarity(
        "Resume",
        "Resume",
    )

    assert score == 100.0