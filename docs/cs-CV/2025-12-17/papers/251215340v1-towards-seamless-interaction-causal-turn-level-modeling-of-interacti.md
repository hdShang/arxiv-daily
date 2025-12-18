---
layout: default
title: Towards Seamless Interaction: Causal Turn-Level Modeling of Interactive 3D Conversational Head Dynamics
---

# Towards Seamless Interaction: Causal Turn-Level Modeling of Interactive 3D Conversational Head Dynamics

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.15340" class="toolbar-btn" target="_blank">📄 arXiv: 2512.15340v1</a>
  <a href="https://arxiv.org/pdf/2512.15340.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.15340v1" onclick="toggleFavorite(this, '2512.15340v1', 'Towards Seamless Interaction: Causal Turn-Level Modeling of Interactive 3D Conversational Head Dynamics')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Junjie Chen, Fei Wang, Zhihao Huang, Qing Zhou, Kun Li, Dan Guo, Linfeng Zhang, Xun Yang

**分类**: cs.CV

**发布日期**: 2025-12-17

**🔗 代码/项目**: [GITHUB](https://github.com/CoderChen01/towards-seamleass-interaction)

---

## 💡 一句话要点

**提出TIMAR，用于建模交互式3D对话头部的因果turn级动态生成。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `3D头部动态生成` `对话建模` `因果自回归` `多模态融合` `扩散模型` `人机交互` `虚拟化身`

## 📋 核心要点

1. 现有方法通常将说话和听讲视为独立过程，或依赖非因果的全序列建模，阻碍了turn之间的时间连贯性。
2. TIMAR通过turn级交错掩码自回归，融合多模态信息并利用因果注意力累积对话历史，从而实现更自然的头部动态生成。
3. 实验表明，TIMAR在DualTalk基准测试上显著降低了Fréchet距离和MSE，并在分布外数据上表现出良好的泛化能力。

## 📝 摘要（中文）

本文提出了一种用于3D对话头部生成的因果框架TIMAR（Turn-level Interleaved Masked AutoRegression），该框架将对话建模为交错的音频-视觉上下文。TIMAR在每个turn中融合多模态信息，并应用turn级因果注意力来累积对话历史。同时，一个轻量级的扩散头预测连续的3D头部动态，捕捉协调性和表达性变化。在DualTalk基准测试上的实验表明，TIMAR在测试集上将Fréchet距离和MSE降低了15-30%，并在分布外数据上取得了类似的提升。源代码将在GitHub仓库https://github.com/CoderChen01/towards-seamleass-interaction 中发布。

## 🔬 方法详解

**问题定义**：现有方法在建模对话场景下的3D头部动态时，通常存在两个主要问题。一是将说话者和听者的头部动作视为独立的，忽略了它们之间的相互影响。二是依赖于非因果的全序列建模，无法保证生成结果的时间连贯性，尤其是在对话的turn切换时容易出现不自然的跳变。这些问题限制了虚拟化身和交互式机器人在对话场景中的应用。

**核心思路**：TIMAR的核心思路是将对话过程建模为一系列交错的音频-视觉上下文turn。每个turn包含说话者的音频信息和听者的头部动态信息，通过这种交错的方式，模型可以学习到说话者和听者之间的相互依赖关系。此外，TIMAR采用因果自回归的方式，保证了生成结果的时间连贯性，避免了turn切换时的突兀感。

**技术框架**：TIMAR的整体框架包括三个主要模块：多模态融合模块、turn级因果注意力模块和扩散头部动态预测模块。首先，多模态融合模块将音频和视觉信息融合到每个turn的上下文中。然后，turn级因果注意力模块利用因果注意力机制，将历史turn的信息累积到当前turn中，从而捕捉对话的历史信息。最后，扩散头部动态预测模块利用扩散模型预测连续的3D头部动态。

**关键创新**：TIMAR的关键创新在于其turn级交错掩码自回归建模方式。这种方式能够有效地建模说话者和听者之间的相互依赖关系，并保证生成结果的时间连贯性。此外，TIMAR采用轻量级的扩散头部动态预测模块，能够生成更加自然和富有表现力的头部动作。

**关键设计**：在多模态融合模块中，论文采用了交叉注意力机制来融合音频和视觉信息。在turn级因果注意力模块中，论文采用了masked self-attention机制，保证了因果性。在扩散头部动态预测模块中，论文采用了U-Net结构，并使用L1损失和对抗损失来训练模型。具体的参数设置和网络结构细节可以在论文的实验部分找到。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15340v1/x2.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15340v1/x3.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15340v1/x4.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

TIMAR在DualTalk基准测试上取得了显著的性能提升。在测试集上，TIMAR将Fréchet距离和MSE分别降低了15-30%。此外，TIMAR在分布外数据上表现出良好的泛化能力，证明了其在实际应用中的潜力。这些实验结果表明，TIMAR能够有效地建模对话场景下的3D头部动态，并生成更加自然和连贯的头部动作。

## 🎯 应用场景

TIMAR的研究成果可广泛应用于虚拟化身、交互式机器人、游戏角色动画等领域。通过生成更自然、连贯的3D对话头部动态，可以提升用户在虚拟环境中的沉浸感和交互体验，使人机交互更加流畅自然。未来，该技术有望应用于远程会议、在线教育、虚拟社交等场景，促进人与机器之间的无缝交流。

## 📄 摘要（原文）

> Human conversation involves continuous exchanges of speech and nonverbal cues such as head nods, gaze shifts, and facial expressions that convey attention and emotion. Modeling these bidirectional dynamics in 3D is essential for building expressive avatars and interactive robots. However, existing frameworks often treat talking and listening as independent processes or rely on non-causal full-sequence modeling, hindering temporal coherence across turns. We present TIMAR (Turn-level Interleaved Masked AutoRegression), a causal framework for 3D conversational head generation that models dialogue as interleaved audio-visual contexts. It fuses multimodal information within each turn and applies turn-level causal attention to accumulate conversational history, while a lightweight diffusion head predicts continuous 3D head dynamics that captures both coordination and expressive variability. Experiments on the DualTalk benchmark show that TIMAR reduces Fréchet Distance and MSE by 15-30% on the test set, and achieves similar gains on out-of-distribution data. The source code will be released in the GitHub repository https://github.com/CoderChen01/towards-seamleass-interaction.

