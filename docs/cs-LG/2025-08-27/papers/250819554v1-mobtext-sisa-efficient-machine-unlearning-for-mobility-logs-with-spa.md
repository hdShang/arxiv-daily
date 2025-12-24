---
layout: default
title: "MobText-SISA: Efficient Machine Unlearning for Mobility Logs with Spatio-Temporal and Natural-Language Data"
---

# MobText-SISA: Efficient Machine Unlearning for Mobility Logs with Spatio-Temporal and Natural-Language Data

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.19554" class="toolbar-btn" target="_blank">📄 arXiv: 2508.19554v1</a>
  <a href="https://arxiv.org/pdf/2508.19554.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.19554v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.19554v1', 'MobText-SISA: Efficient Machine Unlearning for Mobility Logs with Spatio-Temporal and Natural-Language Data')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haruki Yonekura, Ren Ozeki, Tatsuya Amano, Hamada Rizk, Hirozumi Yamaguchi

**分类**: cs.LG

**发布日期**: 2025-08-27

**备注**: Accepted to The 33rd ACM International Conference on Advances in Geographic Information Systems(SIGSPATIAL '25) as a short paper in the Short Paper Track

---

## 💡 一句话要点

**提出MobText-SISA以解决移动日志中的机器遗忘问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器遗忘` `隐私合规` `时空数据` `聚类方法` `增量训练` `多模态分析` `移动平台`

## 📋 核心要点

1. 现有方法在处理移动日志时，无法有效应对用户的删除请求，导致隐私合规性问题。
2. MobText-SISA通过将时空数据嵌入共享潜在空间，并采用相似性感知聚类，优化了机器遗忘的过程。
3. 实验结果显示，MobText-SISA在保持预测准确性的同时，显著提高了删除请求的处理效率。

## 📝 摘要（中文）

现代移动平台存储了大量的GPS轨迹、时间元数据、自由格式文本笔记等非结构化数据。根据GDPR等隐私法规，用户可以随时要求删除其贡献，但从头开始重新训练深度模型的做法不可行。本文提出MobText-SISA，一个可扩展的机器遗忘框架，扩展了分片、隔离、切片和聚合（SISA）训练方法，以处理异构的时空数据。MobText-SISA首先将每次出行的数值和语言特征嵌入共享的潜在空间，然后采用相似性感知聚类将样本分配到不同的分片中，以便未来的删除仅影响单个组成模型，同时保持跨分片的多样性。每个分片以增量方式训练；在推理时，聚合各组成模型的预测结果以生成输出。实验表明，MobText-SISA能够保持基线预测准确性，并在误差和收敛速度上持续优于随机分片。

## 🔬 方法详解

**问题定义**：本文旨在解决在移动日志中实现机器遗忘的具体问题。现有方法在用户请求删除其数据时，通常需要从头重新训练模型，效率低下且不符合隐私法规要求。

**核心思路**：MobText-SISA的核心思路是通过将每次出行的数值和语言特征嵌入共享的潜在空间，并使用相似性感知聚类来优化数据分片，从而在删除请求时仅需重训练受影响的分片。

**技术框架**：MobText-SISA的整体架构包括数据嵌入、相似性感知聚类、分片训练和预测聚合四个主要模块。首先，数据被嵌入到共享潜在空间中，然后通过聚类将样本分配到不同的分片中，最后在推理时聚合各分片的预测结果。

**关键创新**：MobText-SISA的主要创新在于其相似性感知聚类方法，使得未来的删除请求仅影响单个分片，从而提高了机器遗忘的效率和准确性。这与传统方法需要全局重训练的方式形成鲜明对比。

**关键设计**：在设计中，MobText-SISA采用了增量训练策略，确保每个分片从上一个有效检查点开始重训练。此外，聚合预测时采用加权平均的方法，以提高最终输出的准确性。具体的损失函数和网络结构细节在论文中有详细描述。

## 📊 实验亮点

实验结果表明，MobText-SISA在处理删除请求时，能够保持基线预测准确性，并在误差和收敛速度上相较于随机分片方法有显著提升，具体表现为误差降低和收敛速度加快，验证了其在实际应用中的有效性。

## 🎯 应用场景

MobText-SISA的研究成果在城市规模的多模态移动数据分析中具有广泛的应用潜力。它可以帮助移动平台在满足隐私法规的同时，继续提供个性化服务和数据分析，提升用户体验。未来，该框架还可扩展到其他领域，如智能交通、城市规划等。

## 📄 摘要（原文）

> Modern mobility platforms have stored vast streams of GPS trajectories, temporal metadata, free-form textual notes, and other unstructured data. Privacy statutes such as the GDPR require that any individual's contribution be unlearned on demand, yet retraining deep models from scratch for every request is untenable. We introduce MobText-SISA, a scalable machine-unlearning framework that extends Sharded, Isolated, Sliced, and Aggregated (SISA) training to heterogeneous spatio-temporal data. MobText-SISA first embeds each trip's numerical and linguistic features into a shared latent space, then employs similarity-aware clustering to distribute samples across shards so that future deletions touch only a single constituent model while preserving inter-shard diversity. Each shard is trained incrementally; at inference time, constituent predictions are aggregated to yield the output. Deletion requests trigger retraining solely of the affected shard from its last valid checkpoint, guaranteeing exact unlearning. Experiments on a ten-month real-world mobility log demonstrate that MobText-SISA (i) sustains baseline predictive accuracy, and (ii) consistently outperforms random sharding in both error and convergence speed. These results establish MobText-SISA as a practical foundation for privacy-compliant analytics on multimodal mobility data at urban scale.

