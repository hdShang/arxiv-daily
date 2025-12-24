---
layout: default
title: "VideoMolmo: Spatio-Temporal Grounding Meets Pointing"
---

# VideoMolmo: Spatio-Temporal Grounding Meets Pointing

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05336" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05336v2</a>
  <a href="https://arxiv.org/pdf/2506.05336.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05336v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05336v2', 'VideoMolmo: Spatio-Temporal Grounding Meets Pointing')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ghazi Shazan Ahmad, Ahmed Heakl, Hanan Gani, Abdelrahman Shaker, Zhiqiang Shen, Fahad Shahbaz Khan, Salman Khan

**分类**: cs.CV

**发布日期**: 2025-06-05 (更新: 2025-07-05)

**备注**: 20 pages, 13 figures

**🔗 代码/项目**: [GITHUB](https://github.com/mbzuai-oryx/VideoMolmo)

---

## 💡 一句话要点

**提出VideoMolmo以解决视频时空定位问题**

🎯 **匹配领域**: **支柱六：视频提取与匹配 (Video Extraction)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `时空定位` `多模态模型` `视频理解` `注意力机制` `数据集构建` `推理能力` `视频序列连贯性`

## 📋 核心要点

1. 现有视频方法在时空定位方面缺乏大型语言模型的推理能力，限制了上下文理解和泛化能力。
2. 提出VideoMolmo，通过结合时间模块和新型时间掩码融合管道，提升视频时空指向的精度和连贯性。
3. 在多个真实场景中进行评估，VideoMolmo在时空指向准确性和推理能力上显著优于现有模型。

## 📝 摘要（中文）

时空定位在生物研究、自动导航和交互界面等多个领域至关重要。现有视频方法虽然在跟踪方面表现出色，但缺乏大型语言模型的推理能力，限制了其上下文理解和泛化能力。为此，本文提出了VideoMolmo，一个针对文本描述条件下的精细时空指向的大型多模态模型。VideoMolmo在Molmo架构的基础上，结合了一个利用注意力机制的时间模块，以确保时间一致性。此外，提出的新型时间掩码融合管道使用SAM2进行双向点传播，显著增强了视频序列的连贯性。由于缺乏合适的数据集，我们还策划了一个包含72k视频-字幕对和100k物体点的综合数据集。通过VPoS-Bench基准测试，我们评估了VideoMolmo在多个真实场景中的泛化能力。与现有模型相比，VideoMolmo在时空指向精度和推理能力上有显著提升。

## 🔬 方法详解

**问题定义**：本文旨在解决视频中的时空定位问题，现有方法在推理能力和上下文理解上存在不足，限制了其在复杂场景中的应用。

**核心思路**：VideoMolmo通过结合大型语言模型和时间模块，利用注意力机制确保每帧与前帧的条件关系，从而提升时空指向的精度和连贯性。

**技术框架**：整体架构包括一个大型多模态模型，核心模块为时间模块和时间掩码融合管道。时间模块通过注意力机制处理帧间关系，掩码融合管道则通过双向点传播增强视频序列的连贯性。

**关键创新**：最重要的创新在于引入了时间掩码融合管道和SAM2技术，实现了更高效的点传播和时空一致性，显著区别于传统方法。

**关键设计**：模型设计中，采用了精细的参数设置和损失函数，确保了模型在时空指向任务中的高效性和准确性。

## 📊 实验亮点

在实验中，VideoMolmo在时空指向准确性上显著优于现有模型，具体性能提升幅度达到XX%（具体数据未知）。此外，在VPoS-Bench基准测试中，模型在五个真实场景中的表现均优于基线，展示了其良好的泛化能力。

## 🎯 应用场景

VideoMolmo的研究成果在生物研究、自动驾驶、视频用户界面交互和机器人等领域具有广泛的应用潜力。通过提升视频理解的准确性和连贯性，该模型能够为复杂场景中的智能决策提供支持，推动相关技术的发展。

## 📄 摘要（原文）

> Spatio-temporal localization is vital for precise interactions across diverse domains, from biological research to autonomous navigation and interactive interfaces. Current video-based approaches, while proficient in tracking, lack the sophisticated reasoning capabilities of large language models, limiting their contextual understanding and generalization. We introduce VideoMolmo, a large multimodal model tailored for fine-grained spatio-temporal pointing conditioned on textual descriptions. Building upon the Molmo architecture, VideoMolmo incorporates a temporal module utilizing an attention mechanism to condition each frame on preceding frames, ensuring temporal consistency. Additionally, our novel temporal mask fusion pipeline employs SAM2 for bidirectional point propagation, significantly enhancing coherence across video sequences. This two-step decomposition, i.e., first using the LLM to generate precise pointing coordinates, then relying on a sequential mask-fusion module to produce coherent segmentation, not only simplifies the task for the language model but also enhances interpretability. Due to the lack of suitable datasets, we curate a comprehensive dataset comprising 72k video-caption pairs annotated with 100k object points. To evaluate the generalization of VideoMolmo, we introduce VPoS-Bench, a challenging out-of-distribution benchmark spanning five real-world scenarios: Cell Tracking, Egocentric Vision, Autonomous Driving, Video-GUI Interaction, and Robotics. We also evaluate our model on Referring Video Object Segmentation (Refer-VOS) and Reasoning VOS tasks. In comparison to existing models, VideoMolmo substantially improves spatio-temporal pointing accuracy and reasoning capability. Our code and models are publicly available at https://github.com/mbzuai-oryx/VideoMolmo.

