---
layout: default
title: SeqPO-SiMT: Sequential Policy Optimization for Simultaneous Machine Translation
---

# SeqPO-SiMT: Sequential Policy Optimization for Simultaneous Machine Translation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20622" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20622v1</a>
  <a href="https://arxiv.org/pdf/2505.20622.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20622v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20622v1', 'SeqPO-SiMT: Sequential Policy Optimization for Simultaneous Machine Translation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ting Xu, Zhichao Huang, Jiankai Sun, Shanbo Cheng, Wai Lam

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-05-27

**备注**: Accepted by The 63rd Annual Meeting of the Association for Computational Linguistics (ACL 2025)

---

## 💡 一句话要点

**提出SeqPO-SiMT以解决同步机器翻译中的延迟与质量问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `同步机器翻译` `序列决策` `强化学习` `翻译质量` `延迟优化` `定制奖励` `多步任务`

## 📋 核心要点

1. 现有的同步机器翻译方法在处理多步决策时面临延迟和翻译质量的挑战，尤其是在实时翻译场景中。
2. SeqPO-SiMT将同步机器翻译视为序列决策问题，通过定制奖励机制来优化翻译过程，提升翻译质量并降低延迟。
3. 实验结果显示，SeqPO-SiMT在多个数据集上均表现优异，翻译质量显著高于监督微调模型，同时减少了翻译延迟。

## 📝 摘要（中文）

我们提出了同步机器翻译的序列策略优化框架（SeqPO-SiMT），将同步机器翻译任务定义为一个序列决策问题，结合定制奖励以提高翻译质量并降低延迟。与通常应用于单步任务的强化学习方法（如PPO和DPO）不同，SeqPO-SiMT有效地处理多步的同步机器翻译任务。该框架使得同步机器翻译的语言模型能够模拟和优化翻译过程。我们在六个不同领域的数据集上进行了实验，结果表明SeqPO-SiMT在翻译质量和延迟方面均显著优于现有方法，特别是在NEWSTEST2021数据集中，SeqPO-SiMT在COMET指标上比监督微调模型高出1.13分，同时平均延迟减少了6.17。

## 🔬 方法详解

**问题定义**：本论文旨在解决同步机器翻译（SiMT）中延迟与翻译质量之间的矛盾。现有方法多依赖于单步决策，难以有效处理多步翻译任务，导致翻译质量不稳定且延迟较高。

**核心思路**：SeqPO-SiMT通过将SiMT任务建模为序列决策问题，利用定制奖励机制来优化翻译过程，允许模型在翻译过程中进行自我调整，从而提高翻译质量并降低延迟。

**技术框架**：该框架包括多个模块，首先是输入处理模块，将源语言文本转换为模型可理解的格式；接着是决策模块，基于当前上下文生成翻译；最后是奖励评估模块，根据定制奖励反馈调整翻译策略。

**关键创新**：SeqPO-SiMT的主要创新在于其将同步机器翻译任务视为多步决策问题，采用定制奖励机制，显著提升了模型在实时翻译中的表现，与传统的单步强化学习方法形成鲜明对比。

**关键设计**：在设计上，SeqPO-SiMT使用了特定的损失函数来优化翻译质量，并在网络结构上进行了调整，以适应多步决策的需求，确保模型在处理上下文时的有效性。具体参数设置和网络结构细节在实验部分进行了详细描述。

## 📊 实验亮点

实验结果表明，SeqPO-SiMT在多个数据集上均显著优于现有的监督微调模型，具体而言，在NEWSTEST2021数据集中，SeqPO-SiMT在COMET指标上提高了1.13分，同时平均延迟减少了6.17，展示了其在翻译质量和效率上的双重优势。

## 🎯 应用场景

该研究的潜在应用领域包括实时翻译、在线客服和多语言交流平台等。通过提高翻译质量和降低延迟，SeqPO-SiMT能够显著提升用户体验，推动跨语言沟通的效率。此外，该方法的创新思路也为其他需要实时决策的任务提供了借鉴。

## 📄 摘要（原文）

> We present Sequential Policy Optimization for Simultaneous Machine Translation (SeqPO-SiMT), a new policy optimization framework that defines the simultaneous machine translation (SiMT) task as a sequential decision making problem, incorporating a tailored reward to enhance translation quality while reducing latency. In contrast to popular Reinforcement Learning from Human Feedback (RLHF) methods, such as PPO and DPO, which are typically applied in single-step tasks, SeqPO-SiMT effectively tackles the multi-step SiMT task. This intuitive framework allows the SiMT LLMs to simulate and refine the SiMT process using a tailored reward. We conduct experiments on six datasets from diverse domains for En to Zh and Zh to En SiMT tasks, demonstrating that SeqPO-SiMT consistently achieves significantly higher translation quality with lower latency. In particular, SeqPO-SiMT outperforms the supervised fine-tuning (SFT) model by 1.13 points in COMET, while reducing the Average Lagging by 6.17 in the NEWSTEST2021 En to Zh dataset. While SiMT operates with far less context than offline translation, the SiMT results of SeqPO-SiMT on 7B LLM surprisingly rival the offline translation of high-performing LLMs, including Qwen-2.5-7B-Instruct and LLaMA-3-8B-Instruct.

