---
layout: default
title: "MT-Video-Bench: A Holistic Video Understanding Benchmark for Evaluating Multimodal LLMs in Multi-Turn Dialogues"
---

# MT-Video-Bench: A Holistic Video Understanding Benchmark for Evaluating Multimodal LLMs in Multi-Turn Dialogues

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.17722" class="toolbar-btn" target="_blank">📄 arXiv: 2510.17722v1</a>
  <a href="https://arxiv.org/pdf/2510.17722.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.17722v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.17722v1', 'MT-Video-Bench: A Holistic Video Understanding Benchmark for Evaluating Multimodal LLMs in Multi-Turn Dialogues')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yaning Pan, Zekun Wang, Qianqian Xie, Yongqian Wen, Yuanxing Zhang, Guohui Zhang, Haoxuan Hu, Zhiyu Pan, Yibing Huang, Zhidong Gan, Yonghong Lin, An Ping, Tianhao Peng, Jiaheng Liu

**分类**: cs.CV, cs.AI

**发布日期**: 2025-10-20

**备注**: Project Website: https://github.com/NJU-LINK/MT-Video-Bench

---

## 💡 一句话要点

**提出MT-Video-Bench，用于评估多模态LLM在多轮对话中的视频理解能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `视频理解` `多轮对话` `大型语言模型` `评估基准`

## 📋 核心要点

1. 现有视频理解评估基准主要集中于单轮问答，缺乏对多轮交互场景的有效评估。
2. MT-Video-Bench通过构建包含987个多轮对话的基准，全面评估MLLM的感知和交互能力。
3. 实验结果揭示了现有MLLM在处理多轮视频对话方面的性能差异和局限性，为未来研究提供参考。

## 📝 摘要（中文）

多模态大型语言模型（MLLM）的最新发展显著提升了AI理解视觉模态的能力。然而，现有的评估基准仍然局限于单轮问答，忽略了真实场景中多轮对话的复杂性。为了弥补这一差距，我们推出了MT-Video-Bench，这是一个全面的视频理解基准，用于评估MLLM在多轮对话中的表现。具体来说，MT-Video-Bench主要评估六项核心能力，侧重于感知和交互性，包含来自不同领域的987个精心策划的多轮对话。这些能力与实际应用严格对齐，例如交互式体育分析和基于视频的多轮智能辅导。通过MT-Video-Bench，我们广泛评估了各种最先进的开源和闭源MLLM，揭示了它们在处理多轮视频对话方面的显著性能差异和局限性。该基准将公开提供，以促进未来的研究。

## 🔬 方法详解

**问题定义**：现有MLLM的视频理解评估主要集中在单轮问答，无法有效评估模型在真实场景下的多轮交互能力。现有方法缺乏对模型感知能力和交互能力的全面评估，难以反映模型在复杂场景下的实际应用效果。

**核心思路**：MT-Video-Bench的核心思路是构建一个包含多轮对话的视频理解基准，通过模拟真实场景下的交互过程，全面评估MLLM的感知能力和交互能力。该基准侧重于评估模型在多轮对话中理解视频内容、进行推理和生成回复的能力。

**技术框架**：MT-Video-Bench包含987个精心策划的多轮对话，涵盖不同的领域和场景。每个对话都包含视频片段和一系列问题，问题设计旨在评估模型的六项核心能力：感知能力（例如目标检测、场景理解）、交互能力（例如问题回答、对话生成）。基准还提供评估指标，用于衡量模型在不同能力上的表现。

**关键创新**：MT-Video-Bench的关键创新在于其多轮对话的设计，能够更真实地反映模型在实际应用中的表现。与现有单轮问答基准相比，MT-Video-Bench能够更全面地评估模型的感知能力和交互能力。此外，该基准还涵盖了不同的领域和场景，具有更广泛的适用性。

**关键设计**：MT-Video-Bench的关键设计包括：1) 多样化的视频内容，涵盖不同的领域和场景；2) 精心设计的多轮对话，模拟真实场景下的交互过程；3) 明确定义的评估指标，用于衡量模型在不同能力上的表现；4) 六项核心能力，包括目标检测、场景理解、问题回答、对话生成等。

## 📊 实验亮点

通过在MT-Video-Bench上对多种开源和闭源MLLM进行评估，论文揭示了它们在处理多轮视频对话方面的显著性能差异和局限性。例如，一些模型在目标检测和场景理解方面表现良好，但在对话生成方面存在不足。实验结果表明，现有MLLM在处理复杂的多轮视频对话时仍面临挑战，需要进一步的研究和改进。

## 🎯 应用场景

MT-Video-Bench可应用于开发更智能的视频理解系统，例如智能客服、视频监控、智能教育等。通过评估和提升MLLM在多轮视频对话中的能力，可以实现更自然、更高效的人机交互。该基准的发布将促进多模态学习领域的研究，推动视频理解技术的进步，并为相关产业带来潜在的商业价值。

## 📄 摘要（原文）

> The recent development of Multimodal Large Language Models (MLLMs) has significantly advanced AI's ability to understand visual modalities. However, existing evaluation benchmarks remain limited to single-turn question answering, overlooking the complexity of multi-turn dialogues in real-world scenarios. To bridge this gap, we introduce MT-Video-Bench, a holistic video understanding benchmark for evaluating MLLMs in multi-turn dialogues. Specifically, our MT-Video-Bench mainly assesses six core competencies that focus on perceptivity and interactivity, encompassing 987 meticulously curated multi-turn dialogues from diverse domains. These capabilities are rigorously aligned with real-world applications, such as interactive sports analysis and multi-turn video-based intelligent tutoring. With MT-Video-Bench, we extensively evaluate various state-of-the-art open-source and closed-source MLLMs, revealing their significant performance discrepancies and limitations in handling multi-turn video dialogues. The benchmark will be publicly available to foster future research.

