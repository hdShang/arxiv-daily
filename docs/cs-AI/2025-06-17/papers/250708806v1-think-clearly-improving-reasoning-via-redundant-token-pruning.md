---
layout: default
title: "Think Clearly: Improving Reasoning via Redundant Token Pruning"
---

# Think Clearly: Improving Reasoning via Redundant Token Pruning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2507.08806" class="toolbar-btn" target="_blank">📄 arXiv: 2507.08806v1</a>
  <a href="https://arxiv.org/pdf/2507.08806.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2507.08806v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2507.08806v1', 'Think Clearly: Improving Reasoning via Redundant Token Pruning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Daewon Choi, Jimin Lee, Jihoon Tack, Woomin Song, Saket Dingliwal, Sai Muralidhar Jayanthi, Bhavana Ganesh, Jinwoo Shin, Aram Galstyan, Sravan Babu Bodapati

**分类**: cs.AI, cs.CL, cs.LG

**发布日期**: 2025-06-17

---

## 💡 一句话要点

**通过冗余标记修剪提升推理能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `推理能力` `冗余修剪` `注意力机制` `大型语言模型` `数学竞赛` `结构感知`

## 📋 核心要点

1. 现有大型语言模型在推理过程中存在显著的冗余，导致注意力分散，影响最终答案的准确性。
2. 论文提出通过冗余标记修剪的方法，系统识别并去除推理过程中的冗余，以提升推理清晰度和准确性。
3. 实验结果显示，该方法在多个推理密集型基准测试中显著提高了准确性，尤其在数学竞赛基准上表现优异。

## 📝 摘要（中文）

近年来，大型语言模型在长篇推理方面展现出良好的能力，能够遵循结构化的思维链条得出最终答案。然而，研究发现这些推理路径往往存在显著的冗余，尤其在错误答案中，注意力分布较为分散。本文提出通过系统性地识别并去除推理过程中的冗余，显著提升推理性能。具体而言，作者通过测量与特殊的思维结束标记的标记级注意力分数，识别推理冗余，并提出结构感知修剪方法，优先去除低贡献的推理块中的标记。经过冗余标记的剔除，恢复推理生成，实验结果表明该方法在推理密集型基准测试中显著提高了整体准确性，尤其在数学竞赛基准如AIME和AMC中表现突出。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在推理过程中存在的冗余问题，现有方法在处理复杂推理时，注意力分布不均，导致错误答案的产生。

**核心思路**：通过系统性地识别和去除推理过程中的冗余标记，提升推理的清晰度和准确性。具体方法是测量与特殊的思维结束标记的注意力分数，识别出冗余部分。

**技术框架**：整体流程包括三个主要阶段：首先，插入思维结束标记以收集注意力分数；其次，基于注意力分数识别冗余标记并进行修剪；最后，去除思维结束标记，恢复推理生成。

**关键创新**：论文的创新在于提出了结构感知修剪方法，优先去除低贡献的推理块中的标记，而非单个标记，从而更有效地提升推理质量。

**关键设计**：在技术细节上，论文设计了特定的注意力分数计算方法，并通过实验验证了不同标记的贡献度，以指导冗余标记的去除。

## 📊 实验亮点

实验结果表明，采用冗余标记修剪方法后，模型在AIME和AMC等数学竞赛基准测试中准确率显著提升，具体提升幅度达到X%（具体数据待补充），显示出该方法在处理复杂推理任务中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括教育、自动化推理系统和复杂问题求解等。通过提升推理能力，能够在数学、科学等领域的智能辅导和决策支持中发挥重要作用，未来可能推动更高效的智能助手和自动化工具的发展。

## 📄 摘要（原文）

> Recent large language models have shown promising capabilities in long-form reasoning, following structured chains of thought before arriving at a final answer. However, we observe that these reasoning paths tend to include substantial redundancy; analyzing attention patterns reveals that attention scores are widely scattered, particularly incorrect answers exhibit greater attention sparsity. In this paper, we demonstrate that deliberately removing this redundancy in the reasoning process significantly improves performance through clear thinking, i.e., removing distraction. Specifically, we systematically identify reasoning redundancy by measuring token-level attention scores to a special end-of-thinking token, which is appended to an explicit instruction inserted to conclude each intermediate reasoning step. Furthermore, we propose structure-aware pruning that prioritizes removing tokens in low-contributing reasoning chunks over individual tokens. After evicting redundant tokens, we remove the injected end-of-thinking instruction, then resume the reasoning generation. We demonstrate that our method significantly improves overall accuracy across reasoning-intensive benchmarks without any training involved. In particular, our method shows strong performance on challenging mathematical competition benchmarks such as AIME and AMC, where reasoning redundancy is more prevalent.

