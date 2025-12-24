---
layout: default
title: "Clone What You Can't Steal: Black-Box LLM Replication via Logit Leakage and Distillation"
---

# Clone What You Can't Steal: Black-Box LLM Replication via Logit Leakage and Distillation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00973" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00973v1</a>
  <a href="https://arxiv.org/pdf/2509.00973.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00973v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00973v1', 'Clone What You Can\'t Steal: Black-Box LLM Replication via Logit Leakage and Distillation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kanchon Gharami, Hansaka Aluvihare, Shafika Showkat Moni, Berker Peköz

**分类**: cs.CR, cs.AI

**发布日期**: 2025-08-31

**备注**: 8 pages. Accepted for publication in the proceedings of 7th IEEE International Conference on Trust, Privacy and Security in Intelligent Systems, and Applications (IEEE TPS 2025)

---

## 💡 一句话要点

**提出黑箱LLM复制方法以应对API安全漏洞**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `黑箱模型` `大型语言模型` `logit泄漏` `模型蒸馏` `API安全` `奇异值分解` `推理速度提升`

## 📋 核心要点

1. 现有方法主要集中在重建输出层或蒸馏表面行为，但在严格查询限制下重建黑箱模型的研究仍然不足。
2. 本文提出了一种受限复制管道，将部分logit泄漏转化为功能性可部署的替代模型，采用两阶段方法进行处理。
3. 实验显示，6层学生模型重现了教师模型的高达97.6%的性能，且在推理速度和参数量上均有显著提升。

## 📝 摘要（中文）

大型语言模型（LLMs）在关键任务系统中的应用日益广泛，但其API的安全性常常不足，可能导致重要信息泄露。本文提出了一种受限复制管道，通过部分logit泄漏生成可部署的替代模型。该方法分为两个阶段：首先通过奇异值分解重建输出投影矩阵，然后将剩余架构蒸馏为紧凑的学生模型。实验结果表明，6层学生模型能够重现97.6%的教师模型隐藏状态几何，且仅增加7.31%的困惑度，展示了在有限查询条件下快速克隆LLM的可能性，强调了加强推理API安全的紧迫性。

## 🔬 方法详解

**问题定义**：本文旨在解决在API安全性不足的情况下，如何在严格查询限制下有效复制黑箱大型语言模型（LLM）。现有方法主要关注输出层重建或表面行为蒸馏，缺乏对黑箱模型的深入复制研究。

**核心思路**：论文提出的核心思路是通过部分logit泄漏，利用奇异值分解（SVD）重建输出投影矩阵，并将剩余的模型架构蒸馏为紧凑的学生模型。这样的设计旨在在有限的查询次数内实现高效的模型复制。

**技术框架**：整体流程分为两个主要阶段：第一阶段，通过收集少于10k的黑箱查询的top-k logits，使用SVD重建输出投影矩阵；第二阶段，利用开源数据集对不同深度的学生模型进行蒸馏训练。

**关键创新**：最重要的技术创新在于提出了一种新的受限复制管道，能够在严格的查询限制下有效重建黑箱模型的输出层，并成功蒸馏出紧凑的学生模型。这与现有方法的本质区别在于其对查询次数的高效利用。

**关键设计**：在实验中，6层学生模型重现了教师模型的97.6%隐藏状态几何，且困惑度仅增加7.31%。此外，4层变体在推理速度上提升了17.1%，参数量减少了18.1%，展示了模型压缩的有效性。

## 📊 实验亮点

实验结果表明，6层学生模型能够重现教师模型的97.6%性能，困惑度仅增加7.31%。4层变体在推理速度上提升17.1%，参数量减少18.1%。整个攻击过程在24小时内完成，且未触发API速率限制，显示出该方法的高效性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括军事决策支持、卫星操作和网络防御等关键任务系统。通过提高API的安全性和防御能力，可以有效降低黑箱模型被复制的风险，从而保护敏感信息和系统安全。未来，该方法可能推动更安全的模型部署和API设计。

## 📄 摘要（原文）

> Large Language Models (LLMs) are increasingly deployed in mission-critical systems, facilitating tasks such as satellite operations, command-and-control, military decision support, and cyber defense. Many of these systems are accessed through application programming interfaces (APIs). When such APIs lack robust access controls, they can expose full or top-k logits, creating a significant and often overlooked attack surface. Prior art has mainly focused on reconstructing the output projection layer or distilling surface-level behaviors. However, regenerating a black-box model under tight query constraints remains underexplored. We address that gap by introducing a constrained replication pipeline that transforms partial logit leakage into a functional deployable substitute model clone. Our two-stage approach (i) reconstructs the output projection matrix by collecting top-k logits from under 10k black-box queries via singular value decomposition (SVD) over the logits, then (ii) distills the remaining architecture into compact student models with varying transformer depths, trained on an open source dataset. A 6-layer student recreates 97.6% of the 6-layer teacher model's hidden-state geometry, with only a 7.31% perplexity increase, and a 7.58 Negative Log-Likelihood (NLL). A 4-layer variant achieves 17.1% faster inference and 18.1% parameter reduction with comparable performance. The entire attack completes in under 24 graphics processing unit (GPU) hours and avoids triggering API rate-limit defenses. These results demonstrate how quickly a cost-limited adversary can clone an LLM, underscoring the urgent need for hardened inference APIs and secure on-premise defense deployments.

