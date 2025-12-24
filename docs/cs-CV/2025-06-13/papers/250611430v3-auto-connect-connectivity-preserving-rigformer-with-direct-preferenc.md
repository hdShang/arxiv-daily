---
layout: default
title: "Auto-Connect: Connectivity-Preserving RigFormer with Direct Preference Optimization"
---

# Auto-Connect: Connectivity-Preserving RigFormer with Direct Preference Optimization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.11430" class="toolbar-btn" target="_blank">📄 arXiv: 2506.11430v3</a>
  <a href="https://arxiv.org/pdf/2506.11430.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.11430v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.11430v3', 'Auto-Connect: Connectivity-Preserving RigFormer with Direct Preference Optimization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jingfeng Guo, Jian Liu, Jinnan Chen, Shiwei Mao, Changrong Hu, Puhua Jiang, Junlin Yu, Jing Xu, Qi Liu, Lixin Xu, Zhuo Chen, Chunchao Guo

**分类**: cs.CV

**发布日期**: 2025-06-13 (更新: 2025-10-20)

---

## 💡 一句话要点

**提出Auto-Connect以解决自动绑定中骨骼连通性问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `自动绑定` `骨骼连通性` `拓扑优化` `奖励函数` `测地特征` `蒙皮质量` `动画技术`

## 📋 核心要点

1. 现有方法在自动绑定中未能有效保留骨骼的连通性，导致拓扑结构不准确。
2. 论文提出了一种通过连通性保留的标记化方案，自动化骨骼的连接关系，提高了拓扑准确性。
3. 实验结果表明，Auto-Connect在生成解剖学上更合理的骨骼结构和优越的变形特性方面表现出显著提升。

## 📝 摘要（中文）

我们介绍了Auto-Connect，这是一种新颖的自动绑定方法，通过连通性保留的标记化方案显式保留骨骼连通性。与以往方法不同，我们的方法使用特殊标记定义每个关节子节点的端点和每个层级的连接关系，从而有效自动化连通性关系。该方法通过将连通性信息直接集成到预测框架中，显著提高了拓扑准确性。此外，我们实现了一种拓扑感知奖励函数，量化拓扑正确性，并在后训练阶段通过奖励引导的直接偏好优化进行应用。我们还结合隐式测地特征进行潜在的前k个骨骼选择，显著改善了蒙皮质量。通过利用模型潜在空间中的测地距离信息，我们的方法智能地确定每个顶点最具影响力的骨骼，有效减轻了常见的蒙皮伪影。

## 🔬 方法详解

**问题定义**：本论文旨在解决自动绑定过程中骨骼连通性不足的问题。现有方法通常通过预测关节位置或点来确定连通性，导致拓扑结构不准确和蒙皮伪影。

**核心思路**：我们的方法通过引入连通性保留的标记化方案，直接在预测框架中集成连通性信息，从而自动化骨骼的连接关系，提升拓扑准确性。

**技术框架**：整体架构包括三个主要模块：连通性保留的标记化、拓扑感知奖励函数和奖励引导的直接偏好优化。首先，通过特殊标记定义关节的子节点端点；其次，利用奖励函数量化拓扑正确性；最后，通过优化过程提升模型性能。

**关键创新**：最重要的技术创新在于连通性保留的标记化方案和拓扑感知奖励函数的结合，这与现有方法的主要区别在于直接在预测过程中考虑了连通性。

**关键设计**：我们在模型中设置了特殊的标记来定义骨骼连接，并设计了拓扑感知奖励函数以量化拓扑的正确性。此外，隐式测地特征用于潜在骨骼选择，进一步提升了蒙皮质量。

## 📊 实验亮点

实验结果显示，Auto-Connect在拓扑准确性和蒙皮质量方面相较于基线方法有显著提升，具体表现为生成的骨骼结构在解剖学上更合理，变形特性更优越，减少了常见的蒙皮伪影。

## 🎯 应用场景

该研究的潜在应用领域包括动画制作、游戏开发和虚拟现实等场景，能够为角色绑定和动画生成提供更高质量的解决方案。未来，该方法可能推动自动化角色设计和动画技术的发展，提升用户体验。

## 📄 摘要（原文）

> We introduce Auto-Connect, a novel approach for automatic rigging that explicitly preserves skeletal connectivity through a connectivity-preserving tokenization scheme. Unlike previous methods that predict bone positions represented as two joints or first predict points before determining connectivity, our method employs special tokens to define endpoints for each joint's children and for each hierarchical layer, effectively automating connectivity relationships. This approach significantly enhances topological accuracy by integrating connectivity information directly into the prediction framework. To further guarantee high-quality topology, we implement a topology-aware reward function that quantifies topological correctness, which is then utilized in a post-training phase through reward-guided Direct Preference Optimization. Additionally, we incorporate implicit geodesic features for latent top-k bone selection, which substantially improves skinning quality. By leveraging geodesic distance information within the model's latent space, our approach intelligently determines the most influential bones for each vertex, effectively mitigating common skinning artifacts. This combination of connectivity-preserving tokenization, reward-guided fine-tuning, and geodesic-aware bone selection enables our model to consistently generate more anatomically plausible skeletal structures with superior deformation properties.

