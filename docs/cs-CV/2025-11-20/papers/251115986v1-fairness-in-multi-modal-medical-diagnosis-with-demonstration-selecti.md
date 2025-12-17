---
layout: default
title: Fairness in Multi-modal Medical Diagnosis with Demonstration Selection
---

# Fairness in Multi-modal Medical Diagnosis with Demonstration Selection

**arXiv**: [2511.15986v1](https://arxiv.org/abs/2511.15986) | [PDF](https://arxiv.org/pdf/2511.15986.pdf)

**作者**: Dawei Li, Zijian Gu, Peng Wang, Chuhan Song, Zhen Tan, Mohan Zhang, Tianlong Chen, Yu Tian, Song Wang

---

## 💡 一句话要点

**提出公平感知演示选择方法以解决多模态医疗诊断中的公平性问题**

**关键词**: `多模态医疗诊断` `公平性` `演示选择` `上下文学习` `聚类采样` `医疗图像推理`

## 📋 核心要点

1. 多模态大语言模型在医疗图像推理中存在跨人口群体的公平性问题
2. 通过聚类采样构建人口平衡且语义相关的演示，实现无需调优的公平提升
3. 实验表明该方法在多个基准上减少性别、种族和民族差异，同时保持高准确率

## 📄 摘要（原文）

> Multimodal large language models (MLLMs) have shown strong potential for medical image reasoning, yet fairness across demographic groups remains a major concern. Existing debiasing methods often rely on large labeled datasets or fine-tuning, which are impractical for foundation-scale models. We explore In-Context Learning (ICL) as a lightweight, tuning-free alternative for improving fairness. Through systematic analysis, we find that conventional demonstration selection (DS) strategies fail to ensure fairness due to demographic imbalance in selected exemplars. To address this, we propose Fairness-Aware Demonstration Selection (FADS), which builds demographically balanced and semantically relevant demonstrations via clustering-based sampling. Experiments on multiple medical imaging benchmarks show that FADS consistently reduces gender-, race-, and ethnicity-related disparities while maintaining strong accuracy, offering an efficient and scalable path toward fair medical image reasoning. These results highlight the potential of fairness-aware in-context learning as a scalable and data-efficient solution for equitable medical image reasoning.

