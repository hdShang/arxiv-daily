---
layout: default
title: "SAFE: Multitask Failure Detection for Vision-Language-Action Models"
---

# SAFE: Multitask Failure Detection for Vision-Language-Action Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.09937" class="toolbar-btn" target="_blank">📄 arXiv: 2506.09937v2</a>
  <a href="https://arxiv.org/pdf/2506.09937.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.09937v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.09937v2', 'SAFE: Multitask Failure Detection for Vision-Language-Action Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qiao Gu, Yuanliang Ju, Shengxiang Sun, Igor Gilitschenski, Haruki Nishimura, Masha Itkina, Florian Shkurti

**分类**: cs.RO, cs.AI

**发布日期**: 2025-06-11 (更新: 2025-10-30)

**备注**: NeurIPS 2025 camera ready. Project Page: https://vla-safe.github.io/

---

## 💡 一句话要点

**提出SAFE以解决多任务视觉-语言-动作模型的失败检测问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言-动作` `失败检测` `多任务学习` `机器人安全` `深度学习`

## 📋 核心要点

1. 现有的失败检测器仅在特定任务上训练，无法有效泛化到新任务和环境中，导致机器人在新场景下的操作风险增加。
2. 论文提出了SAFE，一个基于VLA内部特征的失败检测器，能够预测任务失败的可能性，从而提高机器人在多任务环境中的安全性。
3. 实验结果表明，SAFE在多种政策架构下均表现出色，达到了最先进的失败检测性能，并在准确性与检测时间之间实现了最佳平衡。

## 📝 摘要（中文）

尽管视觉-语言-动作模型（VLA）在多种操作任务中展现了良好的机器人行为，但在新任务上的成功率有限。为使这些策略能够安全地与环境互动，需要一个能够及时发出警报的失败检测器，以便机器人能够停止、回溯或请求帮助。现有的失败检测器仅在特定任务上进行训练和测试，而通用的VLA需要检测器能够在未见过的任务和新环境中进行泛化。本文提出了多任务失败检测问题，并提出了SAFE，一个针对通用机器人策略的失败检测器。我们分析了VLA特征空间，发现VLA对任务成功和失败具有足够的高层知识，这种知识在不同任务中是通用的。基于这一洞察，我们设计了SAFE，从VLA内部特征中学习并预测一个标量，指示任务失败的可能性。SAFE在成功和失败的回放上进行训练，并在未见过的任务上进行评估。

## 🔬 方法详解

**问题定义**：本文解决的是多任务视觉-语言-动作模型在新任务中的失败检测问题。现有方法的痛点在于其训练和测试仅限于特定任务，导致无法有效应对未知任务的失败情况。

**核心思路**：SAFE的核心思路是利用VLA的内部特征进行学习，提取出与任务成功和失败相关的高层知识，从而预测任务失败的可能性。通过这种方式，SAFE能够在多种任务中进行泛化，提升失败检测的准确性。

**技术框架**：SAFE的整体架构包括特征提取模块、失败预测模块和训练模块。特征提取模块从VLA中提取内部特征，失败预测模块基于这些特征输出一个标量，表示任务失败的可能性，训练模块则通过成功和失败的回放数据进行优化。

**关键创新**：SAFE的主要创新在于其能够从VLA的内部特征中学习，并实现对未见任务的失败检测。这与现有方法的本质区别在于，现有方法通常依赖于特定任务的数据进行训练，缺乏泛化能力。

**关键设计**：在设计中，SAFE采用了适应性损失函数，以平衡成功和失败样本的影响。此外，网络结构经过优化，以确保在不同政策架构下均能有效运行。

## 📊 实验亮点

实验结果显示，SAFE在多种基线模型上均表现出色，达到了最先进的失败检测性能。在准确性和检测时间之间，SAFE实现了最佳的权衡，具体性能数据未详细列出，但相较于其他方法有显著提升。

## 🎯 应用场景

该研究的潜在应用领域包括机器人操作、自动化制造和智能家居等场景。通过提高机器人在未知任务中的安全性，SAFE能够显著降低操作风险，提升用户信任度，并推动机器人技术的广泛应用。

## 📄 摘要（原文）

> While vision-language-action models (VLAs) have shown promising robotic behaviors across a diverse set of manipulation tasks, they achieve limited success rates when deployed on novel tasks out of the box. To allow these policies to safely interact with their environments, we need a failure detector that gives a timely alert such that the robot can stop, backtrack, or ask for help. However, existing failure detectors are trained and tested only on one or a few specific tasks, while generalist VLAs require the detector to generalize and detect failures also in unseen tasks and novel environments. In this paper, we introduce the multitask failure detection problem and propose SAFE, a failure detector for generalist robot policies such as VLAs. We analyze the VLA feature space and find that VLAs have sufficient high-level knowledge about task success and failure, which is generic across different tasks. Based on this insight, we design SAFE to learn from VLA internal features and predict a single scalar indicating the likelihood of task failure. SAFE is trained on both successful and failed rollouts and is evaluated on unseen tasks. SAFE is compatible with different policy architectures. We test it on OpenVLA, $π_0$, and $π_0$-FAST in both simulated and real-world environments extensively. We compare SAFE with diverse baselines and show that SAFE achieves state-of-the-art failure detection performance and the best trade-off between accuracy and detection time using conformal prediction. More qualitative results and code can be found at the project webpage: https://vla-safe.github.io/

