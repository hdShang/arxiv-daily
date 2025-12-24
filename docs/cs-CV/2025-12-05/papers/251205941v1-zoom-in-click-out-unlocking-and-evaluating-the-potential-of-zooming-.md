---
layout: default
title: "Zoom in, Click out: Unlocking and Evaluating the Potential of Zooming for GUI Grounding"
---

# Zoom in, Click out: Unlocking and Evaluating the Potential of Zooming for GUI Grounding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.05941" class="toolbar-btn" target="_blank">📄 arXiv: 2512.05941v1</a>
  <a href="https://arxiv.org/pdf/2512.05941.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.05941v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.05941v1', 'Zoom in, Click out: Unlocking and Evaluating the Potential of Zooming for GUI Grounding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhiyuan Jiang, Shenghao Xie, Wenyi Li, Wenqiang Zu, Peihang Li, Jiahao Qiu, Siqi Pei, Lei Ma, Tiejun Huang, Mengdi Wang, Shilong Liu

**分类**: cs.CV, cs.AI, cs.CL

**发布日期**: 2025-12-05

**备注**: Code is available at https://github.com/Princeton-AI2-Lab/ZoomClick

---

## 💡 一句话要点

**提出ZoomClick，利用缩放先验提升GUI界面元素定位性能**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `GUI定位` `缩放先验` `视觉语言模型` `人机交互` `零样本学习`

## 📋 核心要点

1. 现有GUI定位方法依赖大规模边界框监督，面临跨平台泛化、复杂布局分析和细粒度元素定位等挑战。
2. ZoomClick方法利用缩放操作的先验知识，通过动态空间聚焦和自适应上下文切换，实现更精确的GUI元素定位。
3. 实验表明，ZoomClick显著提升了现有模型的性能，并在多个基准测试中取得了领先的结果，验证了其有效性。

## 📝 摘要（中文）

本文研究了缩放操作在GUI界面元素定位中的潜力，提出了一种无需训练的方法ZoomClick。该方法通过刻画缩放的四个关键属性（预缩放、深度、缩小尺寸、最小裁剪尺寸），充分发挥其在动态空间聚焦和自适应上下文切换方面的能力。实验表明，ZoomClick显著提升了通用视觉-语言模型和专用GUI定位模型的性能，在多个主流基准测试中取得了最先进的结果，例如，UI-Venus-72B在ScreenSpot-Pro上达到了73.1%的成功率。此外，本文还提出了GUIZoom-Bench，一个用于评估模型对缩放操作适应性的基准测试，旨在激发未来研究，以改进缩放操作，从而进一步提升GUI定位任务中的训练和测试时性能。

## 🔬 方法详解

**问题定义**：现有的GUI界面元素定位方法通常依赖于大量的边界框标注数据进行训练，这导致了几个问题：一是跨平台泛化能力差，因为不同平台的GUI布局差异很大；二是需要复杂的布局分析算法来理解GUI的结构；三是在定位细粒度元素时，精度难以保证。这些问题限制了GUI智能体在实际应用中的能力。

**核心思路**：本文的核心思路是利用缩放操作作为一种强大的先验知识来辅助GUI界面元素定位。缩放操作能够动态地聚焦于感兴趣的区域，并自适应地调整上下文信息，从而提高定位的准确性和效率。ZoomClick方法通过模拟用户在GUI界面上的缩放和点击行为，逐步缩小搜索范围，最终定位到目标元素。

**技术框架**：ZoomClick方法主要包含以下几个阶段：1) **预缩放**：根据初始的视觉信息和语言描述，确定一个初始的缩放区域。2) **深度估计**：估计当前缩放的深度，即缩放的次数。3) **缩小尺寸调整**：根据深度信息，自适应地调整缩小的尺寸。4) **最小裁剪尺寸限制**：设置一个最小的裁剪尺寸，防止过度缩放。通过迭代执行这些步骤，ZoomClick方法能够逐步缩小搜索范围，最终定位到目标元素。

**关键创新**：ZoomClick方法最重要的创新点在于它是一种无需训练的方法，完全依赖于缩放操作的先验知识。与现有的需要大量标注数据进行训练的方法不同，ZoomClick方法具有更好的泛化能力和适应性。此外，ZoomClick方法还能够充分利用缩放操作的动态空间聚焦和自适应上下文切换能力，从而提高定位的准确性和效率。

**关键设计**：ZoomClick方法的关键设计包括：1) **缩放区域的选择策略**：根据视觉信息和语言描述，选择最有可能包含目标元素的区域进行缩放。2) **深度估计方法**：根据缩放前后的图像变化，估计当前的缩放深度。3) **缩小尺寸的自适应调整策略**：根据深度信息，自适应地调整缩小的尺寸，以保证缩放的效率和准确性。4) **最小裁剪尺寸的设置**：设置一个最小的裁剪尺寸，防止过度缩放，并保证最终定位的精度。

## 📊 实验亮点

ZoomClick在多个GUI定位基准测试中取得了最先进的结果。例如，UI-Venus-72B模型在ScreenSpot-Pro数据集上达到了73.1%的成功率，相较于之前的最佳方法有显著提升。此外，GUIZoom-Bench基准测试的提出，为未来研究模型对缩放操作的适应性提供了新的评估标准。

## 🎯 应用场景

该研究成果可应用于开发更智能的GUI智能体，例如自动化测试工具、辅助功能软件和人机交互系统。通过提高GUI元素定位的准确性和效率，可以显著提升这些应用的用户体验和功能。未来，该研究还可以扩展到其他领域，例如移动应用开发和虚拟现实环境。

## 📄 摘要（原文）

> Grounding is a fundamental capability for building graphical user interface (GUI) agents. Although existing approaches rely on large-scale bounding box supervision, they still face various challenges, such as cross-platform generalization, complex layout analysis, and fine-grained element localization. In this paper, we investigate zoom as a strong yet underexplored prior for GUI grounding, and propose a training-free method, ZoomClick. By characterizing four key properties of zoom (i.e., pre-zoom, depth, shrink size, minimal crop size), we unlock its full capabilities for dynamic spatial focusing and adaptive context switching. Experiments demonstrate that our method significantly boosts the performance of both general vision-language and specialized GUI grounding models, achieving state-of-the-art results on several mainstream benchmarks; for example, UI-Venus-72B attains a 73.1% success rate on ScreenSpot-Pro. Furthermore, we present GUIZoom-Bench, a benchmark for evaluating model adaptability to zoom, aiming to inspire future research on improving zoom for further training and test-time scaling in GUI grounding tasks.

