---
layout: default
title: "Unlocking the Essence of Beauty: Advanced Aesthetic Reasoning with Relative-Absolute Policy Optimization"
---

# Unlocking the Essence of Beauty: Advanced Aesthetic Reasoning with Relative-Absolute Policy Optimization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.21871" class="toolbar-btn" target="_blank">📄 arXiv: 2509.21871v1</a>
  <a href="https://arxiv.org/pdf/2509.21871.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.21871v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.21871v1', 'Unlocking the Essence of Beauty: Advanced Aesthetic Reasoning with Relative-Absolute Policy Optimization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Boyang Liu, Yifan Hu, Senjie Jin, Shihan Dou, Gonglei Shi, Jie Shao, Tao Gui, Xuanjing Huang

**分类**: cs.CV, cs.AI

**发布日期**: 2025-09-26

---

## 💡 一句话要点

**提出基于相对-绝对策略优化的Aes-R1框架，提升多模态大语言模型的美学推理能力。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `美学评估` `强化学习` `大语言模型` `相对排序` `策略优化` `思维链` `可解释性`

## 📋 核心要点

1. 多模态大语言模型在图像美学评估中表现出色，但缺乏高质量美学推理数据和主观性限制了其准确性和可解释性。
2. Aes-R1框架通过AesCoT流程构建高质量思维链数据，并利用相对-绝对策略优化（RAPO）算法，联合优化绝对分数和相对排序。
3. 实验表明，Aes-R1显著提升了美学评分的准确性和解释性，PLCC/SRCC指标平均提升47.9%/34.8%，并在有限监督下表现出良好的泛化能力。

## 📝 摘要（中文）

本文提出了一种名为Aes-R1的综合美学推理框架，该框架结合了强化学习（RL）。具体而言，Aes-R1集成了一个名为AesCoT的流程，用于构建和过滤高质量的思维链美学推理数据，以实现冷启动。在训练模型生成结构化解释后再进行评分后，我们采用了一种新颖的RL算法，即相对-绝对策略优化（RAPO），该算法联合优化绝对分数回归和相对排序，从而提高了每个图像的准确性和跨图像的偏好判断。Aes-R1使MLLM能够生成基于事实的解释以及可信的分数，从而在统一的框架中增强美学评分和推理。大量实验表明，Aes-R1将骨干网络的平均PLCC/SRCC提高了47.9%/34.8%，超过了类似大小的state-of-the-art基线。更多的消融研究验证了Aes-R1在有限监督和分布外场景下的鲁棒泛化能力。

## 🔬 方法详解

**问题定义**：论文旨在解决多模态大语言模型（MLLM）在图像美学评估中面临的挑战，即缺乏高质量的美学推理数据以及美学判断的主观性。现有方法难以生成准确且具有可解释性的美学判断。

**核心思路**：论文的核心思路是利用强化学习（RL）来训练MLLM，使其能够生成结构化的解释，并同时优化绝对分数回归和相对排序。通过这种方式，模型不仅能够给出准确的美学评分，还能提供可信的推理过程。

**技术框架**：Aes-R1框架包含两个主要阶段：首先，利用AesCoT流程构建和过滤高质量的思维链美学推理数据，用于模型的冷启动。然后，采用相对-绝对策略优化（RAPO）算法，联合优化绝对分数回归和相对排序。整个框架旨在实现美学评分和推理的统一。

**关键创新**：论文的关键创新在于提出了相对-绝对策略优化（RAPO）算法。RAPO算法能够同时优化绝对分数回归和相对排序，从而更好地捕捉美学判断的细微差别和主观性。这与传统的只关注绝对分数回归的方法有本质区别。

**关键设计**：AesCoT流程用于生成高质量的思维链数据，具体实现细节未知。RAPO算法的具体实现细节也未知，但其核心思想是结合绝对分数和相对排序信息来优化策略。损失函数的设计需要同时考虑绝对分数回归的误差和相对排序的误差。网络结构方面，论文使用了多模态大语言模型作为骨干网络，但具体结构细节未知。

## 📊 实验亮点

实验结果表明，Aes-R1框架显著提升了多模态大语言模型的美学推理能力。在多个数据集上，Aes-R1将骨干网络的平均PLCC/SRCC指标提高了47.9%/34.8%，超越了现有state-of-the-art的基线模型。此外，消融实验验证了Aes-R1在有限监督和分布外场景下的鲁棒泛化能力。

## 🎯 应用场景

该研究成果可应用于图像美学评估、图像推荐系统、艺术品鉴赏、摄影辅助等领域。通过提供可解释的美学评分，可以帮助用户更好地理解图像的美学价值，并为相关应用提供更智能化的支持。未来，该技术有望应用于更广泛的多模态内容理解和生成领域。

## 📄 摘要（原文）

> Multimodal large language models (MLLMs) are well suited to image aesthetic assessment, as they can capture high-level aesthetic features leveraging their cross-modal understanding capacity. However, the scarcity of multimodal aesthetic reasoning data and the inherently subjective nature of aesthetic judgment make it difficult for MLLMs to generate accurate aesthetic judgments with interpretable rationales. To this end, we propose Aes-R1, a comprehensive aesthetic reasoning framework with reinforcement learning (RL). Concretely, Aes-R1 integrates a pipeline, AesCoT, to construct and filter high-quality chain-of-thought aesthetic reasoning data used for cold-start. After teaching the model to generate structured explanations prior to scoring, we then employ the Relative-Absolute Policy Optimization (RAPO), a novel RL algorithm that jointly optimizes absolute score regression and relative ranking order, improving both per-image accuracy and cross-image preference judgments. Aes-R1 enables MLLMs to generate grounded explanations alongside faithful scores, thereby enhancing aesthetic scoring and reasoning in a unified framework. Extensive experiments demonstrate that Aes-R1 improves the backbone's average PLCC/SRCC by 47.9%/34.8%, surpassing state-of-the-art baselines of similar size. More ablation studies validate Aes-R1's robust generalization under limited supervision and in out-of-distribution scenarios.

