---
layout: default
title: UniME-V2: MLLM-as-a-Judge for Universal Multimodal Embedding Learning
---

# UniME-V2: MLLM-as-a-Judge for Universal Multimodal Embedding Learning

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.13515" target="_blank" class="toolbar-btn">arXiv: 2510.13515v3</a>
    <a href="https://arxiv.org/pdf/2510.13515.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.13515v3" 
            onclick="toggleFavorite(this, '2510.13515v3', 'UniME-V2: MLLM-as-a-Judge for Universal Multimodal Embedding Learning')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Tiancheng Gu, Kaicheng Yang, Kaichen Zhang, Xiang An, Ziyong Feng, Yueyi Zhang, Weidong Cai, Jiankang Deng, Lidong Bing

**分类**: cs.CV, cs.AI

**发布日期**: 2025-10-15 (更新: 2025-12-08)

**备注**: AAAI2026 Oral, Webpage:https://garygutc.github.io/UniME-v2/

---

## 💡 一句话要点

**UniME-V2：利用MLLM作为判别器进行通用多模态嵌入学习**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态嵌入学习` `多模态大语言模型` `难负样本挖掘` `语义匹配` `信息检索`

## 📋 核心要点

1. 现有通用多模态嵌入模型难以捕捉细微语义差异，负样本多样性不足，区分假负样本能力有限。
2. 提出UniME-V2，利用MLLM作为判别器，生成软语义匹配分数，指导难负样本挖掘和嵌入学习。
3. 实验表明，UniME-V2在MMEB基准和多个检索任务上取得了最先进的性能。

## 📝 摘要（中文）

通用多模态嵌入模型是各种任务的基础。现有方法通常采用批内负样本挖掘，通过测量查询-候选对的相似度。然而，这些方法难以捕捉候选者之间细微的语义差异，并且缺乏负样本的多样性。此外，嵌入在区分假负样本和难负样本方面的判别能力有限。本文利用MLLM先进的理解能力来增强表征学习，并提出了一种新的通用多模态嵌入（UniME-V2）模型。我们的方法首先通过全局检索构建潜在的难负样本集。然后，我们引入MLLM-as-a-Judge机制，该机制利用MLLM评估查询-候选对的语义对齐并生成软语义匹配分数。这些分数作为难负样本挖掘的基础，减轻了假负样本的影响，并能够识别多样化、高质量的难负样本。此外，语义匹配分数被用作软标签，以减轻刚性的一对一映射约束。通过将相似度矩阵与软语义匹配分数矩阵对齐，该模型学习候选者之间的语义区别，从而显著提高其判别能力。为了进一步提高性能，我们提出了UniME-V2-Reranker，这是一个在通过联合成对和列表式优化方法挖掘的难负样本上训练的重排序模型。我们在MMEB基准和多个检索任务上进行了全面的实验，表明我们的方法在所有任务上的平均性能都达到了最先进水平。

## 🔬 方法详解

**问题定义**：现有通用多模态嵌入模型在负样本挖掘方面存在局限性，难以区分假负样本和难负样本，导致模型判别能力不足。批内负样本挖掘方法无法捕捉细微的语义差异，且负样本缺乏多样性。

**核心思路**：利用多模态大语言模型（MLLM）强大的语义理解能力，将其作为“判别器”，评估查询-候选对的语义对齐程度，生成软语义匹配分数。这些分数用于指导难负样本挖掘，并作为软标签优化嵌入学习过程。

**技术框架**：UniME-V2模型包含以下主要阶段：1) 全局检索：构建潜在的难负样本集。2) MLLM-as-a-Judge：利用MLLM评估查询-候选对的语义对齐，生成软语义匹配分数。3) 难负样本挖掘：基于MLLM的语义匹配分数，挖掘高质量的难负样本。4) 嵌入学习：将语义匹配分数作为软标签，优化嵌入空间，增强模型的判别能力。5) UniME-V2-Reranker：使用挖掘的难负样本训练重排序模型，进一步提升检索性能。

**关键创新**：核心创新在于引入了MLLM-as-a-Judge机制，利用MLLM的语义理解能力来指导难负样本挖掘和嵌入学习。与传统的基于相似度度量的负样本挖掘方法相比，MLLM能够更准确地评估语义对齐程度，从而挖掘更高质量的难负样本，并减轻假负样本的影响。

**关键设计**：1) 软语义匹配分数：MLLM输出的语义匹配分数被用作软标签，替代了传统的硬标签，缓解了刚性的一对一映射约束。2) 损失函数：通过对齐相似度矩阵和软语义匹配分数矩阵，模型能够学习候选者之间的语义区别。3) UniME-V2-Reranker：采用联合成对和列表式优化方法，进一步提升检索性能。具体参数设置和网络结构细节在论文中有详细描述（未知）。

## 📊 实验亮点

UniME-V2在MMEB基准测试和多个检索任务上取得了最先进的性能。具体性能数据和提升幅度在论文中有详细展示（未知）。通过引入MLLM-as-a-Judge机制，模型能够更有效地挖掘难负样本，并学习更具判别性的多模态嵌入表示，从而显著提升检索精度。

## 🎯 应用场景

该研究成果可广泛应用于多模态信息检索、跨模态理解、视觉问答、图像描述生成等领域。通过提升多模态嵌入模型的判别能力，可以提高检索精度和用户体验，在电商、搜索引擎、智能助手等场景具有重要的实际应用价值和商业潜力。未来，该方法可以进一步扩展到更多模态和更复杂的任务中。

## 📄 摘要（原文）

> Universal multimodal embedding models are foundational to various tasks. Existing approaches typically employ in-batch negative mining by measuring the similarity of query-candidate pairs. However, these methods often struggle to capture subtle semantic differences among candidates and lack diversity in negative samples. Moreover, the embeddings exhibit limited discriminative ability in distinguishing false and hard negatives. In this paper, we leverage the advanced understanding capabilities of MLLMs to enhance representation learning and present a novel Universal Multimodal Embedding (UniME-V2) model. Our approach first constructs a potential hard negative set through global retrieval. We then introduce the MLLM-as-a-Judge mechanism, which utilizes MLLMs to assess the semantic alignment of query-candidate pairs and generate soft semantic matching scores. These scores serve as a foundation for hard negative mining, mitigating the impact of false negatives and enabling the identification of diverse, high-quality hard negatives. Furthermore, the semantic matching scores are used as soft labels to mitigate the rigid one-to-one mapping constraint. By aligning the similarity matrix with the soft semantic matching score matrix, the model learns semantic distinctions among candidates, significantly enhancing its discriminative capacity. To further improve performance, we propose UniME-V2-Reranker, a reranking model trained on our mined hard negatives through a joint pairwise and listwise optimization approach. We conduct comprehensive experiments on the MMEB benchmark and multiple retrieval tasks, demonstrating that our method achieves state-of-the-art performance on average across all tasks.

