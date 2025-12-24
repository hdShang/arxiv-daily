---
layout: default
title: Semi-Clairvoyant Scheduling of Speculative Decoding Requests to Minimize LLM Inference Latency
---

# Semi-Clairvoyant Scheduling of Speculative Decoding Requests to Minimize LLM Inference Latency

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.17074" class="toolbar-btn" target="_blank">📄 arXiv: 2505.17074v1</a>
  <a href="https://arxiv.org/pdf/2505.17074.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.17074v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.17074v1', 'Semi-Clairvoyant Scheduling of Speculative Decoding Requests to Minimize LLM Inference Latency')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ruixiao Li, Fahao Chen, Peng Li

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-05-20

---

## 💡 一句话要点

**提出LAPS-SD以解决LLM推理延迟问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `推理延迟` `请求调度` `动态优先级队列` `半预知算法` `令牌接受率` `实验结果`

## 📋 核心要点

1. 现有的推理请求调度方法主要依赖于预测输出长度来估计执行时间，导致在动态环境下调度效率低下。
2. LAPS-SD算法通过动态维护多个优先级队列和请求执行抢占，能够根据请求特征自适应调度，从而降低推理延迟。
3. 实验结果显示，LAPS-SD在推理延迟方面相比于最先进的调度方法有显著提升，减少了约39%的延迟。

## 📝 摘要（中文）

论文提出了一种名为Least-Attained/Perceived-Service for Speculative Decoding（LAPS-SD）的半预知请求调度算法，旨在通过动态调度推理请求来降低大型语言模型（LLM）的推理延迟。现有方法仅基于预测的输出长度来估计执行时间，导致调度效率低下。LAPS-SD通过维护多个优先级队列并允许跨队列的请求执行抢占，能够在动态的令牌接受率下有效调度请求。实验结果表明，LAPS-SD相比于现有的调度方法，推理延迟减少了约39%。

## 🔬 方法详解

**问题定义**：论文要解决的问题是如何在大型语言模型推理中有效调度请求，以应对推理时间的不确定性。现有方法仅依赖于输出长度来估计执行时间，无法准确反映实际情况。

**核心思路**：LAPS-SD的核心思路是通过维护多个优先级队列和允许请求抢占，动态适应请求特征，从而在推理过程中有效降低延迟。这样的设计使得算法能够在令牌接受率动态变化时仍然保持高效调度。

**技术框架**：LAPS-SD的整体架构包括多个优先级队列、请求调度模块和令牌验证模块。请求根据特征被分配到不同的队列中，调度模块根据当前的令牌接受率动态调整请求的执行顺序。

**关键创新**：LAPS-SD的关键创新在于其半预知调度策略，能够在令牌接受率不稳定时进行有效的请求调度，显著提高了推理效率。这与传统方法的静态调度形成了鲜明对比。

**关键设计**：在设计中，LAPS-SD采用了动态优先级队列和请求抢占机制，确保在令牌接受率稳定后能够准确估计执行时间。此外，算法的参数设置和队列管理策略也经过精心设计，以优化整体性能。

## 📊 实验亮点

实验结果表明，LAPS-SD相比于最先进的调度方法，推理延迟减少了约39%。这一显著的性能提升展示了LAPS-SD在动态调度环境中的有效性，验证了其在实际应用中的潜力。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、对话系统和实时文本生成等场景。通过降低推理延迟，LAPS-SD能够提升用户体验，尤其是在需要快速响应的应用中，具有显著的实际价值和影响力。

## 📄 摘要（原文）

> Speculative decoding accelerates Large Language Model (LLM) inference by employing a small speculative model (SSM) to generate multiple candidate tokens and verify them using the LLM in parallel. This technique has been widely integrated into LLM inference serving systems. However, inference requests typically exhibit uncertain execution time, which poses a significant challenge of efficiently scheduling requests in these systems. Existing work estimates execution time based solely on predicted output length, which could be inaccurate because execution time depends on both output length and token acceptance rate of verification by the LLM. In this paper, we propose a semi-clairvoyant request scheduling algorithm called Least-Attained/Perceived-Service for Speculative Decoding (LAPS-SD). Given a number of inference requests, LAPS-SD can effectively minimize average inference latency by adaptively scheduling requests according to their features during decoding. When the token acceptance rate is dynamic and execution time is difficult to estimate, LAPS-SD maintains multiple priority queues and allows request execution preemption across different queues. Once the token acceptance rate becomes stable, LAPS-SD can accurately estimate the execution time and schedule requests accordingly. Extensive experiments show that LAPS-SD reduces inference latency by approximately 39\% compared to state-of-the-art scheduling methods.

