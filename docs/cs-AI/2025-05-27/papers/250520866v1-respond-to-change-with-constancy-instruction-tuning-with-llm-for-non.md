---
layout: default
title: Respond to Change with Constancy: Instruction-tuning with LLM for Non-I.I.D. Network Traffic Classification
---

# Respond to Change with Constancy: Instruction-tuning with LLM for Non-I.I.D. Network Traffic Classification

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20866" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20866v1</a>
  <a href="https://arxiv.org/pdf/2505.20866.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20866v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20866v1', 'Respond to Change with Constancy: Instruction-tuning with LLM for Non-I.I.D. Network Traffic Classification')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xinjie Lin, Gang Xiong, Gaopeng Gou, Wenqi Dong, Jing Yu, Zhen Li, Wei Xia

**分类**: cs.CR, cs.AI, cs.NI

**发布日期**: 2025-05-27

**备注**: IEEE Transactions on Information Forensics and Security (TIFS) camera ready, 15 pages, 6 figures, 7 tables

**DOI**: [10.1109/TIFS.2025.3574971](https://doi.org/10.1109/TIFS.2025.3574971)

---

## 💡 一句话要点

**提出ETooL以解决非独立同分布网络流量分类问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `加密流量分类` `大语言模型` `自监督学习` `网络安全` `流量分析` `非独立同分布` `指令调优`

## 📋 核心要点

1. 现有加密流量分类方法面临分布漂移和对标注数据依赖的问题，限制了其在真实场景中的应用。
2. 本文提出ETooL模型，通过自监督指令调优将LLM与流量结构知识结合，增强流量分类能力。
3. ETooL在多个数据集上显著提升了F1分数，尤其在非独立同分布情况下表现优异，验证了其有效性。

## 📝 摘要（中文）

加密流量分类在网络安全中面临巨大挑战，主要由于需要从内容无关的流量数据中提取稳健特征。现有方法存在两个主要问题：一是由于依赖封闭世界假设导致的分布漂移限制了对真实世界变化模式的适应性；二是对标注数据的依赖限制了在数据稀缺或不可用情况下的适用性。本文提出了一种新颖的流量表示模型ETooL，结合了大语言模型（LLM）与流量结构知识，通过自监督指令调优范式建立文本信息与流量交互之间的联系。ETooL在监督和零样本流量分类任务中表现出更强的分类性能和优越的泛化能力。

## 🔬 方法详解

**问题定义**：本文旨在解决加密流量分类中的分布漂移和标注数据稀缺问题。现有方法依赖封闭世界假设，导致在真实环境中适应性不足。

**核心思路**：ETooL通过自监督指令调优，将大语言模型与流量结构知识相结合，建立文本与流量交互的联系，从而提升分类性能。

**技术框架**：ETooL的整体架构包括数据预处理、指令生成、模型训练和分类模块。首先对流量数据进行特征提取，然后生成与流量相关的指令，最后利用LLM进行训练和分类。

**关键创新**：ETooL的主要创新在于将自监督学习与大语言模型结合，突破了传统方法在特征提取和适应性方面的限制，显著提高了分类的鲁棒性和泛化能力。

**关键设计**：在模型设计中，采用了特定的损失函数以优化分类性能，并通过动态调整参数来适应不同的流量分布，确保模型在各种条件下的有效性。

## 📊 实验亮点

ETooL在多个数据集上取得了显著的实验结果，APP53（I.I.D.）的F1分数提升至93.19%和92.11%，APP53（O.O.D.）提升至74.88%和72.13%，ISCX-Botnet（O.O.D.）提升至95.03%和81.95%。这些结果表明ETooL在流量分类任务中的有效性和优越性。

## 🎯 应用场景

ETooL模型在网络安全领域具有广泛的应用潜力，特别是在加密流量监测和异常检测中。其自适应能力使其能够在动态变化的网络环境中保持高效的分类性能，未来可为网络流量分析和安全防护提供更为可靠的技术支持。

## 📄 摘要（原文）

> Encrypted traffic classification is highly challenging in network security due to the need for extracting robust features from content-agnostic traffic data. Existing approaches face critical issues: (i) Distribution drift, caused by reliance on the closedworld assumption, limits adaptability to realworld, shifting patterns; (ii) Dependence on labeled data restricts applicability where such data is scarce or unavailable. Large language models (LLMs) have demonstrated remarkable potential in offering generalizable solutions across a wide range of tasks, achieving notable success in various specialized fields. However, their effectiveness in traffic analysis remains constrained by challenges in adapting to the unique requirements of the traffic domain. In this paper, we introduce a novel traffic representation model named Encrypted Traffic Out-of-Distribution Instruction Tuning with LLM (ETooL), which integrates LLMs with knowledge of traffic structures through a self-supervised instruction tuning paradigm. This framework establishes connections between textual information and traffic interactions. ETooL demonstrates more robust classification performance and superior generalization in both supervised and zero-shot traffic classification tasks. Notably, it achieves significant improvements in F1 scores: APP53 (I.I.D.) to 93.19%(6.62%) and 92.11%(4.19%), APP53 (O.O.D.) to 74.88%(18.17%) and 72.13%(15.15%), and ISCX-Botnet (O.O.D.) to 95.03%(9.16%) and 81.95%(12.08%). Additionally, we construct NETD, a traffic dataset designed to support dynamic distributional shifts, and use it to validate ETooL's effectiveness under varying distributional conditions. Furthermore, we evaluate the efficiency gains achieved through ETooL's instruction tuning approach.

