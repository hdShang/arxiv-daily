---
layout: default
title: Expertise need not monopolize: Action-Specialized Mixture of Experts for Vision-Language-Action Learning
---

# Expertise need not monopolize: Action-Specialized Mixture of Experts for Vision-Language-Action Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.14300" class="toolbar-btn" target="_blank">📄 arXiv: 2510.14300v1</a>
  <a href="https://arxiv.org/pdf/2510.14300.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.14300v1" onclick="toggleFavorite(this, '2510.14300v1', 'Expertise need not monopolize: Action-Specialized Mixture of Experts for Vision-Language-Action Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Weijie Shen, Yitian Liu, Yuhao Wu, Zhixuan Liang, Sijia Gu, Dehui Wang, Tian Nian, Lei Xu, Yusen Qin, Jiangmiao Pang, Xinping Guan, Xiaokang Yang, Yao Mu

**分类**: cs.RO, cs.AI

**发布日期**: 2025-10-16

---

## 💡 一句话要点

**提出AdaMoE，一种动作专用混合专家模型，提升VLA模型在机器人操作任务中的性能和效率。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言-动作学习` `混合专家模型` `机器人操作` `模型扩展` `预训练模型`

## 📋 核心要点

1. 现有VLA模型扩展面临计算资源需求大和机器人数据稀缺的挑战，难以充分利用预训练权重。
2. AdaMoE通过继承预训练权重并引入稀疏激活的MoE层扩展动作专家，实现高效的模型扩展。
3. 实验表明，AdaMoE在多个基准测试和真实世界机器人操作中显著优于基线模型，验证了其有效性。

## 📝 摘要（中文）

视觉-语言-动作(VLA)模型正在快速发展，并在机器人操作任务中展现出良好的能力。然而，扩展VLA模型面临几个关键挑战：(1)从头开始训练新的VLA模型需要大量的计算资源和广泛的数据集。鉴于目前机器人数据的稀缺性，在扩展过程中充分利用预训练的VLA模型权重变得尤为重要。(2)实时控制需要仔细平衡模型容量与计算效率。为了解决这些挑战，我们提出AdaMoE，一种混合专家(MoE)架构，它继承了密集VLA模型的预训练权重，并通过将前馈层替换为稀疏激活的MoE层来扩展动作专家。AdaMoE采用解耦技术，通过一个独立于传统路由器的缩放适配器，将专家选择与专家权重解耦。这使得专家可以基于任务相关性进行选择，并以独立控制的权重做出贡献，从而实现协作专家利用，而不是赢者通吃的模式。我们的方法表明，专业知识不必垄断。相反，通过协作专家利用，我们可以在保持计算效率的同时实现卓越的性能。AdaMoE在关键基准测试中始终优于基线模型，在LIBERO上实现了1.8%的性能提升，在RoboTwin上实现了9.3%的性能提升。最重要的是，在真实世界实验中实现了21.5%的显著改进，验证了其在机器人操作任务中的实际有效性。

## 🔬 方法详解

**问题定义**：现有视觉-语言-动作(VLA)模型在扩展时面临两个主要问题：一是训练成本高昂，需要大量计算资源和数据；二是实时控制对计算效率有较高要求，需要平衡模型容量和效率。现有方法难以充分利用预训练模型权重，且难以在保证性能的同时实现高效计算。

**核心思路**：AdaMoE的核心思路是利用混合专家(MoE)架构，并继承预训练的VLA模型权重。通过将动作专家中的前馈层替换为稀疏激活的MoE层，实现模型容量的扩展，同时保持计算效率。此外，AdaMoE引入解耦技术，将专家选择和专家权重解耦，允许专家协同工作，而非赢者通吃。

**技术框架**：AdaMoE的整体架构基于现有的VLA模型，主要改进在于动作专家部分。它包含以下主要模块：1) 预训练VLA模型：作为AdaMoE的初始化权重；2) MoE层：替换动作专家中的前馈层，实现模型容量扩展；3) 路由器(Router)：根据输入选择激活的专家；4) 缩放适配器(Scale Adapter)：独立控制每个专家的权重，实现专家协作。

**关键创新**：AdaMoE的关键创新在于解耦专家选择和专家权重。传统的MoE模型通常采用赢者通吃策略，即只有被路由器选中的专家才能贡献输出。AdaMoE通过引入缩放适配器，允许所有专家都参与输出，但每个专家的贡献权重由缩放适配器独立控制。这种解耦设计使得专家可以基于任务相关性进行选择，并以独立控制的权重做出贡献，从而实现协作专家利用。

**关键设计**：AdaMoE的关键设计包括：1) MoE层的稀疏激活函数选择，以平衡性能和计算效率；2) 缩放适配器的结构设计，例如使用线性层或非线性层；3) 路由器的选择策略，例如使用Top-K选择或概率选择；4) 损失函数的设计，例如引入辅助损失以平衡专家之间的负载。

## 📊 实验亮点

AdaMoE在LIBERO和RoboTwin基准测试中分别取得了1.8%和9.3%的性能提升。更重要的是，在真实世界机器人操作实验中，AdaMoE实现了21.5%的显著改进，验证了其在实际应用中的有效性。这些结果表明，AdaMoE能够有效提升VLA模型在机器人操作任务中的性能和效率。

## 🎯 应用场景

AdaMoE可应用于各种机器人操作任务，例如物体抓取、装配、导航等。该研究成果有助于降低VLA模型的训练成本，提高模型在资源受限环境中的部署能力，并促进机器人智能的进一步发展。未来，该方法可以扩展到其他多模态学习任务中，例如自动驾驶、智能助手等。

## 📄 摘要（原文）

> Vision-Language-Action (VLA) models are experiencing rapid development and demonstrating promising capabilities in robotic manipulation tasks. However, scaling up VLA models presents several critical challenges: (1) Training new VLA models from scratch demands substantial computational resources and extensive datasets. Given the current scarcity of robot data, it becomes particularly valuable to fully leverage well-pretrained VLA model weights during the scaling process. (2) Real-time control requires carefully balancing model capacity with computational efficiency. To address these challenges, We propose AdaMoE, a Mixture-of-Experts (MoE) architecture that inherits pretrained weights from dense VLA models, and scales up the action expert by substituting the feedforward layers into sparsely activated MoE layers. AdaMoE employs a decoupling technique that decouples expert selection from expert weighting through an independent scale adapter working alongside the traditional router. This enables experts to be selected based on task relevance while contributing with independently controlled weights, allowing collaborative expert utilization rather than winner-takes-all dynamics. Our approach demonstrates that expertise need not monopolize. Instead, through collaborative expert utilization, we can achieve superior performance while maintaining computational efficiency. AdaMoE consistently outperforms the baseline model across key benchmarks, delivering performance gains of 1.8% on LIBERO and 9.3% on RoboTwin. Most importantly, a substantial 21.5% improvement in real-world experiments validates its practical effectiveness for robotic manipulation tasks.

