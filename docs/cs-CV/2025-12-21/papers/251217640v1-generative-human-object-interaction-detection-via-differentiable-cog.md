---
layout: default
title: Generative Human-Object Interaction Detection via Differentiable Cognitive Steering of Multi-modal LLMs
---

# Generative Human-Object Interaction Detection via Differentiable Cognitive Steering of Multi-modal LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.17640" class="toolbar-btn" target="_blank">📄 arXiv: 2512.17640v1</a>
  <a href="https://arxiv.org/pdf/2512.17640.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.17640v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.17640v1', 'Generative Human-Object Interaction Detection via Differentiable Cognitive Steering of Multi-modal LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhaolin Cai, Huiyu Duan, Zitong Xu, Fan Li, Zhi Liu, Jing Liu, Wei Shen, Xiongkuo Min, Guangtao Zhai

**分类**: cs.CV

**发布日期**: 2025-12-19

---

## 💡 一句话要点

**提出GRASP-HO框架，通过可微分认知引导多模态LLM实现生成式人-物交互检测。**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱五：交互与反应 (Interaction & Reaction)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `人-物交互检测` `多模态大语言模型` `生成式模型` `开放词汇` `认知引导` `零样本学习` `混合指导策略`

## 📋 核心要点

1. 现有HOI检测方法受限于预定义的动词集合，难以处理真实场景中复杂多变的交互。
2. GRASP-HO框架将HOI检测重构为开放词汇生成问题，利用MLLM的知识进行推理。
3. 通过可学习的认知引导模块和混合指导策略，GRASP-HO在封闭集和零样本场景下均表现出色。

## 📝 摘要（中文）

人-物交互(HOI)检测旨在定位人-物对以及它们之间的交互。现有方法通常基于封闭世界假设，将该任务视为对预定义动词集合的分类问题，难以泛化到真实场景中未见或模糊的长尾交互。虽然最近的多模态大型语言模型(MLLM)拥有开放词汇理解所需的丰富世界知识，但由于微调成本过高，它们与现有的HOI检测器脱节。为了解决这些限制，我们提出了GRASP-HO，一种新颖的生成式推理和可控感知框架，将HOI检测从封闭集分类任务重新定义为开放词汇生成问题。为了连接视觉和认知，我们首先提取混合交互表示，然后设计一个轻量级的可学习认知引导模块(CSC)，将细粒度的视觉证据注入到冻结的MLLM中以进行有效的推理。为了解决基于分类的HOI数据集和开放词汇生成模型之间的监督不匹配问题，我们引入了一种混合指导策略，将语言建模损失和辅助分类损失相结合，从而在不牺牲生成灵活性的情况下实现判别性 grounding。实验表明，该方法在封闭集上实现了最先进的性能，并具有强大的零样本泛化能力，从而实现了一种统一的范例，无缝地桥接了判别性感知和生成式推理，用于开放世界HOI检测。

## 🔬 方法详解

**问题定义**：现有HOI检测方法主要基于封闭世界假设，依赖于预定义的动词类别进行分类，无法有效处理真实场景中长尾分布的、未知的或语义模糊的交互行为。此外，直接微调大型多模态语言模型（MLLM）进行HOI检测计算成本过高，难以实现。

**核心思路**：GRASP-HO的核心思路是将HOI检测任务从传统的封闭集分类问题转化为开放词汇的生成问题，充分利用MLLM强大的语言理解和生成能力。通过将视觉信息有效地注入到MLLM中，引导其生成描述人-物交互的自然语言描述，从而实现对未知交互的识别。

**技术框架**：GRASP-HO框架主要包含以下几个关键模块：1) 混合交互表示提取模块，用于提取人、物及其交互的视觉特征；2) 可学习认知引导模块(CSC)，用于将提取的视觉特征注入到冻结的MLLM中，引导MLLM进行推理；3) 混合指导策略，结合语言建模损失和辅助分类损失，优化模型训练。

**关键创新**：GRASP-HO的关键创新在于：1) 将HOI检测任务重新定义为开放词汇生成问题，突破了传统方法的类别限制；2) 提出了轻量级的可学习认知引导模块(CSC)，实现了视觉信息到MLLM的有效传递，避免了对MLLM进行昂贵的微调；3) 设计了混合指导策略，解决了分类数据集与生成模型之间的监督不匹配问题。

**关键设计**：认知引导模块（CSC）采用轻量级网络结构，通过注意力机制将视觉特征融入MLLM的输入中。混合指导策略结合了语言建模损失（衡量生成文本的流畅性和准确性）和辅助分类损失（利用现有HOI数据集的类别信息），以提升模型的判别能力。具体损失函数的权重比例需要根据实验进行调整。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17640v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17640v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17640v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，GRASP-HO在封闭集HOI检测任务上取得了state-of-the-art的性能，并在零样本HOI检测任务上表现出强大的泛化能力。相较于传统方法，GRASP-HO在多个数据集上均取得了显著的性能提升，验证了其有效性和优越性。具体提升幅度在论文中有详细数据。

## 🎯 应用场景

GRASP-HO框架在智能监控、人机交互、机器人视觉等领域具有广泛的应用前景。它可以用于识别监控视频中的异常行为，理解人与机器人的交互意图，以及帮助机器人更好地理解和操作周围环境中的物体。该研究为开放世界场景下的人-物交互理解提供了新的思路。

## 📄 摘要（原文）

> Human-object interaction (HOI) detection aims to localize human-object pairs and the interactions between them. Existing methods operate under a closed-world assumption, treating the task as a classification problem over a small, predefined verb set, which struggles to generalize to the long-tail of unseen or ambiguous interactions in the wild. While recent multi-modal large language models (MLLMs) possess the rich world knowledge required for open-vocabulary understanding, they remain decoupled from existing HOI detectors since fine-tuning them is computationally prohibitive. To address these constraints, we propose \GRASP-HO}, a novel Generative Reasoning And Steerable Perception framework that reformulates HOI detection from the closed-set classification task to the open-vocabulary generation problem. To bridge the vision and cognitive, we first extract hybrid interaction representations, then design a lightweight learnable cognitive steering conduit (CSC) module to inject the fine-grained visual evidence into a frozen MLLM for effective reasoning. To address the supervision mismatch between classification-based HOI datasets and open-vocabulary generative models, we introduce a hybrid guidance strategy that coupling the language modeling loss and auxiliary classification loss, enabling discriminative grounding without sacrificing generative flexibility. Experiments demonstrate state-of-the-art closed-set performance and strong zero-shot generalization, achieving a unified paradigm that seamlessly bridges discriminative perception and generative reasoning for open-world HOI detection.

