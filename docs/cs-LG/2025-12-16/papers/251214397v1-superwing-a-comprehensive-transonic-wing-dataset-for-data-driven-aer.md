---
layout: default
title: SuperWing: a comprehensive transonic wing dataset for data-driven aerodynamic design
---

# SuperWing: a comprehensive transonic wing dataset for data-driven aerodynamic design

**arXiv**: [2512.14397v1](https://arxiv.org/abs/2512.14397) | [PDF](https://arxiv.org/pdf/2512.14397.pdf)

**作者**: Yunjia Yang, Weishao Tang, Mengxin Liu, Nils Thuerey, Yufei Zhang, Haixin Chen

**分类**: cs.LG, physics.flu-dyn

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出SuperWing数据集以解决三维翼型数据稀缺问题，加速数据驱动的跨音速翼型气动设计。**

**关键词**: `跨音速翼型数据集` `气动设计` `机器学习代理模型` `三维翼型几何参数化` `雷诺平均Navier-Stokes模拟` `Transformer模型` `零样本泛化` `航空航天工程`

## 📋 核心要点

1. 现有三维翼型气动设计数据集稀缺且多样性不足，限制了机器学习代理模型的通用性发展。
2. 提出SuperWing数据集，通过参数化几何生成和广泛模拟条件，增强翼型形状和流动的多样性。
3. 实验显示模型在预测表面流动时误差低，并实现零样本泛化到复杂基准翼型，验证数据集有效性。

## 📝 摘要（中文）

机器学习代理模型在加速气动设计方面展现出潜力，但现有数据集稀缺且多样性有限，限制了三维翼型通用预测器的发展。本文介绍了SuperWing，这是一个全面的开放跨音速后掠翼气动数据集，包含4,239个参数化翼型几何形状和28,856个雷诺平均Navier-Stokes流场解。数据集中的翼型形状采用简化但富有表现力的几何参数化方法生成，结合了翼展方向上的翼型形状、扭转角和上反角变化，从而在不依赖基准翼型扰动的情况下增强了多样性。所有形状均在覆盖典型飞行包线的广泛马赫数和攻角范围内进行模拟。为展示数据集的实用性，我们基准测试了两个最先进的Transformer模型，它们能准确预测表面流动，并在保留样本上实现了2.5阻力计数误差。在SuperWing上预训练的模型进一步展现出对复杂基准翼型（如DLR-F6和NASA CRM）的强大零样本泛化能力，突显了数据集的多样性和实际应用潜力。

## 🔬 方法详解

论文的核心方法是构建SuperWing数据集，整体框架包括翼型几何参数化生成和流场模拟。关键技术创新点在于采用简化的几何参数化，允许翼展方向上的翼型形状、扭转角和上反角变化，从而在不依赖基准翼型扰动的情况下生成多样化的三维翼型。与现有方法的主要区别在于，SuperWing提供了大规模、高多样性的跨音速翼型数据，覆盖广泛的飞行条件，弥补了现有数据集的不足，支持数据驱动的气动设计研究。

## 📊 实验亮点

最重要的实验结果是Transformer模型在SuperWing数据集上实现了2.5阻力计数误差的准确预测，并在DLR-F6和NASA CRM等复杂基准翼型上展现出强大的零样本泛化能力，突显了数据集的多样性和实用性。

## 🎯 应用场景

该研究可应用于航空航天工程中的翼型优化设计、飞行器气动性能预测和机器学习模型训练。通过提供高质量数据集，能加速气动设计流程，降低计算成本，并促进通用代理模型的发展，具有实际工程价值。

## 📄 摘要（原文）

> Machine-learning surrogate models have shown promise in accelerating aerodynamic design, yet progress toward generalizable predictors for three-dimensional wings has been limited by the scarcity and restricted diversity of existing datasets. Here, we present SuperWing, a comprehensive open dataset of transonic swept-wing aerodynamics comprising 4,239 parameterized wing geometries and 28,856 Reynolds-averaged Navier-Stokes flow field solutions. The wing shapes in the dataset are generated using a simplified yet expressive geometry parameterization that incorporates spanwise variations in airfoil shape, twist, and dihedral, allowing for an enhanced diversity without relying on perturbations of a baseline wing. All shapes are simulated under a broad range of Mach numbers and angles of attack covering the typical flight envelope. To demonstrate the dataset's utility, we benchmark two state-of-the-art Transformers that accurately predict surface flow and achieve a 2.5 drag-count error on held-out samples. Models pretrained on SuperWing further exhibit strong zero-shot generalization to complex benchmark wings such as DLR-F6 and NASA CRM, underscoring the dataset's diversity and potential for practical usage.

