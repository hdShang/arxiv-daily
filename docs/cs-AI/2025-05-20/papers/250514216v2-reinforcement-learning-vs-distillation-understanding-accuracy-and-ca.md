---
layout: default
title: Reinforcement Learning vs. Distillation: Understanding Accuracy and Capability in LLM Reasoning
---

# Reinforcement Learning vs. Distillation: Understanding Accuracy and Capability in LLM Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14216" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14216v2</a>
  <a href="https://arxiv.org/pdf/2505.14216.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14216v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14216v2', 'Reinforcement Learning vs. Distillation: Understanding Accuracy and Capability in LLM Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Minwu Kim, Anubhav Shrestha, Safal Shrestha, Aadim Nepal, Keith Ross

**分类**: cs.AI, cs.CL

**发布日期**: 2025-05-20 (更新: 2025-10-31)

**备注**: 25 pages

---

## 💡 一句话要点

**探讨RLVR与蒸馏在LLM推理中的准确性与能力差异**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `强化学习` `蒸馏训练` `推理能力` `大型语言模型` `模型优化`

## 📋 核心要点

1. 现有的RLVR方法在推理任务中提升准确性时，往往忽视了对困难问题的处理，导致能力未能提升。
2. 本文通过分析RLVR和蒸馏的机制，提出了对推理能力和准确性的深入理解，强调了新知识引入的重要性。
3. 实验结果显示，RLVR在简单问题上生成了高质量响应，但在困难问题上表现不佳，蒸馏的效果也受到限制。

## 📝 摘要（中文）

近期研究表明，带可验证奖励的强化学习（RLVR）虽然提升了大型语言模型（LLM）的整体准确性（pass@1），但在推理任务中往往未能改善能力（pass@k），而蒸馏则能同时提升二者。本文探讨了这些现象背后的机制，发现RLVR在提升简单问题的准确性时，反而牺牲了对困难问题的准确性。同时，RLVR并未仅仅提高简单问题的成功概率，而是在小模型设置下生成了原输出分布中缺失的高质量响应。此外，蒸馏教师响应到同分布问题的实验表明，蒸馏并不总能提升能力，只有在引入新知识时能力才会改善。综上所述，这些发现为理解RLVR和蒸馏如何塑造LLM的推理行为提供了更清晰的视角。

## 🔬 方法详解

**问题定义**：本文旨在解决RLVR在推理任务中提升准确性但未能改善能力的问题，现有方法在处理困难问题时存在明显不足。

**核心思路**：通过对RLVR和蒸馏的机制进行深入分析，揭示二者在提升LLM推理能力和准确性方面的不同影响，强调新知识引入的重要性。

**技术框架**：研究采用实验对比的方法，分析RLVR与蒸馏在不同问题难度下的表现，主要模块包括模型训练、响应生成和能力评估。

**关键创新**：本文的创新在于揭示了RLVR在提升简单问题准确性时对困难问题的负面影响，并指出蒸馏并不总能提升能力，需引入新知识。

**关键设计**：在实验中，设置了不同难度的问题集，采用了特定的损失函数来评估模型在不同问题上的表现，同时关注生成响应的质量和长度。

## 📊 实验亮点

实验结果表明，RLVR在简单问题上生成的高质量响应并未改善困难问题的表现，且蒸馏在能力提升上并不总有效。具体而言，RLVR的能力提升幅度未能超过基线，显示出在处理复杂推理任务时的局限性。

## 🎯 应用场景

该研究为大型语言模型的训练和优化提供了重要的理论基础，尤其是在推理能力的提升方面。通过理解RLVR与蒸馏的不同机制，研究者可以更有效地设计模型训练策略，应用于教育、客服、内容生成等多个领域，提升智能系统的实际应用效果。

## 📄 摘要（原文）

> Recent studies have shown that reinforcement learning with verifiable rewards (RLVR) enhances overall accuracy (pass@1) but often fails to improve capability (pass@k) of LLMs in reasoning tasks, while distillation can improve both. In this paper, we investigate the mechanisms behind these phenomena. First, we demonstrate that RLVR struggles to improve capability as it focuses on improving the accuracy of the easier questions to the detriment of the accuracy of the most difficult questions. Second, we show that RLVR does not merely increase the success probability for the easier questions, but in our small model settings, produces quality responses that were absent in its original output distribution. In addition, we show these responses are neither noticeably longer nor feature more reflection-related keywords, underscoring the need for more reliable indicators of response quality. Third, from the experiment distilling teacher responses to in-distribution problems, we find that capability does not always improve with distillation. We conjecture that capability improves only when new knowledge is introduced, whereas distilling reasoning patterns only improves accuracy but not capability, sacrificing performance on the most difficult questions, similar to RLVR. Together, these findings offer a clearer understanding of how RLVR and distillation shape reasoning behavior in LLMs

