---
layout: default
title: "RotBench: Evaluating Multimodal Large Language Models on Identifying Image Rotation"
---

# RotBench: Evaluating Multimodal Large Language Models on Identifying Image Rotation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.13968" class="toolbar-btn" target="_blank">📄 arXiv: 2508.13968v2</a>
  <a href="https://arxiv.org/pdf/2508.13968.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.13968v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.13968v2', 'RotBench: Evaluating Multimodal Large Language Models on Identifying Image Rotation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tianyi Niu, Jaemin Cho, Elias Stengel-Eskin, Mohit Bansal

**分类**: cs.CV, cs.AI, cs.CL

**发布日期**: 2025-08-19 (更新: 2025-08-20)

**备注**: 20 pages. Code and data: https://github.com/tianyiniu/RotBench

---

## 💡 一句话要点

**提出RotBench以评估多模态大语言模型的图像旋转识别能力**

🎯 **匹配领域**: **支柱七：动作重定向 (Motion Retargeting)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `图像旋转识别` `视觉推理` `基准测试` `空间关系理解`

## 📋 核心要点

1. 现有多模态大语言模型在图像旋转识别任务中表现不佳，尤其是在90°和270°的区分上存在显著不足。
2. 论文提出RotBench基准，通过350幅图像评估MLLMs的视觉推理能力，特别是对图像旋转的识别能力。
3. 实验结果显示，尽管模型在识别0°和180°图像上表现良好，但在90°和270°的区分上几乎没有提升，表明模型的空间推理能力与人类存在显著差距。

## 📝 摘要（中文）

本研究探讨了多模态大语言模型（MLLMs）在识别旋转0°、90°、180°和270°的输入图像方向上的准确性。该任务要求模型具备强大的视觉推理能力，以检测旋转线索并在不同方向上理解图像的空间关系。为此，我们引入了RotBench，一个包含350幅经过人工筛选的生活方式、肖像和风景图像的基准测试。尽管这一任务相对简单，但我们的研究表明，多个最先进的MLLMs，包括GPT-5、o3和Gemini-2.5-Pro，在识别图像旋转方面的表现并不可靠。提供辅助信息或使用链式思维提示仅带来了小幅且不一致的提升。我们的结果显示，大多数模型能够可靠地识别正向（0°）图像，而某些模型能够识别倒置（180°）图像，但没有模型能够可靠地区分90°和270°的旋转。

## 🔬 方法详解

**问题定义**：本研究旨在解决多模态大语言模型在图像旋转识别中的不足，尤其是对90°和270°旋转的区分能力较弱，现有方法未能有效应对这一挑战。

**核心思路**：通过引入RotBench基准，系统评估MLLMs在不同旋转角度下的表现，旨在揭示模型的视觉推理能力与人类的差距。

**技术框架**：RotBench基准包含350幅图像，涵盖生活方式、肖像和风景类型，模型通过分析图像的旋转线索和空间关系进行识别。

**关键创新**：RotBench的引入为评估MLLMs提供了一个新的标准，特别是在旋转识别任务上，填补了现有研究的空白。

**关键设计**：实验中使用了多种辅助信息（如图像标题、深度图等）和链式思维提示，但结果显示这些方法对90°和270°的区分提升有限，表明模型的设计仍需改进。

## 📊 实验亮点

实验结果表明，大多数模型能够可靠识别0°图像，而某些模型在180°图像识别上表现良好，但在90°和270°的区分上几乎没有提升。通过同时展示不同方向的图像，推理模型的表现有所改善，而投票机制则提升了较弱模型的性能。

## 🎯 应用场景

该研究的潜在应用领域包括计算机视觉、自动驾驶、机器人导航等需要图像理解和空间推理的场景。通过提升多模态大语言模型在图像旋转识别上的能力，可以增强其在实际应用中的可靠性和准确性，推动智能系统的发展。

## 📄 摘要（原文）

> We investigate to what extent Multimodal Large Language Models (MLLMs) can accurately identify the orientation of input images rotated 0°, 90°, 180°, and 270°. This task demands robust visual reasoning capabilities to detect rotational cues and contextualize spatial relationships within images, regardless of their orientation. To evaluate MLLMs on these abilities, we introduce RotBench -- a 350-image manually-filtered benchmark comprising lifestyle, portrait, and landscape images. Despite the relatively simple nature of this task, we show that several state-of-the-art open and proprietary MLLMs, including GPT-5, o3, and Gemini-2.5-Pro, do not reliably identify rotation in input images. Providing models with auxiliary information -- including captions, depth maps, and more -- or using chain-of-thought prompting offers only small and inconsistent improvements. Our results indicate that most models are able to reliably identify right-side-up (0°) images, while certain models are able to identify upside-down (180°) images. None can reliably distinguish between 90° and 270°. Simultaneously showing the image rotated in different orientations leads to moderate performance gains for reasoning models, while a modified setup using voting improves the performance of weaker models. We further show that fine-tuning does not improve models' ability to distinguish 90° and 270° rotations, despite substantially improving the identification of 180° images. Together, these results reveal a significant gap between MLLMs' spatial reasoning capabilities and human perception in identifying rotation.

