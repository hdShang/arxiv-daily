---
layout: default
title: "Chain-of-Frames: Advancing Video Understanding in Multimodal LLMs via Frame-Aware Reasoning"
---

# Chain-of-Frames: Advancing Video Understanding in Multimodal LLMs via Frame-Aware Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.00318" class="toolbar-btn" target="_blank">📄 arXiv: 2506.00318v1</a>
  <a href="https://arxiv.org/pdf/2506.00318.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.00318v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.00318v1', 'Chain-of-Frames: Advancing Video Understanding in Multimodal LLMs via Frame-Aware Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sara Ghazanfari, Francesco Croce, Nicolas Flammarion, Prashanth Krishnamurthy, Farshad Khorrami, Siddharth Garg

**分类**: cs.CV

**发布日期**: 2025-05-31

**🔗 代码/项目**: [GITHUB](https://github.com/SaraGhazanfari/CoF)

---

## 💡 一句话要点

**提出基于帧感知推理的视频理解方法以提升多模态LLMs性能**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视频理解` `多模态LLMs` `推理链` `帧感知` `数据集构建` `模型微调` `性能提升`

## 📋 核心要点

1. 现有视频理解方法在推理过程中缺乏对具体视频帧的明确引用，导致性能不足。
2. 本文提出通过创建CoF-Data数据集，训练视频LLMs生成基于帧的推理链，以提升理解能力。
3. 实验结果表明，基于CoF的方法在Video-MME、MVBench和VSI-Bench等基准上超越了现有领先模型，且幻觉率显著降低。

## 📝 摘要（中文）

近期研究表明，在回答用户请求之前，促使大型语言模型（LLMs）生成自然语言推理轨迹可以显著提升其在各项任务中的表现。本文扩展了这一方法至多模态LLMs，使模型能够针对输入图像和视频内容生成思维链（CoT）。我们提出了一种新的视频LLMs，其推理步骤基于相关视频帧，并明确引用这些帧。为此，我们首先创建了CoF-Data，一个包含多样化问题、答案及相应帧基础推理轨迹的大型数据集，涵盖自然和合成视频的多种主题和任务。随后，我们在此链帧数据上微调现有视频LLMs。我们的简单自包含的方法不需要辅助网络来选择或标注相关帧，结果显示基于CoF的方法能够准确引用关键帧生成思维链，从而在多个视频理解基准上提升性能，显著降低幻觉率。

## 🔬 方法详解

**问题定义**：本文旨在解决现有视频理解方法中推理步骤未能明确引用视频帧的问题，导致模型在理解和回答时的准确性不足。

**核心思路**：通过创建一个包含多样化问题和帧基础推理轨迹的数据集（CoF-Data），并在此数据集上微调视频LLMs，使其能够生成与视频帧相关的思维链，从而提升理解能力。

**技术框架**：整体架构包括数据集构建、模型微调和推理生成三个主要阶段。首先，构建CoF-Data数据集；其次，利用该数据集对现有视频LLMs进行微调；最后，生成基于帧的推理链。

**关键创新**：最重要的技术创新在于不依赖于辅助网络来选择或标注相关帧，而是直接在推理过程中引用关键帧，从而简化了模型的结构和训练过程。

**关键设计**：在模型微调过程中，采用了特定的损失函数以优化推理链的准确性，并确保生成的推理链能够有效地与视频帧对应。

## 📊 实验亮点

实验结果显示，基于CoF的数据集训练后，模型在Video-MME、MVBench和VSI-Bench等多个视频理解基准上超越了现有领先的视频LLMs，性能提升幅度显著，且幻觉率降低，表明该方法的有效性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括视频内容分析、智能监控、自动驾驶等。通过提升视频理解能力，能够在多模态交互、信息检索和人机协作等场景中发挥重要作用，推动相关技术的实际应用和发展。

## 📄 摘要（原文）

> Recent work has shown that eliciting Large Language Models (LLMs) to generate reasoning traces in natural language before answering the user's request can significantly improve their performance across tasks. This approach has been extended to multimodal LLMs, where the models can produce chain-of-thoughts (CoT) about the content of input images and videos. In this work, we propose to obtain video LLMs whose reasoning steps are grounded in, and explicitly refer to, the relevant video frames. For this, we first create CoF-Data, a large dataset of diverse questions, answers, and corresponding frame-grounded reasoning traces about both natural and synthetic videos, spanning various topics and tasks. Then, we fine-tune existing video LLMs on this chain-of-frames (CoF) data. Our approach is simple and self-contained, and, unlike existing approaches for video CoT, does not require auxiliary networks to select or caption relevant frames. We show that our models based on CoF are able to generate chain-of-thoughts that accurately refer to the key frames to answer the given question. This, in turn, leads to improved performance across multiple video understanding benchmarks, for example, surpassing leading video LLMs on Video-MME, MVBench, and VSI-Bench, and notably reducing the hallucination rate. Code available at https://github.com/SaraGhazanfari/CoF}{github.com/SaraGhazanfari/CoF.

