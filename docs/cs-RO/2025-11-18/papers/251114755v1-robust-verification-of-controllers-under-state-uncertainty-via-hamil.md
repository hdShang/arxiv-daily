---
layout: default
title: Robust Verification of Controllers under State Uncertainty via Hamilton-Jacobi Reachability Analysis
---

# Robust Verification of Controllers under State Uncertainty via Hamilton-Jacobi Reachability Analysis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.14755" class="toolbar-btn" target="_blank">📄 arXiv: 2511.14755v1</a>
  <a href="https://arxiv.org/pdf/2511.14755.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.14755v1" onclick="toggleFavorite(this, '2511.14755v1', 'Robust Verification of Controllers under State Uncertainty via Hamilton-Jacobi Reachability Analysis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Albert Lin, Alessandro Pinto, Somil Bansal

**分类**: cs.RO, cs.LG, eess.SY

**发布日期**: 2025-11-18

**备注**: Submitted to the 8th Annual Learning for Dynamics & Control Conference

---

## 💡 一句话要点

**提出RoVer-CoRe框架，通过Hamilton-Jacobi可达性分析实现状态不确定性下控制器的鲁棒验证。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `鲁棒验证` `Hamilton-Jacobi可达性分析` `感知不确定性` `自主系统` `控制器设计`

## 📋 核心要点

1. 现有控制器验证方法难以处理复杂的非线性、学习型控制器，且近似可达性分析可能过于保守。
2. RoVer-CoRe框架将控制器、观测函数和状态估计模块串联，构建等效闭环系统，利用HJ可达性分析进行验证。
3. 通过飞机滑行和NN漫游车导航案例研究，验证了RoVer-CoRe框架在安全验证和鲁棒控制器设计方面的有效性。

## 📝 摘要（中文）

随着基于感知的自主系统控制器在现实世界中日益普及，形式化验证其在感知不确定性下的安全性和性能至关重要。然而，此类系统的验证仍然具有挑战性，这主要是由于控制器通常是非线性、非凸、基于学习和/或是黑盒的复杂性。先前的工作提出了基于近似可达性方法的验证算法，但它们通常限制了可以处理的控制器和系统类别，或导致过于保守的分析。Hamilton-Jacobi (HJ) 可达性分析是一种流行的形式化验证工具，适用于一般的非线性系统，可以计算最坏情况下的系统不确定性下的最优可达集；然而，它在基于感知的系统中的应用目前尚未得到充分探索。在这项工作中，我们提出了RoVer-CoRe，一个通过HJ可达性分析进行控制器鲁棒验证的框架。据我们所知，RoVer-CoRe是第一个基于HJ可达性分析的框架，用于验证感知不确定性下的基于感知的系统。我们的关键见解是将系统控制器、观测函数和状态估计模块连接起来，以获得一个等效的闭环系统，该系统与现有的可达性框架兼容。在RoVer-CoRe中，我们提出了用于形式化安全验证和鲁棒控制器设计的新方法。我们通过涉及飞机滑行和基于神经网络的漫游车导航的案例研究证明了该框架的有效性。

## 🔬 方法详解

**问题定义**：论文旨在解决感知不确定性下自主系统控制器的鲁棒验证问题。现有方法，如基于近似可达性的方法，在处理复杂的非线性、学习型控制器时存在局限性，或者产生过于保守的验证结果。这些方法难以保证在实际应用中控制器的安全性。

**核心思路**：论文的核心思路是将整个感知-控制系统视为一个闭环系统，然后利用Hamilton-Jacobi (HJ) 可达性分析来验证该系统的安全性。通过将控制器、观测函数和状态估计模块连接起来，可以将复杂的感知-控制系统转化为一个更易于分析的等效系统。HJ可达性分析能够处理非线性系统，并提供在最坏情况下系统状态的可达集，从而实现鲁棒验证。

**技术框架**：RoVer-CoRe框架包含以下主要步骤：1) 将感知-控制系统建模为闭环系统，包括控制器、观测函数和状态估计模块。2) 使用HJ可达性分析计算在感知不确定性下的可达集。3) 验证可达集是否与不安全区域相交，从而判断系统的安全性。4) 基于可达性分析的结果，进行鲁棒控制器设计，以提高系统的安全性。

**关键创新**：RoVer-CoRe的关键创新在于将HJ可达性分析应用于感知-控制系统的鲁棒验证。这是首次将HJ可达性分析应用于此类系统，并提出了一种将感知模块与控制模块相结合的建模方法。与现有方法相比，RoVer-CoRe能够处理更复杂的控制器，并提供更精确的验证结果。

**关键设计**：RoVer-CoRe框架的关键设计包括：1) 如何选择合适的HJ可达性分析算法，例如半拉格朗日方法。2) 如何定义系统的状态空间和控制输入空间。3) 如何建模感知不确定性，例如使用有界噪声模型。4) 如何定义不安全区域，例如使用障碍物或目标区域。

## 📊 实验亮点

论文通过飞机滑行和基于神经网络的漫游车导航两个案例研究验证了RoVer-CoRe框架的有效性。实验结果表明，该框架能够准确地验证系统的安全性，并指导鲁棒控制器的设计。具体性能数据和对比基线在论文中进行了详细描述，展示了RoVer-CoRe相对于现有方法的优势。

## 🎯 应用场景

RoVer-CoRe框架可应用于各种自主系统，如自动驾驶汽车、无人机、机器人等，尤其适用于对安全性要求较高的场景。该框架能够帮助工程师验证和改进控制器的设计，确保系统在感知不确定性下的安全运行，降低事故风险，提高系统的可靠性。

## 📄 摘要（原文）

> As perception-based controllers for autonomous systems become increasingly popular in the real world, it is important that we can formally verify their safety and performance despite perceptual uncertainty. Unfortunately, the verification of such systems remains challenging, largely due to the complexity of the controllers, which are often nonlinear, nonconvex, learning-based, and/or black-box. Prior works propose verification algorithms that are based on approximate reachability methods, but they often restrict the class of controllers and systems that can be handled or result in overly conservative analyses. Hamilton-Jacobi (HJ) reachability analysis is a popular formal verification tool for general nonlinear systems that can compute optimal reachable sets under worst-case system uncertainties; however, its application to perception-based systems is currently underexplored. In this work, we propose RoVer-CoRe, a framework for the Robust Verification of Controllers via HJ Reachability. To the best of our knowledge, RoVer-CoRe is the first HJ reachability-based framework for the verification of perception-based systems under perceptual uncertainty. Our key insight is to concatenate the system controller, observation function, and the state estimation modules to obtain an equivalent closed-loop system that is readily compatible with existing reachability frameworks. Within RoVer-CoRe, we propose novel methods for formal safety verification and robust controller design. We demonstrate the efficacy of the framework in case studies involving aircraft taxiing and NN-based rover navigation. Code is available at the link in the footnote.

