---
layout: default
title: Offline Multi-Task Multi-Objective Data-Driven Evolutionary Algorithm with Language Surrogate Model and Implicit Q-Learning
---

# Offline Multi-Task Multi-Objective Data-Driven Evolutionary Algorithm with Language Surrogate Model and Implicit Q-Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.15149" class="toolbar-btn" target="_blank">📄 arXiv: 2512.15149v1</a>
  <a href="https://arxiv.org/pdf/2512.15149.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.15149v1" onclick="toggleFavorite(this, '2512.15149v1', 'Offline Multi-Task Multi-Objective Data-Driven Evolutionary Algorithm with Language Surrogate Model and Implicit Q-Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xian-Rong Zhang, Yue-Jiao Gong, Zeyuan Ma, Jun Zhang

**分类**: cs.NE, cs.AI

**发布日期**: 2025-12-17

**备注**: 16 pages

---

## 💡 一句话要点

**提出Q-MetaSur，利用语言模型和强化学习解决离线多任务多目标优化问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多任务优化` `多目标优化` `代理模型` `大型语言模型` `强化学习` `离线学习` `进化算法`

## 📋 核心要点

1. 现有代理建模方法在复杂的多子目标优化问题中存在局限性，需要重复且繁琐的近似。
2. Q-MetaSur将多目标优化问题转化为序列到序列建模，利用大型语言模型进行编码和解码，实现统一的代理学习。
3. 通过两阶段离线训练，结合监督学习和强化学习，Q-MetaSur在CEC2019基准测试中表现优于现有方法。

## 📝 摘要（中文）

本文提出了一种名为Q-MetaSur的即插即用代理建模方案，旨在为多任务多目标优化（MTMOO）提供统一和通用的代理学习。该方法将目标近似转化为序列到序列的建模，其中MTMOO问题通过文本标记化表示。为了在这种自回归建模下运行，引入了一个基于大型语言模型的代理模型，该模型首先编码MTMOO实例，然后解码未见过的决策变量的目标值。为了确保模型训练的稳定性，提出了一种两阶段离线训练策略，该策略结合了监督调优和强化学习微调，首先利用离线数据集来拟合现有知识，然后利用强化学习来增强模型的泛化性能。在CEC2019基准上的大量实验结果表明，Q-MetaSur不仅在目标近似精度方面优于代表性的代理基线，而且还有助于底层进化算法实现期望的优化收敛和改进的帕累托最优性。

## 🔬 方法详解

**问题定义**：论文旨在解决离线多任务多目标优化（MTMOO）问题。现有代理建模方法在处理具有多个子目标的复杂优化问题时，需要进行重复且繁琐的近似，效率较低，且泛化能力有限。

**核心思路**：论文的核心思路是将MTMOO问题转化为序列到序列的建模问题，利用大型语言模型（LLM）学习MTMOO问题的通用表示，并预测目标值。通过文本标记化将MTMOO问题转化为LLM可以处理的序列数据，从而实现统一的代理学习。

**技术框架**：Q-MetaSur包含以下主要模块：1) MTMOO问题文本标记化模块，将MTMOO实例转化为文本序列；2) 基于LLM的代理模型，用于编码MTMOO实例并解码目标值；3) 两阶段离线训练策略，包括监督调优和强化学习微调。整体流程为：首先使用离线数据集进行监督学习，拟合现有知识；然后利用强化学习微调模型，提升泛化性能。

**关键创新**：最重要的技术创新点在于将多目标优化问题转化为序列到序列建模，并利用大型语言模型学习通用表示。与现有方法相比，Q-MetaSur无需针对每个MTMOO问题单独设计代理模型，而是通过学习通用表示，实现更高效、更通用的代理学习。

**关键设计**：关键设计包括：1) 使用文本标记化表示MTMOO问题，例如将决策变量、目标函数等信息转化为文本token；2) 使用Transformer架构的LLM作为代理模型，例如BERT或GPT；3) 两阶段训练策略，监督学习阶段使用均方误差（MSE）等损失函数，强化学习阶段使用Implicit Q-Learning (IQL) 算法，优化模型的泛化性能。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15149v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15149v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15149v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

在CEC2019基准测试中，Q-MetaSur在目标近似精度方面优于代表性的代理基线。实验结果表明，Q-MetaSur不仅能够更准确地预测目标值，而且能够帮助底层进化算法实现更好的优化收敛性和帕累托最优性，显著提升了优化性能。

## 🎯 应用场景

Q-MetaSur可应用于各种需要进行昂贵优化的领域，例如材料设计、药物发现、工程优化等。通过降低优化过程的计算成本，可以加速新材料和新产品的研发，提高工程设计的效率，具有重要的实际应用价值和潜在的经济效益。

## 📄 摘要（原文）

> Data-driven evolutionary algorithms has shown surprising results in addressing expensive optimization problems through robust surrogate modeling. Though promising, existing surrogate modeling schemes may encounter limitations in complex optimization problems with many sub-objectives, which rely on repeated and tedious approximation. To address such technical gap, we propose Q-MetaSur as a plug-and-play surrogate modeling scheme capable of providing unified and generalized surrogate learning. Specifically, we consider multi-task-multi-objective optimization~(MTMOO) in offline setting. Several key designs are proposed: 1) we transform objective approximation into sequence-to-sequence modeling where MTMOO problem can be represented by tenxual tokenization. To operate under such auto-regressive modeling, we introduce a Large Language Model-based surrogate model that first encodes a MTMOO instance and then decodes objective values of unseen decision variables. To ensure stability in training the proposed model, we propose a two-stage offline training strategy that operates as a synergy of supervised tuning and RL fine-tuning, which first exploits offline dataset to fit existing knowledge and then leverages RL to enhance model's generalization performance. Extensive empirical results on the CEC2019 benchmark demonstrate that Q-MetaSur not only outperforms representative surrogate baselines in objective approximation accuracy, but also helps underlying evolutionary algorithms achieve both desired optimization convergence and improved pareto optimality.

