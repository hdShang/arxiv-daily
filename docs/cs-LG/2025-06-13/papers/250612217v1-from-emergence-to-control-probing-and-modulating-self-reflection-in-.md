---
layout: default
title: "From Emergence to Control: Probing and Modulating Self-Reflection in Language Models"
---

# From Emergence to Control: Probing and Modulating Self-Reflection in Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.12217" class="toolbar-btn" target="_blank">📄 arXiv: 2506.12217v1</a>
  <a href="https://arxiv.org/pdf/2506.12217.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.12217v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.12217v1', 'From Emergence to Control: Probing and Modulating Self-Reflection in Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xudong Zhu, Jiachen Jiang, Mohammad Mahdi Khalili, Zhihui Zhu

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-06-13

**备注**: 18 pages, 9 figures

---

## 💡 一句话要点

**提出反思诱导探测方法以增强语言模型自我反思能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自我反思` `语言模型` `强化学习` `推理能力` `模型内部机制` `性能提升` `计算效率`

## 📋 核心要点

1. 现有方法对自我反思的理解不足，尤其是在预训练模型中的表现较为稀少，限制了其推理能力的提升。
2. 提出反思诱导探测方法，通过将微调模型的反思推理痕迹注入预训练模型，以提高自我反思的频率和能力。
3. 实验结果显示，通过增强自我反思向量，推理性能提升达12%，同时抑制该向量可降低计算成本，提供了灵活的质量与效率平衡机制。

## 📝 摘要（中文）

自我反思是大型语言模型（LLM）重新审视、评估和修正自身推理能力的一种行为，最近通过可验证奖励的强化学习（RLVR）得到了增强。尽管自我反思与推理准确性提高相关，但其起源和机制尚不清楚。本文首先表明，自我反思并非RLVR微调模型所独有，预训练模型中也存在这一能力。为探测这一潜在能力，提出了反思诱导探测方法，通过将微调模型的反思触发推理痕迹注入预训练模型，显著提高了Qwen2.5的自我反思频率。此外，分析内部表示显示，无论是预训练还是微调模型，都保持着能够区分自我反思与非自我反思上下文的隐藏状态。基于此，构建了自我反思向量，通过操控该向量实现对自我反思行为的双向控制，实验表明增强该向量可提升推理性能达12%。

## 🔬 方法详解

**问题定义**：本研究旨在解决自我反思在语言模型中的表现不足，尤其是预训练模型中自我反思能力的稀缺性，现有方法未能充分挖掘这一潜力。

**核心思路**：通过反思诱导探测方法，将微调模型中的反思推理痕迹注入预训练模型，以此提高其自我反思的频率，揭示模型的潜在能力。

**技术框架**：整体流程包括：首先识别微调模型中的反思触发痕迹，然后将这些痕迹注入预训练模型，最后通过构建自我反思向量来实现对反思行为的控制。

**关键创新**：最重要的创新在于发现自我反思不仅限于微调模型，并且通过反思诱导探测方法显著提高了预训练模型的自我反思能力，这是与现有方法的本质区别。

**关键设计**：在设计中，关键参数包括反思触发痕迹的选择和注入方式，损失函数的设计确保了反思向量的有效性，网络结构则需支持对自我反思状态的区分。

## 📊 实验亮点

实验结果表明，通过增强自我反思向量，推理性能提升达12%。同时，抑制该向量能够有效降低计算成本，为在推理质量与效率之间的平衡提供了灵活的解决方案。

## 🎯 应用场景

该研究的潜在应用领域包括智能对话系统、自动化内容生成和教育技术等，能够提升模型在复杂推理任务中的表现，具有重要的实际价值。未来，理解模型内部机制将为更精确的行为控制提供基础，推动AI系统的智能化进程。

## 📄 摘要（原文）

> Self-reflection -- the ability of a large language model (LLM) to revisit, evaluate, and revise its own reasoning -- has recently emerged as a powerful behavior enabled by reinforcement learning with verifiable rewards (RLVR). While self-reflection correlates with improved reasoning accuracy, its origin and underlying mechanisms remain poorly understood. In this work, {\it we first show that self-reflection is not exclusive to RLVR fine-tuned models: it already emerges, albeit rarely, in pretrained models}. To probe this latent ability, we introduce Reflection-Inducing Probing, a method that injects reflection-triggering reasoning traces from fine-tuned models into pretrained models. This intervention raises self-reflection frequency of Qwen2.5 from 0.6\% to 18.6\%, revealing a hidden capacity for reflection. Moreover, our analysis of internal representations shows that both pretrained and fine-tuned models maintain hidden states that distinctly separate self-reflective from non-reflective contexts. Leveraging this observation, {\it we then construct a self-reflection vector, a direction in activation space associated with self-reflective reasoning}. By manipulating this vector, we enable bidirectional control over the self-reflective behavior for both pretrained and fine-tuned models. Experiments across multiple reasoning benchmarks show that enhancing these vectors improves reasoning performance by up to 12\%, while suppressing them reduces computational cost, providing a flexible mechanism to navigate the trade-off between reasoning quality and efficiency without requiring additional training. Our findings further our understanding of self-reflection and support a growing body of work showing that understanding model internals can enable precise behavioral control.

