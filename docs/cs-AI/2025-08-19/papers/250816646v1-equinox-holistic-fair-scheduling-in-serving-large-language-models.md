---
layout: default
title: "Equinox: Holistic Fair Scheduling in Serving Large Language Models"
---

# Equinox: Holistic Fair Scheduling in Serving Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.16646" class="toolbar-btn" target="_blank">📄 arXiv: 2508.16646v1</a>
  <a href="https://arxiv.org/pdf/2508.16646.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.16646v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.16646v1', 'Equinox: Holistic Fair Scheduling in Serving Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhixiang Wei, James Yen, Jingyi Chen, Ziyang Zhang, Zhibai Huang, Chen Chen, Xingzi Yu, Yicheng Gu, Chenggang Wu, Yun Wang, Mingyuan Xia, Jie Wu, Hao Wang, Zhengwei Qi

**分类**: cs.DC, cs.AI

**发布日期**: 2025-08-19

---

## 💡 一句话要点

**提出Equinox以解决大语言模型服务中的公平调度问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `公平调度` `资源利用` `混合预测专家` `自适应批处理` `GPU利用率` `性能优化`

## 📋 核心要点

1. 当前大语言模型服务面临调度悖论，难以同时满足用户和运营者的公平性需求。
2. 提出双计数器框架和混合预测专家（MoPE）方法，能够预测关键性能指标以实现公平调度。
3. 实验结果显示，Equinox在吞吐量、延迟和公平性方面均显著优于现有方法，且GPU利用率保持高效。

## 📝 摘要（中文）

本文针对当前大语言模型（LLM）服务的局限性，提出了一种双计数器框架，分别从用户和运营者的角度进行分析。用户公平计数器通过加权令牌和延迟来衡量服务质量，而资源公平计数器则通过吞吐量和GPU利用率来评估运营效率。由于这些指标仅在执行后可用，导致调度悖论，本文引入了一种确定性的混合预测专家（MoPE）框架，以预测用户感知的延迟、输出令牌、吞吐量和GPU利用率。这些预测使得能够计算统一的整体公平性评分，从而通过可调参数实现主动的公平感知调度。我们在Equinox中实现了这一框架，并进行了自适应批处理和无停顿调度等优化。对生产轨迹（ShareGPT、LMSYS）和合成工作负载的评估表明，Equinox在吞吐量上提高了1.3倍，首次令牌延迟降低了60%，公平性提高了13%，同时保持94%的GPU利用率，证明了在异构平台上公平性在有限差异下的有效性。

## 🔬 方法详解

**问题定义**：本文旨在解决当前大语言模型服务中的公平调度问题，现有方法在用户体验和资源利用之间存在矛盾，导致调度效率低下。

**核心思路**：通过引入双计数器框架，分别从用户和运营者的角度衡量公平性，并利用混合预测专家（MoPE）框架预测关键性能指标，以实现主动调度。

**技术框架**：整体架构包括用户公平计数器和资源公平计数器，结合MoPE框架进行性能预测，最终计算统一的整体公平性评分，支持调度决策。

**关键创新**：最重要的创新在于引入了双计数器框架和MoPE预测机制，使得调度过程能够在执行前进行公平性评估，避免了传统方法的调度悖论。

**关键设计**：在设计中，设置了可调参数以平衡用户和资源公平性，采用了自适应批处理和无停顿调度策略，确保系统在高负载下仍能保持高效运行。

## 📊 实验亮点

实验结果表明，Equinox在吞吐量上提高了1.3倍，首次令牌延迟降低了60%，公平性提高了13%，同时保持94%的GPU利用率，显著优于基线方法VTC，证明了其在异构平台上的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括大语言模型的在线服务、云计算平台的资源调度以及多用户环境下的公平性保障。通过实现公平调度，能够提升用户体验，优化资源利用，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> We address the limitations of current LLM serving with a dual-counter framework separating user and operator perspectives. The User Fairness Counter measures quality of service via weighted tokens and latency; the Resource Fairness Counter measures operational efficiency through throughput and GPU utilization. Since these metrics are only available post-execution, creating a scheduling paradox, we introduce a deterministic Mixture of Prediction Experts (MoPE) framework to predict user-perceived latency, output tokens, throughput, and GPU utilization. These predictions enable calculation of a unified Holistic Fairness score that balances both counters through tunable parameters for proactive fairness-aware scheduling. We implement this in Equinox, an open-source system with other optimizations like adaptive batching, and stall-free scheduling. Evaluations on production traces (ShareGPT, LMSYS) and synthetic workloads demonstrate Equinox achieves up to $1.3\times$ higher throughput, 60\% lower time-to-first-token latency, and 13\% higher fairness versus VTC while maintaining 94\% GPU utilization, proving fairness under bounded discrepancy across heterogeneous platforms.

