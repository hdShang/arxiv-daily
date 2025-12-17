---
layout: default
title: SAGE: Style-Adaptive Generalization for Privacy-Constrained Semantic Segmentation Across Domains
---

# SAGE: Style-Adaptive Generalization for Privacy-Constrained Semantic Segmentation Across Domains

**arXiv**: [2512.02369v1](https://arxiv.org/abs/2512.02369) | [PDF](https://arxiv.org/pdf/2512.02369.pdf)

**作者**: Qingmei Li, Yang Zhang, Peifeng Zhang, Haohuan Fu, Juepeng Zheng

---

## 💡 一句话要点

**提出SAGE框架以解决隐私约束下冻结模型的语义分割跨域泛化问题**

**关键词**: `语义分割` `域泛化` `隐私约束` `风格自适应` `视觉提示` `冻结模型`

## 📋 核心要点

1. 核心问题：隐私约束下无法访问模型参数，传统微调受限，需输入级策略提升泛化能力。
2. 方法要点：通过风格转移构建源域多样风格表示，自适应融合风格线索生成动态提示，隐式对齐特征分布。
3. 实验或效果：在五个基准数据集上，SAGE在隐私约束下达到或超越先进方法，优于全微调基线。

## 📄 摘要（原文）

> Domain generalization for semantic segmentation aims to mitigate the degradation in model performance caused by domain shifts. However, in many real-world scenarios, we are unable to access the model parameters and architectural details due to privacy concerns and security constraints. Traditional fine-tuning or adaptation is hindered, leading to the demand for input-level strategies that can enhance generalization without modifying model weights. To this end, we propose a \textbf{S}tyle-\textbf{A}daptive \textbf{GE}neralization framework (\textbf{SAGE}), which improves the generalization of frozen models under privacy constraints. SAGE learns to synthesize visual prompts that implicitly align feature distributions across styles instead of directly fine-tuning the backbone. Specifically, we first utilize style transfer to construct a diverse style representation of the source domain, thereby learning a set of style characteristics that can cover a wide range of visual features. Then, the model adaptively fuses these style cues according to the visual context of each input, forming a dynamic prompt that harmonizes the image appearance without touching the interior of the model. Through this closed-loop design, SAGE effectively bridges the gap between frozen model invariance and the diversity of unseen domains. Extensive experiments on five benchmark datasets demonstrate that SAGE achieves competitive or superior performance compared to state-of-the-art methods under privacy constraints and outperforms full fine-tuning baselines in all settings.

