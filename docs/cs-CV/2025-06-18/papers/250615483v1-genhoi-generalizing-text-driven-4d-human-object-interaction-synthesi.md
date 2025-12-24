---
layout: default
title: "GenHOI: Generalizing Text-driven 4D Human-Object Interaction Synthesis for Unseen Objects"
---

# GenHOI: Generalizing Text-driven 4D Human-Object Interaction Synthesis for Unseen Objects

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.15483" class="toolbar-btn" target="_blank">📄 arXiv: 2506.15483v1</a>
  <a href="https://arxiv.org/pdf/2506.15483.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.15483v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.15483v1', 'GenHOI: Generalizing Text-driven 4D Human-Object Interaction Synthesis for Unseen Objects')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shujia Li, Haiyu Zhang, Xinyuan Chen, Yaohui Wang, Yutong Ban

**分类**: cs.CV, cs.AI

**发布日期**: 2025-06-18

---

## 💡 一句话要点

**提出GenHOI以解决4D人机交互合成中的物体泛化问题**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)** **支柱五：交互与反应 (Interaction & Reaction)**

**关键词**: `4D人机交互` `文本驱动合成` `扩散模型` `稀疏关键帧` `泛化能力` `高保真生成` `接触模式` `虚拟现实`

## 📋 核心要点

1. 现有方法在4D人机交互合成中面临数据集稀缺的问题，限制了对未见物体的泛化能力。
2. 论文提出的GenHOI框架通过Object-AnchorNet和Contact-Aware Diffusion Model实现对未见物体的泛化和高保真4D HOI序列合成。
3. 实验结果显示，GenHOI在OMOMO和3D-FUTURE数据集上取得了最先进的性能，验证了其强大的泛化能力和生成质量。

## 📝 摘要（中文）

尽管扩散模型和大规模运动数据集推动了文本驱动的人类运动合成，但将这些进展扩展到4D人机交互（HOI）仍然面临挑战，主要是由于缺乏大规模4D HOI数据集。在本研究中，我们提出了GenHOI，一个新颖的两阶段框架，旨在实现两个关键目标：1）对未见物体的泛化，2）合成高保真4D HOI序列。在框架的初始阶段，我们采用Object-AnchorNet重建未见物体的稀疏3D HOI关键帧，仅从3D HOI数据集中学习，从而减轻对大规模4D HOI数据集的依赖。随后，我们在第二阶段引入Contact-Aware Diffusion Model（ContactDM），以无缝插值稀疏3D HOI关键帧为密集的时间一致的4D HOI序列。实验结果表明，我们在公开的OMOMO和3D-FUTURE数据集上实现了最先进的结果，展示了对未见物体的强泛化能力，同时实现了高保真的4D HOI生成。

## 🔬 方法详解

**问题定义**：本论文旨在解决4D人机交互合成中的物体泛化问题，现有方法依赖于大规模4D HOI数据集，限制了对未见物体的适应能力。

**核心思路**：论文提出的GenHOI框架通过两阶段的方法，首先利用Object-AnchorNet从3D HOI数据集中重建稀疏的3D关键帧，然后通过Contact-Aware Diffusion Model将其插值为高保真的4D HOI序列，从而减轻对大规模4D数据集的依赖。

**技术框架**：GenHOI框架分为两个主要阶段：第一阶段使用Object-AnchorNet重建稀疏3D HOI关键帧，第二阶段通过Contact-Aware Diffusion Model将这些关键帧插值为密集的4D HOI序列。

**关键创新**：最重要的创新在于引入了Contact-Aware Encoder和Contact-Aware HOI Attention，这些模块能够提取人机接触模式并有效整合接触信号，从而提升生成序列的质量。

**关键设计**：在设计中，Contact-Aware Encoder用于捕捉接触模式，Contact-Aware HOI Attention则用于将接触信号融入扩散模型中，确保生成的4D HOI序列在时间上具有一致性和高保真度。

## 📊 实验亮点

实验结果表明，GenHOI在OMOMO和3D-FUTURE数据集上实现了最先进的性能，相较于基线方法，生成的4D HOI序列在质量和泛化能力上均有显著提升，验证了其有效性。

## 🎯 应用场景

该研究的潜在应用领域包括虚拟现实、游戏开发和人机协作等场景，能够为这些领域提供更为真实和自然的人机交互体验。未来，GenHOI可能推动4D人机交互技术的进一步发展，促进相关应用的普及与创新。

## 📄 摘要（原文）

> While diffusion models and large-scale motion datasets have advanced text-driven human motion synthesis, extending these advances to 4D human-object interaction (HOI) remains challenging, mainly due to the limited availability of large-scale 4D HOI datasets. In our study, we introduce GenHOI, a novel two-stage framework aimed at achieving two key objectives: 1) generalization to unseen objects and 2) the synthesis of high-fidelity 4D HOI sequences. In the initial stage of our framework, we employ an Object-AnchorNet to reconstruct sparse 3D HOI keyframes for unseen objects, learning solely from 3D HOI datasets, thereby mitigating the dependence on large-scale 4D HOI datasets. Subsequently, we introduce a Contact-Aware Diffusion Model (ContactDM) in the second stage to seamlessly interpolate sparse 3D HOI keyframes into densely temporally coherent 4D HOI sequences. To enhance the quality of generated 4D HOI sequences, we propose a novel Contact-Aware Encoder within ContactDM to extract human-object contact patterns and a novel Contact-Aware HOI Attention to effectively integrate the contact signals into diffusion models. Experimental results show that we achieve state-of-the-art results on the publicly available OMOMO and 3D-FUTURE datasets, demonstrating strong generalization abilities to unseen objects, while enabling high-fidelity 4D HOI generation.

