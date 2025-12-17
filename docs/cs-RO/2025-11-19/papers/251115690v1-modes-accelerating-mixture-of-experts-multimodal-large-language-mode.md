---
layout: default
title: MoDES: Accelerating Mixture-of-Experts Multimodal Large Language Models via Dynamic Expert Skipping
---

# MoDES: Accelerating Mixture-of-Experts Multimodal Large Language Models via Dynamic Expert Skipping

**arXiv**: [2511.15690v1](https://arxiv.org/abs/2511.15690) | [PDF](https://arxiv.org/pdf/2511.15690.pdf)

**作者**: Yushi Huang, Zining Wang, Zhihang Yuan, Yifu Ding, Ruihao Gong, Jinyang Guo, Xianglong Liu, Jun Zhang

---

## 💡 一句话要点

**提出MoDES框架以动态跳过专家，加速MoE多模态大语言模型推理**

**关键词**: `多模态大语言模型` `专家混合模型` `动态专家跳过` `推理加速` `全局调制门控` `双模态阈值`

## 📋 核心要点

1. 核心问题：MoE多模态大语言模型计算效率低，现有专家跳过方法导致性能显著下降
2. 方法要点：引入全局调制局部门控机制和双模态阈值法，自适应跳过冗余专家
3. 实验或效果：在多个基准测试中性能提升达10.67%，推理速度显著提高

## 📄 摘要（原文）

> Mixture-of-Experts (MoE) Multimodal large language models (MLLMs) excel at vision-language tasks, but they suffer from high computational inefficiency. To reduce inference overhead, expert skipping methods have been proposed to deactivate redundant experts based on the current input tokens. However, we find that applying these methods-originally designed for unimodal large language models (LLMs)-to MLLMs results in considerable performance degradation. This is primarily because such methods fail to account for the heterogeneous contributions of experts across MoE layers and modality-specific behaviors of tokens within these layers. Motivated by these findings, we propose MoDES, the first training-free framework that adaptively skips experts to enable efficient and accurate MoE MLLM inference. It incorporates a globally-modulated local gating (GMLG) mechanism that integrates global layer-wise importance into local routing probabilities to accurately estimate per-token expert importance. A dual-modality thresholding (DMT) method is then applied, which processes tokens from each modality separately, to derive the skipping schedule. To set the optimal thresholds, we introduce a frontier search algorithm that exploits monotonicity properties, cutting convergence time from several days to a few hours. Extensive experiments for 3 model series across 13 benchmarks demonstrate that MoDES far outperforms previous approaches. For instance, when skipping 88% experts for Qwen3-VL-MoE-30B-A3B-Instruct, the performance boost is up to 10.67% (97.33% vs. 86.66%). Furthermore, MoDES significantly enhances inference speed, improving the prefilling time by 2.16$\times$ and the decoding time by 1.26$\times$.

