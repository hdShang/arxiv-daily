---
layout: default
title: Multimodal Reasoning Agent for Zero-Shot Composed Image Retrieval
---

# Multimodal Reasoning Agent for Zero-Shot Composed Image Retrieval

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.19952" class="toolbar-btn" target="_blank">📄 arXiv: 2505.19952v1</a>
  <a href="https://arxiv.org/pdf/2505.19952.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.19952v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.19952v1', 'Multimodal Reasoning Agent for Zero-Shot Composed Image Retrieval')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Rong-Cheng Tu, Wenhao Sun, Hanzhe You, Yingjie Wang, Jiaxing Huang, Li Shen, Dacheng Tao

**分类**: cs.CV, cs.IR

**发布日期**: 2025-05-26

---

## 💡 一句话要点

**提出多模态推理代理以解决零样本组合图像检索问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `零样本检索` `多模态推理` `图像检索` `对比学习` `无监督学习`

## 📋 核心要点

1. 现有方法依赖中介文本进行组合查询与目标图像的对齐，导致错误传播和性能下降。
2. 本文提出的多模态推理代理（MRA）直接构建图像与文本的三元组，消除了对文本中介的依赖。
3. 在FashionIQ、CIRR和CIRCO数据集上，本文方法在多个指标上均显著优于现有基线，提升幅度可达9.6%。

## 📝 摘要（中文）

零样本组合图像检索（ZS-CIR）旨在根据组合查询（包含参考图像和修改文本）检索目标图像，而无需依赖标注训练数据。现有方法通常使用大型语言模型生成合成目标文本，作为组合查询与目标图像之间的中介锚点。然而，这种对中介文本的依赖引入了错误传播，导致检索性能下降。为了解决这些问题，本文提出了一种新颖的框架，采用多模态推理代理（MRA）直接构建三元组<参考图像、修改文本、目标图像>，仅使用未标记的图像数据进行训练。通过在这些合成三元组上训练，模型能够直接捕捉组合查询与候选图像之间的关系。大量实验表明，该方法在多个标准CIR基准上显著提升了检索性能。

## 🔬 方法详解

**问题定义**：本文解决零样本组合图像检索（ZS-CIR）问题，现有方法依赖生成的中介文本，导致错误传播和检索性能下降。

**核心思路**：提出多模态推理代理（MRA），通过直接构建<参考图像、修改文本、目标图像>三元组，消除对中介文本的依赖，从而提高检索精度。

**技术框架**：整体架构包括数据准备、三元组构建和模型训练三个主要阶段。首先，从未标记的图像数据中生成合成三元组，然后利用这些三元组进行模型训练。

**关键创新**：MRA的最大创新在于直接利用图像数据构建三元组，避免了中介文本的引入，从根本上减少了错误传播的风险。

**关键设计**：模型采用对比学习的损失函数，通过优化组合查询与目标图像之间的相似性，关键参数设置包括学习率和批量大小等，确保模型在训练过程中的稳定性和收敛性。

## 📊 实验亮点

在FashionIQ数据集上，本文方法的平均R@10提升至少7.5%；在CIRR数据集上，R@1提升9.6%；在CIRCO数据集上，mAP@5提升9.5%。这些结果表明，本文方法在多个标准基准上均显著优于现有基线。

## 🎯 应用场景

该研究的潜在应用领域包括电子商务、社交媒体和内容检索等场景，能够帮助用户更高效地找到符合特定需求的图像。未来，该方法可能推动无监督学习和多模态检索技术的发展，提升图像检索的智能化水平。

## 📄 摘要（原文）

> Zero-Shot Composed Image Retrieval (ZS-CIR) aims to retrieve target images given a compositional query, consisting of a reference image and a modifying text-without relying on annotated training data. Existing approaches often generate a synthetic target text using large language models (LLMs) to serve as an intermediate anchor between the compositional query and the target image. Models are then trained to align the compositional query with the generated text, and separately align images with their corresponding texts using contrastive learning. However, this reliance on intermediate text introduces error propagation, as inaccuracies in query-to-text and text-to-image mappings accumulate, ultimately degrading retrieval performance. To address these problems, we propose a novel framework by employing a Multimodal Reasoning Agent (MRA) for ZS-CIR. MRA eliminates the dependence on textual intermediaries by directly constructing triplets, <reference image, modification text, target image>, using only unlabeled image data. By training on these synthetic triplets, our model learns to capture the relationships between compositional queries and candidate images directly. Extensive experiments on three standard CIR benchmarks demonstrate the effectiveness of our approach. On the FashionIQ dataset, our method improves Average R@10 by at least 7.5\% over existing baselines; on CIRR, it boosts R@1 by 9.6\%; and on CIRCO, it increases mAP@5 by 9.5\%.

