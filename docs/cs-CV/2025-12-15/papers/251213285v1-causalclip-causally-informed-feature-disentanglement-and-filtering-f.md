---
layout: default
title: CausalCLIP: Causally-Informed Feature Disentanglement and Filtering for Generalizable Detection of Generated Images
---

# CausalCLIP: Causally-Informed Feature Disentanglement and Filtering for Generalizable Detection of Generated Images

**arXiv**: [2512.13285v1](https://arxiv.org/abs/2512.13285) | [PDF](https://arxiv.org/pdf/2512.13285.pdf)

**作者**: Bo Liu, Qiao Qin, Qinghui He

---

## 💡 一句话要点

**提出CausalCLIP框架，通过因果特征解耦与过滤提升生成图像检测的泛化能力**

**关键词**: `生成图像检测` `特征解耦` `因果推理` `泛化能力` `CLIP模型`

## 📋 核心要点

1. 现有方法特征高度纠缠，混合因果与非因果特征，限制泛化
2. 基于结构因果模型，利用Gumbel-Softmax掩码和HSIC约束解耦特征
3. 在未见生成模型上测试，准确率和平均精度显著优于先进方法

## 📄 摘要（原文）

> The rapid advancement of generative models has increased the demand for generated image detectors capable of generalizing across diverse and evolving generation techniques. However, existing methods, including those leveraging pre-trained vision-language models, often produce highly entangled representations, mixing task-relevant forensic cues (causal features) with spurious or irrelevant patterns (non-causal features), thus limiting generalization. To address this issue, we propose CausalCLIP, a framework that explicitly disentangles causal from non-causal features and employs targeted filtering guided by causal inference principles to retain only the most transferable and discriminative forensic cues. By modeling the generation process with a structural causal model and enforcing statistical independence through Gumbel-Softmax-based feature masking and Hilbert-Schmidt Independence Criterion (HSIC) constraints, CausalCLIP isolates stable causal features robust to distribution shifts. When tested on unseen generative models from different series, CausalCLIP demonstrates strong generalization ability, achieving improvements of 6.83% in accuracy and 4.06% in average precision over state-of-the-art methods.

