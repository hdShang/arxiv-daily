---
layout: default
title: "Logit-Gap Steering: Efficient Short-Suffix Jailbreaks for Aligned Large Language Models"
---

# Logit-Gap Steering: Efficient Short-Suffix Jailbreaks for Aligned Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.24056" class="toolbar-btn" target="_blank">📄 arXiv: 2506.24056v1</a>
  <a href="https://arxiv.org/pdf/2506.24056.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.24056v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.24056v1', 'Logit-Gap Steering: Efficient Short-Suffix Jailbreaks for Aligned Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tung-Ling Li, Hongliang Liu

**分类**: cs.CR, cs.CL, cs.LG

**发布日期**: 2025-06-30

---

## 💡 一句话要点

**提出Logit-Gap Steering以高效破解对齐的大型语言模型**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `对齐` `破解方法` `安全性测试` `自然语言处理`

## 📋 核心要点

1. 现有的破解方法在效率和成功率上存在不足，尤其是在处理对齐的大型语言模型时，调用次数过多且成功率不高。
2. 本文提出的Logit-Gap Steering框架通过一次性遍历词汇表来优化拒绝-确认差距，显著提高了破解效率。
3. 实验结果表明，该方法在多种检查点上成功率提升至80-100%，且调用次数减少两个数量级，保持了主题一致性。

## 📝 摘要（中文）

本文介绍了一种快速的破解框架——Logit-Gap Steering，它将RLHF对齐语言模型的拒绝-确认差距视为对词汇表的单次遍历。通过前向可计算的评分，该方法将差距缩减与KL惩罚和奖励转移的轻量级代理相结合，使得“排序-求和-停止”的过程在一秒内完成，并返回一个短后缀——相比于束搜索或梯度攻击，模型调用次数减少两个数量级。该后缀在未见提示上具有良好的泛化能力，并且在从0.5B到70B的检查点上均能提升一次性攻击成功率至80-100%，同时保持主题一致性。除了效率，这些后缀还揭示了句子边界奖励悬崖和其他对齐伪影，为安全调优如何重塑内部表示提供了轻量级探测手段。

## 🔬 方法详解

**问题定义**：本文旨在解决现有破解方法在对齐大型语言模型时效率低下和成功率不足的问题。现有方法通常需要多次调用模型，导致时间和资源的浪费。

**核心思路**：Logit-Gap Steering的核心思路是将拒绝-确认差距转化为对词汇表的单次遍历，通过前向可计算的评分机制来优化这一过程，从而实现快速且高效的破解。

**技术框架**：该方法的整体架构包括三个主要阶段：首先计算拒绝-确认差距的评分，其次结合KL惩罚和奖励转移的轻量级代理，最后进行“排序-求和-停止”的操作，以快速返回短后缀。

**关键创新**：最重要的技术创新在于通过前向可计算的评分机制实现了对拒绝-确认差距的快速优化，与传统方法相比，显著减少了模型调用次数并提高了成功率。

**关键设计**：在设计上，采用了轻量级的KL惩罚和奖励转移代理，确保了评分的高效计算，同时在参数设置上进行了优化，以适应从0.5B到70B的不同模型检查点。

## 📊 实验亮点

实验结果显示，Logit-Gap Steering方法在多个检查点上实现了80-100%的攻击成功率，相比于基线方法，模型调用次数减少了两个数量级，显著提升了效率和效果。

## 🎯 应用场景

该研究的潜在应用领域包括对大型语言模型的安全性测试、模型对齐的评估以及自然语言处理中的对抗攻击研究。通过高效的破解方法，研究人员可以更好地理解模型的内部机制和安全性，从而为未来的模型设计提供指导。

## 📄 摘要（原文）

> We introduce logit-gap steering, a fast jailbreak framework that casts the refusal-affirmation gap of RLHF-aligned language models as a single pass over the vocabulary. A forward-computable score blends gap reduction with lightweight proxies for KL penalty and reward shift, allowing a "sort-sum-stop" sweep to complete in under a second and return a short suffix--two orders of magnitude fewer model calls than beam or gradient attacks. The same suffix generalises to unseen prompts and scales from 0.5 B to 70 B checkpoints, lifting one-shot attack success from baseline levels to 80-100% while preserving topical coherence. Beyond efficiency, these suffixes expose sentence-boundary reward cliffs and other alignment artefacts, offering a lightweight probe into how safety tuning reshapes internal representations.

