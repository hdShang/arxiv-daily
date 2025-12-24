---
layout: default
title: "Breaking the SFT Plateau: Multimodal Structured Reinforcement Learning for Chart-to-Code Generation"
---

# Breaking the SFT Plateau: Multimodal Structured Reinforcement Learning for Chart-to-Code Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.13587" class="toolbar-btn" target="_blank">📄 arXiv: 2508.13587v1</a>
  <a href="https://arxiv.org/pdf/2508.13587.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.13587v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.13587v1', 'Breaking the SFT Plateau: Multimodal Structured Reinforcement Learning for Chart-to-Code Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lei Chen, Xuanle Zhao, Zhixiong Zeng, Jing Huang, Liming Zheng, Yufeng Zhong, Lin Ma

**分类**: cs.AI, cs.CV

**发布日期**: 2025-08-19

**备注**: technical report

---

## 💡 一句话要点

**提出多模态结构化强化学习以解决图表到代码生成问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `图表到代码生成` `多模态学习` `强化学习` `结构化奖励` `自动化编程`

## 📋 核心要点

1. 现有的监督微调方法在图表到代码生成任务中面临性能瓶颈，难以满足复杂推理的需求。
2. 论文提出的多模态结构化强化学习（MSRL）方法，通过多层次结构化奖励系统来优化生成的代码质量。
3. 实验结果显示，MSRL在多个基准测试中显著提升了性能，突破了传统SFT方法的局限性。

## 📝 摘要（中文）

尽管强化学习在视觉语言模型中的推理能力已得到验证，但在需要深入理解信息丰富图像和生成结构化输出的任务中，其应用仍然不足。图表到代码生成正是这一挑战的典型例子，要求对视觉图表进行复杂推理以生成结构化代码。仅依赖监督微调（SFT）往往不够，突显出有效的强化学习策略的必要性。本文提出的多模态结构化强化学习（MSRL）方法，通过构建包含300万个真实世界arXiv表格的图表-代码对的训练语料库，显著突破了SFT的性能瓶颈。实验结果表明，MSRL在ChartMimic和ReachQA基准上分别提升了6.2%和9.9%的高层次指标，达到了与先进闭源模型竞争的性能。

## 🔬 方法详解

**问题定义**：本文旨在解决图表到代码生成任务中，现有监督微调方法（SFT）所面临的性能瓶颈和复杂推理能力不足的问题。现有方法在处理信息丰富的图像时，往往无法有效生成结构化输出。

**核心思路**：论文提出的多模态结构化强化学习（MSRL）方法，通过引入多层次的结构化奖励机制，结合文本和视觉反馈，来提升生成代码的质量和准确性。这样的设计旨在更好地评估和奖励生成代码的细节和结构相似性。

**技术框架**：MSRL方法的整体架构包括两个主要阶段：首先是基于文本的规则奖励系统，用于验证代码的细粒度细节；其次是基于视觉的模型奖励系统，通过将生成的代码渲染为图像并使用评估模型来评估结构相似性。

**关键创新**：最重要的技术创新在于引入了多层次的结构化奖励系统，结合文本和视觉信息进行评估，这与传统的单一奖励机制有本质区别。

**关键设计**：在关键设计上，论文构建了一个包含300万个图表-代码对的大规模训练语料库，并在训练过程中采用了两阶段的课程学习策略，以确保训练的稳定性和有效性。

## 📊 实验亮点

实验结果表明，MSRL方法在ChartMimic和ReachQA基准测试中分别提升了6.2%和9.9%的高层次指标，显著突破了传统SFT方法的性能瓶颈，达到了与先进闭源模型的竞争水平。这一成果展示了多模态结构化奖励在复杂任务中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括自动化编程、数据可视化工具以及智能助理等。通过提升图表到代码生成的准确性和效率，MSRL方法能够为开发者提供更强大的工具，促进数据分析和决策支持的自动化。未来，该方法可能在更广泛的多模态学习任务中发挥重要作用。

## 📄 摘要（原文）

> While reinforcement learning (RL) has proven highly effective for general reasoning in vision-language models, its application to tasks requiring in-depth understanding of information-rich images and generation of structured outputs remains underexplored. Chart-to-code generation exemplifies this challenge, demanding complex reasoning over visual charts to generate structured code. Supervised fine-tuning (SFT) alone is often insufficient, highlighting the need for effective RL strategies that appropriately reward structured outputs. We systematically investigate the performance plateau in SFT through large-scale experiments and propose Multimodal Structured Reinforcement Learning (MSRL) for chart-to-code generation, which substantially breaks through this plateau. We construct the largest training corpus to date, containing 3 million chart-code pairs from real-world arXiv tables to mitigate simplistic patterns of prior synthetic data. Despite reaching state-of-the-art performance, our experiments show that scaling SFT data eventually hits a plateau where further increases yield negligible improvements. Our MSRL method leverages a multi-granularity structured reward system using multimodal textual and visual feedback. At the textual level, rule-based rewards validate fine-grained code details. At the visual level, model-based rewards assess structural similarity by rendering generated code into images and employing an evaluator model. We implement this within a two-stage curriculum for training stability. Results demonstrate that MSRL significantly breaks the SFT plateau, improving high-level metrics by 6.2% and 9.9% on ChartMimic and ReachQA benchmarks respectively, achieving competitive performance with advanced closed-source models.

