from pathlib import Path

CURRENT_PATH = Path(__file__).parent.parent
DATA_BASE_PATH = Path.joinpath(CURRENT_PATH, 'data_base', 'test.db')
