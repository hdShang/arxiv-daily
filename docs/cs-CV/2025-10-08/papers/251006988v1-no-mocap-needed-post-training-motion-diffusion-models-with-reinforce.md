---
layout: default
title: No MoCap Needed: Post-Training Motion Diffusion Models with Reinforcement Learning using Only Textual Prompts
---

# No MoCap Needed: Post-Training Motion Diffusion Models with Reinforcement Learning using Only Textual Prompts

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.06988" class="toolbar-btn" target="_blank">📄 arXiv: 2510.06988v1</a>
  <a href="https://arxiv.org/pdf/2510.06988.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.06988v1" onclick="toggleFavorite(this, '2510.06988v1', 'No MoCap Needed: Post-Training Motion Diffusion Models with Reinforcement Learning using Only Textual Prompts')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Girolamo Macaluso, Lorenzo Mandelli, Mirko Bicchierai, Stefano Berretti, Andrew D. Bagdanov

**分类**: cs.CV

**发布日期**: 2025-10-08

---

## 💡 一句话要点

**提出基于强化学习的后训练运动扩散模型，仅用文本提示即可实现动作迁移。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱四：生成式动作 (Generative Motion)** **支柱六：视频提取与匹配 (Video Extraction)** **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `运动生成` `扩散模型` `强化学习` `文本提示` `动作迁移`

## 📋 核心要点

1. 现有运动生成模型需要大量动作捕捉数据进行训练或微调，难以适应新动作或风格。
2. 利用强化学习，仅通过文本提示微调预训练的运动扩散模型，无需额外的动作捕捉数据。
3. 实验表明，该方法在提高生成运动质量和多样性的同时，保持了原始分布上的性能。

## 📝 摘要（中文）

本文提出了一种基于强化学习的后训练框架，用于微调预训练的运动扩散模型，仅使用文本提示，无需任何运动ground truth。该方法利用预训练的文本-运动检索网络作为奖励信号，并使用Denoising Diffusion Policy Optimization优化扩散策略，从而有效地将模型的生成分布转移到目标域，而无需配对的运动数据。我们在HumanML3D和KIT-ML数据集上，针对跨数据集适应和留一法运动实验，在潜在空间和联合空间扩散架构上评估了该方法。定量指标和用户研究的结果表明，该方法始终提高了生成运动的质量和多样性，同时保持了原始分布上的性能。该方法是一种灵活、数据高效且保护隐私的运动适应解决方案。

## 🔬 方法详解

**问题定义**：现有运动生成模型在适应新的动作或风格时，通常需要大量的动作捕捉数据进行重新训练或微调，这使得模型难以扩展到新的领域，并且成本高昂。此外，获取高质量的动作捕捉数据本身也是一个挑战。

**核心思路**：本文的核心思路是利用强化学习，在不需要任何运动ground truth的情况下，仅通过文本提示来微调预训练的运动扩散模型。通过将文本-运动检索网络作为奖励信号，引导模型生成与文本描述更匹配的运动。

**技术框架**：该方法包含以下主要模块：1) 预训练的文本-运动扩散模型，用于生成初始运动；2) 预训练的文本-运动检索网络，用于评估生成运动与文本提示的匹配程度，并提供奖励信号；3) 基于Denoising Diffusion Policy Optimization (DDPO) 的强化学习算法，用于优化扩散模型的生成策略。整体流程是：给定文本提示，扩散模型生成运动，检索网络评估运动与文本的匹配度，DDPO根据奖励信号更新扩散模型参数，迭代优化。

**关键创新**：最重要的创新点在于，它提出了一种完全基于文本提示的运动模型微调方法，无需任何运动数据。这使得模型可以轻松地适应新的动作或风格，并且保护了运动数据的隐私。与现有方法相比，该方法更加灵活、数据高效且具有更好的可扩展性。

**关键设计**：该方法使用预训练的文本-运动检索网络作为奖励函数，奖励函数的设计直接影响了模型的性能。DDPO算法的选择也很关键，它能够有效地优化扩散模型的生成策略。具体的参数设置包括学习率、奖励函数的权重、以及DDPO算法的超参数等。此外，扩散模型的架构（latent-space或joint-space）也会影响最终的生成效果。

## 📊 实验亮点

实验结果表明，该方法在HumanML3D和KIT-ML数据集上，显著提高了生成运动的质量和多样性。用户研究表明，生成的运动在真实性和与文本描述的匹配度方面均优于基线方法。此外，该方法在保持原始分布性能的同时，成功地将模型的生成分布转移到目标域。

## 🎯 应用场景

该研究成果可应用于虚拟现实、游戏开发、动画制作等领域，能够根据文本描述自动生成高质量的人体运动动画。例如，游戏开发者可以通过输入简单的文本指令，快速生成角色所需的各种动作，从而提高开发效率。此外，该方法还可以用于生成个性化的运动训练方案，根据用户的文本描述生成定制化的运动序列。

## 📄 摘要（原文）

> Diffusion models have recently advanced human motion generation, producing realistic and diverse animations from textual prompts. However, adapting these models to unseen actions or styles typically requires additional motion capture data and full retraining, which is costly and difficult to scale. We propose a post-training framework based on Reinforcement Learning that fine-tunes pretrained motion diffusion models using only textual prompts, without requiring any motion ground truth. Our approach employs a pretrained text-motion retrieval network as a reward signal and optimizes the diffusion policy with Denoising Diffusion Policy Optimization, effectively shifting the model's generative distribution toward the target domain without relying on paired motion data. We evaluate our method on cross-dataset adaptation and leave-one-out motion experiments using the HumanML3D and KIT-ML datasets across both latent- and joint-space diffusion architectures. Results from quantitative metrics and user studies show that our approach consistently improves the quality and diversity of generated motions, while preserving performance on the original distribution. Our approach is a flexible, data-efficient, and privacy-preserving solution for motion adaptation.

