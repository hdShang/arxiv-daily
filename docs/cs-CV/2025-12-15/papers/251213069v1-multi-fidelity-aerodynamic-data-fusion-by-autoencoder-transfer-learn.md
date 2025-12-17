---
layout: default
title: Multi-fidelity aerodynamic data fusion by autoencoder transfer learning
---

# Multi-fidelity aerodynamic data fusion by autoencoder transfer learning

**arXiv**: [2512.13069v1](https://arxiv.org/abs/2512.13069) | [PDF](https://arxiv.org/pdf/2512.13069.pdf)

**作者**: Javier Nieto-Centenero, Esther Andrés, Rodrigo Castellanos

---

## 💡 一句话要点

**提出基于自编码器迁移学习与多分割保形预测的多保真度框架，以解决数据稀缺下气动预测的准确性与不确定性量化问题。**

**关键词**: `多保真度数据融合` `自编码器迁移学习` `不确定性量化` `气动预测` `数据稀缺建模`

## 📋 核心要点

1. 核心问题：高保真度气动模拟计算成本高，数据稀缺限制数据驱动建模的准确性。
2. 方法要点：利用低保真度数据学习潜在物理表示，通过迁移学习微调解码器，结合多分割保形预测进行不确定性量化。
3. 实验或效果：在NACA翼型和跨音速机翼数据库上，模型以极少高保真度数据实现高精度压力预测，不确定性覆盖超过95%。

## 📄 摘要（原文）

> Accurate aerodynamic prediction often relies on high-fidelity simulations; however, their prohibitive computational costs severely limit their applicability in data-driven modeling. This limitation motivates the development of multi-fidelity strategies that leverage inexpensive low-fidelity information without compromising accuracy. Addressing this challenge, this work presents a multi-fidelity deep learning framework that combines autoencoder-based transfer learning with a newly developed Multi-Split Conformal Prediction (MSCP) strategy to achieve uncertainty-aware aerodynamic data fusion under extreme data scarcity. The methodology leverages abundant Low-Fidelity (LF) data to learn a compact latent physics representation, which acts as a frozen knowledge base for a decoder that is subsequently fine-tuned using scarce HF samples. Tested on surface-pressure distributions for NACA airfoils (2D) and a transonic wing (3D) databases, the model successfully corrects LF deviations and achieves high-accuracy pressure predictions using minimal HF training data. Furthermore, the MSCP framework produces robust, actionable uncertainty bands with pointwise coverage exceeding 95%. By combining extreme data efficiency with uncertainty quantification, this work offers a scalable and reliable solution for aerodynamic regression in data-scarce environments.

