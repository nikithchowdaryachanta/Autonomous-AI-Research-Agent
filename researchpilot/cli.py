import argparse
from .agent import ResearchAgent
from .config import Settings

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("query")
    parser.add_argument("--max-sources", type=int, default=6)
    args = parser.parse_args()

    result = ResearchAgent(Settings()).run(
        args.query,
        args.max_sources,
    )

    print(result["report"]["markdown"])

if __name__ == "__main__":
    main()
