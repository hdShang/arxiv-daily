---
layout: default
title: "DGM4+: Dataset Extension for Global Scene Inconsistency"
---

# DGM4+: Dataset Extension for Global Scene Inconsistency

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.26047" class="toolbar-btn" target="_blank">📄 arXiv: 2509.26047v1</a>
  <a href="https://arxiv.org/pdf/2509.26047.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.26047v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.26047v1', 'DGM4+: Dataset Extension for Global Scene Inconsistency')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Gagandeep Singh, Samudi Amarsinghe, Priyanka Singh, Xue Li

**分类**: cs.CV

**发布日期**: 2025-09-30

**备注**: 8 pages, 3 figures

**🔗 代码/项目**: [GITHUB](https://github.com/Gaganx0/DGM4plus)

---

## 💡 一句话要点

**DGM4+：扩展数据集以应对全局场景不一致性，提升多模态伪造检测能力。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态伪造检测` `全局场景不一致性` `数据集扩展` `前景背景不匹配` `文本操纵`

## 📋 核心要点

1. 现有多模态伪造检测数据集主要关注局部篡改，缺乏对全局场景不一致性的有效覆盖，限制了模型的泛化能力。
2. DGM4+数据集通过引入前景-背景不匹配和文本操纵的混合，模拟真实世界中常见的全局伪造场景，增强模型的鲁棒性。
3. 该数据集包含5000个高质量样本，并采用严格的质量控制流程，确保数据的真实性和可靠性，为多模态模型评估提供基准。

## 📝 摘要（中文）

生成模型的快速发展显著降低了制作具有说服力的多模态虚假信息的门槛。伪造图像和篡改的标题越来越多地共同出现，以创建具有说服力的虚假叙述。检测和定位多模态媒体操纵(DGM4)数据集为该领域的研究奠定了基础，但它仅限于局部操纵，如换脸、属性编辑和标题更改。这留下了一个关键的空白：全局不一致性，例如不匹配的前景和背景，这些在现实世界的伪造品中非常普遍。为了解决这个问题，我们使用5000个高质量的样本扩展了DGM4，这些样本引入了前景-背景(FG-BG)不匹配及其与文本操纵的混合。使用OpenAI的gpt-image-1和精心设计的提示，我们生成以人为中心的新闻风格图像，其中真实的人物被放置在荒谬或不可能的背景中(例如，一位老师平静地在火星表面向学生讲话)。标题在三种条件下生成：字面、文本属性和文本分割，从而产生三个新的操纵类别：FG-BG、FG-BG+TA和FG-BG+TS。质量控制管道强制执行一到三个可见的面孔、感知哈希去重、基于OCR的文本清理和真实的新闻标题长度。通过引入全局操纵，我们的扩展补充了现有的数据集，创建了一个基准DGM4+，用于测试检测器在局部和全局推理上的能力。该资源旨在加强对多模态模型(如HAMMER)的评估，这些模型目前难以处理FG-BG不一致性。我们发布了我们的DGM4+数据集和生成脚本。

## 🔬 方法详解

**问题定义**：现有数据集如DGM4主要关注局部图像篡改和文本修改，忽略了全局场景不一致性，例如将人物放置在不合理的背景中。这种全局不一致性在实际伪造信息中越来越常见，现有方法难以有效检测此类伪造。

**核心思路**：通过扩展DGM4数据集，引入包含前景-背景(FG-BG)不匹配的样本，并结合文本操纵，从而创建一个更具挑战性和现实性的多模态伪造检测基准。核心在于模拟真实世界中全局场景不一致性的伪造手法。

**技术框架**：DGM4+数据集的生成流程主要包括以下几个阶段：1) 使用OpenAI的gpt-image-1模型生成图像，通过精心设计的提示，将真实人物放置在荒谬或不可能的背景中。2) 生成三种类型的标题：字面、文本属性和文本分割，与图像进行组合。3) 进行严格的质量控制，包括人脸数量控制、感知哈希去重、OCR文本清理和标题长度控制。

**关键创新**：DGM4+的关键创新在于引入了全局场景不一致性作为一种新的伪造类型，弥补了现有数据集的不足。此外，结合文本操纵，创建了更复杂的多模态伪造场景，更贴近真实世界的伪造信息。

**关键设计**：在图像生成方面，使用OpenAI的gpt-image-1模型，并设计了详细的提示，以控制生成图像的内容和风格。在质量控制方面，采用了一系列策略，包括限制图像中人脸的数量（1-3个）、使用感知哈希进行重复数据删除、使用OCR技术清理文本错误以及限制标题长度，以确保数据集的质量和真实性。

## 📊 实验亮点

DGM4+数据集通过引入全局场景不一致性，显著提升了多模态伪造检测的难度。实验表明，现有模型如HAMMER在DGM4+数据集上的性能显著下降，表明该数据集能够有效评估模型对全局推理的能力。DGM4+为开发更强大的多模态伪造检测模型提供了新的基准。

## 🎯 应用场景

DGM4+数据集可用于训练和评估多模态伪造检测模型，提高模型对全局场景不一致性的识别能力。该数据集有助于开发更鲁棒和可靠的伪造检测系统，应用于社交媒体内容审核、新闻真实性验证等领域，从而减少虚假信息传播。

## 📄 摘要（原文）

> The rapid advances in generative models have significantly lowered the barrier to producing convincing multimodal disinformation. Fabricated images and manipulated captions increasingly co-occur to create persuasive false narratives. While the Detecting and Grounding Multi-Modal Media Manipulation (DGM4) dataset established a foundation for research in this area, it is restricted to local manipulations such as face swaps, attribute edits, and caption changes. This leaves a critical gap: global inconsistencies, such as mismatched foregrounds and backgrounds, which are now prevalent in real-world forgeries. To address this, we extend DGM4 with 5,000 high-quality samples that introduce Foreground-Background (FG-BG) mismatches and their hybrids with text manipulations. Using OpenAI's gpt-image-1 and carefully designed prompts, we generate human-centric news-style images where authentic figures are placed into absurd or impossible backdrops (e.g., a teacher calmly addressing students on the surface of Mars). Captions are produced under three conditions: literal, text attribute, and text split, yielding three new manipulation categories: FG-BG, FG-BG+TA, and FG-BG+TS. Quality control pipelines enforce one-to-three visible faces, perceptual hash deduplication, OCR-based text scrubbing, and realistic headline length. By introducing global manipulations, our extension complements existing datasets, creating a benchmark DGM4+ that tests detectors on both local and global reasoning. This resource is intended to strengthen evaluation of multimodal models such as HAMMER, which currently struggle with FG-BG inconsistencies. We release our DGM4+ dataset and generation script at https://github.com/Gaganx0/DGM4plus

