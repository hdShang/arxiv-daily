---
layout: default
title: DiFR: Inference Verification Despite Nondeterminism
---

# DiFR: Inference Verification Despite Nondeterminism

**arXiv**: [2511.20621v1](https://arxiv.org/abs/2511.20621) | [PDF](https://arxiv.org/pdf/2511.20621.pdf)

**作者**: Adam Karvonen, Daniel Reuter, Roy Rinberg, Luke Marks, Adrià Garriga-Alonso, Keri Warr

---

## 💡 一句话要点

**提出Token-DiFR和Activation-DiFR方法以验证LLM推理正确性**

**关键词**: `推理验证` `大语言模型` `随机种子同步` `激活压缩` `量化检测`

## 📋 核心要点

1. LLM推理中数值噪声导致结果差异，难以区分合法变化与错误
2. Token-DiFR比较生成令牌与参考实现预测，Activation-DiFR压缩激活用于验证
3. 实验显示高精度检测量化错误，AUC>0.999，减少通信开销

## 📄 摘要（原文）

> As demand for LLM inference grows, it is becoming increasingly important that providers and their customers can verify that inference processes are performed correctly, without errors or tampering. However, re-running the same inference process twice often leads to different results due to benign numerical noise, making it difficult to distinguish legitimate variation from actual problems. To address this problem, we introduce Token-DiFR (Token-Divergence-From-Reference), a method for verifying inference outputs by comparing generated tokens against predictions made by a trusted reference implementation conditioned on the same random seed. Sampling seed synchronization tightly constrains valid outputs, leaving providers minimal room to deviate from correct inference, which allows output tokens themselves to serve as auditable evidence of correctness at zero additional cost to the provider. Token-DiFR reliably identifies sampling errors, simulated bugs, and model quantization, detecting 4-bit quantization with AUC $>$ 0.999 within 300 output tokens. For applications requiring sample-efficient forward-pass verification, we additionally introduce Activation-DiFR, a scheme that uses random orthogonal projections to compress activations into compact fingerprints for subsequent verification. Activation-DiFR detects 4-bit quantization with AUC $>$ 0.999 using just 2 output tokens, while reducing communication overhead by 25-75% relative to existing methods. We release an open-source integration with vLLM to accelerate practical deployment of verifiable inference.

