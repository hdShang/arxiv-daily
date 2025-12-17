---
layout: default
title: Causal Structure Learning for Dynamical Systems with Theoretical Score Analysis
---

# Causal Structure Learning for Dynamical Systems with Theoretical Score Analysis

**arXiv**: [2512.14361v1](https://arxiv.org/abs/2512.14361) | [PDF](https://arxiv.org/pdf/2512.14361.pdf)

**作者**: Nicholas Tagliapietra, Katharina Ensinger, Christoph Zimmer, Osman Mian

**分类**: cs.LG, cs.AI, math.DS

**发布日期**: 2025-12-16

**备注**: Accepted as Oral at AAAI 2026 Conference

---

## 💡 一句话要点

**提出CaDyT方法，基于差分因果模型与高斯过程推理，解决动态系统中连续时间因果发现难题。**

🎯 **匹配领域**: **视觉里程计** **强化学习**

**关键词**: `因果发现` `动态系统` `连续时间建模` `高斯过程` `差分因果模型` `算法马尔可夫条件` `最小描述长度` `不规则采样数据`

## 📋 核心要点

1. 现有方法在动态系统因果发现中面临挑战：时间离散化导致不规则采样数据性能差，或忽略底层因果关系。
2. CaDyT基于差分因果模型，利用高斯过程推理建模连续时间动态，通过贪婪搜索识别因果结构。
3. 实验表明，CaDyT在规则和不规则采样数据上均优于现有方法，发现的网络更接近真实动态。

## 📝 摘要（中文）

现实世界系统根据其潜在因果关系在连续时间内演化，但其动态特性往往未知。现有学习方法通常要么离散化时间——导致在不规则采样数据上性能不佳，要么忽略底层因果关系。我们提出CaDyT，一种用于动态系统因果发现的新方法，同时应对这两个挑战。与使用离散时间动态贝叶斯网络建模该问题的最先进因果发现方法不同，我们的公式基于差分因果模型，该模型允许对系统的连续性质进行更温和的假设建模。CaDyT利用精确的高斯过程推理来建模连续时间动态，这更符合底层动态过程。我们提出了一种实用的实例化方法，通过由算法马尔可夫条件和最小描述长度原则指导的贪婪搜索来识别因果结构。我们的实验表明，CaDyT在规则和不规则采样数据上均优于最先进的方法，发现的因果网络更接近真实的底层动态。

## 🔬 方法详解

CaDyT的整体框架基于差分因果模型，通过高斯过程推理精确建模连续时间动态，避免了传统离散时间方法的局限性。关键技术创新点在于结合差分因果模型的温和假设与高斯过程推理的灵活性，实现对系统连续性质的更准确描述。与现有方法的主要区别在于：不同于使用离散时间动态贝叶斯网络的方法，CaDyT直接处理连续时间，更符合实际动态过程；同时，其实用实例化通过算法马尔可夫条件和最小描述长度原则指导的贪婪搜索，高效识别因果结构。

## 📊 实验亮点

CaDyT在规则和不规则采样数据上的实验均优于最先进方法，显著提升了因果网络发现的准确性，更接近真实底层动态，验证了其在连续时间建模中的有效性。

## 🎯 应用场景

该研究可应用于需要建模连续时间动态的领域，如生物医学信号分析、金融时间序列预测、机器人控制和环境监测，帮助揭示系统内在因果关系，提升模型解释性和预测准确性。

## 📄 摘要（原文）

> Real world systems evolve in continuous-time according to their underlying causal relationships, yet their dynamics are often unknown. Existing approaches to learning such dynamics typically either discretize time -- leading to poor performance on irregularly sampled data -- or ignore the underlying causality. We propose CaDyT, a novel method for causal discovery on dynamical systems addressing both these challenges. In contrast to state-of-the-art causal discovery methods that model the problem using discrete-time Dynamic Bayesian networks, our formulation is grounded in Difference-based causal models, which allow milder assumptions for modeling the continuous nature of the system. CaDyT leverages exact Gaussian Process inference for modeling the continuous-time dynamics which is more aligned with the underlying dynamical process. We propose a practical instantiation that identifies the causal structure via a greedy search guided by the Algorithmic Markov Condition and Minimum Description Length principle. Our experiments show that CaDyT outperforms state-of-the-art methods on both regularly and irregularly-sampled data, discovering causal networks closer to the true underlying dynamics.

