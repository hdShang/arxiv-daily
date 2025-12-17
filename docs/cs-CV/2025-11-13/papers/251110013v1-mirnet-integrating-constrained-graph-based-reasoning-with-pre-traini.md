---
layout: default
title: MIRNet: Integrating Constrained Graph-Based Reasoning with Pre-training for Diagnostic Medical Imaging
---

# MIRNet: Integrating Constrained Graph-Based Reasoning with Pre-training for Diagnostic Medical Imaging

**arXiv**: [2511.10013v1](https://arxiv.org/abs/2511.10013) | [PDF](https://arxiv.org/pdf/2511.10013.pdf)

**作者**: Shufeng Kong, Zijie Wang, Nuan Cui, Hao Tang, Yihan Meng, Yuanyuan Wei, Feifan Chen, Yingheng Wang, Zhuo Cai, Yaonan Wang, Yulong Zhang, Yuzheng Li, Zibin Zheng, Caihua Liu

---

## 💡 一句话要点

**提出MIRNet框架，结合自监督预训练与图推理，解决医学图像诊断中的标注稀缺和标签不平衡问题。**

**关键词**: `医学图像诊断` `自监督预训练` `图注意力网络` `约束优化` `舌像分析` `标签不平衡处理`

## 📋 核心要点

1. 核心问题：医学图像标注稀缺、标签不平衡和临床合理性约束，尤其在舌像诊断中。
2. 方法要点：使用MAE自监督预训练、GAT建模标签相关性、约束优化和ASL损失处理不平衡。
3. 实验或效果：在TongueAtlas-4K数据集上验证，达到先进性能，可泛化至其他医学图像任务。

## 📄 摘要（原文）

> Automated interpretation of medical images demands robust modeling of complex visual-semantic relationships while addressing annotation scarcity, label imbalance, and clinical plausibility constraints. We introduce MIRNet (Medical Image Reasoner Network), a novel framework that integrates self-supervised pre-training with constrained graph-based reasoning. Tongue image diagnosis is a particularly challenging domain that requires fine-grained visual and semantic understanding. Our approach leverages self-supervised masked autoencoder (MAE) to learn transferable visual representations from unlabeled data; employs graph attention networks (GAT) to model label correlations through expert-defined structured graphs; enforces clinical priors via constraint-aware optimization using KL divergence and regularization losses; and mitigates imbalance using asymmetric loss (ASL) and boosting ensembles. To address annotation scarcity, we also introduce TongueAtlas-4K, a comprehensive expert-curated benchmark comprising 4,000 images annotated with 22 diagnostic labels--representing the largest public dataset in tongue analysis. Validation shows our method achieves state-of-the-art performance. While optimized for tongue diagnosis, the framework readily generalizes to broader diagnostic medical imaging tasks.

