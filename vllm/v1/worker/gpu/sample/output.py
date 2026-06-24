# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
from dataclasses import dataclass

import torch

from vllm.v1.outputs import LogprobsTensors


@dataclass
class SamplerOutput:
    sampled_token_ids: torch.Tensor
    logprobs_tensors: LogprobsTensors | None
    num_nans: torch.Tensor | None
<<<<<<< HEAD
    num_sampled: torch.Tensor | None
    num_rejected: torch.Tensor | None = None
=======
    entropy: torch.Tensor | None = None  # [num_reqs], float32
<<<<<<< HEAD
>>>>>>> 4cf559d7e (return logprob entropy memory efficient)
=======
    variance: torch.Tensor | None = None  # [num_reqs], float32
>>>>>>> 7600be7a1 (add exact analytic variance)
