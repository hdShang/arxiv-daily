---
layout: default
title: Dataset Distillation for Pre-Trained Self-Supervised Vision Models
---

# Dataset Distillation for Pre-Trained Self-Supervised Vision Models

**arXiv**: [2511.16674v1](https://arxiv.org/abs/2511.16674) | [PDF](https://arxiv.org/pdf/2511.16674.pdf)

**作者**: George Cazenavette, Antonio Torralba, Vincent Sitzmann

---

## 💡 一句话要点

**提出线性梯度匹配方法，为预训练自监督视觉模型蒸馏数据集以优化线性分类器训练。**

**关键词**: `数据集蒸馏` `自监督学习` `线性分类器` `梯度匹配` `模型泛化` `细粒度分类`

## 📋 核心要点

1. 核心问题：现有数据集蒸馏方法未针对预训练自监督模型优化线性分类器训练。
2. 方法要点：优化合成图像，使其通过预训练特征提取器后，线性分类器梯度与真实数据相似。
3. 实验或效果：合成数据性能超越真实图像基线，并跨模型泛化，提升细粒度分类和模型可解释性。

## 📄 摘要（原文）

> The task of dataset distillation aims to find a small set of synthetic images such that training a model on them reproduces the performance of the same model trained on a much larger dataset of real samples. Existing distillation methods focus on synthesizing datasets that enable training randomly initialized models. In contrast, state-of-the-art vision approaches are increasingly building on large, pre-trained self-supervised models rather than training from scratch. In this paper, we investigate the problem of distilling datasets that enable us to optimally train linear probes on top of such large, pre-trained vision models. We introduce a method of dataset distillation for this task called Linear Gradient Matching that optimizes the synthetic images such that, when passed through a pre-trained feature extractor, they induce gradients in the linear classifier similar to those produced by the real data. Our method yields synthetic data that outperform all real-image baselines and, remarkably, generalize across pre-trained vision models, enabling us, for instance, to train a linear CLIP probe that performs competitively using a dataset distilled via a DINO backbone. Further, we show that our distilled datasets are exceptionally effective for fine-grained classification and provide a valuable tool for model interpretability, predicting, among other things, how similar two models' embedding spaces are under the platonic representation hypothesis or whether a model is sensitive to spurious correlations in adversarial datasets.

