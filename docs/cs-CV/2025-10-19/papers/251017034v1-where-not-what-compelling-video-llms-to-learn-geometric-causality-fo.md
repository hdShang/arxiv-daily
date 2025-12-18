---
layout: default
title: Where, Not What: Compelling Video LLMs to Learn Geometric Causality for 3D-Grounding
---

# Where, Not What: Compelling Video LLMs to Learn Geometric Causality for 3D-Grounding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.17034" class="toolbar-btn" target="_blank">📄 arXiv: 2510.17034v1</a>
  <a href="https://arxiv.org/pdf/2510.17034.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.17034v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.17034v1', 'Where, Not What: Compelling Video LLMs to Learn Geometric Causality for 3D-Grounding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yutong Zhong

**分类**: cs.CV

**发布日期**: 2025-10-19

---

## 💡 一句话要点

**提出W2R2框架，解决视频LLM中3D grounding的2D语义偏见问题。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `3D Grounding` `视觉-语言模型` `多模态融合` `表示学习` `几何推理`

## 📋 核心要点

1. 现有VLM在3D grounding中过度依赖2D图像特征，忽略3D几何信息，导致“2D语义偏见”和定位精度下降。
2. W2R2框架通过解耦2D和3D特征表示，分别作为语义信标和空间锚点，从而抑制2D语义偏见。
3. 在ScanRefer和ScanQA数据集上，W2R2显著提升了3D grounding的定位精度和鲁棒性，尤其在复杂场景中。

## 📝 摘要（中文）

多模态3D grounding在视觉-语言模型（VLM）中备受关注，旨在提升复杂环境中的空间推理能力。然而，这些模型存在严重的“2D语义偏见”，过度依赖2D图像特征进行粗略定位，很大程度上忽略了3D几何输入，导致融合性能欠佳。本文提出了一种名为What-Where Representation Re-Forming (W2R2) 的新型训练框架，通过解耦表示学习和有针对性的捷径抑制来解决这个问题。我们的方法从根本上重塑了模型的内部空间，将2D特征指定为“What”识别的语义信标，将3D特征指定为“Where”定位的空间锚点，从而在不修改推理架构的情况下实现精确的3D grounding。关键组件包括一个双目标损失函数，其中包含一个对齐损失，该损失使用适应的交叉熵来监督融合预测，以实现多模态协同；以及一个伪标签损失，该损失通过基于边际的机制惩罚过于有效的2D主导伪输出。在ScanRefer和ScanQA上进行的实验证明了W2R2的有效性，在定位精度和鲁棒性方面取得了显著提升，尤其是在杂乱的户外场景中。

## 🔬 方法详解

**问题定义**：现有视觉-语言模型在进行3D grounding时，过度依赖2D图像的语义信息，而忽略了3D几何信息提供的空间线索。这种“2D语义偏见”导致模型在复杂场景下定位精度下降，无法充分利用多模态信息的优势。现有方法难以有效融合2D语义和3D几何信息，导致次优的3D grounding性能。

**核心思路**：W2R2的核心思路是通过解耦2D和3D特征的表示，强制模型学习将2D特征作为“What”的语义信息来源，将3D特征作为“Where”的空间信息来源。通过这种方式，模型可以更好地利用3D几何信息进行精确定位，从而克服2D语义偏见。这种解耦是通过特定的损失函数和训练策略来实现的。

**技术框架**：W2R2框架主要包含以下几个阶段：首先，模型接收视觉和语言输入，提取2D图像特征和3D几何特征。然后，通过特征融合模块将多模态特征进行融合。接下来，模型基于融合后的特征进行3D grounding预测。最后，通过双目标损失函数对模型进行训练，包括对齐损失和伪标签损失。整个框架在训练阶段进行优化，推理阶段保持不变。

**关键创新**：W2R2最重要的技术创新点在于其解耦表示学习和有针对性的捷径抑制策略。与现有方法不同，W2R2不是简单地将2D和3D特征进行融合，而是通过特定的损失函数和训练策略，强制模型学习将2D和3D特征分别作为语义和空间信息的来源。这种解耦表示学习可以有效抑制2D语义偏见，提高3D grounding的精度和鲁棒性。

**关键设计**：W2R2的关键设计包括：1) 对齐损失：使用适应的交叉熵损失来监督融合预测，鼓励多模态特征的协同作用。2) 伪标签损失：通过基于边际的机制惩罚过于有效的2D主导伪输出，从而抑制2D语义偏见。3) 双目标损失函数：将对齐损失和伪标签损失结合起来，共同优化模型。具体的损失函数权重和边际参数需要根据实验进行调整。

## 📊 实验亮点

实验结果表明，W2R2在ScanRefer和ScanQA数据集上取得了显著的性能提升。在ScanRefer数据集上，W2R2的定位精度提高了X%，在ScanQA数据集上，W2R2的鲁棒性提高了Y%。尤其是在杂乱的户外场景中，W2R2的性能提升更为明显，证明了其有效抑制2D语义偏见的能力。具体数值X和Y需要在论文中查找。

## 🎯 应用场景

该研究成果可应用于机器人导航、自动驾驶、增强现实等领域。通过提升3D grounding的精度和鲁棒性，可以使机器人在复杂环境中更好地理解和定位物体，从而实现更智能的交互和决策。未来，该技术有望应用于智能家居、工业自动化等领域，提升人机协作效率。

## 📄 摘要（原文）

> Multimodal 3D grounding has garnered considerable interest in Vision-Language Models (VLMs) \cite{yin2025spatial} for advancing spatial reasoning in complex environments. However, these models suffer from a severe "2D semantic bias" that arises from over-reliance on 2D image features for coarse localization, largely disregarding 3D geometric inputs and resulting in suboptimal fusion performance. In this paper, we propose a novel training framework called What-Where Representation Re-Forming (W2R2) to tackle this issue via disentangled representation learning and targeted shortcut suppression. Our approach fundamentally reshapes the model's internal space by designating 2D features as semantic beacons for "What" identification and 3D features as spatial anchors for "Where" localization, enabling precise 3D grounding without modifying inference architecture. Key components include a dual-objective loss function with an Alignment Loss that supervises fused predictions using adapted cross-entropy for multimodal synergy, and a Pseudo-Label Loss that penalizes overly effective 2D-dominant pseudo-outputs via a margin-based mechanism. Experiments conducted on ScanRefer and ScanQA demonstrate the effectiveness of W2R2, with significant gains in localization accuracy and robustness, particularly in cluttered outdoor scenes.

