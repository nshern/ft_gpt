from ft_gpt.engine.create_engine import create_engine
from ft_gpt.settings import init_settings

if __name__ == "__main__":
    init_settings()
    query_engine = create_engine()
    print("\n")

    while True:
        query = input("Q: ")

        if query == "reset":
            print("Resetting")
            query_engine.reset()
        else:
            r = query_engine.chat(query)
            print(f"response:{r.response}\n")
            print(f"sources: {r.sources}\n")
            print(f"source_nodes: {r.source_nodes}\n")
