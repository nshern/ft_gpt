from ft_gpt import utils
from ft_gpt.etl.loader import Loader

# from llama_index.core.memory import ChatMemoryBuffer


def generate_pre_promt():
    dates_of_sittings = utils.get_dates_of_sittings(reverse=True)

    prompt = (
        "You are a helpful chatbot that answers questions about meeting notes (mødereferater) from the Danish Folketing.\n"
        "You should only answer questions related to this topic.\n"
        f"The date today is {utils.get_current_date()}. of February 2024. Every mention of a time and date should be in relation to this piece of information.\n"
        f"You have access to meeting notes from the following dates:\n {dates_of_sittings}\n"
        "You may only communicate in Danish and should refrain entirely from communicating in any other language.\n"
    )

    return prompt


def create_engine():
    loader = Loader()
    loader.run()
    index = loader.index
    system_prompt = generate_pre_promt()
    query_engine = index.as_chat_engine(
        chat_mode="openai", system_prompt=system_prompt, verbose=True  # type: ignore
    )
    return query_engine
