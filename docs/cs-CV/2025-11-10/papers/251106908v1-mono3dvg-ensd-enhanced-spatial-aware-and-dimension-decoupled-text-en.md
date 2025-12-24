---
layout: default
title: "Mono3DVG-EnSD: Enhanced Spatial-aware and Dimension-decoupled Text Encoding for Monocular 3D Visual Grounding"
---

# Mono3DVG-EnSD: Enhanced Spatial-aware and Dimension-decoupled Text Encoding for Monocular 3D Visual Grounding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.06908" class="toolbar-btn" target="_blank">📄 arXiv: 2511.06908v1</a>
  <a href="https://arxiv.org/pdf/2511.06908.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.06908v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.06908v1', 'Mono3DVG-EnSD: Enhanced Spatial-aware and Dimension-decoupled Text Encoding for Monocular 3D Visual Grounding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuzhen Li, Min Liu, Zhaoyang Li, Yuan Bian, Xueping Wang, Erbo Zhai, Yaonan Wang

**分类**: cs.CV, cs.MM

**发布日期**: 2025-11-10

**备注**: 10 pages

---

## 💡 一句话要点

**提出Mono3DVG-EnSD框架，增强单目3D视觉定位中空间感知和维度解耦的文本编码。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `单目3D视觉定位` `视觉定位` `自然语言处理` `跨模态融合` `空间关系推理`

## 📋 核心要点

1. 现有Mono3DVG方法过度依赖高确定性关键词，忽略了文本中蕴含的空间关系描述。
2. Mono3DVG-EnSD框架通过CLIP-LCA和D2M模块，分别增强空间感知能力和解耦跨维度特征。
3. 在Mono3DRefer数据集上，Mono3DVG-EnSD在各项指标上均取得SOTA，远距离定位精度显著提升。

## 📝 摘要（中文）

本文提出了一种新的单目3D视觉定位(Mono3DVG)框架Mono3DVG-EnSD，旨在解决现有方法过度依赖高确定性关键词而忽略空间描述，以及通用文本特征中2D/3D信息混合导致跨维度干扰的问题。该框架集成了CLIP引导的词汇确定性适配器(CLIP-LCA)和维度解耦模块(D2M)。CLIP-LCA动态屏蔽高确定性关键词，保留低确定性空间描述，促使模型更深入理解文本中的空间关系。D2M从通用文本特征中解耦维度特定的(2D/3D)文本特征，以指导相应维度的视觉特征，从而减轻跨维度干扰。在Mono3DRefer数据集上的实验表明，该方法在所有指标上均达到了最先进的性能，尤其是在远距离(Far(Acc@0.5))场景下，性能提升了+13.54%。

## 🔬 方法详解

**问题定义**：单目3D视觉定位旨在利用文本描述在RGB图像中定位3D物体。现有方法的痛点在于：1)过度依赖文本中显式的高确定性关键词，忽略了隐式的空间关系描述；2)通用文本特征混合了2D和3D信息，与单一维度的视觉特征融合时会产生跨维度干扰。

**核心思路**：本文的核心思路是增强模型对文本中空间关系的理解，并解耦文本特征中的2D和3D信息，从而更有效地指导视觉特征的学习。通过CLIP-LCA模块关注空间描述，通过D2M模块避免跨维度干扰，提升定位精度。

**技术框架**：Mono3DVG-EnSD框架主要包含两个关键模块：CLIP-Guided Lexical Certainty Adapter (CLIP-LCA) 和 Dimension-Decoupled Module (D2M)。首先，CLIP-LCA用于动态调整文本特征，突出空间描述。然后，D2M将通用文本特征分解为2D和3D特定特征，分别与对应的2D和3D视觉特征进行融合。最后，融合后的特征用于预测3D物体的位置。

**关键创新**：该论文的关键创新在于：1)提出了CLIP-LCA模块，通过动态屏蔽高确定性关键词，迫使模型学习文本中更丰富的空间关系；2)提出了D2M模块，通过解耦文本特征中的2D和3D信息，避免了跨维度干扰，提升了特征融合的效率。与现有方法相比，该方法更关注文本中的空间信息，并解决了跨维度特征融合的问题。

**关键设计**：CLIP-LCA模块利用CLIP模型计算文本中每个词的确定性得分，并根据得分动态调整词的权重。D2M模块使用线性层将通用文本特征分解为2D和3D特定特征。损失函数包括定位损失和分类损失，用于优化模型的定位和识别能力。具体参数设置和网络结构细节在论文中有详细描述。

## 📊 实验亮点

实验结果表明，Mono3DVG-EnSD在Mono3DRefer数据集上取得了SOTA性能。尤其是在具有挑战性的远距离(Far(Acc@0.5))场景下，该方法相比现有最佳方法提升了+13.54%。这表明该方法在处理复杂场景和远距离物体定位方面具有显著优势。

## 🎯 应用场景

该研究成果可应用于机器人导航、自动驾驶、增强现实等领域。例如，机器人可以通过自然语言指令在复杂环境中定位目标物体；自动驾驶系统可以根据乘客的语音指令识别并定位车辆周围的特定物体；增强现实应用可以根据用户的文本描述在真实场景中叠加虚拟物体。

## 📄 摘要（原文）

> Monocular 3D Visual Grounding (Mono3DVG) is an emerging task that locates 3D objects in RGB images using text descriptions with geometric cues. However, existing methods face two key limitations. Firstly, they often over-rely on high-certainty keywords that explicitly identify the target object while neglecting critical spatial descriptions. Secondly, generalized textual features contain both 2D and 3D descriptive information, thereby capturing an additional dimension of details compared to singular 2D or 3D visual features. This characteristic leads to cross-dimensional interference when refining visual features under text guidance. To overcome these challenges, we propose Mono3DVG-EnSD, a novel framework that integrates two key components: the CLIP-Guided Lexical Certainty Adapter (CLIP-LCA) and the Dimension-Decoupled Module (D2M). The CLIP-LCA dynamically masks high-certainty keywords while retaining low-certainty implicit spatial descriptions, thereby forcing the model to develop a deeper understanding of spatial relationships in captions for object localization. Meanwhile, the D2M decouples dimension-specific (2D/3D) textual features from generalized textual features to guide corresponding visual features at same dimension, which mitigates cross-dimensional interference by ensuring dimensionally-consistent cross-modal interactions. Through comprehensive comparisons and ablation studies on the Mono3DRefer dataset, our method achieves state-of-the-art (SOTA) performance across all metrics. Notably, it improves the challenging Far(Acc@0.5) scenario by a significant +13.54%.

