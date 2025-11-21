import logging
import os

# Cria pasta de logs
os.makedirs("logs", exist_ok=True)

# Configuração do logger
logging.basicConfig(
    filename="logs/execution.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger()
