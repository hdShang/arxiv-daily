---
layout: default
title: "SETR: A Two-Stage Semantic-Enhanced Framework for Zero-Shot Composed Image Retrieval"
---

# SETR: A Two-Stage Semantic-Enhanced Framework for Zero-Shot Composed Image Retrieval

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.26012" class="toolbar-btn" target="_blank">📄 arXiv: 2509.26012v1</a>
  <a href="https://arxiv.org/pdf/2509.26012.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.26012v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.26012v1', 'SETR: A Two-Stage Semantic-Enhanced Framework for Zero-Shot Composed Image Retrieval')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuqi Xiao, Yingying Zhu

**分类**: cs.CV

**发布日期**: 2025-09-30

---

## 💡 一句话要点

**提出SETR：一种语义增强的两阶段框架，用于零样本组合图像检索**

🎯 **匹配领域**: **支柱六：视频提取与匹配 (Video Extraction)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `零样本学习` `组合图像检索` `多模态学习` `语义理解` `两阶段检索`

## 📋 核心要点

1. 现有零样本组合图像检索方法依赖联合特征融合，易受无关背景干扰，且缺乏细粒度语义关系建模能力。
2. SETR采用两阶段检索策略，首先通过交集驱动的粗检索过滤干扰，再利用多模态LLM进行细粒度重排序。
3. 实验表明，SETR在CIRR等数据集上取得了SOTA性能，Recall@1提升高达15.15个百分点，验证了两阶段推理的有效性。

## 📝 摘要（中文）

零样本组合图像检索(ZS-CIR)旨在给定参考图像和相关文本的情况下检索目标图像，而无需昂贵的三元组标注。现有的基于CLIP的方法面临两个核心挑战：(1)基于联合的特征融合无差别地聚合所有视觉线索，携带了不相关的背景细节，稀释了预期的修改；(2)来自CLIP嵌入的全局余弦相似性缺乏解决细粒度语义关系的能力。为了解决这些问题，我们提出了SETR(语义增强的两阶段检索)。在粗检索阶段，SETR引入了一种交集驱动的策略，仅保留参考图像和相关文本之间的重叠语义，从而过滤掉联合融合固有的干扰因素，并产生更干净、高精度的候选集。在细粒度重排序阶段，我们采用具有低秩适应的预训练多模态LLM来进行二元语义相关性判断(“是/否”)，通过显式验证关系和属性级别的连贯性，超越了CLIP的全局特征匹配。这两个阶段共同构成了一个互补的流程：粗检索以高召回率缩小候选池，而重排序确保与细微的文本修改精确对齐。在CIRR、Fashion-IQ和CIRCO上的实验表明，SETR实现了新的最先进性能，在CIRR上将Recall@1提高了高达15.15个百分点。我们的结果确立了两阶段推理作为鲁棒且可移植的ZS-CIR的通用范例。

## 🔬 方法详解

**问题定义**：零样本组合图像检索(ZS-CIR)旨在根据给定的参考图像和描述性文本，检索经过文本描述修改后的目标图像。现有方法，特别是基于CLIP的方法，主要依赖于将参考图像和文本描述进行简单的联合特征融合，这导致两个主要问题：一是融合过程中会引入不相关的背景信息，干扰检索；二是全局余弦相似度匹配难以捕捉细粒度的语义关系，例如属性级别的修改。

**核心思路**：SETR的核心思路是将检索过程分解为两个阶段：粗检索和细粒度重排序。粗检索阶段旨在快速缩小搜索范围，保留高召回率；细粒度重排序阶段则专注于精确匹配，利用更强大的语义理解能力来提升检索精度。这种两阶段的设计旨在克服现有方法在特征融合和语义理解方面的局限性。

**技术框架**：SETR框架包含两个主要阶段：
1. **粗检索阶段**：使用交集驱动的策略，提取参考图像和文本描述之间的共享语义信息，过滤掉不相关的背景细节，生成候选集。
2. **细粒度重排序阶段**：利用预训练的多模态LLM，对候选集中的图像进行二元语义相关性判断（“是/否”），判断图像是否符合文本描述的修改。

**关键创新**：SETR的关键创新在于：
1. **交集驱动的特征提取**：不同于传统的联合特征融合，SETR只保留参考图像和文本描述之间的重叠语义，减少了背景噪声的干扰。
2. **多模态LLM的二元语义判断**：利用LLM强大的语义理解能力，显式地验证图像和文本描述之间的关系和属性一致性，超越了简单的全局特征匹配。

**关键设计**：
1. **交集驱动策略**：具体实现细节未知，但核心思想是设计一种机制，能够有效提取参考图像和文本描述的共享语义信息。
2. **低秩适应(LoRA)**：在细粒度重排序阶段，使用LoRA对预训练的多模态LLM进行微调，使其适应ZS-CIR任务。LoRA通过引入少量可训练参数，降低了微调的计算成本。
3. **二元语义相关性判断**：将重排序问题转化为二元分类问题，使用LLM判断候选图像是否与文本描述相关，从而实现更精确的语义匹配。

## 📊 实验亮点

SETR在CIRR、Fashion-IQ和CIRCO三个数据集上均取得了显著的性能提升。在最具挑战性的CIRR数据集上，SETR的Recall@1指标提升了高达15.15个百分点，超越了现有的SOTA方法，证明了其在零样本组合图像检索任务中的有效性。

## 🎯 应用场景

SETR在电商、时尚、室内设计等领域具有广泛的应用前景。例如，用户可以通过上传一张沙发图片并描述“换成蓝色”，快速检索到符合要求的蓝色沙发。该研究有助于提升图像检索的准确性和用户体验，并为更智能的图像搜索和编辑工具奠定基础。

## 📄 摘要（原文）

> Zero-shot Composed Image Retrieval (ZS-CIR) aims to retrieve a target image given a reference image and a relative text, without relying on costly triplet annotations. Existing CLIP-based methods face two core challenges: (1) union-based feature fusion indiscriminately aggregates all visual cues, carrying over irrelevant background details that dilute the intended modification, and (2) global cosine similarity from CLIP embeddings lacks the ability to resolve fine-grained semantic relations. To address these issues, we propose SETR (Semantic-enhanced Two-Stage Retrieval). In the coarse retrieval stage, SETR introduces an intersection-driven strategy that retains only the overlapping semantics between the reference image and relative text, thereby filtering out distractors inherent to union-based fusion and producing a cleaner, high-precision candidate set. In the fine-grained re-ranking stage, we adapt a pretrained multimodal LLM with Low-Rank Adaptation to conduct binary semantic relevance judgments ("Yes/No"), which goes beyond CLIP's global feature matching by explicitly verifying relational and attribute-level consistency. Together, these two stages form a complementary pipeline: coarse retrieval narrows the candidate pool with high recall, while re-ranking ensures precise alignment with nuanced textual modifications. Experiments on CIRR, Fashion-IQ, and CIRCO show that SETR achieves new state-of-the-art performance, improving Recall@1 on CIRR by up to 15.15 points. Our results establish two-stage reasoning as a general paradigm for robust and portable ZS-CIR.

