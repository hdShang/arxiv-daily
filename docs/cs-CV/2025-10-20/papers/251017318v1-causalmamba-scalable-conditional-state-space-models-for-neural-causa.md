---
layout: default
title: "CausalMamba: Scalable Conditional State Space Models for Neural Causal Inference"
---

# CausalMamba: Scalable Conditional State Space Models for Neural Causal Inference

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.17318" class="toolbar-btn" target="_blank">📄 arXiv: 2510.17318v1</a>
  <a href="https://arxiv.org/pdf/2510.17318.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.17318v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.17318v1', 'CausalMamba: Scalable Conditional State Space Models for Neural Causal Inference')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sangyoon Bae, Jiook Cha

**分类**: cs.CV

**发布日期**: 2025-10-20

---

## 💡 一句话要点

**CausalMamba：用于神经因果推断的可扩展条件状态空间模型**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `神经因果推断` `fMRI` `BOLD信号` `状态空间模型` `Mamba架构` `动态因果建模` `神经科学`

## 📋 核心要点

1. 现有基于fMRI的因果推断方法，如DCM，面临BOLD信号扭曲和计算复杂度高的挑战。
2. CausalMamba将因果推断分解为BOLD反卷积和条件Mamba架构的因果图推断两个阶段。
3. 实验表明，CausalMamba在模拟和真实fMRI数据上均优于传统方法，并能揭示大脑网络动态。

## 📝 摘要（中文）

本文提出CausalMamba，一个可扩展的框架，旨在解决基于fMRI的因果推断中的根本性限制：从血流动力学扭曲的BOLD信号中推断神经因果关系的病态性，以及现有方法（如动态因果建模DCM）的计算复杂性。我们的方法将这个复杂的逆问题分解为两个易于处理的阶段：BOLD反卷积以恢复潜在的神经活动，然后使用一种新颖的条件Mamba架构进行因果图推断。在模拟数据上，CausalMamba比DCM实现了高37%的准确率。关键的是，当应用于真实的task fMRI数据时，我们的方法以88%的保真度恢复了公认的神经通路，而传统方法在超过99%的受试者中未能识别出这些规范回路。此外，我们对工作记忆数据的网络分析表明，大脑根据刺激策略性地转移其主要的因果枢纽，招募执行或显著性网络——传统方法无法检测到这种复杂的重构。这项工作为神经科学家提供了一种用于大规模因果推断的实用工具，可以捕捉认知功能的基本回路模式和灵活的网络动态。

## 🔬 方法详解

**问题定义**：论文旨在解决基于fMRI的神经因果推断问题。现有方法，如动态因果建模（DCM），由于BOLD信号的血流动力学扭曲以及计算复杂性，难以准确有效地推断神经活动之间的因果关系。DCM等方法在处理大规模数据时计算成本过高，且对BOLD信号的建模过于简化，导致推断结果不准确。

**核心思路**：CausalMamba的核心思路是将复杂的因果推断问题分解为两个更容易处理的步骤：首先，通过BOLD反卷积恢复潜在的神经活动；然后，利用一种新颖的条件Mamba架构，基于恢复的神经活动进行因果图推断。这种分解降低了问题的复杂度，并允许使用更高效的模型进行因果关系建模。

**技术框架**：CausalMamba的整体框架包含两个主要阶段：1) BOLD反卷积：使用某种反卷积技术（论文中未明确指定具体方法，可能使用了现有的反卷积算法）从fMRI的BOLD信号中估计潜在的神经活动。2) 因果图推断：使用条件Mamba架构，基于反卷积得到的神经活动，推断神经区域之间的因果关系。条件Mamba架构接收神经活动数据作为输入，并输出一个表示神经区域之间因果连接的图。

**关键创新**：CausalMamba的关键创新在于使用条件Mamba架构进行因果图推断。Mamba是一种新型的状态空间模型，具有高效的计算能力和长程依赖建模能力，使其能够处理fMRI数据中的复杂时间动态。此外，将因果推断分解为BOLD反卷积和因果图推断两个阶段，简化了问题，并允许针对每个阶段使用更合适的模型。

**关键设计**：论文中没有详细描述BOLD反卷积的具体方法，可能使用了现有的反卷积算法。条件Mamba架构的具体结构和参数设置也未详细说明，但可以推断其输入为反卷积后的神经活动数据，输出为因果图。损失函数的设计可能包括对因果图结构的约束，例如稀疏性约束，以鼓励模型学习更简洁的因果关系。

## 📊 实验亮点

CausalMamba在模拟数据上比DCM提高了37%的准确率。在真实task fMRI数据上，CausalMamba以88%的保真度恢复了公认的神经通路，而传统方法在超过99%的受试者中未能识别出这些规范回路。对工作记忆数据的网络分析揭示了大脑根据刺激策略性地转移其主要的因果枢纽，招募执行或显著性网络，这种复杂的重构是传统方法无法检测到的。

## 🎯 应用场景

CausalMamba为神经科学研究提供了一种强大的工具，可用于大规模神经因果推断。它可以应用于研究各种认知功能（如工作记忆、注意力和决策）的神经机制，揭示大脑不同区域之间的因果关系。该方法还可以用于诊断和治疗神经系统疾病，例如阿尔茨海默病和精神分裂症，通过识别疾病相关的神经回路异常，为精准治疗提供依据。未来，CausalMamba有望促进我们对大脑功能的深入理解，并推动神经科学和临床医学的发展。

## 📄 摘要（原文）

> We introduce CausalMamba, a scalable framework that addresses fundamental limitations in fMRI-based causal inference: the ill-posed nature of inferring neural causality from hemodynamically distorted BOLD signals and the computational intractability of existing methods like Dynamic Causal Modeling (DCM). Our approach decomposes this complex inverse problem into two tractable stages: BOLD deconvolution to recover latent neural activity, followed by causal graph inference using a novel Conditional Mamba architecture. On simulated data, CausalMamba achieves 37% higher accuracy than DCM. Critically, when applied to real task fMRI data, our method recovers well-established neural pathways with 88% fidelity, whereas conventional approaches fail to identify these canonical circuits in over 99% of subjects. Furthermore, our network analysis of working memory data reveals that the brain strategically shifts its primary causal hub-recruiting executive or salience networks depending on the stimulus-a sophisticated reconfiguration that remains undetected by traditional methods. This work provides neuroscientists with a practical tool for large-scale causal inference that captures both fundamental circuit motifs and flexible network dynamics underlying cognitive function.

