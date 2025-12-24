---
layout: default
title: "CapGeo: A Caption-Assisted Approach to Geometric Reasoning"
---

# CapGeo: A Caption-Assisted Approach to Geometric Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.09302" class="toolbar-btn" target="_blank">📄 arXiv: 2510.09302v1</a>
  <a href="https://arxiv.org/pdf/2510.09302.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.09302v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.09302v1', 'CapGeo: A Caption-Assisted Approach to Geometric Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuying Li, Siyi Qian, Hao Liang, Leqi Zheng, Ruichuan An, Yongzhen Guo, Wentao Zhang

**分类**: cs.CV, cs.AI, cs.CL

**发布日期**: 2025-10-10

**备注**: preprint, under review

---

## 💡 一句话要点

**CapGeo：一种基于图文描述的几何推理方法**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `几何推理` `多模态学习` `图文描述` `大语言模型` `视觉理解`

## 📋 核心要点

1. 多模态大语言模型在几何推理方面存在瓶颈，即使是最先进的模型也难以可靠地解决几何问题。
2. CapGeo通过将几何图形转换为文本描述，辅助模型理解几何图，从而弥合视觉和文本模态之间的差距。
3. 实验表明，CapGeo显著提升了几何推理性能，Qwen2.5-VL-72B和Claude-Opus-4分别提升至59.0%和73.0%。

## 📝 摘要（中文）

几何推理是多模态大型语言模型（MLLMs）面临的核心挑战。即使是最先进的闭源系统，如GPT-O3和Gemini-2.5-Pro，尽管在国际数学奥林匹克（IMO）等任务上表现出强大的文本推理能力，但在解决几何问题时仍然存在困难。这种差距表明瓶颈在于理解几何图，而非推理本身。由于几何图形通常可以用简洁的文本形式忠实地描述，因此将视觉内容转换为图文描述提供了一个有希望的方向。受此启发，我们提出了CapGeo，一个基于图文描述辅助的推理框架，弥合了视觉和文本模态之间的差距。实验表明，当模型配备图文描述时，性能得到显著提升：Qwen2.5-VL-72B从8.6%（仅视觉）提高到59.0%，而Claude-Opus-4从44.8%提高到73.0%。为了系统地评估和识别高质量的几何图文描述模型，我们进一步提出了CapGeo-Bench，一个包含4,641个精心策划的图形-图文描述对的数据集。至关重要的是，CapGeo-Bench包含一个基于关键点的评估指标，该指标与下游CapGeo性能密切相关，从而能够可靠地评估几何图文描述能力。我们的框架和基准共同突出了推进MLLM中几何推理的新途径。

## 🔬 方法详解

**问题定义**：论文旨在解决多模态大语言模型（MLLMs）在几何推理任务中表现不佳的问题。现有方法直接依赖模型对几何图形的视觉理解，但由于几何图形的复杂性和模型的视觉理解能力限制，导致推理性能较差。现有方法的痛点在于无法有效利用几何图形中蕴含的丰富信息。

**核心思路**：论文的核心思路是将几何图形转换为文本描述（caption），利用文本模态的强大推理能力辅助视觉推理。通过将视觉信息转化为文本信息，降低了模型对视觉理解的难度，并可以更好地利用预训练语言模型的知识。

**技术框架**：CapGeo框架主要包含两个阶段：1) 几何图形图文描述生成阶段：使用图文描述模型将几何图形转换为文本描述。2) 图文描述辅助推理阶段：将生成的图文描述与问题文本一起输入到多模态大语言模型中进行推理，得到最终答案。CapGeo-Bench数据集用于训练和评估图文描述模型。

**关键创新**：论文的关键创新在于提出了图文描述辅助的几何推理框架CapGeo，以及构建了用于评估几何图文描述质量的CapGeo-Bench数据集。CapGeo-Bench数据集包含一个基于关键点的评估指标，该指标与下游几何推理性能高度相关，可以有效评估图文描述的质量。

**关键设计**：CapGeo-Bench数据集包含4,641个图形-图文描述对，涵盖了各种类型的几何图形和问题。基于关键点的评估指标通过比较生成图文描述中关键点与真实关键点之间的差异来评估图文描述的准确性。论文使用了Qwen2.5-VL-72B和Claude-Opus-4等模型进行实验，并对比了有无图文描述辅助的性能差异。具体的参数设置和网络结构细节在论文中未详细说明，可能需要参考相关模型的官方文档。

## 📊 实验亮点

实验结果表明，CapGeo框架能够显著提升多模态大语言模型在几何推理任务中的性能。例如，Qwen2.5-VL-72B模型在仅使用视觉信息时，准确率仅为8.6%，而在CapGeo框架的辅助下，准确率提升至59.0%。Claude-Opus-4模型也从44.8%提升至73.0%。这些结果表明，图文描述辅助是一种有效的几何推理方法。

## 🎯 应用场景

该研究成果可应用于教育领域，例如智能辅导系统，帮助学生更好地理解几何概念和解决几何问题。此外，该方法还可以应用于机器人视觉、自动驾驶等领域，提高机器对复杂几何环境的理解和推理能力，具有广阔的应用前景和实际价值。

## 📄 摘要（原文）

> Geometric reasoning remains a core challenge for Multimodal Large Language Models (MLLMs). Even the most advanced closed-source systems, such as GPT-O3 and Gemini-2.5-Pro, still struggle to solve geometry problems reliably, despite exhibiting strong textual reasoning abilities on tasks like the International Mathematical Olympiad (IMO). This gap suggests that the bottleneck lies in understanding geometric diagrams rather than reasoning itself. Since geometric figures can often be faithfully described in concise textual form, converting visual content into captions offers a promising direction. Motivated by this insight, we introduce CapGeo, a caption-assisted reasoning framework that bridges visual and textual modalities. Experiments show substantial improvements when models are equipped with captions: Qwen2.5-VL-72B improves from 8.6% (vision-only) to 59.0%, while Claude-Opus-4 rises from 44.8% to 73.0%. To systematically evaluate and identify high-quality geometric captioning models, we further propose CapGeo-Bench, a dataset of 4,641 curated figure-caption pairs. Crucially, CapGeo-Bench incorporates a keypoint-based evaluation metric that correlates strongly with downstream CapGeo performance, enabling reliable assessment of geometric captioning ability. Together, our framework and benchmark highlight a new pathway toward advancing geometric reasoning in MLLMs.

