---
layout: default
title: Auto-Vocabulary 3D Object Detection
---

# Auto-Vocabulary 3D Object Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16077" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16077v1</a>
  <a href="https://arxiv.org/pdf/2512.16077.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16077v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16077v1', 'Auto-Vocabulary 3D Object Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haomeng Zhang, Kuan-Chuan Peng, Suhas Lohit, Raymond A. Yeh

**分类**: cs.CV

**发布日期**: 2025-12-18

**备注**: technical report

---

## 💡 一句话要点

**提出AV3DOD，实现无需用户干预的自动词汇3D目标检测**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `3D目标检测` `开放词汇` `自动词汇` `视觉-语言模型` `图像字幕`

## 📋 核心要点

1. 现有开放词汇3D目标检测依赖用户指定类别，限制了其自动化程度和泛化能力。
2. AV3DOD利用2D视觉-语言模型自动生成类别，无需人工干预，提升了检测的灵活性。
3. 实验表明，AV3DOD在ScanNetV2数据集上，mAP提升3.48，语义质量SS提升24.5%。

## 📝 摘要（中文）

开放词汇3D目标检测方法能够定位训练期间未见过的类别的3D框。尽管名称如此，现有方法在训练和推理时都依赖于用户指定的类别。我们提出研究自动词汇3D目标检测（AV3DOD），其中类别是为检测到的对象自动生成的，无需任何用户输入。为此，我们引入了语义分数（SS）来评估生成的类名称的质量。然后，我们开发了一个新颖的框架AV3DOD，它利用2D视觉-语言模型（VLM）通过图像字幕、伪3D框生成和特征空间语义扩展来生成丰富的语义候选。AV3DOD在ScanNetV2和SUNRGB-D数据集上的定位（mAP）和语义质量（SS）方面均实现了最先进的（SOTA）性能。值得注意的是，它超过了SOTA方法CoDA，在ScanNetV2上总体mAP提高了3.48，并且在SS方面实现了24.5%的相对改进。

## 🔬 方法详解

**问题定义**：现有开放词汇3D目标检测方法虽然能够检测训练集中未见过的类别，但仍然依赖于用户在训练和推理阶段提供类别信息。这限制了系统的自动化程度，并且可能无法覆盖所有潜在的类别。因此，需要一种能够自动生成类别名称的3D目标检测方法。

**核心思路**：AV3DOD的核心思路是利用2D视觉-语言模型（VLM）的强大语义理解能力，从图像中提取丰富的语义信息，并将其用于生成3D目标的类别名称。通过图像字幕、伪3D框生成和特征空间语义扩展等技术，将2D视觉信息与3D几何信息相结合，从而实现自动化的类别生成。

**技术框架**：AV3DOD框架主要包含以下几个阶段：1) **图像字幕**：使用2D VLM对场景图像进行描述，生成初始的语义候选。2) **伪3D框生成**：根据检测到的3D目标，在图像中生成对应的伪3D框，并提取框内的视觉特征。3) **特征空间语义扩展**：利用VLM将视觉特征映射到语义空间，并结合图像字幕生成的语义候选，进行语义扩展和筛选。4) **语义分数评估**：引入语义分数（SS）来评估生成的类别名称的质量，选择最佳的类别名称。

**关键创新**：AV3DOD的关键创新在于实现了完全自动化的类别生成，无需任何用户输入。通过巧妙地利用2D VLM的语义理解能力，将2D视觉信息与3D几何信息相结合，从而克服了传统方法对人工标注的依赖。此外，语义分数（SS）的引入为评估生成类别名称的质量提供了一种有效的手段。

**关键设计**：在图像字幕阶段，使用了预训练的2D VLM模型，例如CLIP或ALIGN。在伪3D框生成阶段，需要根据3D目标的位置和大小，将其投影到2D图像平面上，并生成对应的伪3D框。在特征空间语义扩展阶段，使用了余弦相似度等方法来衡量视觉特征和语义候选之间的相似度。语义分数（SS）的计算方式需要根据具体的任务和数据集进行调整，可以考虑使用语言模型的困惑度或人工评估等方法。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16077v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16077v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16077v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

AV3DOD在ScanNetV2和SUNRGB-D数据集上取得了显著的性能提升。在ScanNetV2数据集上，AV3DOD的总体mAP超过了SOTA方法CoDA 3.48，并且在语义质量（SS）方面实现了24.5%的相对改进。这些结果表明，AV3DOD能够有效地生成高质量的类别名称，并提高3D目标检测的性能。

## 🎯 应用场景

AV3DOD可应用于机器人导航、自动驾驶、场景理解等领域。在这些场景中，系统需要识别各种各样的物体，而人工标注所有类别是不现实的。AV3DOD能够自动生成类别名称，从而扩展了系统的识别能力，提高了其适应性和鲁棒性。未来，该技术有望应用于更广泛的场景，例如智能家居、虚拟现实等。

## 📄 摘要（原文）

> Open-vocabulary 3D object detection methods are able to localize 3D boxes of classes unseen during training. Despite the name, existing methods rely on user-specified classes both at training and inference. We propose to study Auto-Vocabulary 3D Object Detection (AV3DOD), where the classes are automatically generated for the detected objects without any user input. To this end, we introduce Semantic Score (SS) to evaluate the quality of the generated class names. We then develop a novel framework, AV3DOD, which leverages 2D vision-language models (VLMs) to generate rich semantic candidates through image captioning, pseudo 3D box generation, and feature-space semantics expansion. AV3DOD achieves the state-of-the-art (SOTA) performance on both localization (mAP) and semantic quality (SS) on the ScanNetV2 and SUNRGB-D datasets. Notably, it surpasses the SOTA, CoDA, by 3.48 overall mAP and attains a 24.5% relative improvement in SS on ScanNetV2.

