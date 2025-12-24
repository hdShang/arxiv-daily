---
layout: default
title: "NavMoE: Hybrid Model- and Learning-based Traversability Estimation for Local Navigation via Mixture of Experts"
---

# NavMoE: Hybrid Model- and Learning-based Traversability Estimation for Local Navigation via Mixture of Experts

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.12747" class="toolbar-btn" target="_blank">📄 arXiv: 2509.12747v2</a>
  <a href="https://arxiv.org/pdf/2509.12747.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.12747v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.12747v2', 'NavMoE: Hybrid Model- and Learning-based Traversability Estimation for Local Navigation via Mixture of Experts')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Botao He, Amir Hossein Shahidzadeh, Yu Chen, Jiayi Wu, Tianrui Guan, Guofei Chen, Howie Choset, Dinesh Manocha, Glen Chou, Cornelia Fermuller, Yiannis Aloimonos

**分类**: cs.RO

**发布日期**: 2025-09-16 (更新: 2025-09-17)

---

## 💡 一句话要点

**提出NavMoE，通过混合专家模型实现机器人局部导航中更高效、泛化的地形可通行性估计。**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `机器人导航` `可通行性估计` `混合专家模型` `深度学习` `局部规划`

## 📋 核心要点

1. 现有可通行性估计方法难以在保证可靠性和鲁棒性的同时，有效编码不同环境下的几何和语义信息。
2. NavMoE 采用混合专家模型，针对不同地形类型选择专门的模型，并通过门控网络动态调整各模型的权重。
3. 实验表明，NavMoE 在跨域泛化能力和计算效率方面优于单一专家模型和完整集成模型，计算成本降低81.2%。

## 📝 摘要（中文）

本文探讨了机器人导航中的可通行性估计问题。可通行性估计的关键瓶颈在于如何在不同环境中高效地实现可靠且鲁棒的预测，同时准确地编码几何和语义信息。我们提出了一种名为Navigation via Mixture of Experts (NAVMOE) 的分层模块化方法，用于可通行性估计和局部导航。NAVMOE 结合了针对特定地形类型的多个专门模型，每个模型可以是经典的基于模型的方法，也可以是基于学习的方法，用于预测特定地形类型的可通行性。NAVMOE 通过门控网络，根据输入环境动态地加权不同模型的贡献。总的来说，我们的方法提供了三个优点：首先，NAVMOE 能够自适应地利用针对不同地形的专门方法进行可通行性估计，从而增强了在不同和未见环境中的泛化能力。其次，通过引入无需训练的惰性门控机制，我们的方法在解决方案质量损失可忽略不计的情况下显著提高了效率，该机制旨在最大限度地减少推理过程中激活的专家数量。第三，我们的方法使用两阶段训练策略，可以在包含不可微模块的混合 MoE 方法中训练门控网络。大量的实验表明，NAVMOE 在不同领域中提供了比任何单个专家或完整集成更好的效率和性能平衡，通过惰性门控将平均计算成本降低了 81.2%，而路径质量的损失不到 2%。

## 🔬 方法详解

**问题定义**：论文旨在解决机器人局部导航中，在不同地形环境下进行准确、高效且具有泛化能力的可通行性估计问题。现有方法要么依赖于特定环境的先验知识，泛化性差；要么计算复杂度高，难以满足实时性要求。

**核心思路**：论文的核心思路是利用混合专家模型（MoE），将不同的可通行性估计模型（专家）针对性地应用于不同的地形类型。通过门控网络动态地选择和加权这些专家，从而实现对不同环境的自适应和高效处理。

**技术框架**：NavMoE 的整体框架包含以下几个主要模块：1) 特征提取模块：从输入的环境数据（例如，深度图像、点云）中提取几何和语义特征。2) 专家模块：包含多个针对特定地形类型设计的可通行性估计模型，可以是基于模型的传统方法，也可以是基于学习的深度学习模型。3) 门控网络：根据输入特征，动态地为每个专家分配权重，决定其在最终可通行性估计中的贡献。4) 惰性门控机制：为了提高效率，只激活权重较高的专家，减少计算量。

**关键创新**：NavMoE 的关键创新在于混合专家模型的架构和惰性门控机制。混合专家模型能够针对不同地形选择最合适的专家，提高泛化能力。惰性门控机制则能够在保证性能的前提下，显著降低计算成本。此外，两阶段训练策略解决了混合模型中不可微模块的训练问题。

**关键设计**：门控网络的设计至关重要，它决定了如何选择和加权不同的专家。论文采用了一种两阶段训练策略：首先，独立训练每个专家模型；然后，固定专家模型的参数，训练门控网络。惰性门控机制通过设定一个阈值，只激活权重高于该阈值的专家。损失函数的设计需要平衡可通行性估计的准确性和计算效率。

## 📊 实验亮点

实验结果表明，NavMoE 在多个数据集上都取得了优于单一专家模型和完整集成模型的性能。通过惰性门控机制，NavMoE 将平均计算成本降低了 81.2%，而路径质量的损失不到 2%。这表明 NavMoE 在效率和性能之间取得了良好的平衡，并且具有很强的跨域泛化能力。

## 🎯 应用场景

NavMoE 可应用于各种机器人导航场景，例如自动驾驶、无人机巡检、移动机器人等。该方法能够提高机器人在复杂和未知环境中的导航能力，降低计算成本，并增强系统的鲁棒性和可靠性。未来，该研究可以扩展到更复杂的环境和任务中，例如在恶劣天气或光照条件下进行导航。

## 📄 摘要（原文）

> This paper explores traversability estimation for robot navigation. A key bottleneck in traversability estimation lies in efficiently achieving reliable and robust predictions while accurately encoding both geometric and semantic information across diverse environments. We introduce Navigation via Mixture of Experts (NAVMOE), a hierarchical and modular approach for traversability estimation and local navigation. NAVMOE combines multiple specialized models for specific terrain types, each of which can be either a classical model-based or a learning-based approach that predicts traversability for specific terrain types. NAVMOE dynamically weights the contributions of different models based on the input environment through a gating network. Overall, our approach offers three advantages: First, NAVMOE enables traversability estimation to adaptively leverage specialized approaches for different terrains, which enhances generalization across diverse and unseen environments. Second, our approach significantly improves efficiency with negligible cost of solution quality by introducing a training-free lazy gating mechanism, which is designed to minimize the number of activated experts during inference. Third, our approach uses a two-stage training strategy that enables the training for the gating networks within the hybrid MoE method that contains nondifferentiable modules. Extensive experiments show that NAVMOE delivers a better efficiency and performance balance than any individual expert or full ensemble across different domains, improving cross-domain generalization and reducing average computational cost by 81.2% via lazy gating, with less than a 2% loss in path quality.

