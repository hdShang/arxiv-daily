---
layout: default
title: "CoPatch: Zero-Shot Referring Image Segmentation by Leveraging Untapped Spatial Knowledge in CLIP"
---

# CoPatch: Zero-Shot Referring Image Segmentation by Leveraging Untapped Spatial Knowledge in CLIP

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.23098" class="toolbar-btn" target="_blank">📄 arXiv: 2509.23098v1</a>
  <a href="https://arxiv.org/pdf/2509.23098.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.23098v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.23098v1', 'CoPatch: Zero-Shot Referring Image Segmentation by Leveraging Untapped Spatial Knowledge in CLIP')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Na Min An, Inha Kang, Minhyun Lee, Hyunjung Shim

**分类**: cs.CV, cs.AI

**发布日期**: 2025-09-27

**备注**: 28 pages, 22 Figures, 11 Tables

---

## 💡 一句话要点

**CoPatch：利用CLIP中未开发的 spatial knowledge 实现零样本指代图像分割**

🎯 **匹配领域**: **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `指代图像分割` `零样本学习` `视觉-语言模型` `CLIP` `空间推理`

## 📋 核心要点

1. 现有指代图像分割方法难以有效利用CLIP等VLM中的空间信息，限制了模型性能。
2. CoPatch通过挖掘CLIP内部组件，增强文本和图像模态的空间表示，提升空间定位能力。
3. 实验表明，CoPatch在多个数据集上显著提升了零样本指代图像分割的性能，无需额外训练。

## 📝 摘要（中文）

空间定位对于指代图像分割（RIS）至关重要，该任务旨在定位由语言描述的对象。现有的基础视觉-语言模型（VLMs），如CLIP，擅长对齐图像和文本，但在理解空间关系方面存在困难。在语言流中，大多数现有方法通常只关注主要名词短语，从而削弱了上下文token。在视觉流中，CLIP为具有不同空间布局的图像生成相似的特征，导致对空间结构的敏感性有限。为了解决这些限制，我们提出了CoPatch，一个零样本RIS框架，它利用内部模型组件来增强文本和图像模态中的空间表示。对于语言，CoPatch通过结合携带空间线索的上下文token来构建混合文本特征。对于视觉，它使用我们从中间层发现的新路径提取patch级别的图像特征，其中空间结构得到更好的保留。这些增强的特征被融合到聚类的图像-文本相似度图CoMap中，从而实现精确的mask选择。因此，CoPatch在RefCOCO、RefCOCO+、RefCOCOg和PhraseCut上显著提高了零样本RIS的空间定位性能（+2-7 mIoU），而无需任何额外的训练。我们的研究结果强调了恢复和利用VLMs中固有嵌入的未开发空间知识的重要性，从而为零样本RIS开辟了机会。

## 🔬 方法详解

**问题定义**：论文旨在解决零样本指代图像分割任务中，现有方法无法充分利用CLIP等视觉-语言模型（VLM）中蕴含的空间信息的问题。现有方法通常只关注文本中的主要名词短语，忽略了上下文token提供的空间线索，并且CLIP对具有不同空间布局的图像产生相似的视觉特征，导致空间定位能力不足。

**核心思路**：论文的核心思路是挖掘并增强CLIP模型内部的文本和图像特征，以提升其空间感知能力。具体来说，通过融合上下文token来丰富文本特征，并从CLIP的中间层提取patch级别的图像特征，从而更好地保留空间结构信息。

**技术框架**：CoPatch框架主要包含以下几个模块：1) 混合文本特征提取模块，通过融合上下文token来增强文本特征；2) Patch级别图像特征提取模块，从CLIP的中间层提取patch级别的图像特征；3) 图像-文本相似度图（CoMap）构建模块，将增强的文本和图像特征融合到CoMap中；4) Mask选择模块，基于CoMap选择最佳的分割mask。

**关键创新**：论文的关键创新在于：1) 提出了一种混合文本特征提取方法，有效利用了上下文token中的空间信息；2) 发现了一种从CLIP中间层提取patch级别图像特征的有效路径，更好地保留了空间结构信息；3) 构建了聚类的图像-文本相似度图（CoMap），实现了更精确的mask选择。

**关键设计**：在文本特征提取方面，论文没有详细说明上下文token融合的具体方式，但强调了其重要性。在图像特征提取方面，论文提到发现了一种从中间层提取patch级别特征的“路径”，但没有给出具体的网络层数或操作细节。CoMap的构建和mask选择的具体算法也未详细描述，这些都属于未知信息。

## 📊 实验亮点

CoPatch在四个基准数据集（RefCOCO、RefCOCO+、RefCOCOg和PhraseCut）上进行了评估，结果表明，该方法在零样本指代图像分割任务中取得了显著的性能提升，mIoU指标平均提升了2-7个百分点，证明了其有效性，且无需任何额外的训练。

## 🎯 应用场景

CoPatch的潜在应用领域包括智能图像编辑、视觉导航、机器人交互等。例如，在智能图像编辑中，用户可以通过自然语言指定要编辑的对象及其位置；在视觉导航中，机器人可以根据指令找到特定位置的目标物体。该研究有助于提升视觉-语言模型的空间理解能力，推动人机交互和智能系统的发展。

## 📄 摘要（原文）

> Spatial grounding is crucial for referring image segmentation (RIS), where the goal of the task is to localize an object described by language. Current foundational vision-language models (VLMs), such as CLIP, excel at aligning images and text but struggle with understanding spatial relationships. Within the language stream, most existing methods often focus on the primary noun phrase when extracting local text features, undermining contextual tokens. Within the vision stream, CLIP generates similar features for images with different spatial layouts, resulting in limited sensitivity to spatial structure. To address these limitations, we propose \textsc{CoPatch}, a zero-shot RIS framework that leverages internal model components to enhance spatial representations in both text and image modalities. For language, \textsc{CoPatch} constructs hybrid text features by incorporating context tokens carrying spatial cues. For vision, it extracts patch-level image features using our novel path discovered from intermediate layers, where spatial structure is better preserved. These enhanced features are fused into a clustered image-text similarity map, \texttt{CoMap}, enabling precise mask selection. As a result, \textsc{CoPatch} significantly improves spatial grounding in zero-shot RIS across RefCOCO, RefCOCO+, RefCOCOg, and PhraseCut (+ 2--7 mIoU) without requiring any additional training. Our findings underscore the importance of recovering and leveraging the untapped spatial knowledge inherently embedded in VLMs, thereby paving the way for opportunities in zero-shot RIS.

