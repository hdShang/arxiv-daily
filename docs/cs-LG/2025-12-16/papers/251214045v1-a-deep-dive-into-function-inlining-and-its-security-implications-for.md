---
layout: default
title: A Deep Dive into Function Inlining and its Security Implications for ML-based Binary Analysis
---

# A Deep Dive into Function Inlining and its Security Implications for ML-based Binary Analysis

**arXiv**: [2512.14045v1](https://arxiv.org/abs/2512.14045) | [PDF](https://arxiv.org/pdf/2512.14045.pdf)

**作者**: Omar Abusabha, Jiyong Uhm, Tamer Abuhmed, Hyungjoon Koo

**分类**: cs.CR, cs.LG, cs.PL

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**首次全面研究函数内联对基于机器学习的二进制分析安全影响，揭示极端内联可被利用以规避ML模型。**

🎯 **匹配领域**: **视觉里程计**

**关键词**: `函数内联` `二进制分析` `机器学习安全` `编译器优化` `极端内联` `模型鲁棒性` `LLVM成本模型` `静态特征`

## 📋 核心要点

1. 现有方法未充分探索函数内联对基于ML的二进制分析安全影响，导致模型鲁棒性未知。
2. 论文提出极端内联概念，通过剖析LLVM成本模型和组合编译器选项来系统评估内联影响。
3. 实验发现ML模型对内联高度敏感，极端内联可被利用制作规避性二进制变体，破坏模型一致性。

## 📝 摘要（中文）

函数内联优化是现代编译器中广泛使用的转换技术，它通过将调用点替换为被调用函数体来提高性能。然而，这种转换会显著影响机器指令和控制流图等静态特征，这些特征对二进制分析至关重要。尽管其影响广泛，但函数内联的安全影响至今仍未得到充分探索。本文首次从基于机器学习的二进制分析角度对函数内联进行了全面研究。为此，我们剖析了LLVM成本模型中的内联决策流程，并探索了编译器选项的组合，这些组合能够将函数内联比率提升到标准优化级别之上，我们称之为极端内联。我们专注于五个用于安全的ML辅助二进制分析任务，使用20个独特模型来系统评估它们在极端内联场景下的鲁棒性。我们的大量实验揭示了几个重要发现：i）函数内联虽然意图上是良性转换，但可能（间接）影响ML模型行为，可能被利用来规避判别性或生成性ML模型；ii）依赖静态特征的ML模型可能对内联高度敏感；iii）微妙的编译器设置可被利用来故意制作规避性二进制变体；iv）内联比率在不同应用程序和构建配置中差异很大，破坏了ML模型训练和评估中一致性假设。

## 🔬 方法详解

论文的核心方法包括：整体框架基于LLVM编译器，通过剖析其成本模型中的内联决策流程，探索编译器选项组合以实施极端内联。关键技术创新点在于首次系统研究函数内联对ML模型的影响，并定义极端内联作为评估场景。与现有方法的主要区别在于，现有研究多关注内联的性能优化，而本文聚焦其安全影响，特别是对基于静态特征的ML模型的鲁棒性挑战，通过多任务、多模型实验设计进行全面评估。

## 📊 实验亮点

实验发现函数内联可间接影响ML模型行为，极端内联下模型敏感度高，内联比率差异大破坏训练一致性，为安全分析提供新视角。

## 🎯 应用场景

该研究在二进制安全分析领域具有重要应用价值，可用于评估和提升ML模型对编译器优化的鲁棒性，指导安全工具开发，防止攻击者利用内联等优化技术规避检测，增强软件供应链安全。

## 📄 摘要（原文）

> A function inlining optimization is a widely used transformation in modern compilers, which replaces a call site with the callee's body in need. While this transformation improves performance, it significantly impacts static features such as machine instructions and control flow graphs, which are crucial to binary analysis. Yet, despite its broad impact, the security impact of function inlining remains underexplored to date. In this paper, we present the first comprehensive study of function inlining through the lens of machine learning-based binary analysis. To this end, we dissect the inlining decision pipeline within the LLVM's cost model and explore the combinations of the compiler options that aggressively promote the function inlining ratio beyond standard optimization levels, which we term extreme inlining. We focus on five ML-assisted binary analysis tasks for security, using 20 unique models to systematically evaluate their robustness under extreme inlining scenarios. Our extensive experiments reveal several significant findings: i) function inlining, though a benign transformation in intent, can (in)directly affect ML model behaviors, being potentially exploited by evading discriminative or generative ML models; ii) ML models relying on static features can be highly sensitive to inlining; iii) subtle compiler settings can be leveraged to deliberately craft evasive binary variants; and iv) inlining ratios vary substantially across applications and build configurations, undermining assumptions of consistency in training and evaluation of ML models.

