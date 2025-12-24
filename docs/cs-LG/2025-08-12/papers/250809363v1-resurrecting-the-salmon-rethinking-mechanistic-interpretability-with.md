---
layout: default
title: "Resurrecting the Salmon: Rethinking Mechanistic Interpretability with Domain-Specific Sparse Autoencoders"
---

# Resurrecting the Salmon: Rethinking Mechanistic Interpretability with Domain-Specific Sparse Autoencoders

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09363" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09363v1</a>
  <a href="https://arxiv.org/pdf/2508.09363.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09363v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09363v1', 'Resurrecting the Salmon: Rethinking Mechanistic Interpretability with Domain-Specific Sparse Autoencoders')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Charles O'Neill, Mudith Jayasekara, Max Kirkby

**分类**: cs.LG

**发布日期**: 2025-08-12

---

## 💡 一句话要点

**提出领域特定稀疏自编码器以提升语言模型的可解释性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `稀疏自编码器` `可解释性` `领域特定模型` `医学文本` `大型语言模型` `重构误差` `特征学习`

## 📋 核心要点

1. 现有的稀疏自编码器在广泛数据分布上训练，导致潜在特征难以解释，且存在大量重构误差。
2. 本文提出将SAE训练限制在特定领域，以便更好地捕捉领域特定特征，从而提高模型的可解释性。
3. 实验结果表明，领域特定的SAEs在方差解释、损失恢复和线性残差误差方面均优于传统的广域SAEs。

## 📝 摘要（中文）

稀疏自编码器（SAEs）通过将大型语言模型（LLM）的激活分解为潜在特征，揭示其机制结构。传统的SAEs在广泛的数据分布上训练，导致固定的潜在预算只能捕捉高频、通用模式，从而产生显著的线性“暗物质”重构误差，并使得潜在特征相互碎片化或吸收，增加了解释的复杂性。本文展示了将SAE训练限制在特定领域（如医学文本）可以重新分配容量，改善重构保真度和可解释性。通过在Gemma-2模型的第20层激活上使用195k临床问答示例训练JumpReLU SAEs，我们发现领域限制的SAEs解释了多达20%的方差，达到了更高的损失恢复，并减少了线性残差误差。自动化和人工评估确认所学特征与临床相关概念（如“味觉感受”或“传染性单核细胞增多症”）一致，而非频繁但无信息的标记。

## 🔬 方法详解

**问题定义**：本文旨在解决传统稀疏自编码器在广泛数据分布上训练所导致的重构误差和潜在特征难以解释的问题。现有方法在捕捉领域特定信息时存在显著不足。

**核心思路**：通过将SAE的训练限制在特定领域（如医学文本），重新分配模型容量，以便更好地捕捉与该领域相关的特征，从而提高模型的重构保真度和可解释性。

**技术框架**：整体架构包括数据预处理、SAE模型设计、训练过程和评估模块。模型使用JumpReLU激活函数，专注于第20层的激活进行训练。

**关键创新**：最重要的技术创新在于领域限制的训练策略，这与传统的广域SAEs形成鲜明对比，使得模型能够更有效地捕捉领域特定的线性结构。

**关键设计**：在模型设计中，采用了JumpReLU激活函数，并使用195k个临床问答示例进行训练。损失函数的选择和参数设置经过精心设计，以确保模型在特定领域的表现最佳。

## 📊 实验亮点

实验结果显示，领域特定的SAEs能够解释多达20%的方差，损失恢复率显著提高，并且线性残差误差减少。这些结果通过自动化和人工评估得到了验证，表明所学特征与临床相关概念高度一致，优于传统的广域SAEs。

## 🎯 应用场景

该研究的潜在应用领域包括医学文本分析、临床决策支持系统和医疗信息提取等。通过提高模型的可解释性，能够帮助医疗专业人员更好地理解和利用大型语言模型的输出，从而提升临床应用的实际价值。未来，该方法可能影响其他领域的模型训练策略，推动更具针对性的模型开发。

## 📄 摘要（原文）

> Sparse autoencoders (SAEs) decompose large language model (LLM) activations into latent features that reveal mechanistic structure. Conventional SAEs train on broad data distributions, forcing a fixed latent budget to capture only high-frequency, generic patterns. This often results in significant linear ``dark matter'' in reconstruction error and produces latents that fragment or absorb each other, complicating interpretation. We show that restricting SAE training to a well-defined domain (medical text) reallocates capacity to domain-specific features, improving both reconstruction fidelity and interpretability. Training JumpReLU SAEs on layer-20 activations of Gemma-2 models using 195k clinical QA examples, we find that domain-confined SAEs explain up to 20\% more variance, achieve higher loss recovery, and reduce linear residual error compared to broad-domain SAEs. Automated and human evaluations confirm that learned features align with clinically meaningful concepts (e.g., ``taste sensations'' or ``infectious mononucleosis''), rather than frequent but uninformative tokens. These domain-specific SAEs capture relevant linear structure, leaving a smaller, more purely nonlinear residual. We conclude that domain-confinement mitigates key limitations of broad-domain SAEs, enabling more complete and interpretable latent decompositions, and suggesting the field may need to question ``foundation-model'' scaling for general-purpose SAEs.

