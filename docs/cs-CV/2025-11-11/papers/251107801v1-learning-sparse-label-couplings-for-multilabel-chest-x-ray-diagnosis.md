---
layout: default
title: Learning Sparse Label Couplings for Multilabel Chest X-Ray Diagnosis
---

# Learning Sparse Label Couplings for Multilabel Chest X-Ray Diagnosis

**arXiv**: [2511.07801v1](https://arxiv.org/abs/2511.07801) | [PDF](https://arxiv.org/pdf/2511.07801.pdf)

**作者**: Utkarsh Prakash Srivastava, Kaushik Gupta, Kaushik Nath

---

## 💡 一句话要点

**提出稀疏标签耦合模块以增强多标签胸部X光诊断性能**

**关键词**: `多标签分类` `胸部X光诊断` `标签耦合` `类别不平衡` `轻量级优化` `测试时增强`

## 📋 核心要点

1. 核心问题：多标签胸部X光分类中标签共现与类别不平衡问题
2. 方法要点：使用SE-ResNeXt101骨干，添加轻量级标签图优化模块学习稀疏耦合
3. 实验或效果：在验证集上一致提升宏观AUC，计算开销可忽略

## 📄 摘要（原文）

> We study multilabel classification of chest X-rays and present a simple, strong pipeline built on SE-ResNeXt101 $(32 \times 4d)$. The backbone is finetuned for 14 thoracic findings with a sigmoid head, trained using Multilabel Iterative Stratification (MIS) for robust cross-validation splits that preserve label co-occurrence. To address extreme class imbalance and asymmetric error costs, we optimize with Asymmetric Loss, employ mixed-precision (AMP), cosine learning-rate decay with warm-up, gradient clipping, and an exponential moving average (EMA) of weights. We propose a lightweight Label-Graph Refinement module placed after the classifier: given per-label probabilities, it learns a sparse, trainable inter-label coupling matrix that refines logits via a single message-passing step while adding only an L1-regularized parameter head. At inference, we apply horizontal flip test-time augmentation (TTA) and average predictions across MIS folds (a compact deep ensemble). Evaluation uses macro AUC averaging classwise ROC-AUC and skipping single-class labels in a fold to reflect balanced performance across conditions. On our dataset, a strong SE-ResNeXt101 baseline attains competitive macro AUC (e.g., 92.64% in our runs). Adding the Label-Graph Refinement consistently improves validation macro AUC across folds with negligible compute. The resulting method is reproducible, hardware-friendly, and requires no extra annotations, offering a practical route to stronger multilabel CXR classifiers.

