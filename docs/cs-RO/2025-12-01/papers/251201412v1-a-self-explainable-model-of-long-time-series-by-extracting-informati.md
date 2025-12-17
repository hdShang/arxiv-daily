---
layout: default
title: A Self-explainable Model of Long Time Series by Extracting Informative Structured Causal Patterns
---

# A Self-explainable Model of Long Time Series by Extracting Informative Structured Causal Patterns

**arXiv**: [2512.01412v1](https://arxiv.org/abs/2512.01412) | [PDF](https://arxiv.org/pdf/2512.01412.pdf)

**作者**: Ziqian Wang, Yuxiao Cheng, Jinli Suo

---

## 💡 一句话要点

**提出EXCAP框架以解决长时序建模中解释性不足的问题，通过提取结构化因果模式增强可解释性。**

**关键词**: `长时序建模` `可解释AI` `因果模式提取` `注意力机制` `预测准确性` `高风险应用`

## 📋 核心要点

1. 核心问题：现有可解释AI方法仅生成点状重要性分数，无法捕捉趋势、周期等时序结构，削弱长时序模型的信任度。
2. 方法要点：结合注意力分割器提取连贯时序模式、因果图引导的解码器和潜在聚合机制，满足连续性、模式中心、因果解耦和忠实性要求。
3. 实验或效果：在分类和预测基准测试中，EXCAP保持高预测准确性，同时生成连贯且因果基础的解释，适用于医疗和金融等高风险领域。

## 📄 摘要（原文）

> Explainability is essential for neural networks that model long time series, yet most existing explainable AI methods only produce point-wise importance scores and fail to capture temporal structures such as trends, cycles, and regime changes. This limitation weakens human interpretability and trust in long-horizon models. To address these issues, we identify four key requirements for interpretable time-series modeling: temporal continuity, pattern-centric explanation, causal disentanglement, and faithfulness to the model's inference process. We propose EXCAP, a unified framework that satisfies all four requirements. EXCAP combines an attention-based segmenter that extracts coherent temporal patterns, a causally structured decoder guided by a pre-trained causal graph, and a latent aggregation mechanism that enforces representation stability. Our theoretical analysis shows that EXCAP provides smooth and stable explanations over time and is robust to perturbations in causal masks. Extensive experiments on classification and forecasting benchmarks demonstrate that EXCAP achieves strong predictive accuracy while generating coherent and causally grounded explanations. These results show that EXCAP offers a principled and scalable approach to interpretable modeling of long time series with relevance to high-stakes domains such as healthcare and finance.

