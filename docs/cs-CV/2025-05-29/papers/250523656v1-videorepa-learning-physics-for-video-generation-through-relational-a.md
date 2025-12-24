---
layout: default
title: "VideoREPA: Learning Physics for Video Generation through Relational Alignment with Foundation Models"
---

# VideoREPA: Learning Physics for Video Generation through Relational Alignment with Foundation Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.23656" class="toolbar-btn" target="_blank">📄 arXiv: 2505.23656v1</a>
  <a href="https://arxiv.org/pdf/2505.23656.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.23656v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.23656v1', 'VideoREPA: Learning Physics for Video Generation through Relational Alignment with Foundation Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiangdong Zhang, Jiaqi Liao, Shaofeng Zhang, Fanqing Meng, Xiangpeng Wan, Junchi Yan, Yu Cheng

**分类**: cs.CV

**发布日期**: 2025-05-29

**🔗 代码/项目**: [PROJECT_PAGE](https://videorepa.github.io/)

---

## 💡 一句话要点

**提出VideoREPA以解决视频生成中的物理理解问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱四：生成式动作 (Generative Motion)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视频生成` `物理理解` `蒸馏训练` `时空对齐` `多模态学习`

## 📋 核心要点

1. 现有的文本到视频生成模型在生成物理合理内容方面存在显著不足，难以准确理解物理规律。
2. 论文提出VideoREPA框架，通过对齐令牌级关系，将视频理解模型的物理知识蒸馏到T2V模型中。
3. 实验结果显示，VideoREPA在物理常识方面显著提升了基线模型CogVideoX的性能，表现出强大的生成能力。

## 📝 摘要（中文）

近年来，文本到视频（T2V）扩散模型的进展使得高保真和真实的视频合成成为可能。然而，现有的T2V模型在生成物理上合理的内容方面存在困难，主要由于其对物理理解的能力有限。我们发现，尽管T2V模型的表示在一定程度上具备物理理解能力，但与最新的视频自监督学习方法相比，仍显不足。为此，我们提出了一种新框架VideoREPA，通过对齐令牌级关系，将视频理解基础模型中的物理理解能力蒸馏到T2V模型中，从而缩小物理理解的差距，实现更具物理合理性的视频生成。我们引入了令牌关系蒸馏（TRD）损失，利用时空对齐为强大的预训练T2V模型的微调提供软指导，这是与以往表示对齐方法的关键区别。实证评估表明，VideoREPA显著增强了基线方法CogVideoX的物理常识，取得了相关基准的显著提升。

## 🔬 方法详解

**问题定义**：论文要解决的问题是现有文本到视频生成模型在生成物理合理内容时的不足，特别是它们对物理规律的理解能力较弱。现有方法在物理理解方面的表现远不如最新的视频自监督学习方法。

**核心思路**：论文的核心解决思路是通过VideoREPA框架，将视频理解基础模型中的物理理解能力蒸馏到T2V模型中，具体通过对齐令牌级关系来实现。这种设计旨在缩小物理理解的差距，从而提高生成视频的物理合理性。

**技术框架**：VideoREPA的整体架构包括两个主要模块：视频理解基础模型和文本到视频生成模型。首先，通过对视频理解模型进行训练，提取其物理知识；然后，通过令牌关系蒸馏损失（TRD）将这些知识应用于T2V模型的微调过程中。

**关键创新**：最重要的技术创新点在于引入了令牌关系蒸馏（TRD）损失，这一方法利用时空对齐为T2V模型的微调提供了软指导。这与以往的表示对齐方法有本质区别，后者通常不专注于物理知识的注入。

**关键设计**：在关键设计方面，TRD损失函数的构建是核心，强调了时空对齐的重要性。此外，模型的参数设置和网络结构经过精心设计，以确保在微调过程中能够有效地传递物理知识。具体的参数设置和网络结构细节在论文中进行了详细描述。

## 📊 实验亮点

实验结果表明，VideoREPA显著提升了基线模型CogVideoX的物理常识，具体在相关基准测试中取得了显著的性能提升，展示了其在生成符合直观物理规律的视频方面的强大能力。

## 🎯 应用场景

该研究的潜在应用领域包括影视制作、游戏开发和虚拟现实等场景，能够为这些领域提供更为真实和物理合理的视频生成能力。未来，随着技术的进一步发展，VideoREPA可能在自动化内容创作和智能交互系统中发挥重要作用，提升用户体验。

## 📄 摘要（原文）

> Recent advancements in text-to-video (T2V) diffusion models have enabled high-fidelity and realistic video synthesis. However, current T2V models often struggle to generate physically plausible content due to their limited inherent ability to accurately understand physics. We found that while the representations within T2V models possess some capacity for physics understanding, they lag significantly behind those from recent video self-supervised learning methods. To this end, we propose a novel framework called VideoREPA, which distills physics understanding capability from video understanding foundation models into T2V models by aligning token-level relations. This closes the physics understanding gap and enable more physics-plausible generation. Specifically, we introduce the Token Relation Distillation (TRD) loss, leveraging spatio-temporal alignment to provide soft guidance suitable for finetuning powerful pre-trained T2V models, a critical departure from prior representation alignment (REPA) methods. To our knowledge, VideoREPA is the first REPA method designed for finetuning T2V models and specifically for injecting physical knowledge. Empirical evaluations show that VideoREPA substantially enhances the physics commonsense of baseline method, CogVideoX, achieving significant improvement on relevant benchmarks and demonstrating a strong capacity for generating videos consistent with intuitive physics. More video results are available at https://videorepa.github.io/.

