---
layout: default
title: "MLA: A Multisensory Language-Action Model for Multimodal Understanding and Forecasting in Robotic Manipulation"
---

# MLA: A Multisensory Language-Action Model for Multimodal Understanding and Forecasting in Robotic Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.26642" class="toolbar-btn" target="_blank">📄 arXiv: 2509.26642v1</a>
  <a href="https://arxiv.org/pdf/2509.26642.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.26642v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.26642v1', 'MLA: A Multisensory Language-Action Model for Multimodal Understanding and Forecasting in Robotic Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhuoyang Liu, Jiaming Liu, Jiadong Xu, Nuowei Han, Chenyang Gu, Hao Chen, Kaichen Zhou, Renrui Zhang, Kai Chin Hsieh, Kun Wu, Zhengping Che, Jian Tang, Shanghang Zhang

**分类**: cs.RO

**发布日期**: 2025-09-30

---

## 💡 一句话要点

**提出MLA多感官语言-动作模型，增强机器人操作中多模态理解与预测能力**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多感官融合` `机器人操作` `视觉语言动作模型` `物理世界建模` `大型语言模型`

## 📋 核心要点

1. 现有VLA模型在机器人操作中忽略了对机器人特定多感官信息的全面理解，限制了复杂操作的性能。
2. MLA模型通过无编码器多模态对齐方案和未来多感官生成后训练策略，增强了对物理世界的理解和预测能力。
3. 实验结果表明，MLA模型在复杂操作任务中显著优于现有方法，并在未见配置中表现出更好的泛化能力。

## 📝 摘要（中文）

视觉-语言-动作模型(VLA)通过继承视觉-语言模型(VLM)并学习动作生成，已在机器人操作任务中展现出泛化能力。然而，现有VLA模型主要关注视觉和语言的解释以生成动作，忽略了机器人与空间物理世界的感知和交互。为此，我们提出了一个多感官语言-动作(MLA)模型，它协同感知异构感官模态，并预测未来的多感官目标，以促进物理世界建模。具体来说，为了增强感知表征，我们提出了一种无编码器的多模态对齐方案，创新性地将大型语言模型本身重新用作感知模块，通过位置对应直接解释2D图像、3D点云和触觉token。为了进一步增强MLA对物理动态的理解，我们设计了一种未来多感官生成后训练策略，使MLA能够推理语义、几何和交互信息，为动作生成提供更强大的条件。在评估中，MLA模型在复杂、接触丰富的真实世界任务中，分别优于先前的最先进的2D和3D VLA方法12%和24%，同时也展示了对未见配置的改进泛化能力。

## 🔬 方法详解

**问题定义**：现有视觉-语言-动作模型(VLA)在机器人操作任务中，主要依赖视觉和语言信息生成动作，而忽略了机器人与物理世界的交互感知，特别是多感官信息的融合和利用。这导致模型在复杂、接触丰富的任务中表现不佳，泛化能力受限。现有方法难以有效建模物理世界的动态变化和多模态信息之间的关联。

**核心思路**：MLA的核心思路是利用大型语言模型(LLM)作为多模态信息的统一处理框架，通过无编码器的对齐方式，将视觉(2D图像、3D点云)和触觉信息直接映射到LLM的token空间中。此外，通过未来多感官生成任务，让模型学习预测未来的感官状态，从而更好地理解物理世界的动态变化，为动作生成提供更鲁棒的条件。

**技术框架**：MLA模型主要包含两个核心模块：多模态感知模块和未来多感官生成模块。多模态感知模块负责将2D图像、3D点云和触觉信息通过位置对应关系对齐到LLM的token空间。未来多感官生成模块则利用LLM预测未来的多感官状态，包括视觉、触觉等信息。整个流程是，首先通过多模态感知模块提取多模态特征，然后利用未来多感官生成模块预测未来状态，最后基于预测的状态生成动作。

**关键创新**：MLA的关键创新在于以下两点：一是提出了无编码器的多模态对齐方案，直接利用LLM作为感知模块，避免了传统编码器可能带来的信息损失；二是设计了未来多感官生成后训练策略，使模型能够推理物理世界的动态变化，从而更好地理解和预测环境。

**关键设计**：在多模态对齐方面，使用了位置编码将不同模态的信息对齐到LLM的token空间。在未来多感官生成方面，采用了自回归的方式预测未来的多感官状态，并使用了交叉熵损失函数进行训练。具体来说，2D图像和3D点云通过预训练的视觉模型提取特征，然后通过线性层映射到LLM的token空间。触觉信息则直接通过embedding层映射到token空间。在训练过程中，使用了teacher forcing策略，即使用真实的历史状态作为输入来预测未来的状态。

## 📊 实验亮点

MLA模型在真实世界的机器人操作任务中取得了显著的性能提升。在复杂、接触丰富的任务中，MLA模型分别优于先前的最先进的2D和3D VLA方法12%和24%。此外，MLA模型在未见过的配置中也表现出更好的泛化能力，证明了其在实际应用中的潜力。

## 🎯 应用场景

MLA模型可应用于各种需要复杂操作和精细控制的机器人任务，如装配、抓取、操作工具等。该模型能够提升机器人在未知环境中的适应性和泛化能力，降低对人工示教的依赖，从而加速机器人在工业、医疗、服务等领域的应用。

## 📄 摘要（原文）

> Vision-language-action models (VLAs) have shown generalization capabilities in robotic manipulation tasks by inheriting from vision-language models (VLMs) and learning action generation. Most VLA models focus on interpreting vision and language to generate actions, whereas robots must perceive and interact within the spatial-physical world. This gap highlights the need for a comprehensive understanding of robotic-specific multisensory information, which is crucial for achieving complex and contact-rich control. To this end, we introduce a multisensory language-action (MLA) model that collaboratively perceives heterogeneous sensory modalities and predicts future multisensory objectives to facilitate physical world modeling. Specifically, to enhance perceptual representations, we propose an encoder-free multimodal alignment scheme that innovatively repurposes the large language model itself as a perception module, directly interpreting multimodal cues by aligning 2D images, 3D point clouds, and tactile tokens through positional correspondence. To further enhance MLA's understanding of physical dynamics, we design a future multisensory generation post-training strategy that enables MLA to reason about semantic, geometric, and interaction information, providing more robust conditions for action generation. For evaluation, the MLA model outperforms the previous state-of-the-art 2D and 3D VLA methods by 12% and 24% in complex, contact-rich real-world tasks, respectively, while also demonstrating improved generalization to unseen configurations. Project website: https://sites.google.com/view/open-mla

