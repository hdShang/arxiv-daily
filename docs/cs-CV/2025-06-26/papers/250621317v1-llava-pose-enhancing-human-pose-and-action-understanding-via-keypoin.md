---
layout: default
title: "LLaVA-Pose: Enhancing Human Pose and Action Understanding via Keypoint-Integrated Instruction Tuning"
---

# LLaVA-Pose: Enhancing Human Pose and Action Understanding via Keypoint-Integrated Instruction Tuning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21317" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21317v1</a>
  <a href="https://arxiv.org/pdf/2506.21317.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21317v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21317v1', 'LLaVA-Pose: Enhancing Human Pose and Action Understanding via Keypoint-Integrated Instruction Tuning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dewen Zhang, Tahir Hussain, Wangpeng An, Hayaru Shouno

**分类**: cs.CV

**发布日期**: 2025-06-26

**备注**: arXiv admin note: substantial text overlap with arXiv:2409.09306

**🔗 代码/项目**: [GITHUB](https://github.com/Ody-trek/LLaVA-Pose)

---

## 💡 一句话要点

**提出LLaVA-Pose以解决人类姿态与动作理解问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `人类姿态理解` `动作识别` `视觉语言模型` `多模态学习` `数据集构建`

## 📋 核心要点

1. 现有视觉语言模型在处理人类姿态和动作理解时表现不佳，缺乏专门的指令跟随数据。
2. 本文提出了一种将人体关键点与传统视觉特征结合的方法，以生成更精准的视觉理解数据。
3. 实验结果表明，微调后的LLaVA-Pose模型在E-HPAUB基准上性能提升了33.2%，验证了关键点集成数据的有效性。

## 📝 摘要（中文）

当前的视觉语言模型（VLMs）在一般视觉理解任务中表现良好，但在处理与人类姿态和动作相关的复杂视觉任务时表现不佳，原因在于缺乏专门的视觉语言指令跟随数据。本文提出了一种通过将人体关键点与传统视觉特征（如标题和边界框）相结合的方法，生成此类数据，从而更精确地理解以人为中心的场景。我们构建了一个包含200,328个样本的数据集，旨在微调模型以应对人类中心任务，重点关注对话、详细描述和复杂推理。通过在扩展人类姿态与动作理解基准（E-HPAUB）上评估模型性能，我们对LLaVA-1.5-7B模型进行了微调，结果显示显著提升，整体性能提高了33.2%。

## 🔬 方法详解

**问题定义**：本文旨在解决现有视觉语言模型在复杂人类姿态和动作理解任务中的不足，主要痛点在于缺乏专门的指令跟随数据，导致模型性能不佳。

**核心思路**：通过将人体关键点与传统视觉特征（如标题和边界框）相结合，生成专门的数据集，以提高模型对人类中心场景的理解能力。这样的设计使得模型能够更好地捕捉与人类姿态和动作相关的细节。

**技术框架**：整体架构包括数据集构建、模型微调和性能评估三个主要模块。首先，构建包含200,328个样本的数据集；其次，使用该数据集对LLaVA-1.5-7B模型进行微调；最后，通过扩展人类姿态与动作理解基准（E-HPAUB）评估模型性能。

**关键创新**：最重要的技术创新在于关键点集成数据的生成方法，这与现有方法的本质区别在于通过关键点信息增强了模型对人类姿态和动作的理解能力。

**关键设计**：在数据集构建过程中，结合了多种视觉特征，并设计了适当的损失函数以优化模型性能，确保模型能够有效学习人类姿态和动作的复杂关系。具体的网络结构和参数设置在实验中经过多次调优，以达到最佳效果。

## 📊 实验亮点

实验结果显示，微调后的LLaVA-Pose模型在E-HPAUB基准上实现了33.2%的性能提升，相较于原始的LLaVA-1.5-7B模型，验证了关键点集成数据在多模态模型中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括智能监控、虚拟现实、增强现实和人机交互等。通过提升人类姿态和动作理解能力，LLaVA-Pose能够在这些领域中实现更自然的交互和更智能的分析，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Current vision-language models (VLMs) are well-adapted for general visual understanding tasks. However, they perform inadequately when handling complex visual tasks related to human poses and actions due to the lack of specialized vision-language instruction-following data. We introduce a method for generating such data by integrating human keypoints with traditional visual features such as captions and bounding boxes, enabling more precise understanding of human-centric scenes. Our approach constructs a dataset comprising 200,328 samples tailored to fine-tune models for human-centric tasks, focusing on three areas: conversation, detailed description, and complex reasoning. We establish an Extended Human Pose and Action Understanding Benchmark (E-HPAUB) to assess model performance on human pose and action understanding. We fine-tune the LLaVA-1.5-7B model using this dataset and evaluate our resulting LLaVA-Pose model on the benchmark, achieving significant improvements. Experimental results show an overall improvement of 33.2% compared to the original LLaVA-1.5-7B model. These findings highlight the effectiveness of keypoint-integrated data in enhancing multimodal models for human-centric visual understanding. Code is available at https://github.com/Ody-trek/LLaVA-Pose.

