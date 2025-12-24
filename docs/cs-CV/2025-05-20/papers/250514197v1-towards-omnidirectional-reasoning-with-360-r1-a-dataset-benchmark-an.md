---
layout: default
title: "Towards Omnidirectional Reasoning with 360-R1: A Dataset, Benchmark, and GRPO-based Method"
---

# Towards Omnidirectional Reasoning with 360-R1: A Dataset, Benchmark, and GRPO-based Method

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14197" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14197v1</a>
  <a href="https://arxiv.org/pdf/2505.14197.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14197v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14197v1', 'Towards Omnidirectional Reasoning with 360-R1: A Dataset, Benchmark, and GRPO-based Method')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xinshen Zhang, Zhen Ye, Xu Zheng

**分类**: cs.CV

**发布日期**: 2025-05-20

---

## 💡 一句话要点

**提出OmniVQA数据集与360-R1方法以解决全景视觉问答问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `全景视觉问答` `多模态学习` `强化学习` `奖励函数设计` `数据集构建` `模型评估`

## 📋 核心要点

1. 现有多模态大型语言模型在全景视觉问答中存在对象定位和特征提取等方面的显著局限性。
2. 本文提出OmniVQA数据集和360-R1方法，通过引入新颖的奖励函数来改进全景问答能力。
3. 实验结果表明，360-R1方法在全景视觉问答任务上相较于现有方法提升了6%的性能。

## 📝 摘要（中文）

全景图像（ODIs）以其360°视野为增强现实和具身人工智能等沉浸式应用提供了无与伦比的空间感知能力。然而，现有的多模态大型语言模型（MLLMs）在理解和推理全景场景方面的能力仍未得到充分探索。本文通过引入OmniVQA数据集和基准，首次对全景视觉问答进行评估，揭示了现有MLLMs在对象定位、特征提取和幻觉抑制等方面的显著局限性。基于OmniVQA数据集，我们进一步提出了一种基于Qwen2.5-VL-Instruct的规则强化学习方法360-R1，设计了三种新颖的奖励函数，实验结果显示该方法在全景空间上有6%的提升。

## 🔬 方法详解

**问题定义**：本文旨在解决现有多模态大型语言模型在全景视觉问答中的不足，尤其是在对象定位、特征提取和幻觉抑制方面的挑战。

**核心思路**：论文提出了OmniVQA数据集和360-R1方法，通过引入基于规则的强化学习和新颖的奖励函数，旨在提升模型在全景图像中的推理能力。

**技术框架**：整体架构包括数据集构建、基准测试和360-R1方法的实现，主要模块包括奖励函数设计和模型训练。

**关键创新**：最重要的创新点在于提出了三种新颖的奖励函数，分别是推理过程相似性奖励、答案语义准确性奖励和结构格式合规奖励，这些设计旨在更好地适应全景视觉问答的需求。

**关键设计**：在360-R1方法中，奖励函数的设计是关键，确保模型能够在全景场景中进行有效的推理和回答，同时采用了Qwen2.5-VL-Instruct作为基础模型进行改进。

## 📊 实验亮点

实验结果显示，360-R1方法在全景视觉问答任务上相较于现有最先进的模型提升了6%的性能，充分验证了新颖奖励函数的有效性和必要性。

## 🎯 应用场景

该研究的潜在应用领域包括增强现实、虚拟现实和具身人工智能等，能够为这些领域提供更精准的视觉理解能力。通过提升全景视觉问答的性能，未来可在智能助手、教育和娱乐等多个场景中发挥重要作用。

## 📄 摘要（原文）

> Omnidirectional images (ODIs), with their 360° field of view, provide unparalleled spatial awareness for immersive applications like augmented reality and embodied AI. However, the capability of existing multi-modal large language models (MLLMs) to comprehend and reason about such panoramic scenes remains underexplored. This paper addresses this gap by introducing OmniVQA, the first dataset and conducting the first benchmark for omnidirectional visual question answering. Our evaluation of state-of-the-art MLLMs reveals significant limitations in handling omnidirectional visual question answering, highlighting persistent challenges in object localization, feature extraction, and hallucination suppression within panoramic contexts. These results underscore the disconnect between current MLLM capabilities and the demands of omnidirectional visual understanding, which calls for dedicated architectural or training innovations tailored to 360° imagery. Building on the OmniVQA dataset and benchmark, we further introduce a rule-based reinforcement learning method, 360-R1, based on Qwen2.5-VL-Instruct. Concretely, we modify the group relative policy optimization (GRPO) by proposing three novel reward functions: (1) reasoning process similarity reward, (2) answer semantic accuracy reward, and (3) structured format compliance reward. Extensive experiments on our OmniVQA demonstrate the superiority of our proposed method in omnidirectional space (+6% improvement).

