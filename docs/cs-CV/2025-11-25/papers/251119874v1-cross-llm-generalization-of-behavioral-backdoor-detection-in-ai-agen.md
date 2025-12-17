---
layout: default
title: Cross-LLM Generalization of Behavioral Backdoor Detection in AI Agent Supply Chains
---

# Cross-LLM Generalization of Behavioral Backdoor Detection in AI Agent Supply Chains

**arXiv**: [2511.19874v1](https://arxiv.org/abs/2511.19874) | [PDF](https://arxiv.org/pdf/2511.19874.pdf)

**作者**: Arun Chowdary Sanna

---

## 💡 一句话要点

**提出跨LLM行为后门检测方法以解决AI代理供应链中的泛化问题**

**关键词**: `行为后门检测` `跨LLM泛化` `AI代理供应链` `模型特定特征` `检测框架`

## 📋 核心要点

1. 核心问题：AI代理依赖共享组件导致供应链漏洞，跨LLM行为后门检测泛化能力未知
2. 方法要点：评估六种生产LLM，分析模型特定行为特征，引入模型身份特征提升检测
3. 实验或效果：单模型检测跨模型准确率仅49.2%，模型感知方法达90.6%准确率

## 📄 摘要（原文）

> As AI agents become integral to enterprise workflows, their reliance on shared tool libraries and pre-trained components creates significant supply chain vulnerabilities. While previous work has demonstrated behavioral backdoor detection within individual LLM architectures, the critical question of cross-LLM generalization remains unexplored, a gap with serious implications for organizations deploying multiple AI systems. We present the first systematic study of cross-LLM behavioral backdoor detection, evaluating generalization across six production LLMs (GPT-5.1, Claude Sonnet 4.5, Grok 4.1, Llama 4 Maverick, GPT-OSS 120B, and DeepSeek Chat V3.1). Through 1,198 execution traces and 36 cross-model experiments, we quantify a critical finding: single-model detectors achieve 92.7% accuracy within their training distribution but only 49.2% across different LLMs, a 43.4 percentage point generalization gap equivalent to random guessing. Our analysis reveals that this gap stems from model-specific behavioral signatures, particularly in temporal features (coefficient of variation > 0.8), while structural features remain stable across architectures. We show that model-aware detection incorporating model identity as an additional feature achieves 90.6% accuracy universally across all evaluated models. We release our multi-LLM trace dataset and detection framework to enable reproducible research.

