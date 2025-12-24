---
layout: default
title: "Aux-Think: Exploring Reasoning Strategies for Data-Efficient Vision-Language Navigation"
---

# Aux-Think: Exploring Reasoning Strategies for Data-Efficient Vision-Language Navigation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.11886" class="toolbar-btn" target="_blank">📄 arXiv: 2505.11886v4</a>
  <a href="https://arxiv.org/pdf/2505.11886.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.11886v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.11886v4', 'Aux-Think: Exploring Reasoning Strategies for Data-Efficient Vision-Language Navigation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shuo Wang, Yongcai Wang, Wanting Li, Xudong Cai, Yucheng Wang, Maiyue Chen, Kaihui Wang, Zhizhong Su, Deying Li, Zhaoxin Fan

**分类**: cs.RO

**发布日期**: 2025-05-17 (更新: 2025-10-14)

**期刊**: NeurIPS 2025

---

## 💡 一句话要点

**提出Aux-Think以解决视觉语言导航中的推理策略问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言导航` `推理策略` `链式思维` `多模态学习` `智能体导航`

## 📋 核心要点

1. 现有的视觉语言导航方法在推理策略的应用上存在不足，尤其是在长时间任务中，推理的有效性未得到充分验证。
2. 本文提出Aux-Think框架，通过链式思维监督训练模型，使其在推理过程中更高效，同时在在线预测中直接进行动作推断。
3. 实验结果显示，Aux-Think在相同数据规模下显著提升了导航性能，并减少了训练所需的工作量。

## 📝 摘要（中文）

视觉语言导航（VLN）是开发能够根据自然语言指令在复杂现实环境中导航的具身智能体的重要任务。尽管大型预训练模型在VLN中显著提高了泛化能力和指令基础，但推理策略在导航这一以动作为中心的长期任务中的作用仍未得到充分探索。为此，本文首次系统评估了VLN中的推理策略，包括直接动作预测、动作前推理和动作后推理。研究发现推理时间的推理崩溃问题，表明将推理整合到VLN中的挑战。基于此，我们提出了Aux-Think框架，通过链式思维监督训练模型内化结构化推理模式，同时在在线预测中直接推断动作。为支持该框架，我们发布了首个链式思维注释数据集R2R-CoT-320k。实验表明，Aux-Think大幅减少训练工作量，并在相同数据规模下实现最佳性能。

## 🔬 方法详解

**问题定义**：本文旨在解决视觉语言导航中推理策略的不足，尤其是推理时间的推理崩溃问题，这影响了导航的准确性。现有方法在长时间任务中未能有效整合推理能力。

**核心思路**：Aux-Think框架的核心思想是通过链式思维监督训练模型，使其能够内化结构化的推理模式，同时在实际推断中直接进行动作预测，避免推理过程对实时性能的影响。

**技术框架**：该框架包括三个主要模块：推理策略评估、链式思维监督训练和在线动作推断。首先评估不同推理策略的效果，然后通过监督学习优化模型，最后在推断阶段直接生成动作。

**关键创新**：最重要的创新点在于提出了Aux-Think框架，结合了推理策略与直接动作预测的优势，解决了推理时间崩溃的问题，与传统方法相比具有本质区别。

**关键设计**：在模型设计中，采用了链式思维的损失函数来指导推理过程，并在网络结构上进行了优化，以适应长时间任务的需求。

## 📊 实验亮点

实验结果表明，Aux-Think在相同数据规模下显著提升了导航性能，具体表现为在多个基准测试中超越了现有最佳模型，减少了训练时间和资源消耗，展示了其在视觉语言导航中的有效性。

## 🎯 应用场景

该研究的潜在应用场景包括智能机器人、自动驾驶系统以及虚拟助手等领域，能够提升这些系统在复杂环境中的导航能力和响应效率。未来，Aux-Think框架可能推动更高效的多模态交互和智能体自主学习的研究进展。

## 📄 摘要（原文）

> Vision-Language Navigation (VLN) is a critical task for developing embodied agents that can follow natural language instructions to navigate in complex real-world environments. Recent advances in VLN by large pretrained models have significantly improved generalization and instruction grounding compared to traditional approaches. However, the role of reasoning strategies in navigation-an action-centric, long-horizon task-remains underexplored, despite Chain-of-Thought (CoT) reasoning's demonstrated success in static tasks like visual question answering. To address this gap, we conduct the first systematic evaluation of reasoning strategies for VLN, including No-Think (direct action prediction), Pre-Think (reason before action), and Post-Think (reason after action). Surprisingly, our findings reveal the Inference-time Reasoning Collapse issue, where inference-time reasoning degrades navigation accuracy, highlighting the challenges of integrating reasoning into VLN. Based on this insight, we propose Aux-Think, a framework that trains models to internalize structured reasoning patterns through CoT supervision, while inferring action directly without reasoning in online prediction. To support this framework, we release R2R-CoT-320k, the first Chain-of-Thought annotated dataset for VLN. Extensive experiments show that Aux-Think reduces training effort greatly and achieves the best performance under the same data scale.

