---
layout: default
title: Long-horizon Reasoning Agent for Olympiad-Level Mathematical Problem Solving
---

# Long-horizon Reasoning Agent for Olympiad-Level Mathematical Problem Solving

**arXiv**: [2512.10739v1](https://arxiv.org/abs/2512.10739) | [PDF](https://arxiv.org/pdf/2512.10739.pdf)

**作者**: Songyang Gao, Yuzhe Gu, Zijian Wu, Lingkai Kong, Wenwei Zhang, Zhongrui Cai, Fan Zheng, Tianyou Ma, Junhao Shen, Haiteng Zhao, Duanyang Zhang, Huilun Zhang, Kuikun Liu, Chengqi Lyu, Yanhui Duan, Chiyu Chen, Ningsheng Ma, Jianfei Gao, Han Lyu, Dahua Lin, Kai Chen

---

## 💡 一句话要点

**提出基于结果的流程验证器，以解决长推理链中不可靠中间步骤的验证难题。**

**关键词**: `推理验证` `主动学习` `拒绝微调` `数学问题求解` `长链推理`

## 📋 核心要点

1. 当前基于结果的验证器无法检查长推理链中的中间步骤，而基于流程的验证器受限于高质量标注稀缺。
2. 提出OPV验证器，通过总结长推理链的结果来验证其推理过程，实现准确高效的验证和大规模标注。
3. 采用迭代主动学习框架，结合专家标注和拒绝微调，在多个基准测试中取得最先进性能。

## 📄 摘要（原文）

> Large language models (LLMs) have achieved significant progress in solving complex reasoning tasks by Reinforcement Learning with Verifiable Rewards (RLVR). This advancement is also inseparable from the oversight automated by reliable verifiers. However, current outcome-based verifiers (OVs) are unable to inspect the unreliable intermediate steps in the long reasoning chains of thought (CoTs). Meanwhile, current process-based verifiers (PVs) have difficulties in reliably detecting errors in the complex long CoTs, limited by the scarcity of high-quality annotations due to the prohibitive costs of human annotations. Therefore, we propose the \textbf{O}utcome-based \textbf{P}rocess \textbf{V}erifier (OPV), which verifies the rationale process of summarized outcomes from long CoTs to achieve both accurate and efficient verification and enable large-scale annotation. To empower the proposed verifier, we adopt an iterative active learning framework with expert annotations to progressively improve the verification capability of OPV with fewer annotation costs. Specifically, in each iteration, the most uncertain cases of the current best OPV are annotated and then subsequently used to train a new OPV through Rejection Fine-Tuning (RFT) and RLVR for the next round. Extensive experiments demonstrate OPV's superior performance and broad applicability. It achieves new state-of-the-art results on our held-out \textsc{\thisbench}, outperforming much larger open-source models such as Qwen3-Max-Preview with an F1 score of 83.1 compared to 76.3. Furthermore, OPV effectively detects false positives within synthetic dataset, closely align with expert assessment. When collaborating with policy models, OPV consistently yields performance gains, e.g., raising the accuracy of DeepSeek-R1-Distill-Qwen-32B from 55.2\% to 73.3\% on AIME2025 as the compute budget scales.

