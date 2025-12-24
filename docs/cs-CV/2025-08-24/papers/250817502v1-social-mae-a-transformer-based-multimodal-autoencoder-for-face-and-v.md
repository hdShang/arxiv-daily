---
layout: default
title: "Social-MAE: A Transformer-Based Multimodal Autoencoder for Face and Voice"
---

# Social-MAE: A Transformer-Based Multimodal Autoencoder for Face and Voice

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.17502" class="toolbar-btn" target="_blank">📄 arXiv: 2508.17502v1</a>
  <a href="https://arxiv.org/pdf/2508.17502.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.17502v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.17502v1', 'Social-MAE: A Transformer-Based Multimodal Autoencoder for Face and Voice')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hugo Bohy, Minh Tran, Kevin El Haddad, Thierry Dutoit, Mohammad Soleymani

**分类**: cs.CV

**发布日期**: 2025-08-24

**备注**: 5 pages, 3 figures, IEEE FG 2024 conference

**期刊**: 2024 IEEE 18th International Conference on Automatic Face and Gesture Recognition (FG)

**🔗 代码/项目**: [GITHUB](https://github.com/HuBohy/SocialMAE)

---

## 💡 一句话要点

**提出Social-MAE以解决多模态社交行为理解问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `自监督学习` `情感识别` `社交行为分析` `音频-视觉融合`

## 📋 核心要点

1. 现有方法在理解多模态社交行为时面临挑战，尤其是在处理音频和视觉信息的融合方面。
2. Social-MAE通过修改CAV-MAE架构，增强了输入帧数量，并在大规模社交数据集上进行自监督预训练，提升了模型的表现。
3. 实验结果显示，Social-MAE在多模态情感识别和笑声识别任务上达到了最先进的水平，显性个性估计也表现出竞争力。

## 📝 摘要（中文）

人类社交行为本质上是多模态的，因此需要开发强大的视听模型来进行感知。本文提出了Social-MAE，这是一种基于扩展版对比音频-视觉掩码自编码器（CAV-MAE）的预训练视听掩码自编码器，专门针对社交数据进行预训练。我们对CAV-MAE进行了修改，使其能够接收更多帧作为输入，并在大规模人类社交互动数据集（VoxCeleb2）上以自监督方式进行预训练。通过对不同社交和情感下游任务（如情感识别、笑声检测和显性个性估计）进行微调和评估，我们展示了该模型的有效性。该模型在多模态情感识别和笑声识别上取得了最先进的结果，并在显性个性估计上表现出竞争力，证明了领域内自监督预训练的有效性。

## 🔬 方法详解

**问题定义**：本论文旨在解决多模态社交行为理解中的音频与视觉信息融合不足的问题。现有方法在处理复杂社交场景时，往往无法有效捕捉多模态信息的关联性。

**核心思路**：论文提出的Social-MAE通过扩展CAV-MAE的输入能力，能够处理更多的帧数据，从而更全面地捕捉社交行为中的音频和视觉信息。自监督预训练使得模型在特定领域内获得更好的表现。

**技术框架**：Social-MAE的整体架构包括音频和视觉信息的输入模块、掩码自编码器核心以及自监督预训练阶段。模型首先接收多帧音频和视觉数据，然后通过掩码机制进行特征学习，最后在下游任务中进行微调。

**关键创新**：最重要的技术创新在于对CAV-MAE的扩展，使其能够处理更多的输入帧，并在大规模社交数据集上进行自监督预训练。这一设计显著提升了模型在多模态任务上的表现。

**关键设计**：在模型设计中，关键参数包括输入帧的数量、掩码比例和损失函数的选择。网络结构采用了Transformer架构，以便更好地捕捉长距离依赖关系。

## 📊 实验亮点

实验结果表明，Social-MAE在多模态情感识别任务中达到了最先进的性能，准确率超过了现有基线模型，笑声识别任务也表现出显著提升，显示出自监督预训练的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括社交机器人、情感计算和人机交互等。通过提升多模态理解能力，Social-MAE能够在情感识别、社交行为分析等方面提供更精准的支持，未来可能在智能助手和社交媒体分析中发挥重要作用。

## 📄 摘要（原文）

> Human social behaviors are inherently multimodal necessitating the development of powerful audiovisual models for their perception. In this paper, we present Social-MAE, our pre-trained audiovisual Masked Autoencoder based on an extended version of Contrastive Audio-Visual Masked Auto-Encoder (CAV-MAE), which is pre-trained on audiovisual social data. Specifically, we modify CAV-MAE to receive a larger number of frames as input and pre-train it on a large dataset of human social interaction (VoxCeleb2) in a self-supervised manner. We demonstrate the effectiveness of this model by finetuning and evaluating the model on different social and affective downstream tasks, namely, emotion recognition, laughter detection and apparent personality estimation. The model achieves state-of-the-art results on multimodal emotion recognition and laughter recognition and competitive results for apparent personality estimation, demonstrating the effectiveness of in-domain self-supervised pre-training. Code and model weight are available here https://github.com/HuBohy/SocialMAE.

