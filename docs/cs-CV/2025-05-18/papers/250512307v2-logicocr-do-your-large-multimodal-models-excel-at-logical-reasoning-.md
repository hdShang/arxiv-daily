---
layout: default
title: LogicOCR: Do Your Large Multimodal Models Excel at Logical Reasoning on Text-Rich Images?
---

# LogicOCR: Do Your Large Multimodal Models Excel at Logical Reasoning on Text-Rich Images?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.12307" class="toolbar-btn" target="_blank">📄 arXiv: 2505.12307v2</a>
  <a href="https://arxiv.org/pdf/2505.12307.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.12307v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.12307v2', 'LogicOCR: Do Your Large Multimodal Models Excel at Logical Reasoning on Text-Rich Images?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Maoyuan Ye, Haibin He, Qihuang Zhong, Jing Zhang, Juhua Liu, Bo Du

**分类**: cs.CV, cs.CL

**发布日期**: 2025-05-18 (更新: 2025-11-26)

**备注**: GitHub: https://github.com/MiliLab/LogicOCR

**🔗 代码/项目**: [GITHUB](https://github.com/MiliLab/LogicOCR)

---

## 💡 一句话要点

**提出LogicOCR以解决多模态模型在文本丰富图像上的逻辑推理问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态模型` `逻辑推理` `光学字符识别` `文本丰富图像` `基准测试` `生成图像` `注意力机制` `文本线索`

## 📋 核心要点

1. 现有大型多模态模型在处理文本丰富图像时的逻辑推理能力不足，尚未充分探索其潜力。
2. 论文提出LogicOCR基准，通过生成和真实图像的多样化问题，评估LMMs在逻辑推理上的表现。
3. 实验结果显示，LMMs在多模态推理上仍落后于文本输入，提出的TextCue方法有效提升了模型的推理准确率。

## 📝 摘要（中文）

近年来，大型多模态模型（LMMs）的发展极大地提升了其推理和光学字符识别（OCR）能力。然而，它们在文本丰富图像上的复杂逻辑推理表现仍未得到充分探索。为此，我们提出了LogicOCR基准，包含2780个问题，分为LogicOCR-Gen和LogicOCR-Real两个子集。我们首先从中国国家公务员考试中整理文本语料，并定制自动化流程引导GPT-Image-1生成具有多样布局和字体的图像，确保上下文相关性和视觉真实感。然后，生成的图像经过人工验证。我们在Chain-of-Thought（CoT）和直接回答设置下评估了一系列代表性的LMMs，分析结果揭示了测试时间缩放、输入模态差异和视觉-文本方向敏感性等关键见解。值得注意的是，LMMs在多模态推理方面仍落后于文本输入，表明它们尚未完全实现视觉阅读与推理的结合。此外，我们提出了TextCue，一种无训练的方法，增强LMMs对解决问题时重要文本线索的感知。实验表明，该方法在CoT设置下相较于LLaVA-OV-1.5-8B提升了1.8%的准确率。我们的基准可在https://github.com/MiliLab/LogicOCR获取。

## 🔬 方法详解

**问题定义**：本论文旨在解决大型多模态模型在文本丰富图像上的逻辑推理能力不足的问题。现有方法在处理复杂视觉-文本信息时表现不佳，未能充分发挥其潜力。

**核心思路**：论文提出LogicOCR基准，包含多样化的生成和真实图像问题，以全面评估LMMs的逻辑推理能力。同时，提出TextCue方法，增强模型对重要文本线索的感知。

**技术框架**：整体架构包括两个主要部分：LogicOCR-Gen和LogicOCR-Real。前者通过自动化流程生成多样化图像，后者则基于真实图像设计自由形式问题。评估阶段使用Chain-of-Thought和直接回答两种设置。

**关键创新**：最重要的创新是提出了TextCue方法，通过利用LMMs的注意力图和文本分割技术，增强模型对重要文本区域的关注。这一方法在逻辑推理任务中显著提升了模型的表现。

**关键设计**：在生成图像时，采用了多样的布局和字体，确保生成内容的上下文相关性。TextCue方法中，关键设计包括对注意力图的分析和文本区域的裁剪与放大，以增强视觉信息的有效性。

## 📊 实验亮点

实验结果显示，LogicOCR基准下，LMMs在多模态推理任务中表现不佳，尤其是在与文本输入的对比中。通过引入TextCue方法，模型在CoT设置下实现了1.8%的准确率提升，相较于基线LLaVA-OV-1.5-8B，展现了显著的改进。

## 🎯 应用场景

该研究的潜在应用领域包括教育、文档分析和智能问答系统等。通过提升多模态模型在复杂视觉-文本任务中的推理能力，能够为实际应用提供更准确的结果，推动相关技术的发展与应用。

## 📄 摘要（原文）

> Recent advances in Large Multimodal Models (LMMs) have revolutionized their reasoning and Optical Character Recognition (OCR) capabilities. However, their complex logical reasoning performance on text-rich images remains underexplored. To bridge this gap, we introduce LogicOCR, a benchmark comprising 2780 questions with two subsets, i.e., LogicOCR-Gen with 1100 multi-choice questions on generated images, and LogicOCR-Real with 1680 meticulously designed free-form questions on real-world images. For constructing LogicOCR-Gen, we first curate a text corpus from the Chinese National Civil Servant Examination, and customize an automatic pipeline to steer GPT-Image-1 to generate images with varied layouts and fonts, ensuring contextual relevance and visual realism. Then, the generated images are manually verified. We evaluate a range of representative LMMs under Chain-of-Thought (CoT) and direct-answer settings. Our multi-dimensional analysis reveals key insights, such as the impact of test-time scaling, input modality differences, and sensitivity to visual-text orientation. Notably, LMMs still lag in multimodal reasoning compared to text-only inputs, indicating that they have not fully bridged visual reading with reasoning. Moreover, we propose TextCue, a training-free method that enhances LMMs' perception of image regions containing important text cues for solving questions. We leverage LMMs' attention maps and an off-the-shelf text segmentation specialist to determine the region, which is then cropped and enlarged to augment the original image. Experiments show its effectiveness, e.g., a 1.8% accuracy gain over LLaVA-OV-1.5-8B under the CoT setting. Our benchmark is available at https://github.com/MiliLab/LogicOCR.

