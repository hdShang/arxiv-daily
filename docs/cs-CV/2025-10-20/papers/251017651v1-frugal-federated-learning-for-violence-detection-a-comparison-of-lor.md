---
layout: default
title: Frugal Federated Learning for Violence Detection: A Comparison of LoRA-Tuned VLMs and Personalized CNNs
---

# Frugal Federated Learning for Violence Detection: A Comparison of LoRA-Tuned VLMs and Personalized CNNs

**arXiv**: [2510.17651v1](https://arxiv.org/abs/2510.17651) | [PDF](https://arxiv.org/pdf/2510.17651.pdf)

**作者**: Sébastien Thuau, Siba Haidar, Ayush Bajracharya, Rachid Chelouah

---

## 💡 一句话要点

**比较LoRA调优视觉语言模型与个性化CNN在联邦暴力检测中的性能与能效**

**关键词**: `联邦学习` `暴力检测` `视觉语言模型` `低秩适应` `3D卷积神经网络` `能效分析`

## 📋 核心要点

1. 核心问题：在非独立同分布联邦学习设置下，实现高精度、低能耗的暴力检测。
2. 方法要点：对比零样本/联邦微调视觉语言模型与个性化训练紧凑3D卷积神经网络。
3. 实验或效果：两种方法准确率超90%，CNN3D在ROC AUC和能耗上略优，VLMs适合上下文推理。

## 📄 摘要（原文）

> We examine frugal federated learning approaches to violence detection by
> comparing two complementary strategies: (i) zero-shot and federated fine-tuning
> of vision-language models (VLMs), and (ii) personalized training of a compact
> 3D convolutional neural network (CNN3D). Using LLaVA-7B and a 65.8M parameter
> CNN3D as representative cases, we evaluate accuracy, calibration, and energy
> usage under realistic non-IID settings.
>   Both approaches exceed 90% accuracy. CNN3D slightly outperforms Low-Rank
> Adaptation(LoRA)-tuned VLMs in ROC AUC and log loss, while using less energy.
> VLMs remain favorable for contextual reasoning and multimodal inference. We
> quantify energy and CO$_2$ emissions across training and inference, and analyze
> sustainability trade-offs for deployment.
>   To our knowledge, this is the first comparative study of LoRA-tuned
> vision-language models and personalized CNNs for federated violence detection,
> with an emphasis on energy efficiency and environmental metrics.
>   These findings support a hybrid model: lightweight CNNs for routine
> classification, with selective VLM activation for complex or descriptive
> scenarios. The resulting framework offers a reproducible baseline for
> responsible, resource-aware AI in video surveillance, with extensions toward
> real-time, multimodal, and lifecycle-aware systems.

