---
layout: default
title: Physically consistent model learning for reaction-diffusion systems
---

# Physically consistent model learning for reaction-diffusion systems

**arXiv**: [2512.14240v1](https://arxiv.org/abs/2512.14240) | [PDF](https://arxiv.org/pdf/2512.14240.pdf)

**作者**: Erion Morina, Martin Holler

**分类**: cs.LG, math.AP, math.OC

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出物理一致的反应-扩散系统数据驱动建模方法，确保质量守恒和准正性约束**

**关键词**: `反应-扩散系统` `物理一致性建模` `数据驱动模型` `质量守恒` `准正性` `正则化学习` `偏微分方程学习` `模型适定性`

## 📋 核心要点

1. 现有数据驱动建模方法常忽略物理约束，导致反应-扩散系统模型可能违反质量守恒和准正性等基本物理原理。
2. 提出系统修改参数化反应项的技术，将质量守恒和准正性直接嵌入学习过程，确保模型物理一致性。
3. 理论证明学习解收敛到唯一正则化最小化解，并提供准正性函数逼近结果，提升模型可靠性和适定性。

## 📝 摘要（中文）

本文解决了从数据中学习反应-扩散系统同时确保学习模型的物理一致性和适定性的问题。基于结构化模型学习的正则化框架，我们专注于学习参数化反应项，并研究如何将关键物理属性（如质量守恒和准正性）直接纳入学习过程。我们的主要贡献有两个方面：首先，我们提出了系统修改给定参数化反应项类别的技术，使所得项固有地满足质量守恒和准正性，确保学习的反应-扩散系统保持非负性并遵循物理原理。这些修改还保证了所得偏微分方程在额外正则性和增长条件下的适定性。其次，我们使用这些物理一致的反应项，将基于正则化的模型学习的现有理论结果扩展到反应-扩散系统。具体来说，我们证明了即使强制执行守恒定律和准正性，学习问题的解也会收敛到极限系统的唯一正则化最小化解。此外，我们提供了准正性函数的逼近结果，这对于构建物理一致的参数化至关重要。这些结果推动了与基本物理定律一致的可解释且可靠的数据驱动反应-扩散系统模型的发展。

## 🔬 方法详解

论文基于正则化框架进行结构化模型学习，核心方法包括两个关键技术：一是系统修改参数化反应项类别，通过数学构造使反应项固有满足质量守恒和准正性，从而确保学习到的反应-扩散系统保持非负性并遵循物理原理；二是扩展理论分析，将现有正则化模型学习理论应用于这些物理一致的反应项，证明学习问题的解收敛性。与现有方法的主要区别在于直接整合物理约束到学习过程中，而非后处理或忽略约束，这增强了模型的物理可解释性和适定性。

## 📊 实验亮点

理论证明学习解在强制执行质量守恒和准正性约束下仍收敛到唯一正则化最小化解，提供了准正性函数的逼近结果，确保模型物理一致性和适定性，提升了数据驱动反应-扩散系统模型的可靠性和可解释性。

## 🎯 应用场景

该研究可应用于生物化学过程模拟、生态学种群动力学、材料科学中的扩散现象等领域，为开发可靠的数据驱动模型提供基础，有助于预测和优化复杂物理系统行为。

## 📄 摘要（原文）

> This paper addresses the problem of learning reaction-diffusion (RD) systems from data while ensuring physical consistency and well-posedness of the learned models. Building on a regularization-based framework for structured model learning, we focus on learning parameterized reaction terms and investigate how to incorporate key physical properties, such as mass conservation and quasipositivity, directly into the learning process. Our main contributions are twofold: First, we propose techniques to systematically modify a given class of parameterized reaction terms such that the resulting terms inherently satisfy mass conservation and quasipositivity, ensuring that the learned RD systems preserve non-negativity and adhere to physical principles. These modifications also guarantee well-posedness of the resulting PDEs under additional regularity and growth conditions. Second, we extend existing theoretical results on regularization-based model learning to RD systems using these physically consistent reaction terms. Specifically, we prove that solutions to the learning problem converge to a unique, regularization-minimizing solution of a limit system even when conservation laws and quasipositivity are enforced. In addition, we provide approximation results for quasipositive functions, essential for constructing physically consistent parameterizations. These results advance the development of interpretable and reliable data-driven models for RD systems that align with fundamental physical laws.

