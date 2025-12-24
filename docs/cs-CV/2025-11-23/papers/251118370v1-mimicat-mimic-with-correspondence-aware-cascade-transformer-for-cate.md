---
layout: default
title: "MimiCAT: Mimic with Correspondence-Aware Cascade-Transformer for Category-Free 3D Pose Transfer"
---

# MimiCAT: Mimic with Correspondence-Aware Cascade-Transformer for Category-Free 3D Pose Transfer

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.18370" class="toolbar-btn" target="_blank">📄 arXiv: 2511.18370v1</a>
  <a href="https://arxiv.org/pdf/2511.18370.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.18370v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.18370v1', 'MimiCAT: Mimic with Correspondence-Aware Cascade-Transformer for Category-Free 3D Pose Transfer')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zenghao Chai, Chen Tang, Yongkang Wong, Xulei Yang, Mohan Kankanhalli

**分类**: cs.CV, cs.GR

**发布日期**: 2025-11-23

**备注**: tech report

---

## 💡 一句话要点

**MimiCAT：基于对应感知级联Transformer的无类别3D姿态迁移**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `3D姿态迁移` `无类别` `软对应` `Transformer` `条件生成`

## 📋 核心要点

1. 现有3D姿态迁移方法难以处理结构差异大的角色，限制了其在无类别场景下的应用。
2. MimiCAT通过学习软对应关系，实现了不同角色间灵活的多对多匹配，从而进行姿态迁移。
3. 实验结果表明，MimiCAT在跨角色姿态迁移方面显著优于现有方法，能够生成更合理的姿势。

## 📝 摘要（中文）

本文提出了一种无类别3D姿态迁移方法，旨在将源网格的姿态风格迁移到目标角色，同时保留目标角色的几何形状和源角色的姿态特征。现有方法大多局限于结构相似的角色，无法推广到无类别场景（例如，将人形的姿势转移到四足动物）。主要挑战在于不同角色类型固有的结构和变换多样性，这通常导致不匹配的区域和较差的迁移质量。为了解决这些问题，我们首先构建了一个包含数百万个姿势和数百个不同角色的数据集。我们进一步提出了MimiCAT，一个为无类别3D姿态迁移设计的级联Transformer模型。MimiCAT不依赖于严格的一对一对应关系映射，而是利用语义关键点标签来学习一种新的软对应关系，从而实现角色之间灵活的多对多匹配。姿态迁移被形式化为一个条件生成过程，其中源变换首先通过软对应匹配投影到目标上，然后使用形状条件表示进行细化。大量的定性和定量实验表明，MimiCAT可以在不同的角色之间迁移合理的姿势，显著优于仅限于窄类别迁移（例如，人形到人形）的先前方法。

## 🔬 方法详解

**问题定义**：现有3D姿态迁移方法主要针对结构相似的角色，例如人形到人形的迁移。当源角色和目标角色的结构差异较大时，例如人形到四足动物的迁移，现有方法难以建立准确的对应关系，导致迁移效果不佳。因此，需要一种能够处理不同类别角色之间姿态迁移的方法。

**核心思路**：MimiCAT的核心思路是学习一种软对应关系，而不是依赖于严格的一对一对应关系。通过语义关键点标签，MimiCAT可以建立源角色和目标角色之间的多对多匹配关系，从而实现灵活的姿态迁移。这种软对应关系能够更好地适应不同角色之间的结构差异。

**技术框架**：MimiCAT是一个级联Transformer模型，包含以下主要模块：1) 软对应匹配模块：利用语义关键点标签学习源角色和目标角色之间的软对应关系。2) 姿态投影模块：将源角色的姿态变换通过软对应关系投影到目标角色上。3) 形状条件细化模块：使用目标角色的形状信息对投影后的姿态进行细化，生成最终的姿态。

**关键创新**：MimiCAT的关键创新在于提出了基于软对应关系的姿态迁移方法。与现有方法依赖于严格的一对一对应关系不同，MimiCAT通过学习软对应关系，能够更好地处理不同角色之间的结构差异，从而实现更准确的姿态迁移。

**关键设计**：MimiCAT的关键设计包括：1) 使用Transformer网络学习软对应关系。2) 使用级联结构逐步细化姿态。3) 使用形状条件表示来提高姿态的准确性。具体的损失函数设计未知，网络结构细节未知。

## 📊 实验亮点

MimiCAT在跨角色姿态迁移方面取得了显著的性能提升。通过定性和定量实验，证明了MimiCAT能够生成更合理的姿势，显著优于现有方法。具体的性能数据和提升幅度在摘要中未明确给出，属于未知信息。

## 🎯 应用场景

该研究成果可应用于动画制作、游戏开发、虚拟现实等领域。例如，可以将一个角色的动作风格迁移到另一个角色上，从而快速生成新的动画内容。此外，该方法还可以用于机器人控制，使机器人能够模仿人类或其他动物的动作。

## 📄 摘要（原文）

> 3D pose transfer aims to transfer the pose-style of a source mesh to a target character while preserving both the target's geometry and the source's pose characteristic. Existing methods are largely restricted to characters with similar structures and fail to generalize to category-free settings (e.g., transferring a humanoid's pose to a quadruped). The key challenge lies in the structural and transformation diversity inherent in distinct character types, which often leads to mismatched regions and poor transfer quality. To address these issues, we first construct a million-scale pose dataset across hundreds of distinct characters. We further propose MimiCAT, a cascade-transformer model designed for category-free 3D pose transfer. Instead of relying on strict one-to-one correspondence mappings, MimiCAT leverages semantic keypoint labels to learn a novel soft correspondence that enables flexible many-to-many matching across characters. The pose transfer is then formulated as a conditional generation process, in which the source transformations are first projected onto the target through soft correspondence matching and subsequently refined using shape-conditioned representations. Extensive qualitative and quantitative experiments demonstrate that MimiCAT transfers plausible poses across different characters, significantly outperforming prior methods that are limited to narrow category transfer (e.g., humanoid-to-humanoid).

