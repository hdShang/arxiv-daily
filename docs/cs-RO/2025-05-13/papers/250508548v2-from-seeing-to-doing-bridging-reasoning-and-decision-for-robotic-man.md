---
layout: default
title: "From Seeing to Doing: Bridging Reasoning and Decision for Robotic Manipulation"
---

# From Seeing to Doing: Bridging Reasoning and Decision for Robotic Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.08548" class="toolbar-btn" target="_blank">📄 arXiv: 2505.08548v2</a>
  <a href="https://arxiv.org/pdf/2505.08548.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.08548v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.08548v2', 'From Seeing to Doing: Bridging Reasoning and Decision for Robotic Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yifu Yuan, Haiqin Cui, Yibin Chen, Zibin Dong, Fei Ni, Longxin Kou, Jinyi Liu, Pengyi Li, Yan Zheng, Jianye Hao

**分类**: cs.RO, cs.AI, cs.LG

**发布日期**: 2025-05-13 (更新: 2025-05-27)

**备注**: Our project homepage: https://embodied-fsd.github.io/

---

## 💡 一句话要点

**提出FSD模型以解决机器人操作中的零-shot泛化问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱七：动作重定向 (Motion Retargeting)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器人操作` `视觉-语言模型` `空间关系推理` `零-shot学习` `泛化能力` `自一致性机制` `层次化数据处理` `多模态融合`

## 📋 核心要点

1. 现有的视觉-语言-动作模型在面对未见场景和新任务时，零-shot性能不足，难以实现泛化。
2. 本文提出FSD模型，通过空间关系推理生成中间表示，提供细粒度的操作指导，从而提升机器人操作能力。
3. 实验结果表明，FSD在SimplerEnv中成功率达到40.6%，在8个真实任务中达到72%，相较于最强基线提升30%。

## 📝 摘要（中文）

在机器人操作中，实现泛化能力仍然是一个关键挑战，尤其是在未见场景和新任务中。现有的视觉-语言-动作（VLA）模型虽然基于通用的视觉-语言模型（VLMs），但由于具身数据集中存在的稀缺性和异质性，导致其零-shot性能不足。为了解决这些局限性，本文提出了FSD（From Seeing to Doing），一种新颖的视觉-语言模型，通过空间关系推理生成中间表示，为机器人操作提供细粒度指导。通过大量实验，我们验证了FSD在“看”和“做”方面的能力，在8个基准测试中表现出色，并在我们提出的更具挑战性的基准VABench上也取得了良好结果。我们还验证了在机器人操作中的零-shot能力，在SimplerEnv和真实机器人环境中显著提升了性能。

## 🔬 方法详解

**问题定义**：本文旨在解决机器人操作中的零-shot泛化能力不足的问题。现有方法在面对新任务和未见场景时，往往无法有效执行操作，导致性能下降。

**核心思路**：FSD模型的核心思路是通过空间关系推理生成中间表示，从而为机器人操作提供细粒度的指导。这种设计旨在增强模型对复杂场景的理解和操作能力。

**技术框架**：FSD的整体架构包括一个层次化的数据处理管道和自一致性机制。数据处理管道负责训练数据的准备和处理，自一致性机制则确保空间坐标与视觉信号的对齐。

**关键创新**：FSD的主要创新在于其通过空间关系推理生成中间表示的能力，这与现有方法的直接映射方式有本质区别，能够更好地处理复杂的操作任务。

**关键设计**：在模型设计中，FSD采用了特定的损失函数来优化空间关系的推理，同时在网络结构上引入了层次化模块，以增强模型的表达能力和泛化能力。

## 📊 实验亮点

FSD模型在多个基准测试中表现出色，在SimplerEnv中成功率达到40.6%，在8个真实任务中成功率达到72%。相较于最强基线，FSD的性能提升幅度达30%，显示出其在零-shot机器人操作中的显著优势。

## 🎯 应用场景

该研究的潜在应用领域包括智能家居、工业自动化和服务机器人等。通过提升机器人在复杂环境中的操作能力，FSD模型能够在实际应用中实现更高的灵活性和效率，推动机器人技术的进一步发展。

## 📄 摘要（原文）

> Achieving generalization in robotic manipulation remains a critical challenge, particularly for unseen scenarios and novel tasks. Current Vision-Language-Action (VLA) models, while building on top of general Vision-Language Models (VLMs), still fall short of achieving robust zero-shot performance due to the scarcity and heterogeneity prevalent in embodied datasets. To address these limitations, we propose FSD (From Seeing to Doing), a novel vision-language model that generates intermediate representations through spatial relationship reasoning, providing fine-grained guidance for robotic manipulation. Our approach combines a hierarchical data pipeline for training with a self-consistency mechanism that aligns spatial coordinates with visual signals. Through extensive experiments, we comprehensively validated FSD's capabilities in both "seeing" and "doing," achieving outstanding performance across 8 benchmarks for general spatial reasoning and embodied reference abilities, as well as on our proposed more challenging benchmark VABench. We also verified zero-shot capabilities in robot manipulation, demonstrating significant performance improvements over baseline methods in both SimplerEnv and real robot settings. Experimental results show that FSD achieves 40.6% success rate in SimplerEnv and 72% success rate across 8 real-world tasks, outperforming the strongest baseline by 30%.

