---
layout: default
title: "TATTOO: Training-free AesTheTic-aware Outfit recOmmendation"
---

# TATTOO: Training-free AesTheTic-aware Outfit recOmmendation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.23242" class="toolbar-btn" target="_blank">📄 arXiv: 2509.23242v1</a>
  <a href="https://arxiv.org/pdf/2509.23242.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.23242v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.23242v1', 'TATTOO: Training-free AesTheTic-aware Outfit recOmmendation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuntian Wu, Xiaonan Hu, Ziqi Zhou, Hao Lu

**分类**: cs.CV

**发布日期**: 2025-09-27

**备注**: 4 figures, 4 tables

---

## 💡 一句话要点

**提出TATTOO：一种无需训练的、具有美学意识的服装搭配推荐方法**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `服装搭配推荐` `多模态大语言模型` `零样本学习` `美学感知` `链式思考`

## 📋 核心要点

1. 现有服装搭配推荐方法依赖大量标注数据进行训练，成本高昂，且缺乏对人类美学的显式建模。
2. TATTOO利用多模态大语言模型，无需训练即可生成目标物品描述和美学配置文件，实现美学感知的推荐。
3. 在Aesthetic-100数据集上，TATTOO取得了SOTA性能，并在Polyvore数据集上展示了先进的零样本检索能力。

## 📝 摘要（中文）

全球时尚电商市场严重依赖于智能且具有美学意识的服装搭配工具来促进销售。虽然之前的研究已经探讨了服装搭配和兼容物品检索的问题，但它们大多需要在大规模标注数据上进行昂贵的、特定于任务的训练，并且没有努力用明确的人类美学来指导服装推荐。在多模态大型语言模型（MLLM）时代，我们展示了传统的基于训练的流程可以简化为无需训练的模式，从而获得更好的推荐分数并增强美学意识。我们通过TATTOO来实现这一点，这是一种无需训练的、具有美学意识的服装推荐方法。它首先使用MLLM生成目标物品描述，然后使用美学链式思考将图像提炼成结构化的美学配置文件，包括颜色、风格、场合、季节、材质和平衡。通过使用动态熵门控机制将服装的视觉摘要与文本描述和美学向量融合，候选物品可以在共享嵌入空间中表示并相应地排序。在真实世界的评估集Aesthetic-100上的实验表明，与现有的基于训练的方法相比，TATTOO实现了最先进的性能。另一个标准的Polyvore数据集也被用来衡量我们无需训练的方法的先进的零样本检索能力。

## 🔬 方法详解

**问题定义**：论文旨在解决服装搭配推荐问题，现有方法主要依赖于大规模标注数据的训练，训练成本高昂，并且缺乏对人类美学知识的有效利用，导致推荐结果可能不符合人类审美偏好。

**核心思路**：论文的核心思路是利用多模态大型语言模型（MLLM）的强大能力，将视觉信息转化为文本描述和结构化的美学特征，从而实现无需训练的美学感知服装搭配推荐。通过MLLM对服装图像进行理解，提取颜色、风格、场合等美学属性，并将其融入到推荐过程中。

**技术框架**：TATTOO方法主要包含以下几个阶段：1) 使用MLLM生成目标物品的文本描述；2) 通过美学链式思考（Aesthetic Chain-of-Thought）将图像提炼成结构化的美学配置文件，包括颜色、风格、场合、季节、材质和平衡等属性；3) 使用动态熵门控机制融合服装的视觉摘要、文本描述和美学向量；4) 在共享嵌入空间中表示候选物品，并根据相似度进行排序和推荐。

**关键创新**：该方法最重要的创新点在于提出了一个无需训练的服装搭配推荐框架，摆脱了对大规模标注数据的依赖。通过MLLM和美学链式思考，能够有效地提取和利用服装的美学特征，从而提升推荐结果的美学质量。与现有方法相比，TATTOO更加灵活和高效，并且能够更好地适应新的时尚趋势。

**关键设计**：动态熵门控机制是关键设计之一，它用于自适应地融合视觉摘要、文本描述和美学向量，从而更好地表示服装的特征。具体实现细节（如损失函数、网络结构等）在论文中可能未详细描述，属于未知信息。

## 📊 实验亮点

TATTOO在Aesthetic-100数据集上取得了state-of-the-art的性能，超越了现有的基于训练的方法。此外，在Polyvore数据集上的实验也证明了TATTOO具有先进的零样本检索能力，表明其具有良好的泛化性能和适应性。

## 🎯 应用场景

该研究成果可应用于电商平台的服装搭配推荐系统，帮助用户快速找到符合个人风格和场合需求的服装搭配方案，提升用户购物体验和平台销售额。此外，该方法还可应用于时尚设计领域，为设计师提供灵感和参考，辅助服装设计和搭配。

## 📄 摘要（原文）

> The global fashion e-commerce market relies significantly on intelligent and aesthetic-aware outfit-completion tools to promote sales. While previous studies have approached the problem of fashion outfit-completion and compatible-item retrieval, most of them require expensive, task-specific training on large-scale labeled data, and no effort is made to guide outfit recommendation with explicit human aesthetics. In the era of Multimodal Large Language Models (MLLMs), we show that the conventional training-based pipeline could be streamlined to a training-free paradigm, with better recommendation scores and enhanced aesthetic awareness. We achieve this with TATTOO, a Training-free AesTheTic-aware Outfit recommendation approach. It first generates a target-item description using MLLMs, followed by an aesthetic chain-of-thought used to distill the images into a structured aesthetic profile including color, style, occasion, season, material, and balance. By fusing the visual summary of the outfit with the textual description and aesthetics vectors using a dynamic entropy-gated mechanism, candidate items can be represented in a shared embedding space and be ranked accordingly. Experiments on a real-world evaluation set Aesthetic-100 show that TATTOO achieves state-of-the-art performance compared with existing training-based methods. Another standard Polyvore dataset is also used to measure the advanced zero-shot retrieval capability of our training-free method.

