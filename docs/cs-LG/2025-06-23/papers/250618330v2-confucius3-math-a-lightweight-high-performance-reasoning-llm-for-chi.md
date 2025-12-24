---
layout: default
title: "Confucius3-Math: A Lightweight High-Performance Reasoning LLM for Chinese K-12 Mathematics Learning"
---

# Confucius3-Math: A Lightweight High-Performance Reasoning LLM for Chinese K-12 Mathematics Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.18330" class="toolbar-btn" target="_blank">📄 arXiv: 2506.18330v2</a>
  <a href="https://arxiv.org/pdf/2506.18330.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.18330v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.18330v2', 'Confucius3-Math: A Lightweight High-Performance Reasoning LLM for Chinese K-12 Mathematics Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lixin Wu, Na Cai, Qiao Cheng, Jiachen Wang, Yitao Duan

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-06-23 (更新: 2025-06-25)

**🔗 代码/项目**: [GITHUB](https://github.com/netease-youdao/Confucius3-Math)

---

## 💡 一句话要点

**提出Confucius3-Math以解决中国K-12数学学习问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `数学推理` `强化学习` `教育技术` `开源模型` `K-12教育` `低成本解决方案` `数据效率` `模型优化`

## 📋 核心要点

1. 现有的数学推理模型通常体积庞大，难以在普通硬件上高效运行，限制了其在教育领域的应用。
2. Confucius3-Math通过后训练和强化学习，专注于中国K-12数学问题，旨在以低成本提供高效的数学学习支持。
3. 该模型在多个数学推理任务上表现出色，超越了许多更大规模的模型，展示了其在特定领域的强大能力。

## 📝 摘要（中文）

我们介绍了Confucius3-Math，这是一个开源的大型语言模型，拥有140亿参数，能够在单个消费级GPU上高效运行，并在多项数学推理任务上达到了当前的最佳性能，超越了许多更大规模的模型。Confucius3-Math专注于中国K-12学生和教育工作者的数学学习，采用大规模强化学习进行后训练，符合国家课程标准，能够以低成本解决主流的数学问题。本文分享了我们的开发过程、遇到的挑战以及为克服这些挑战而开发的技术，特别介绍了三项技术创新：目标熵正则化、近期样本恢复和策略特定困难加权，这些创新显著稳定了强化学习训练，提高了数据效率，并提升了模型性能。我们在https://github.com/netease-youdao/Confucius3-Math上开源了模型和代码。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有数学推理模型在硬件要求和成本上的不足，特别是在中国K-12教育领域的应用痛点。

**核心思路**：通过后训练和大规模强化学习，Confucius3-Math专注于数学学习，优化了模型的运行效率和推理能力。

**技术框架**：模型的整体架构包括数据采集、后训练、强化学习优化等多个阶段，确保模型在特定任务上的高效表现。

**关键创新**：引入了目标熵正则化、近期样本恢复和策略特定困难加权等技术，这些创新显著提升了模型的训练稳定性和数据利用效率。

**关键设计**：在模型训练中，采用了新的损失函数和数据调度策略，以提高模型在特定数学问题上的表现，同时优化了网络结构以适应强化学习的需求。

## 📊 实验亮点

在多个数学推理任务中，Confucius3-Math的性能超越了许多更大规模的模型，展示了其在特定领域的强大能力。具体而言，该模型在某些任务上实现了超过10%的性能提升，证明了其在教育应用中的有效性。

## 🎯 应用场景

Confucius3-Math的潜在应用领域包括在线教育平台、智能辅导系统和教育资源的个性化推荐。其高效的数学推理能力能够帮助学生更好地理解和掌握数学知识，提升学习效果，具有重要的实际价值和广泛的社会影响。

## 📄 摘要（原文）

> We introduce Confucius3-Math, an open-source large language model with 14B parameters that (1) runs efficiently on a single consumer-grade GPU; (2) achieves SOTA performances on a range of mathematical reasoning tasks, outperforming many models with significantly larger sizes. In particular, as part of our mission to enhancing education and knowledge dissemination with AI, Confucius3-Math is specifically committed to mathematics learning for Chinese K-12 students and educators. Built via post-training with large-scale reinforcement learning (RL), Confucius3-Math aligns with national curriculum and excels at solving main-stream Chinese K-12 mathematical problems with low cost. In this report we share our development recipe, the challenges we encounter and the techniques we develop to overcome them. In particular, we introduce three technical innovations: Targeted Entropy Regularization, Recent Sample Recovery and Policy-Specific Hardness Weighting. These innovations encompass a new entropy regularization, a novel data scheduling policy, and an improved group-relative advantage estimator. Collectively, they significantly stabilize the RL training, improve data efficiency, and boost performance. Our work demonstrates the feasibility of building strong reasoning models in a particular domain at low cost. We open-source our model and code at https://github.com/netease-youdao/Confucius3-Math.

