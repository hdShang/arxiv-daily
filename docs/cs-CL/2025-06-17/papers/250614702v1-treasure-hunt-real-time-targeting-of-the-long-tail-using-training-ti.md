---
layout: default
title: "Treasure Hunt: Real-time Targeting of the Long Tail using Training-Time Markers"
---

# Treasure Hunt: Real-time Targeting of the Long Tail using Training-Time Markers

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.14702" class="toolbar-btn" target="_blank">📄 arXiv: 2506.14702v1</a>
  <a href="https://arxiv.org/pdf/2506.14702.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.14702v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.14702v1', 'Treasure Hunt: Real-time Targeting of the Long Tail using Training-Time Markers')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Daniel D'souza, Julia Kreutzer, Adrien Morisot, Ahmet Üstün, Sara Hooker

**分类**: cs.CL, cs.LG

**发布日期**: 2025-06-17

---

## 💡 一句话要点

**提出训练时标记优化以提升长尾特征表现**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长尾特征` `模型微调` `生成控制` `自然语言处理` `稀有特征`

## 📋 核心要点

1. 现有模型在稀有特征上的表现不佳，难以适应训练中未充分代表的用例。
2. 通过优化训练协议，创建数据特征和任务来源的分类法，提升模型在推理时的可控性和性能。
3. 实验结果显示，使用标记后生成质量平均提升5.7%，在代表性不足的领域提升超过9.1%。

## 📝 摘要（中文）

现代机器学习面临的一个重大挑战是如何在稀有和代表性不足的特征上表现良好。现有的大型通用模型在高频使用场景中表现最佳，难以适应训练语料中代表性不足的特定用例。本文探讨了如何优化训练协议，以提高推理时对这些用例的可控性和性能。通过创建数据特征和任务来源的详细分类法，作者提出了一种灵活的方法，使模型能够在推理时自动推断这些标记，从而显著提升了长尾样本的生成质量，尤其在代表性不足的领域中取得了超过9.1%的性能提升。

## 🔬 方法详解

**问题定义**：本文旨在解决现代机器学习模型在长尾特征上的表现不足，尤其是在训练语料中代表性不足的用例。现有方法依赖于提示工程或少量示例，导致模型对小变化敏感，且难以保持性能。

**核心思路**：论文提出通过优化训练过程，创建一套详细的数据特征和任务来源分类法，使模型在推理时能够自动推断标记，从而提高对长尾特征的响应能力和生成质量。

**技术框架**：整体架构包括数据标记的生成、模型的微调和推理阶段。模型在训练时学习如何识别和生成这些标记，推理时则可选择性地使用这些标记来控制生成结果。

**关键创新**：最重要的创新在于将训练和推理过程结合，通过明确的标记控制生成属性，显著提升了模型在长尾特征上的表现。这一方法与传统的依赖固定提示的方式有本质区别。

**关键设计**：在模型微调过程中，采用了特定的损失函数和网络结构，以确保模型能够有效学习到标记的生成。同时，设计了灵活的参数设置，使得标记在推理时可以选择性使用。

## 📊 实验亮点

实验结果显示，使用训练时标记后，模型在开放式生成质量上平均提升5.7%，在代表性不足的领域提升超过9.1%。在特定任务如CodeRepair上，表现提升达到14.1%，在长度指令跟随评估中绝对提升达到35.3%。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、代码生成和其他需要处理稀有特征的任务。通过提升模型在长尾特征上的表现，能够更好地满足特定行业或领域的需求，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> One of the most profound challenges of modern machine learning is performing well on the long-tail of rare and underrepresented features. Large general-purpose models are trained for many tasks, but work best on high-frequency use cases. After training, it is hard to adapt a model to perform well on specific use cases underrepresented in the training corpus. Relying on prompt engineering or few-shot examples to maximize the output quality on a particular test case can be frustrating, as models can be highly sensitive to small changes, react in unpredicted ways or rely on a fixed system prompt for maintaining performance. In this work, we ask: "Can we optimize our training protocols to both improve controllability and performance on underrepresented use cases at inference time?" We revisit the divide between training and inference techniques to improve long-tail performance while providing users with a set of control levers the model is trained to be responsive to. We create a detailed taxonomy of data characteristics and task provenance to explicitly control generation attributes and implicitly condition generations at inference time. We fine-tune a base model to infer these markers automatically, which makes them optional at inference time. This principled and flexible approach yields pronounced improvements in performance, especially on examples from the long tail of the training distribution. While we observe an average lift of 5.7% win rates in open-ended generation quality with our markers, we see over 9.1% gains in underrepresented domains. We also observe relative lifts of up to 14.1% on underrepresented tasks like CodeRepair and absolute improvements of 35.3% on length instruction following evaluations.

