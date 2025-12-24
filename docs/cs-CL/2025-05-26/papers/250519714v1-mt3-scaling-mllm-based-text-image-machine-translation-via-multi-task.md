---
layout: default
title: "MT$^{3}$: Scaling MLLM-based Text Image Machine Translation via Multi-Task Reinforcement Learning"
---

# MT$^{3}$: Scaling MLLM-based Text Image Machine Translation via Multi-Task Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.19714" class="toolbar-btn" target="_blank">📄 arXiv: 2505.19714v1</a>
  <a href="https://arxiv.org/pdf/2505.19714.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.19714v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.19714v1', 'MT$^{3}$: Scaling MLLM-based Text Image Machine Translation via Multi-Task Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhaopeng Feng, Yupu Liang, Shaosheng Cao, Jiayuan Su, Jiahan Ren, Zhe Xu, Yao Hu, Wenxuan Huang, Jian Wu, Zuozhu Liu

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-05-26

**备注**: Work in progress

---

## 💡 一句话要点

**提出MT³框架以解决文本图像机器翻译中的多任务挑战**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `文本图像翻译` `多任务学习` `强化学习` `多模态大语言模型` `社交媒体翻译` `光学字符识别` `上下文推理`

## 📋 核心要点

1. TIMT面临的核心问题是现有方法在光学字符识别和视觉-文本推理方面的不足，导致翻译质量不高。
2. 本文提出的MT³框架通过多任务强化学习，针对文本识别、上下文推理和翻译进行优化，提升了TIMT的整体性能。
3. 实验结果显示，MT³-7B-Zero在MIT-10M基准上超越了Qwen2.5-VL-72B和InternVL2.5-78B等强基线，表现出色。

## 📝 摘要（中文）

文本图像机器翻译（TIMT）是将图像中嵌入的文本内容进行翻译的任务，对于无障碍访问、跨语言信息获取和实际文档理解至关重要。然而，由于需要准确的光学字符识别（OCR）、稳健的视觉-文本推理和高质量翻译，TIMT仍然面临复杂挑战。为了解决这一问题，本文提出了MT³框架，首次将多任务强化学习应用于多模态大语言模型（MLLMs）以实现端到端的TIMT。MT³采用多任务优化范式，针对文本识别、上下文感知推理和翻译三个关键子技能进行训练，使用新颖的多混合奖励机制，提供细粒度的非二元反馈。此外，本文还引入了XHSPost社交媒体TIMT基准，以便在真实的跨文化社交媒体环境中评估TIMT。MT³-7B-Zero在最新的MIT-10M基准上取得了领先结果，超越了多个强基线模型。

## 🔬 方法详解

**问题定义**：本文旨在解决文本图像机器翻译（TIMT）中的多任务挑战，现有方法在处理光学字符识别、视觉-文本推理和翻译时常常需要复杂的多阶段管道，导致效率低下和翻译质量不佳。

**核心思路**：MT³框架通过引入多任务强化学习，针对TIMT的三个关键子任务进行联合优化，旨在提升模型的整体性能和适应性。该设计使得模型能够在不同任务间共享知识，从而提高翻译的准确性和流畅性。

**技术框架**：MT³的整体架构包括三个主要模块：文本识别模块、上下文感知推理模块和翻译模块。通过多任务学习，这些模块能够协同工作，优化最终的翻译结果。模型使用新颖的多混合奖励机制进行训练，以适应TIMT的复杂性。

**关键创新**：MT³的主要创新在于将多任务强化学习应用于TIMT，首次实现了端到端的翻译过程。与传统方法相比，该框架能够提供细粒度的反馈，促进模型在多个任务上的协同学习。

**关键设计**：模型采用了适应性奖励机制，结合规则基础的强化学习策略，确保在训练过程中能够有效地处理不同任务的复杂性。损失函数设计上，考虑了各个子任务的特性，确保模型在训练时能够平衡各项任务的优化。

## 📊 实验亮点

MT³-7B-Zero在MIT-10M基准上取得了领先的实验结果，超越了Qwen2.5-VL-72B和InternVL2.5-78B等强基线，提升幅度显著，展示了其在多任务学习和强化学习方面的优势。

## 🎯 应用场景

该研究的潜在应用领域包括社交媒体内容翻译、跨文化信息获取和无障碍技术等。通过提升文本图像机器翻译的准确性和效率，MT³框架能够在多种实际场景中提供更好的用户体验，促进信息的无障碍传播和理解。

## 📄 摘要（原文）

> Text Image Machine Translation (TIMT)-the task of translating textual content embedded in images-is critical for applications in accessibility, cross-lingual information access, and real-world document understanding. However, TIMT remains a complex challenge due to the need for accurate optical character recognition (OCR), robust visual-text reasoning, and high-quality translation, often requiring cascading multi-stage pipelines. Recent advances in large-scale Reinforcement Learning (RL) have improved reasoning in Large Language Models (LLMs) and Multimodal LLMs (MLLMs), but their application to end-to-end TIMT is still underexplored. To bridge this gap, we introduce MT$^{3}$, the first framework to apply Multi-Task RL to MLLMs for end-to-end TIMT. MT$^{3}$ adopts a multi-task optimization paradigm targeting three key sub-skills: text recognition, context-aware reasoning, and translation. It is trained using a novel multi-mixed reward mechanism that adapts rule-based RL strategies to TIMT's intricacies, offering fine-grained, non-binary feedback across tasks. Furthermore, to facilitate the evaluation of TIMT in authentic cross-cultural and real-world social media contexts, we introduced XHSPost, the first social media TIMT benchmark. Our MT$^{3}$-7B-Zero achieves state-of-the-art results on the latest in-domain MIT-10M benchmark, outperforming strong baselines such as Qwen2.5-VL-72B and InternVL2.5-78B by notable margins across multiple metrics. Additionally, the model shows strong generalization to out-of-distribution language pairs and datasets. In-depth analyses reveal how multi-task synergy, reinforcement learning initialization, curriculum design, and reward formulation contribute to advancing MLLM-driven TIMT.

