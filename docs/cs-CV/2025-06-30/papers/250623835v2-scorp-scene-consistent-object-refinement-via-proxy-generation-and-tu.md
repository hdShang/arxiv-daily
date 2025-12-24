---
layout: default
title: "SCORP: Scene-Consistent Object Refinement via Proxy Generation and Tuning"
---

# SCORP: Scene-Consistent Object Refinement via Proxy Generation and Tuning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.23835" class="toolbar-btn" target="_blank">📄 arXiv: 2506.23835v2</a>
  <a href="https://arxiv.org/pdf/2506.23835.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.23835v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.23835v2', 'SCORP: Scene-Consistent Object Refinement via Proxy Generation and Tuning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ziwei Chen, Ziling Liu, Zitong Huang, Mingqi Gao, Feng Zheng

**分类**: cs.CV

**发布日期**: 2025-06-30 (更新: 2025-09-22)

**备注**: 8 pages with 6 figures. Project page: https://polysummit.github.io/scorp.github.io/

**🔗 代码/项目**: [GITHUB](https://github.com/PolySummit/SCORP)

---

## 💡 一句话要点

**提出SCORP以解决场景重建中对象视角缺失问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `3D重建` `物体建模` `视角缺失` `生成模型` `深度学习` `几何补全` `虚拟现实` `增强现实`

## 📋 核心要点

1. 现有方法在场景重建中难以处理物体的视角缺失，导致物体级建模精度不足。
2. SCORP通过生成代理并逐步调优，利用3D生成模型恢复缺失视角下的物体几何和外观。
3. 在多个基准测试中，SCORP在新视角合成和几何补全任务上表现优异，超越了现有方法。

## 📝 摘要（中文）

在场景重建中，物体的视角缺失是常见问题，因为相机路径通常优先捕捉整体场景结构，而非单个物体。这使得在保持准确场景级表示的同时，实现高保真物体级建模变得极具挑战性。为了解决这一问题，本文提出了场景一致性物体精细化框架SCORP，该框架利用3D生成先验在缺失视角下恢复物体的细粒度几何和外观。SCORP通过代理生成和调优的两阶段过程，确保在未见视角下原始物体的高保真几何和外观，同时保持空间定位和外观的一致性。在多个具有挑战性的基准测试中，SCORP在新视角合成和几何补全任务上均超越了最新的基线方法。

## 🔬 方法详解

**问题定义**：本文旨在解决在场景重建中物体视角缺失导致的高保真物体级建模困难。现有方法往往无法在缺失视角下准确重建物体的几何和外观，影响了下游任务的性能。

**核心思路**：SCORP的核心思路是通过生成代理并进行调优，利用3D生成先验来恢复物体的细粒度几何和外观。该方法设计旨在在缺失视角下保持物体的一致性和高保真度。

**技术框架**：SCORP的整体架构包括两个主要阶段：首先，通过3D生成模型生成代理，替代退化的物体；然后，逐步调优每个代理，使其与退化物体在7自由度姿态下对齐，并通过注册约束增强来修正空间和外观的不一致性。

**关键创新**：SCORP的主要创新在于其两阶段的代理调优过程，确保在未见视角下物体的高保真几何和外观。这一方法与现有技术的本质区别在于其强调了空间一致性和外观一致性。

**关键设计**：在设计中，SCORP采用了特定的损失函数来优化几何和外观的一致性，并利用深度学习网络结构进行代理生成和调优，确保了模型的有效性和鲁棒性。

## 📊 实验亮点

在多个具有挑战性的基准测试中，SCORP在新视角合成和几何补全任务上表现出色，均超越了最新的基线方法，具体提升幅度达到XX%（具体数据需根据实验结果填入）。这一结果表明SCORP在高保真物体重建方面的有效性和优越性。

## 🎯 应用场景

SCORP的研究成果在多个领域具有广泛的应用潜力，包括虚拟现实、增强现实、游戏开发以及机器人视觉等。通过提高物体重建的精度，SCORP能够为这些领域提供更真实的场景表现，进而提升用户体验和交互效果。未来，SCORP的技术也可能推动智能机器人在复杂环境中的自主导航和操作能力。

## 📄 摘要（原文）

> Viewpoint missing of objects is common in scene reconstruction, as camera paths typically prioritize capturing the overall scene structure rather than individual objects. This makes it highly challenging to achieve high-fidelity object-level modeling while maintaining accurate scene-level representation. Addressing this issue is critical for advancing downstream tasks requiring high-fidelity object reconstruction. In this paper, we introduce Scene-Consistent Object Refinement via Proxy Generation and Tuning (SCORP), a novel 3D enhancement framework that leverages 3D generative priors to recover fine-grained object geometry and appearance under missing views. Starting with proxy generation by substituting degraded objects using a 3D generation model, SCORP then progressively refines geometry and texture by aligning each proxy to its degraded counterpart in 7-DoF pose, followed by correcting spatial and appearance inconsistencies through registration-constrained enhancement. This two-stage proxy tuning ensures the high-fidelity geometry and appearance of the original object in unseen views while maintaining consistency in spatial positioning, observed geometry, and appearance. Across challenging benchmarks, SCORP achieves consistent gains over recent state-of-the-art baselines on both novel view synthesis and geometry completion tasks. SCORP is available at https://github.com/PolySummit/SCORP.

