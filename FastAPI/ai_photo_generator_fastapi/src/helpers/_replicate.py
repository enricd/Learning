from functools import lru_cache

from decouple import config
from replicate.client import Client
from replicate.exceptions import ReplicateError


REPLICATE_API_TOKEN = config("REPLICATE_API_TOKEN")
REPLICATE_MODEL = config("REPLICATE_MODEL")
REPLICATE_MODEL_VERSION = config("REPLICATE_MODEL_VERSION")

@lru_cache
def get_replicate_client():
    return Client(api_token=REPLICATE_API_TOKEN)


@lru_cache
def get_replicate_model_version():
    replicate_client = get_replicate_client()
    rep_model = replicate_client.models.get(REPLICATE_MODEL)
    rep_version = rep_model.versions.get(REPLICATE_MODEL_VERSION)

    return rep_version


def generate_image(
    prompt, 
    require_trigger_word=True, 
    trigger_word="TOK"
):
    if require_trigger_word:
        if trigger_word not in prompt:
            raise Exception(f"Trigger word {trigger_word} not found in prompt")
    input_args = {
        "prompt": prompt,
        "num_outputs": 2, 
        "output_format": "jpg",
    }
    replicate_client = get_replicate_client()
    rep_version = get_replicate_model_version()
    pred = replicate_client.predictions.create(
        version=rep_version,
        input=input_args,
    )

    return pred


def list_pred_results(
        model=REPLICATE_MODEL, 
        version=REPLICATE_MODEL_VERSION,
        status=None,
        max_size=100,
    ):
    replicate_client = get_replicate_client()
    preds = replicate_client.predictions.list()
    results = list(preds.results)
    while preds.next:
        _preds = replicate_client.predictions.list(preds.next)
        results += list(_preds.results)
        if len(results) >= max_size:
            break
    results = [x for x in results if x.model == model and x.version == version]
    if status is not None:
        results = [x for x in results if x.status == status]
        
    return results


def get_prediction_detail(
        prediction_id=None,
    ):
    replicate_client = get_replicate_client()
    try:
        pred = replicate_client.predictions.get(prediction_id)
    
    except ReplicateError:
        return None, 404
    
    except:
        return None, 500

    return pred, 200
    
