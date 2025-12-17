---
layout: default
title: SAGE: Spuriousness-Aware Guided Prompt Exploration for Mitigating Multimodal Bias
---

# SAGE: Spuriousness-Aware Guided Prompt Exploration for Mitigating Multimodal Bias

**arXiv**: [2511.13005v1](https://arxiv.org/abs/2511.13005) | [PDF](https://arxiv.org/pdf/2511.13005.pdf)

**作者**: Wenqian Ye, Di Wang, Guangtao Zheng, Bohan Liu, Aidong Zhang

---

## 💡 一句话要点

**提出SAGE方法以缓解多模态虚假偏见，提升零样本分类鲁棒性**

**关键词**: `多模态偏见缓解` `零样本分类` `提示工程` `CLIP模型` `鲁棒性提升`

## 📋 核心要点

1. CLIP模型存在多模态虚假偏见，依赖虚假特征如背景而非核心对象特征
2. SAGE通过引导提示选择，无需训练或外部知识，增强类间语义分离
3. 在多个基准数据集和骨干模型上实验，SAGE提升零样本性能和泛化能力

## 📄 摘要（原文）

> Large vision-language models, such as CLIP, have shown strong zero-shot classification performance by aligning images and text in a shared embedding space. However, CLIP models often develop multimodal spurious biases, which is the undesirable tendency to rely on spurious features. For example, CLIP may infer object types in images based on frequently co-occurring backgrounds rather than the object's core features. This bias significantly impairs the robustness of pre-trained CLIP models on out-of-distribution data, where such cross-modal associations no longer hold. Existing methods for mitigating multimodal spurious bias typically require fine-tuning on downstream data or prior knowledge of the bias, which undermines the out-of-the-box usability of CLIP. In this paper, we first theoretically analyze the impact of multimodal spurious bias in zero-shot classification. Based on this insight, we propose Spuriousness-Aware Guided Exploration (SAGE), a simple and effective method that mitigates spurious bias through guided prompt selection. SAGE requires no training, fine-tuning, or external annotations. It explores a space of prompt templates and selects the prompts that induce the largest semantic separation between classes, thereby improving worst-group robustness. Extensive experiments on four real-world benchmark datasets and five popular backbone models demonstrate that SAGE consistently improves zero-shot performance and generalization, outperforming previous zero-shot approaches without any external knowledge or model updates.

