---
layout: default
title: "Athena: Enhancing Multimodal Reasoning with Data-efficient Process Reward Models"
---

# Athena: Enhancing Multimodal Reasoning with Data-efficient Process Reward Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.09532" class="toolbar-btn" target="_blank">📄 arXiv: 2506.09532v4</a>
  <a href="https://arxiv.org/pdf/2506.09532.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.09532v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.09532v4', 'Athena: Enhancing Multimodal Reasoning with Data-efficient Process Reward Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shuai Wang, Zhenhua Liu, Jiaheng Wei, Xuanwu Yin, Dong Li, Emad Barsoum

**分类**: cs.LG, cs.AI, cs.CL, cs.CV

**发布日期**: 2025-06-11 (更新: 2025-12-04)

---

## 💡 一句话要点

**提出Athena-PRM以高效解决多模态推理中的奖励模型问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态推理` `奖励模型` `过程标注` `数据效率` `模型优化` `智能系统` `自动化评估`

## 📋 核心要点

1. 现有的奖励模型开发通常需要大量的时间和财力投入，尤其是对推理步骤的逐步标注存在挑战。
2. 论文提出Athena-PRM，通过利用弱补全者与强补全者的预测一致性来高效生成高质量的过程标注数据。
3. Athena-PRM在多个基准测试中表现优异，尤其在WeMath和MathVista上分别提升了10.2和7.1分，且在VisualProcessBench上达到了最新的SoTA结果。

## 📝 摘要（中文）

我们提出了Athena-PRM，这是一种多模态过程奖励模型，旨在评估解决复杂推理问题每一步的奖励分数。开发高性能的奖励模型通常需要大量时间和财力投入，主要是因为需要对推理步骤进行逐步标注。传统的自动标注方法，如蒙特卡洛估计，往往产生噪声标签并且计算成本高。为高效生成高质量的过程标注数据，我们提出利用弱补全者与强补全者之间的预测一致性作为识别可靠过程标签的标准。Athena-PRM在多个场景和基准测试中表现出色，仅需5000个样本。此外，我们还开发了两种有效策略以提升奖励模型的性能：ORM初始化和负样本的上采样。我们的实验验证了Athena-PRM在多个基准和场景中的优越性能。

## 🔬 方法详解

**问题定义**：论文旨在解决多模态推理中奖励模型的开发问题，现有方法在标注推理步骤时面临高成本和噪声标签的挑战。

**核心思路**：Athena-PRM通过利用弱补全者与强补全者之间的预测一致性，来高效生成可靠的过程标注数据，从而降低对标注的依赖。

**技术框架**：Athena-PRM的整体架构包括数据生成模块、奖励评估模块和模型训练模块。数据生成模块负责生成过程标注数据，奖励评估模块则用于评估每一步的奖励分数，模型训练模块则进行模型的优化和调整。

**关键创新**：Athena-PRM的核心创新在于通过预测一致性来识别可靠的过程标签，这一方法显著降低了对人工标注的需求，并提高了数据的质量。

**关键设计**：在模型设计中，采用了ORM初始化和负样本的上采样策略，以增强模型的学习能力和泛化能力。

## 📊 实验亮点

Athena-PRM在多个基准测试中表现优异，使用Qwen2.5-VL-7B作为策略模型时，在WeMath和MathVista上分别提升了10.2和7.1分。此外，Athena-PRM在VisualProcessBench上达到了最新的SoTA结果，超越了之前的SoTA 3.9 F1-score，显示出其在推理步骤正确性评估中的强大能力。

## 🎯 应用场景

Athena-PRM的研究成果可广泛应用于复杂推理任务的自动化评估，如教育领域的智能辅导系统、机器人决策支持系统以及多模态数据分析等。其高效的奖励模型设计将推动相关领域的进一步发展，提升智能系统的推理能力和准确性。

## 📄 摘要（原文）

> We present Athena-PRM, a multimodal process reward model (PRM) designed to evaluate the reward score for each step in solving complex reasoning problems. Developing high-performance PRMs typically demands significant time and financial investment, primarily due to the necessity for step-level annotations of reasoning steps. Conventional automated labeling methods, such as Monte Carlo estimation, often produce noisy labels and incur substantial computational costs. To efficiently generate high-quality process-labeled data, we propose leveraging prediction consistency between weak and strong completers as a criterion for identifying reliable process labels. Remarkably, Athena-PRM demonstrates outstanding effectiveness across various scenarios and benchmarks with just 5,000 samples. Furthermore, we also develop two effective strategies to improve the performance of PRMs: ORM initialization and up-sampling for negative data. We validate our approach in three specific scenarios: verification for test time scaling, direct evaluation of reasoning step correctness, and reward ranked fine-tuning. Our Athena-PRM consistently achieves superior performance across multiple benchmarks and scenarios. Notably, when using Qwen2.5-VL-7B as the policy model, Athena-PRM enhances performance by 10.2 points on WeMath and 7.1 points on MathVista for test time scaling. Furthermore, Athena-PRM sets the state-of-the-art (SoTA) results in VisualProcessBench and outperforms the previous SoTA by 3.9 F1-score, showcasing its robust capability to accurately assess the correctness of the reasoning step. Additionally, utilizing Athena-PRM as the reward model, we develop Athena-7B with reward ranked fine-tuning and outperforms baseline with a significant margin on five benchmarks.

