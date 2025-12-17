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

**首次全面研究函数内联对基于机器学习的二进制分析安全影响，揭示极端内联下模型脆弱性。**

**关键词**: `函数内联` `二进制分析` `机器学习安全` `编译器优化` `模型鲁棒性` `极端内联` `LLVM` `静态特征`

## 📋 核心要点

1. 现有方法不足：函数内联对二进制分析安全影响未充分探索，ML模型鲁棒性假设可能不成立。
2. 方法要点：剖析LLVM内联决策流程，探索极端内联设置，系统评估ML模型在安全任务中的表现。
3. 实验效果：发现内联可被利用逃避ML模型，模型敏感性高，编译器设置影响显著，内联比率差异大。

## 📝 摘要（中文）

函数内联优化是现代编译器中广泛使用的转换，通过将调用点替换为被调用函数体来提升性能，但显著影响机器指令和控制流图等静态特征，这些特征对二进制分析至关重要。尽管其影响广泛，函数内联的安全影响至今尚未得到充分探索。本文首次从基于机器学习的二进制分析角度，对函数内联进行全面研究。为此，我们剖析了LLVM成本模型中的内联决策流程，并探索了编译器选项的组合，这些组合能激进地提升函数内联比率，超越标准优化级别，我们称之为极端内联。我们聚焦于五个安全相关的ML辅助二进制分析任务，使用20个独特模型，系统评估它们在极端内联场景下的鲁棒性。大量实验揭示了几个重要发现：i) 函数内联虽意图良性，但可直接或间接影响ML模型行为，可能被利用以逃避判别性或生成性ML模型；ii) 依赖静态特征的ML模型对内联高度敏感；iii) 细微的编译器设置可被利用来故意制作逃避性二进制变体；iv) 内联比率在不同应用和构建配置中差异显著，削弱了ML模型训练和评估中一致性假设。

## 🔬 方法详解

论文核心方法包括：整体框架基于LLVM编译器，通过分析其成本模型中的内联决策流程，识别影响内联比率的因素；关键技术创新点在于提出极端内联概念，通过组合编译器选项（如优化标志和启发式参数）激进提升内联比率，超越标准-O1/-O2/-O3级别；与现有方法的主要区别在于，现有研究多关注内联的性能优化，而本文首次系统研究其对ML-based二进制分析安全的影响，并引入极端内联作为攻击向量，评估模型鲁棒性。

## 📊 实验亮点

实验显示，极端内联下，ML模型在五个安全任务中表现显著下降，内联比率最高提升至标准优化的数倍，模型逃避攻击成功率增加，揭示了内联作为隐蔽攻击向量的潜力。

## 🎯 应用场景

该研究潜在应用于二进制安全分析领域，如恶意软件检测、漏洞挖掘和代码混淆防御，通过揭示内联对ML模型的脆弱性，可指导更鲁棒的模型设计和编译器安全优化，提升实际安全系统的可靠性。

## 📄 摘要（原文）

> A function inlining optimization is a widely used transformation in modern compilers, which replaces a call site with the callee's body in need. While this transformation improves performance, it significantly impacts static features such as machine instructions and control flow graphs, which are crucial to binary analysis. Yet, despite its broad impact, the security impact of function inlining remains underexplored to date. In this paper, we present the first comprehensive study of function inlining through the lens of machine learning-based binary analysis. To this end, we dissect the inlining decision pipeline within the LLVM's cost model and explore the combinations of the compiler options that aggressively promote the function inlining ratio beyond standard optimization levels, which we term extreme inlining. We focus on five ML-assisted binary analysis tasks for security, using 20 unique models to systematically evaluate their robustness under extreme inlining scenarios. Our extensive experiments reveal several significant findings: i) function inlining, though a benign transformation in intent, can (in)directly affect ML model behaviors, being potentially exploited by evading discriminative or generative ML models; ii) ML models relying on static features can be highly sensitive to inlining; iii) subtle compiler settings can be leveraged to deliberately craft evasive binary variants; and iv) inlining ratios vary substantially across applications and build configurations, undermining assumptions of consistency in training and evaluation of ML models.

