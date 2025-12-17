---
layout: default
title: PVeRA: Probabilistic Vector-Based Random Matrix Adaptation
---

# PVeRA: Probabilistic Vector-Based Random Matrix Adaptation

**arXiv**: [2512.07703v1](https://arxiv.org/abs/2512.07703) | [PDF](https://arxiv.org/pdf/2512.07703.pdf)

**作者**: Leo Fillioux, Enzo Ferrante, Paul-Henry Cournède, Maria Vakalopoulou, Stergios Christodoulidis

---

## 💡 一句话要点

**提出PVeRA概率向量适配器，以增强基础模型在小数据高效适应中的性能。**

**关键词**: `参数高效适应` `概率适配器` `基础模型` `低秩矩阵` `VTAB-1k基准`

## 📋 核心要点

1. 核心问题：基础模型适应需大量数据与计算，现有方法如VeRA适配器在参数效率上仍有局限。
2. 方法要点：将VeRA的低秩矩阵修改为概率版本，处理输入模糊性并支持训练与测试时的不同采样配置。
3. 实验或效果：在VTAB-1k基准测试中，PVeRA优于VeRA及其他适配器，代码已开源。

## 📄 摘要（原文）

> Large foundation models have emerged in the last years and are pushing performance boundaries for a variety of tasks. Training or even finetuning such models demands vast datasets and computational resources, which are often scarce and costly. Adaptation methods provide a computationally efficient solution to address these limitations by allowing such models to be finetuned on small amounts of data and computing power. This is achieved by appending new trainable modules to frozen backbones with only a fraction of the trainable parameters and fitting only these modules on novel tasks. Recently, the VeRA adapter was shown to excel in parameter-efficient adaptations by utilizing a pair of frozen random low-rank matrices shared across all layers. In this paper, we propose PVeRA, a probabilistic version of the VeRA adapter, which modifies the low-rank matrices of VeRA in a probabilistic manner. This modification naturally allows handling inherent ambiguities in the input and allows for different sampling configurations during training and testing. A comprehensive evaluation was performed on the VTAB-1k benchmark and seven adapters, with PVeRA outperforming VeRA and other adapters. Our code for training models with PVeRA and benchmarking all adapters is available https://github.com/leofillioux/pvera.

