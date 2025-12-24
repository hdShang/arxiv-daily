---
layout: default
title: "From Data to Modeling: Fully Open-vocabulary Scene Graph Generation"
---

# From Data to Modeling: Fully Open-vocabulary Scene Graph Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20106" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20106v1</a>
  <a href="https://arxiv.org/pdf/2505.20106.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20106v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20106v1', 'From Data to Modeling: Fully Open-vocabulary Scene Graph Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zuyao Chen, Jinlin Wu, Zhen Lei, Chang Wen Chen

**分类**: cs.CV

**发布日期**: 2025-05-26

---

## 💡 一句话要点

**提出OvSGTR以解决传统场景图生成的开放词汇问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `开放词汇` `场景图生成` `变换器架构` `弱监督学习` `关系感知预训练`

## 📋 核心要点

1. 现有的场景图生成方法通常限制在固定的词汇内，无法适应新兴概念，影响实际应用。
2. OvSGTR通过联合预测对象和关系，采用DETR-like架构和关系感知预训练策略，突破了传统模型的限制。
3. 在VG150基准上，OvSGTR在闭集和开放词汇场景下均表现出色，展示了其在视觉理解中的潜力。

## 📝 摘要（中文）

我们提出了OvSGTR，这是一种新颖的基于变换器的框架，用于完全开放词汇的场景图生成，克服了传统闭集模型的局限性。传统方法将对象和关系识别限制在固定词汇内，限制了其在新概念频繁出现的现实场景中的适用性。我们的方案超越了预定义类别，联合预测对象（节点）及其相互关系（边）。OvSGTR利用类似DETR的架构，结合冻结的图像主干和文本编码器提取高质量的视觉和语义特征，并通过变换器解码器进行端到端的场景图预测。为增强模型对复杂视觉关系的理解，我们提出了一种关系感知的预训练策略，采用弱监督方式合成场景图注释。实验结果表明，OvSGTR在VG150基准上实现了多种设置下的最先进性能。

## 🔬 方法详解

**问题定义**：本论文旨在解决传统场景图生成模型在开放词汇场景中的局限性，现有方法无法处理新出现的对象和关系，限制了其应用范围。

**核心思路**：OvSGTR通过联合预测对象和关系，采用变换器架构，结合弱监督的关系感知预训练策略，增强模型对复杂视觉关系的理解。

**技术框架**：OvSGTR的整体架构包括一个冻结的图像主干和文本编码器，用于提取视觉和语义特征，随后通过变换器解码器进行场景图的端到端预测。

**关键创新**：本研究的核心创新在于提出了开放词汇的场景图生成方法，结合了关系感知的预训练策略和视觉概念保留机制，显著提升了模型在新概念场景下的表现。

**关键设计**：模型采用了DETR-like架构，结合了多种生成监督信号的管道，确保在微调过程中保留丰富的语义线索，同时引入知识蒸馏策略以应对灾难性遗忘问题。

## 📊 实验亮点

在VG150基准测试中，OvSGTR在多个设置下实现了最先进的性能，包括闭集和开放词汇对象检测、关系基础和完全开放词汇场景，展示了其在复杂视觉理解中的有效性和可靠性。

## 🎯 应用场景

该研究的潜在应用领域包括智能监控、自动驾驶、虚拟现实等，能够提升计算机视觉系统对复杂场景的理解能力，推动相关技术的实际应用和发展。未来，该方法可能在更广泛的视觉理解任务中发挥重要作用，促进开放词汇的智能系统构建。

## 📄 摘要（原文）

> We present OvSGTR, a novel transformer-based framework for fully open-vocabulary scene graph generation that overcomes the limitations of traditional closed-set models. Conventional methods restrict both object and relationship recognition to a fixed vocabulary, hindering their applicability to real-world scenarios where novel concepts frequently emerge. In contrast, our approach jointly predicts objects (nodes) and their inter-relationships (edges) beyond predefined categories. OvSGTR leverages a DETR-like architecture featuring a frozen image backbone and text encoder to extract high-quality visual and semantic features, which are then fused via a transformer decoder for end-to-end scene graph prediction. To enrich the model's understanding of complex visual relations, we propose a relation-aware pre-training strategy that synthesizes scene graph annotations in a weakly supervised manner. Specifically, we investigate three pipelines--scene parser-based, LLM-based, and multimodal LLM-based--to generate transferable supervision signals with minimal manual annotation. Furthermore, we address the common issue of catastrophic forgetting in open-vocabulary settings by incorporating a visual-concept retention mechanism coupled with a knowledge distillation strategy, ensuring that the model retains rich semantic cues during fine-tuning. Extensive experiments on the VG150 benchmark demonstrate that OvSGTR achieves state-of-the-art performance across multiple settings, including closed-set, open-vocabulary object detection-based, relation-based, and fully open-vocabulary scenarios. Our results highlight the promise of large-scale relation-aware pre-training and transformer architectures for advancing scene graph generation towards more generalized and reliable visual understanding.

