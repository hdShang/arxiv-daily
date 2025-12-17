---
layout: default
title: Dynamic-eDiTor: Training-Free Text-Driven 4D Scene Editing with Multimodal Diffusion Transformer
---

# Dynamic-eDiTor: Training-Free Text-Driven 4D Scene Editing with Multimodal Diffusion Transformer

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.00677" class="toolbar-btn" target="_blank">📄 arXiv: 2512.00677v1</a>
  <a href="https://arxiv.org/pdf/2512.00677.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.00677v1" onclick="toggleFavorite(this, '2512.00677v1', 'Dynamic-eDiTor: Training-Free Text-Driven 4D Scene Editing with Multimodal Diffusion Transformer')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dong In Lee, Hyungjun Doh, Seunggeun Chi, Runlin Duan, Sangpil Kim, Karthik Ramani

**分类**: cs.CV, cs.AI

**发布日期**: 2025-11-30

**备注**: 4D Scene Editing

**🔗 代码/项目**: [PROJECT_PAGE](https://di-lee.github.io/dynamic-eDiTor/)

---

## 💡 一句话要点

**Dynamic-eDiTor：基于多模态扩散Transformer的免训练文本驱动4D场景编辑**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `4D场景编辑` `文本驱动` `多模态扩散Transformer` `4D高斯溅射` `时空一致性` `免训练` `动态NeRF`

## 📋 核心要点

1. 现有文本驱动4D场景编辑方法难以保证编辑过程中跨视角和时间的一致性，导致运动扭曲和几何漂移。
2. Dynamic-eDiTor利用多模态扩散Transformer和4DGS，通过时空注意力机制和上下文令牌传播实现一致性编辑。
3. 实验表明，Dynamic-eDiTor在DyNeRF数据集上实现了更高的编辑保真度以及多视角和时间一致性。

## 📝 摘要（中文）

本文提出Dynamic-eDiTor，一个免训练的文本驱动4D编辑框架，它利用多模态扩散Transformer (MM-DiT) 和4D高斯溅射 (4DGS) 实现动态4D场景编辑。由于确保编辑过程中跨空间和时间的多视角和时间一致性存在挑战，文本驱动的4D场景编辑仍有待探索。现有方法依赖于独立编辑帧的2D扩散模型，常导致运动扭曲、几何漂移和不完整的编辑。Dynamic-eDiTor包含时空子网格注意力(STGA)，用于局部一致的跨视角和时间融合，以及上下文令牌传播(CTP)，用于通过令牌继承和光流引导的令牌替换进行全局传播。这些组件使Dynamic-eDiTor能够执行无缝、全局一致的多视角视频编辑，无需额外训练，并直接优化预训练的源4DGS。在多视角视频数据集DyNeRF上的大量实验表明，我们的方法实现了优于现有方法的编辑保真度以及多视角和时间一致性。

## 🔬 方法详解

**问题定义**：本文旨在解决文本驱动的动态4D场景编辑问题。现有方法，特别是基于2D扩散模型的方法，在独立编辑视频帧时，难以保证编辑结果在不同视角和时间上的连续性和一致性，导致运动扭曲、几何漂移以及编辑不完整等问题。这些问题限制了4D场景编辑的实用性和真实感。

**核心思路**：Dynamic-eDiTor的核心思路是利用多模态扩散Transformer (MM-DiT) 的强大生成能力，并结合4D高斯溅射 (4DGS) 的高效渲染特性，在无需额外训练的情况下，实现对4D场景的文本驱动编辑。通过引入时空子网格注意力 (STGA) 和上下文令牌传播 (CTP) 机制，确保编辑结果在时间和空间上的局部和全局一致性。

**技术框架**：Dynamic-eDiTor的整体框架包括以下几个主要步骤：1) 使用预训练的4DGS重建动态场景。2) 将场景投影到多个视角，生成多视角图像序列。3) 使用文本提示和MM-DiT对图像序列进行编辑，其中STGA负责局部一致性，CTP负责全局一致性。4) 将编辑后的图像序列反投影回4D空间，更新4DGS参数，得到编辑后的动态场景。

**关键创新**：Dynamic-eDiTor的关键创新在于：1) 提出了一种免训练的4D场景编辑方法，避免了耗时的训练过程。2) 引入了时空子网格注意力 (STGA) 机制，用于在局部范围内融合跨视角和时间的信息，保证编辑结果的局部一致性。3) 提出了上下文令牌传播 (CTP) 机制，通过令牌继承和光流引导的令牌替换，实现全局范围内的信息传播，保证编辑结果的全局一致性。

**关键设计**：STGA将图像划分为子网格，并在每个子网格内进行自注意力计算，从而捕捉局部时空关系。CTP利用光流估计相邻帧之间的运动信息，将上下文信息从一帧传递到另一帧，从而实现全局一致性。损失函数主要包括扩散模型的重建损失和正则化项，用于约束4DGS参数的更新，避免过度变形。

## 📊 实验亮点

实验结果表明，Dynamic-eDiTor在DyNeRF数据集上显著优于现有方法，在编辑保真度和时空一致性方面均取得了显著提升。定性结果展示了其在复杂场景下的编辑能力，例如改变物体的材质、形状和颜色，同时保持场景的动态性和真实感。定量指标也验证了其在多视角一致性和时间一致性方面的优势。

## 🎯 应用场景

Dynamic-eDiTor具有广泛的应用前景，包括电影特效制作、游戏开发、虚拟现实/增强现实内容创作、以及产品设计和可视化等领域。它能够让用户通过简单的文本指令，轻松地对动态4D场景进行编辑和修改，极大地降低了内容创作的门槛，并提升了创作效率。未来，该技术有望应用于更复杂的场景编辑任务，例如人物动作编辑、场景光照调整等。

## 📄 摘要（原文）

> Recent progress in 4D representations, such as Dynamic NeRF and 4D Gaussian Splatting (4DGS), has enabled dynamic 4D scene reconstruction. However, text-driven 4D scene editing remains under-explored due to the challenge of ensuring both multi-view and temporal consistency across space and time during editing. Existing studies rely on 2D diffusion models that edit frames independently, often causing motion distortion, geometric drift, and incomplete editing. We introduce Dynamic-eDiTor, a training-free text-driven 4D editing framework leveraging Multimodal Diffusion Transformer (MM-DiT) and 4DGS. This mechanism consists of Spatio-Temporal Sub-Grid Attention (STGA) for locally consistent cross-view and temporal fusion, and Context Token Propagation (CTP) for global propagation via token inheritance and optical-flow-guided token replacement. Together, these components allow Dynamic-eDiTor to perform seamless, globally consistent multi-view video without additional training and directly optimize pre-trained source 4DGS. Extensive experiments on multi-view video dataset DyNeRF demonstrate that our method achieves superior editing fidelity and both multi-view and temporal consistency prior approaches. Project page for results and code: https://di-lee.github.io/dynamic-eDiTor/

