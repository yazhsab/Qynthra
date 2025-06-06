"""
Quantum Large Language Model (QLLM) package.

This package provides a quantum-enhanced large language model implementation
using PennyLane for quantum computing integration.
"""

from quantum_llm.qllm_base import QLLMBase
from quantum_llm.qllm_advanced import QLLMAdvanced, QLLMWithKVCache
from quantum_llm.tokenization import QLLMTokenizer

# Import multimodal components
from quantum_llm.multimodal.model import MultimodalQLLM
from quantum_llm.multimodal.encoders import (
    TextEncoder,
    ImageEncoder,
    AudioEncoder,
    MultimodalFusion
)
from quantum_llm.multimodal.data_encoding import (
    create_multimodal_embedding_circuit,
    create_modality_specific_embedding,
    image_to_quantum_encoding,
    audio_to_quantum_encoding
)
from quantum_llm.multimodal.attention import (
    ClassicalCrossModalAttention,
    quantum_cross_modal_attention
)
from quantum_llm.multimodal.preprocessing import (
    TextPreprocessor,
    ImagePreprocessor,
    AudioPreprocessor,
    MultimodalPreprocessor
)
from quantum_llm.multimodal.kv_cache import (
    MultimodalKVCache,
    MultimodalQLLMWithKVCache
)
from quantum_llm.multimodal.training import (
    MultimodalDataset,
    MultimodalTrainer,
    MultimodalEvaluator
)

__version__ = "0.1.0"