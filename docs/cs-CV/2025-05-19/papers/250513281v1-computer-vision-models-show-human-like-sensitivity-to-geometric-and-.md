---
layout: default
title: Computer Vision Models Show Human-Like Sensitivity to Geometric and Topological Concepts
---

# Computer Vision Models Show Human-Like Sensitivity to Geometric and Topological Concepts

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13281" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13281v1</a>
  <a href="https://arxiv.org/pdf/2505.13281.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13281v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13281v1', 'Computer Vision Models Show Human-Like Sensitivity to Geometric and Topological Concepts')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zekun Wang, Sashank Varma

**分类**: cs.CV

**发布日期**: 2025-05-19

**备注**: 10 pages, 4 figures, CosSci 2025

**期刊**: Cognitive Science Society 2025

---

## 💡 一句话要点

**利用计算机视觉模型探讨人类对几何与拓扑概念的敏感性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `计算机视觉` `几何概念` `拓扑概念` `变换器模型` `多模态学习` `认知科学` `机器学习`

## 📋 核心要点

1. 现有的认知科学研究主要集中在几何和拓扑概念的先天性，而缺乏对后天学习的探讨。
2. 本文通过计算机视觉模型，探讨GT概念是否可以通过与环境的互动而获得，提出了新的研究视角。
3. 实验结果显示，基于变换器的模型在GT概念的识别上表现优异，超过了幼儿的表现，并与儿童的难易程度一致。

## 📝 摘要（中文）

随着机器学习模型的快速发展，认知科学家越来越关注这些模型与人类思维的对齐程度。本文研究了计算机视觉模型在几何和拓扑（GT）概念上的表现，提出这些概念可能通过日常环境交互“免费”学习。通过对卷积神经网络、基于变换器的模型和视觉-语言模型的比较，发现基于变换器的模型在准确性上超越了幼儿，并与儿童的表现高度一致。相对而言，视觉-语言模型的表现不佳，表明简单的多模态融合可能会削弱对抽象几何的敏感性。这些发现支持使用计算机视觉模型来评估学习理论在解释人类GT概念敏感性方面的充分性。

## 🔬 方法详解

**问题定义**：本文旨在探讨计算机视觉模型在几何和拓扑概念上的敏感性，现有研究主要认为这些概念是先天的，而缺乏对后天学习的实证支持。

**核心思路**：通过对比不同类型的计算机视觉模型，验证GT概念是否可以通过环境交互学习，提出了新的视角来理解人类的认知能力。

**技术框架**：研究使用三类模型：卷积神经网络（CNN）、基于变换器的模型和视觉-语言模型，进行“奇异物体”任务，评估其在43个GT概念上的表现。

**关键创新**：基于变换器的模型在准确性上超越了幼儿，且与儿童的表现高度一致，显示出其在理解GT概念上的潜力。相较之下，视觉-语言模型的表现较差，揭示了多模态融合的潜在问题。

**关键设计**：模型训练使用了大规模图像数据集，任务设计为“奇异物体”选择，评估模型在不同GT概念上的表现，关键参数和损失函数的选择旨在优化模型的学习能力。

## 📊 实验亮点

实验结果显示，基于变换器的模型在GT概念的识别上达到了最高准确率，超过了幼儿的表现，并且在难易程度上与儿童的表现高度一致。这一发现表明，计算机视觉模型在理解复杂概念方面具有潜力，尤其是在几何和拓扑领域。

## 🎯 应用场景

该研究的潜在应用领域包括教育技术、人工智能辅助学习以及认知科学研究。通过理解计算机视觉模型如何学习几何和拓扑概念，可以为开发更智能的教育工具提供理论支持，促进人机交互的进一步发展。

## 📄 摘要（原文）

> With the rapid improvement of machine learning (ML) models, cognitive scientists are increasingly asking about their alignment with how humans think. Here, we ask this question for computer vision models and human sensitivity to geometric and topological (GT) concepts. Under the core knowledge account, these concepts are innate and supported by dedicated neural circuitry. In this work, we investigate an alternative explanation, that GT concepts are learned ``for free'' through everyday interaction with the environment. We do so using computer visions models, which are trained on large image datasets. We build on prior studies to investigate the overall performance and human alignment of three classes of models -- convolutional neural networks (CNNs), transformer-based models, and vision-language models -- on an odd-one-out task testing 43 GT concepts spanning seven classes. Transformer-based models achieve the highest overall accuracy, surpassing that of young children. They also show strong alignment with children's performance, finding the same classes of concepts easy vs. difficult. By contrast, vision-language models underperform their vision-only counterparts and deviate further from human profiles, indicating that naïve multimodality might compromise abstract geometric sensitivity. These findings support the use of computer vision models to evaluate the sufficiency of the learning account for explaining human sensitivity to GT concepts, while also suggesting that integrating linguistic and visual representations might have unpredicted deleterious consequences.

