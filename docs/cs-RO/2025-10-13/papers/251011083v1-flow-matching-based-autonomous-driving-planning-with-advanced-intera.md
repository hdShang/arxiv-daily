---
layout: default
title: Flow Matching-Based Autonomous Driving Planning with Advanced Interactive Behavior Modeling
---

# Flow Matching-Based Autonomous Driving Planning with Advanced Interactive Behavior Modeling

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.11083" class="toolbar-btn" target="_blank">📄 arXiv: 2510.11083v1</a>
  <a href="https://arxiv.org/pdf/2510.11083.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.11083v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.11083v1', 'Flow Matching-Based Autonomous Driving Planning with Advanced Interactive Behavior Modeling')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tianyi Tan, Yinan Zheng, Ruiming Liang, Zexu Wang, Kexin Zheng, Jinliang Zheng, Jianxiong Li, Xianyuan Zhan, Jingjing Liu

**分类**: cs.RO, cs.AI

**发布日期**: 2025-10-13

**备注**: 26 pages, 6 figures. Accepted at NeurIPS 2025

---

## 💡 一句话要点

**Flow Planner：基于流匹配的自动驾驶规划，提升交互行为建模能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱四：生成式动作 (Generative Motion)**

**关键词**: `自动驾驶规划` `交互行为建模` `流匹配` `轨迹预测` `多模态生成`

## 📋 核心要点

1. 现有自动驾驶规划方法在复杂交互场景中建模驾驶行为不足，依赖过度设计的架构且缺乏专用交互建模机制。
2. Flow Planner通过细粒度轨迹Token化、高效时空融合架构和流匹配生成，提升交互行为建模能力。
3. 在nuPlan和interPlan数据集上的实验表明，Flow Planner在交互场景中实现了最先进的性能。

## 📝 摘要（中文）

在复杂场景中建模交互式驾驶行为仍然是自动驾驶规划的一个根本挑战。基于学习的方法试图利用先进的生成模型来解决这一挑战，从而消除了对过度设计的表征融合架构的依赖。然而，简单地堆叠Transformer模块的粗暴实现缺乏用于建模真实驾驶场景中常见的交互行为的专用机制。交互式驾驶数据的稀缺性进一步加剧了这个问题，使得传统的模仿学习方法无法捕捉高价值的交互行为。我们提出了Flow Planner，通过数据建模、模型架构和学习方案的协同创新来解决这些问题。具体来说，我们首先引入细粒度的轨迹Token化，将轨迹分解为重叠的片段，以降低整个轨迹建模的复杂性。通过精心设计的架构，我们实现了规划和场景信息的有效的时间和空间融合，以更好地捕捉交互行为。此外，该框架结合了流匹配和无分类器引导，用于多模态行为生成，在推理过程中动态地重新加权代理交互，以保持连贯的响应策略，为交互式场景理解提供了关键的提升。在大型nuPlan数据集和具有挑战性的交互式interPlan数据集上的实验结果表明，Flow Planner在基于学习的方法中实现了最先进的性能，同时有效地建模了复杂驾驶场景中的交互行为。

## 🔬 方法详解

**问题定义**：自动驾驶规划需要在复杂交互场景中准确预测其他车辆的行为，从而做出安全合理的决策。现有方法，特别是基于学习的方法，通常依赖于复杂的特征工程和人为设计的交互模块，缺乏对交互行为的有效建模机制，并且难以处理交互数据稀缺的问题。简单堆叠Transformer模块无法有效捕捉驾驶场景中常见的交互行为。

**核心思路**：Flow Planner的核心思路是通过协同优化数据建模、模型架构和学习方案来提升交互行为建模能力。具体来说，通过细粒度的轨迹Token化降低建模复杂度，设计高效的时空融合架构捕捉交互信息，并利用流匹配生成多模态交互行为，从而在交互场景中实现更准确的预测和规划。

**技术框架**：Flow Planner的整体框架包含以下几个主要模块：1) 细粒度轨迹Token化模块，将轨迹分解为重叠的片段；2) 时空融合模块，用于融合规划和场景信息，捕捉交互行为；3) 基于流匹配的生成模块，利用无分类器引导生成多模态行为；4) 规划模块，基于生成的行为预测进行路径规划。整个流程首先对输入数据进行Token化，然后通过时空融合模块提取特征，再利用流匹配生成模块预测交互行为，最后进行路径规划。

**关键创新**：Flow Planner的关键创新在于以下几个方面：1) 细粒度轨迹Token化，降低了轨迹建模的复杂度；2) 精心设计的时空融合架构，能够更有效地捕捉交互行为；3) 引入流匹配和无分类器引导，实现了多模态行为生成，并动态地重新加权代理交互，从而保持连贯的响应策略。

**关键设计**：在数据建模方面，采用了重叠的轨迹片段，以增加数据量并减少建模难度。在模型架构方面，设计了专门的时空融合模块，利用注意力机制融合规划和场景信息。在学习方案方面，采用了流匹配损失函数和无分类器引导，以生成多样化的交互行为。具体的参数设置和网络结构细节在论文中有详细描述。

## 📊 实验亮点

Flow Planner在nuPlan和interPlan数据集上取得了显著的实验成果。在nuPlan数据集上，Flow Planner的性能优于其他基于学习的方法。在更具挑战性的interPlan数据集上，Flow Planner展示了其在建模复杂交互行为方面的优势，实现了最先进的性能，证明了其在复杂驾驶场景中的有效性。

## 🎯 应用场景

Flow Planner可应用于各种自动驾驶场景，尤其是在城市道路、高速公路等复杂交通环境中，能够提升自动驾驶系统对其他车辆行为的预测能力，从而提高驾驶安全性、舒适性和效率。该研究成果也有助于推动高级驾驶辅助系统（ADAS）的发展，并为未来实现完全自动驾驶提供技术支撑。

## 📄 摘要（原文）

> Modeling interactive driving behaviors in complex scenarios remains a fundamental challenge for autonomous driving planning. Learning-based approaches attempt to address this challenge with advanced generative models, removing the dependency on over-engineered architectures for representation fusion. However, brute-force implementation by simply stacking transformer blocks lacks a dedicated mechanism for modeling interactive behaviors that are common in real driving scenarios. The scarcity of interactive driving data further exacerbates this problem, leaving conventional imitation learning methods ill-equipped to capture high-value interactive behaviors. We propose Flow Planner, which tackles these problems through coordinated innovations in data modeling, model architecture, and learning scheme. Specifically, we first introduce fine-grained trajectory tokenization, which decomposes the trajectory into overlapping segments to decrease the complexity of whole trajectory modeling. With a sophisticatedly designed architecture, we achieve efficient temporal and spatial fusion of planning and scene information, to better capture interactive behaviors. In addition, the framework incorporates flow matching with classifier-free guidance for multi-modal behavior generation, which dynamically reweights agent interactions during inference to maintain coherent response strategies, providing a critical boost for interactive scenario understanding. Experimental results on the large-scale nuPlan dataset and challenging interactive interPlan dataset demonstrate that Flow Planner achieves state-of-the-art performance among learning-based approaches while effectively modeling interactive behaviors in complex driving scenarios.

