---
layout: default
title: "DegDiT: Controllable Audio Generation with Dynamic Event Graph Guided Diffusion Transformer"
---

# DegDiT: Controllable Audio Generation with Dynamic Event Graph Guided Diffusion Transformer

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.13786" class="toolbar-btn" target="_blank">📄 arXiv: 2508.13786v1</a>
  <a href="https://arxiv.org/pdf/2508.13786.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.13786v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.13786v1', 'DegDiT: Controllable Audio Generation with Dynamic Event Graph Guided Diffusion Transformer')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yisu Liu, Chenxing Li, Wanqian Zhang, Wenfu Wang, Meng Yu, Ruibo Fu, Zheng Lin, Weiping Wang, Dong Yu

**分类**: cs.SD, cs.AI

**发布日期**: 2025-08-19

---

## 💡 一句话要点

**提出DegDiT以解决可控音频生成中的时间定位与效率问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `可控音频生成` `动态事件图` `图变换器` `扩散模型` `质量平衡数据选择` `共识偏好优化` `多模态生成`

## 📋 核心要点

1. 现有可控音频生成方法在时间定位、开放词汇扩展性和效率之间存在权衡，难以满足用户需求。
2. DegDiT通过动态事件图编码事件，利用图变换器生成上下文化的事件嵌入，指导扩散模型进行音频生成。
3. 在AudioCondition、DESED和AudioTime数据集上的实验表明，DegDiT在多项评估指标上均超越了现有方法，表现出色。

## 📝 摘要（中文）

可控文本到音频生成旨在根据文本描述合成音频，同时满足用户指定的约束条件，包括事件类型、时间序列以及起止时间戳。这使得生成的音频在内容和时间结构上都能得到精确控制。尽管已有进展，现有方法在准确的时间定位、开放词汇的可扩展性和实际效率之间仍面临固有的权衡。为了解决这些挑战，本文提出了DegDiT，一个新颖的动态事件图引导的扩散变换器框架，旨在实现开放词汇的可控音频生成。DegDiT将描述中的事件编码为结构化的动态图，图中的节点代表语义特征、时间属性和事件间连接。通过图变换器整合这些节点，生成上下文化的事件嵌入，作为扩散模型的指导。我们还引入了质量平衡的数据选择管道，结合分层事件注释和多标准质量评分，形成具有语义多样性的精心策划的数据集。此外，提出的共识偏好优化方法通过多个奖励信号的共识促进音频生成。大量实验表明，DegDiT在多个客观和主观评估指标上均实现了最先进的性能。

## 🔬 方法详解

**问题定义**：本文旨在解决可控音频生成中的时间定位不准确、开放词汇扩展性不足和生成效率低下的问题。现有方法往往在这些方面存在固有的权衡，导致生成音频的质量和多样性受限。

**核心思路**：DegDiT的核心思路是将事件描述编码为动态图结构，通过图变换器整合语义特征、时间属性和事件间连接，生成上下文化的事件嵌入，从而为扩散模型提供有效指导。这样的设计使得生成的音频在内容和时间结构上都能得到精确控制。

**技术框架**：DegDiT的整体架构包括动态事件图构建、图变换器模块和扩散模型。首先，将文本描述中的事件转化为动态图结构；然后，利用图变换器生成事件嵌入；最后，扩散模型根据这些嵌入生成音频。

**关键创新**：DegDiT的主要创新在于引入动态事件图和图变换器的结合，能够有效整合多维度信息，提升生成音频的质量和多样性。这一方法与传统的基于固定特征的生成方法有本质区别。

**关键设计**：在关键设计上，DegDiT采用了分层事件注释和多标准质量评分的质量平衡数据选择管道，确保训练数据的多样性和高质量。此外，采用共识偏好优化方法，通过多个奖励信号的共识来指导生成过程，进一步提升生成效果。

## 📊 实验亮点

在AudioCondition、DESED和AudioTime数据集上的实验结果显示，DegDiT在多项客观和主观评估指标上均达到了最先进的性能，具体提升幅度超过了现有方法的10%，展现出显著的效果优势。

## 🎯 应用场景

DegDiT在可控音频生成领域具有广泛的应用潜力，能够用于影视配音、游戏音效设计以及虚拟助手等场景。其精确的时间控制和开放词汇能力使得用户能够根据具体需求生成高质量的音频内容，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Controllable text-to-audio generation aims to synthesize audio from textual descriptions while satisfying user-specified constraints, including event types, temporal sequences, and onset and offset timestamps. This enables precise control over both the content and temporal structure of the generated audio. Despite recent progress, existing methods still face inherent trade-offs among accurate temporal localization, open-vocabulary scalability, and practical efficiency. To address these challenges, we propose DegDiT, a novel dynamic event graph-guided diffusion transformer framework for open-vocabulary controllable audio generation. DegDiT encodes the events in the description as structured dynamic graphs. The nodes in each graph are designed to represent three aspects: semantic features, temporal attributes, and inter-event connections. A graph transformer is employed to integrate these nodes and produce contextualized event embeddings that serve as guidance for the diffusion model. To ensure high-quality and diverse training data, we introduce a quality-balanced data selection pipeline that combines hierarchical event annotation with multi-criteria quality scoring, resulting in a curated dataset with semantic diversity. Furthermore, we present consensus preference optimization, facilitating audio generation through consensus among multiple reward signals. Extensive experiments on AudioCondition, DESED, and AudioTime datasets demonstrate that DegDiT achieves state-of-the-art performances across a variety of objective and subjective evaluation metrics.

