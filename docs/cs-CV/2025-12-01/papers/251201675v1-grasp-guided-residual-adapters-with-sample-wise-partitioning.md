---
layout: default
title: GRASP: Guided Residual Adapters with Sample-wise Partitioning
---

# GRASP: Guided Residual Adapters with Sample-wise Partitioning

**arXiv**: [2512.01675v1](https://arxiv.org/abs/2512.01675) | [PDF](https://arxiv.org/pdf/2512.01675.pdf)

**作者**: Felix Nützel, Mischa Dombrowski, Bernhard Kainz

---

## 💡 一句话要点

**提出GRASP方法，通过样本分区和残差适配器解决长尾数据下扩散模型的梯度冲突问题。**

**关键词**: `长尾学习` `扩散模型` `残差适配器` `梯度冲突` `医学图像生成` `样本分区`

## 📋 核心要点

1. 核心问题：长尾数据中罕见类别导致扩散模型梯度冲突，输出质量与多样性下降。
2. 方法要点：基于外部先验静态分区样本，注入集群特定残差适配器进行微调，避免梯度冲突。
3. 实验或效果：在MIMIC-CXR-LT等数据集上，GRASP在FID和多样性指标上优于基线，提升罕见类别性能。

## 📄 摘要（原文）

> Recent advances in text-to-image diffusion models enable high-fidelity generation across diverse prompts. However, these models falter in long-tail settings, such as medical imaging, where rare pathologies comprise a small fraction of data. This results in mode collapse: tail-class outputs lack quality and diversity, undermining the goal of synthetic data augmentation for underrepresented conditions. We pinpoint gradient conflicts between frequent head and rare tail classes as the primary culprit, a factor unaddressed by existing sampling or conditioning methods that mainly steer inference without altering the learned distribution. To resolve this, we propose GRASP: Guided Residual Adapters with Sample-wise Partitioning. GRASP uses external priors to statically partition samples into clusters that minimize intra-group gradient clashes. It then fine-tunes pre-trained models by injecting cluster-specific residual adapters into transformer feedforward layers, bypassing learned gating for stability and efficiency. On the long-tail MIMIC-CXR-LT dataset, GRASP yields superior FID and diversity metrics, especially for rare classes, outperforming baselines like vanilla fine-tuning and Mixture of Experts variants. Downstream classification on NIH-CXR-LT improves considerably for tail labels. Generalization to ImageNet-LT confirms broad applicability. Our method is lightweight, scalable, and readily integrates with diffusion pipelines.

