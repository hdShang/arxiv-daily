---
layout: default
title: Seeing is Not Reasoning: MVPBench for Graph-based Evaluation of Multi-path Visual Physical CoT
---

# Seeing is Not Reasoning: MVPBench for Graph-based Evaluation of Multi-path Visual Physical CoT

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24182" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24182v1</a>
  <a href="https://arxiv.org/pdf/2505.24182.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24182v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24182v1', 'Seeing is Not Reasoning: MVPBench for Graph-based Evaluation of Multi-path Visual Physical CoT')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhuobai Dong, Junchao Yi, Ziyuan Zheng, Haochen Han, Xiangxi Zheng, Alex Jinpeng Wang, Fangming Liu, Linjie Li

**分类**: cs.CV, cs.AI

**发布日期**: 2025-05-30

---

## 💡 一句话要点

**提出MVPBench以解决多模态大语言模型的视觉物理推理问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉推理` `多模态大语言模型` `物理推理` `图基评估` `推理链`

## 📋 核心要点

1. 现有多模态大语言模型在视觉物理推理方面存在显著不足，无法有效理解物理法则和空间关系。
2. 本文提出MVPBench基准，通过视觉推理链评估模型的视觉物理推理能力，强调连贯的逐步推理过程。
3. 实验结果表明，当前最先进的模型在视觉推理准确性上表现不佳，且后训练对齐方法可能会损害空间推理能力。

## 📝 摘要（中文）

理解物理世界的规律，如运动法则、空间关系和因果关系，对多模态大语言模型（MLLMs）构成了基本挑战。尽管OpenAI的o3和GPT-4o在感知和推理能力上取得了显著进展，但研究表明这些模型在视觉物理推理方面存在严重不足，无法掌握基本的物理法则和复杂场景中的空间交互。为此，本文提出了MVPBench，一个旨在通过视觉推理链（CoT）严格评估视觉物理推理能力的基准，要求模型不仅提供正确答案，还需展示基于视觉线索的连贯推理路径。实验结果显示，即使是最先进的MLLMs在物理领域的视觉推理准确性和图像-文本对齐度也表现不佳。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态大语言模型在视觉物理推理中的不足，尤其是在复杂场景中对物理法则和空间关系的理解。现有方法往往依赖文本先验，导致模型在视觉理解上表现不佳。

**核心思路**：提出MVPBench基准，强调通过视觉推理链进行评估，要求模型不仅给出正确答案，还需提供基于视觉线索的连贯推理路径。这种设计模拟了人类在现实物理过程中的推理方式。

**技术框架**：MVPBench包含多个模块，首先是多图像输入的示例，其次是要求模型提供最终答案和推理路径，最后通过图基CoT一致性度量评估推理的有效性。

**关键创新**：引入图基CoT一致性度量，验证模型推理路径是否符合有效的物理逻辑。这一创新与现有方法的主要区别在于强调视觉理解而非文本先验。

**关键设计**：在设计中，特别关注减少文本先验的影响，鼓励模型依赖视觉信息进行推理。同时，实验中使用了多样化的示例，以确保评估的细致性和全面性。

## 📊 实验亮点

实验结果显示，即使是最先进的多模态大语言模型在视觉物理推理的准确性上仍然较低，且图像与文本的对齐度不足。值得注意的是，基于强化学习的后训练对齐方法在空间推理上反而表现不佳，提示我们需要重新审视当前的微调实践。

## 🎯 应用场景

该研究的潜在应用领域包括机器人视觉、自动驾驶、智能监控等，能够帮助模型更好地理解和推理物理世界中的复杂场景。未来，MVPBench可能成为评估视觉推理能力的标准工具，推动多模态大语言模型的进一步发展。

## 📄 摘要（原文）

> Understanding the physical world - governed by laws of motion, spatial relations, and causality - poses a fundamental challenge for multimodal large language models (MLLMs). While recent advances such as OpenAI o3 and GPT-4o demonstrate impressive perceptual and reasoning capabilities, our investigation reveals these models struggle profoundly with visual physical reasoning, failing to grasp basic physical laws, spatial interactions, and causal effects in complex scenes. More importantly, they often fail to follow coherent reasoning chains grounded in visual evidence, especially when multiple steps are needed to arrive at the correct answer. To rigorously evaluate this capability, we introduce MVPBench, a curated benchmark designed to rigorously evaluate visual physical reasoning through the lens of visual chain-of-thought (CoT). Each example features interleaved multi-image inputs and demands not only the correct final answer but also a coherent, step-by-step reasoning path grounded in evolving visual cues. This setup mirrors how humans reason through real-world physical processes over time. To ensure fine-grained evaluation, we introduce a graph-based CoT consistency metric that verifies whether the reasoning path of model adheres to valid physical logic. Additionally, we minimize shortcut exploitation from text priors, encouraging models to rely on visual understanding. Experimental results reveal a concerning trend: even cutting-edge MLLMs exhibit poor visual reasoning accuracy and weak image-text alignment in physical domains. Surprisingly, RL-based post-training alignment - commonly believed to improve visual reasoning performance - often harms spatial reasoning, suggesting a need to rethink current fine-tuning practices.

