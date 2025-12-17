---
layout: default
title: Going with the Speed of Sound: Pushing Neural Surrogates into Highly-turbulent Transonic Regimes
---

# Going with the Speed of Sound: Pushing Neural Surrogates into Highly-turbulent Transonic Regimes

**arXiv**: [2511.21474v1](https://arxiv.org/abs/2511.21474) | [PDF](https://arxiv.org/pdf/2511.21474.pdf)

**作者**: Fabian Paischer, Leo Cotteleer, Yann Dreze, Richard Kurle, Dylan Rubini, Maurits Bleeker, Tobias Kronlachner, Johannes Brandstetter

---

## 💡 一句话要点

**提出AB-UPT神经代理模型以解决跨音速3D翼型气动优化问题**

**关键词**: `神经代理模型` `跨音速气动` `3D翼型数据集` `升阻优化` `OOD泛化`

## 📋 核心要点

1. 核心问题：现有神经代理模型难以处理跨音速高非线性可压缩流和3D效应如翼尖涡
2. 方法要点：构建包含3万样本的3D翼型跨音速CFD数据集，支持升阻系数计算
3. 实验或效果：AB-UPT在未见翼型上泛化良好，能近似物理一致的升阻帕累托前沿

## 📄 摘要（原文）

> The widespread use of neural surrogates in automotive aerodynamics, enabled by datasets such as DrivAerML and DrivAerNet++, has primarily focused on bluff-body flows with large wakes. Extending these methods to aerospace, particularly in the transonic regime, remains challenging due to the high level of non-linearity of compressible flows and 3D effects such as wingtip vortices. Existing aerospace datasets predominantly focus on 2D airfoils, neglecting these critical 3D phenomena. To address this gap, we present a new dataset of CFD simulations for 3D wings in the transonic regime. The dataset comprises volumetric and surface-level fields for around $30,000$ samples with unique geometry and inflow conditions. This allows computation of lift and drag coefficients, providing a foundation for data-driven aerodynamic optimization of the drag-lift Pareto front. We evaluate several state-of-the-art neural surrogates on our dataset, including Transolver and AB-UPT, focusing on their out-of-distribution (OOD) generalization over geometry and inflow variations. AB-UPT demonstrates strong performance for transonic flowfields and reproduces physically consistent drag-lift Pareto fronts even for unseen wing configurations. Our results demonstrate that AB-UPT can approximate drag-lift Pareto fronts for unseen geometries, highlighting its potential as an efficient and effective tool for rapid aerodynamic design exploration. To facilitate future research, we open-source our dataset at https://huggingface.co/datasets/EmmiAI/Emmi-Wing.

