---
layout: default
title: "Seeing What Tastes Good: Revisiting Multimodal Distributional Semantics in the Billion Parameter Era"
---

# Seeing What Tastes Good: Revisiting Multimodal Distributional Semantics in the Billion Parameter Era

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.03994" class="toolbar-btn" target="_blank">📄 arXiv: 2506.03994v1</a>
  <a href="https://arxiv.org/pdf/2506.03994.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.03994v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.03994v1', 'Seeing What Tastes Good: Revisiting Multimodal Distributional Semantics in the Billion Parameter Era')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dan Oneata, Desmond Elliott, Stella Frank

**分类**: cs.CL, cs.CV

**发布日期**: 2025-06-04

**备注**: ACL Findings 2025

---

## 💡 一句话要点

**探讨多模态分布语义在亿参数时代的表现**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `分布语义` `图像编码器` `语言模型` `属性预测`

## 📋 核心要点

1. 现有的基础模型在理解具体物体概念的语义特征方面存在不足，尤其是对非视觉属性的理解。
2. 本文提出通过探测任务评估多模态图像编码器与语言模型在物体属性认知上的表现，以探索模态间的互补性。
3. 实验结果显示，多模态图像编码器在性能上略优于语言模型，而仅图像编码器在某些方面表现相当，揭示了单模态学习的潜力。

## 📝 摘要（中文）

人类的学习和概念表征是基于感知运动经验的，这与当前最先进的基础模型形成对比。本文研究了大规模模型在表示具体物体概念的语义特征规范方面的有效性，例如“玫瑰是红色的，闻起来香甜，是一种花”。我们使用探测任务测试这些模型对物体属性的认知。评估了仅训练于图像数据的图像编码器、多模态训练的图像编码器和仅语言模型在预测经典McRae规范的扩展版本及Binder属性评分数据集的表现。结果表明，多模态图像编码器略优于仅语言的方法，而仅图像编码器在非视觉属性上与语言模型表现相当。这些结果为单模态学习的潜力及模态间的互补性提供了新见解。

## 🔬 方法详解

**问题定义**：本文旨在解决大规模模型在理解具体物体概念的语义特征方面的不足，尤其是对非视觉属性的认知能力。现有方法主要依赖于单一模态，未能充分利用多模态信息的互补性。

**核心思路**：通过探测任务评估不同类型的编码器，包括仅图像、仅语言和多模态训练的图像编码器，来测试它们对物体属性的认知能力。这样的设计旨在揭示模态间的互补性及单模态学习的潜力。

**技术框架**：研究采用了多种编码器进行对比实验，主要模块包括图像编码器、语言模型和探测任务的设计。实验通过对比不同模型在McRae规范和Binder数据集上的表现，评估其对物体属性的理解能力。

**关键创新**：论文的主要创新在于通过多模态与单模态模型的对比，揭示了图像编码器在理解非视觉属性方面的潜力，挑战了传统对语言模型的依赖。

**关键设计**：在实验中，使用了扩展的McRae规范和Binder数据集作为评估标准，模型的训练过程采用了标准的损失函数和网络结构设计，确保了结果的可靠性与可比性。

## 📊 实验亮点

实验结果显示，多模态图像编码器在属性预测任务中略优于语言模型，且仅图像编码器在某些非视觉属性上表现出与语言模型相当的能力。这一发现表明，单模态学习在理解具体物体概念方面具有重要价值，拓展了对多模态学习的理解。

## 🎯 应用场景

该研究的潜在应用领域包括计算机视觉、自然语言处理及人机交互等。通过深入理解多模态学习的优势，未来可以在智能助手、自动驾驶和机器人等领域实现更为精准的感知与决策能力，提升用户体验和系统性能。

## 📄 摘要（原文）

> Human learning and conceptual representation is grounded in sensorimotor experience, in contrast to state-of-the-art foundation models. In this paper, we investigate how well such large-scale models, trained on vast quantities of data, represent the semantic feature norms of concrete object concepts, e.g. a ROSE is red, smells sweet, and is a flower. More specifically, we use probing tasks to test which properties of objects these models are aware of. We evaluate image encoders trained on image data alone, as well as multimodally-trained image encoders and language-only models, on predicting an extended denser version of the classic McRae norms and the newer Binder dataset of attribute ratings. We find that multimodal image encoders slightly outperform language-only approaches, and that image-only encoders perform comparably to the language models, even on non-visual attributes that are classified as "encyclopedic" or "function". These results offer new insights into what can be learned from pure unimodal learning, and the complementarity of the modalities.

