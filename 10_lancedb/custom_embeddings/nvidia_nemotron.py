import os
from dotenv import load_dotenv
from openai import OpenAI
from lancedb.embeddings import TextEmbeddingFunction, get_registry
import numpy as np

load_dotenv()

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.getenv("NVIDIA_API"),
    max_retries=3,
    timeout=60.0,
)


@get_registry().register("nvidia-nemotron")
class NvidiaNemotronEmbedding(TextEmbeddingFunction):
    model: str = "nvidia/nemotron-3.5-embed-8b"
    dimensions: int = 4096

    def ndims(self) -> int:
        return self.dimensions

    def _embed_one(self, text: str, input_type: str) -> np.ndarray:
        response = client.embeddings.create(
            model=self.model,
            input=[text],
            extra_body={"input_type": input_type},
        )
        vector = np.asarray(response.data[0].embedding, dtype=np.float32)
        return vector

    def generate_embeddings(self, texts, *args, **kwargs):
        texts = self.sanitize_input(texts)
        return [self._embed_one(text, input_type="passage") for text in texts]

    def compute_source_embeddings(self, texts, *args, **kwargs):
        return self.generate_embeddings(texts)

    def compute_query_embeddings(self, query, *args, **kwargs):
        texts = self.sanitize_input(query)
        return [self._embed_one(text, input_type="query") for text in texts]
