---
layout: default
title: Empowering Dynamic Urban Navigation with Stereo and Mid-Level Vision
---

# Empowering Dynamic Urban Navigation with Stereo and Mid-Level Vision

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.10956" class="toolbar-btn" target="_blank">📄 arXiv: 2512.10956v1</a>
  <a href="https://arxiv.org/pdf/2512.10956.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.10956v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.10956v1', 'Empowering Dynamic Urban Navigation with Stereo and Mid-Level Vision')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wentao Zhou, Xuweiyi Chen, Vignesh Rajagopal, Jeffrey Chen, Rohan Chandra, Zezhou Cheng

**分类**: cs.CV

**发布日期**: 2025-12-11

**备注**: Project Page: https://www.cs.virginia.edu/~tsx4zn/stereowalk/

---

## 💡 一句话要点

**StereoWalker：融合双目视觉与中层视觉增强动态城市导航**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `双目视觉` `机器人导航` `中层视觉` `深度估计` `动态环境`

## 📋 核心要点

1. 现有端到端机器人导航模型依赖单目视觉，忽略中层视觉信息，导致在动态环境中几何理解不足。
2. StereoWalker利用双目视觉解决深度尺度模糊，并结合深度估计和像素跟踪等中层视觉模块增强几何和运动理解。
3. 实验表明，StereoWalker仅用少量数据即可达到甚至超越现有单目方法的性能，验证了中层视觉的有效性。

## 📝 摘要（中文）

语言和视觉领域的基础模型的成功激发了对完全端到端机器人导航基础模型（NFMs）的研究。NFMs直接将单目视觉输入映射到控制动作，完全忽略了中层视觉模块（跟踪、深度估计等）。虽然视觉能力将隐式出现的假设引人注目，但它需要大量的像素到动作的监督，而这些监督很难获得。在动态和非结构化环境中，挑战尤其明显，因为稳健的导航需要精确的几何和动态理解，而单目视图中的深度尺度模糊进一步限制了精确的空间推理。在本文中，我们表明，依赖单目视觉并忽略中层视觉先验是低效的。我们提出了StereoWalker，它使用双目输入和显式中层视觉（如深度估计和密集像素跟踪）来增强NFMs。我们的直觉很简单：双目输入解决了深度尺度模糊，而现代中层视觉模型提供了动态场景中可靠的几何和运动结构。我们还策划了一个大型双目导航数据集，其中包含来自互联网双目视频的自动动作注释，以支持StereoWalker的训练并促进未来的研究。通过我们的实验，我们发现中层视觉使StereoWalker能够以仅1.5%的训练数据达到与最先进技术相当的性能，并使用完整数据超越最先进技术。我们还观察到，双目视觉比单目输入产生更高的导航性能。

## 🔬 方法详解

**问题定义**：现有基于单目视觉的端到端导航模型在动态城市环境中表现不佳，主要原因是单目视觉存在深度尺度模糊，难以准确理解场景的几何结构和运动信息。此外，完全依赖端到端学习需要大量像素级别的动作标注数据，获取成本高昂。

**核心思路**：论文的核心思路是利用双目视觉提供准确的深度信息，并结合中层视觉模块（如深度估计和密集像素跟踪）来显式地提取场景的几何和运动结构。通过融合这些信息，模型可以更有效地进行空间推理和导航决策。

**技术框架**：StereoWalker的整体框架包括以下几个主要模块：1) 双目视觉输入：使用双目相机获取左右图像；2) 深度估计：利用双目图像估计场景的深度图；3) 密集像素跟踪：跟踪图像中像素的运动轨迹，提取运动信息；4) 导航策略学习：将双目图像、深度图和运动信息作为输入，学习导航策略，输出控制指令。

**关键创新**：论文的关键创新在于将双目视觉和中层视觉模块显式地融入到端到端导航模型中。与以往依赖单目视觉和隐式学习几何信息的模型相比，StereoWalker能够更有效地利用几何和运动信息，从而提高导航性能。

**关键设计**：论文的关键设计包括：1) 使用现有的深度估计和像素跟踪模型，避免从头训练；2) 设计合适的网络结构，将双目图像、深度图和运动信息融合在一起；3) 采用模仿学习的方式训练导航策略，利用自动标注的数据进行训练。

## 📊 实验亮点

StereoWalker在实验中表现出色，仅使用1.5%的训练数据即可达到与最先进单目方法相当的性能，使用完整数据集时，性能超越现有方法。实验还证明，双目视觉输入显著优于单目视觉输入，验证了双目视觉和中层视觉对于动态城市导航的重要性。

## 🎯 应用场景

该研究成果可应用于自动驾驶、机器人导航、无人机等领域。通过提升机器人在复杂动态环境中的导航能力，可以提高自动驾驶系统的安全性，扩展机器人的应用范围，例如在物流、安防、巡检等场景中实现自主导航。

## 📄 摘要（原文）

> The success of foundation models in language and vision motivated research in fully end-to-end robot navigation foundation models (NFMs). NFMs directly map monocular visual input to control actions and ignore mid-level vision modules (tracking, depth estimation, etc) entirely. While the assumption that vision capabilities will emerge implicitly is compelling, it requires large amounts of pixel-to-action supervision that are difficult to obtain. The challenge is especially pronounced in dynamic and unstructured settings, where robust navigation requires precise geometric and dynamic understanding, while the depth-scale ambiguity in monocular views further limits accurate spatial reasoning. In this paper, we show that relying on monocular vision and ignoring mid-level vision priors is inefficient.
>   We present StereoWalker, which augments NFMs with stereo inputs and explicit mid-level vision such as depth estimation and dense pixel tracking. Our intuition is straightforward: stereo inputs resolve the depth-scale ambiguity, and modern mid-level vision models provide reliable geometric and motion structure in dynamic scenes. We also curate a large stereo navigation dataset with automatic action annotation from Internet stereo videos to support training of StereoWalker and to facilitate future research. Through our experiments, we find that mid-level vision enables StereoWalker to achieve a comparable performance as the state-of-the-art using only 1.5% of the training data, and surpasses the state-of-the-art using the full data. We also observe that stereo vision yields higher navigation performance than monocular input.

