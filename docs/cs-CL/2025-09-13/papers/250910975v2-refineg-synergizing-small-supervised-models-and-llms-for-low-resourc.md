---
layout: default
title: "ReFineG: Synergizing Small Supervised Models and LLMs for Low-Resource Grounded Multimodal NER"
---

# ReFineG: Synergizing Small Supervised Models and LLMs for Low-Resource Grounded Multimodal NER

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.10975" class="toolbar-btn" target="_blank">📄 arXiv: 2509.10975v2</a>
  <a href="https://arxiv.org/pdf/2509.10975.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.10975v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.10975v2', 'ReFineG: Synergizing Small Supervised Models and LLMs for Low-Resource Grounded Multimodal NER')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jielong Tang, Shuang Wang, Zhenxing Wang, Jianxing Yu, Jian Yin

**分类**: cs.IR, cs.CL

**发布日期**: 2025-09-13 (更新: 2025-11-12)

**备注**: CCKS 2025 Shared Task Paper

---

## 💡 一句话要点

**ReFineG：结合小监督模型与LLM，解决低资源GMNER问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `GMNER` `多模态命名实体识别` `低资源学习` `大语言模型` `知识迁移`

## 📋 核心要点

1. 现有GMNER方法依赖大量标注数据，在低资源场景下性能受限，MLLM虽有泛化能力，但存在领域知识冲突。
2. ReFineG通过三阶段框架，结合小监督模型和冻结的MLLM，利用数据合成、不确定性选择和上下文选择提升性能。
3. 在CCKS2025 GMNER共享任务中，ReFineG取得了第二名的成绩，验证了其在低资源场景下的有效性。

## 📝 摘要（中文）

Grounded Multimodal Named Entity Recognition (GMNER) 通过联合检测文本提及并在视觉区域中进行定位，扩展了传统的 NER。现有的监督方法虽然性能强大，但依赖于昂贵的多模态标注，并且在低资源领域表现不佳。多模态大型语言模型 (MLLM) 显示出强大的泛化能力，但存在领域知识冲突，会为特定领域的实体生成冗余或不正确的提及。为了解决这些挑战，我们提出了 ReFineG，这是一个三阶段的协作框架，它集成了小型监督模型和冻结的 MLLM，用于低资源 GMNER。在训练阶段，一种领域感知的 NER 数据合成策略将 LLM 知识转移到具有监督训练的小型模型，同时避免领域知识冲突。在细化阶段，一种基于不确定性的机制保留来自监督模型的置信预测，并将不确定的预测委托给 MLLM。在定位阶段，一种多模态上下文选择算法通过类比推理增强视觉定位。在 CCKS2025 GMNER 共享任务中，ReFineG 在在线排行榜上排名第二，F1 得分为 0.6461，证明了其在有限标注下的有效性。

## 🔬 方法详解

**问题定义**：论文旨在解决低资源场景下的Grounded Multimodal Named Entity Recognition (GMNER)问题。现有方法主要依赖大规模标注数据进行监督学习，但在标注数据稀缺的情况下，模型性能显著下降。同时，直接使用多模态大语言模型(MLLM)进行GMNER任务，容易受到领域知识冲突的影响，产生不准确或冗余的实体提及。

**核心思路**：论文的核心思路是结合小规模监督模型和冻结的MLLM的优势，利用小规模监督模型学习领域特定知识，并利用MLLM的泛化能力。通过一个三阶段的框架，实现知识的有效迁移和融合，从而在低资源场景下提升GMNER的性能。该方法旨在避免直接微调MLLM带来的高成本和潜在的灾难性遗忘问题。

**技术框架**：ReFineG框架包含三个阶段：训练阶段、细化阶段和定位阶段。在训练阶段，利用领域感知的NER数据合成策略，将LLM的知识迁移到小规模监督模型中。在细化阶段，基于不确定性的机制，选择性地使用监督模型和MLLM的预测结果。监督模型置信度高的预测被保留，而置信度低的预测则委托给MLLM。在定位阶段，使用多模态上下文选择算法，通过类比推理增强视觉定位的准确性。

**关键创新**：该论文的关键创新在于提出了一种协同利用小规模监督模型和冻结MLLM的框架，有效解决了低资源GMNER问题。与直接微调MLLM或完全依赖监督模型的方法相比，ReFineG能够更好地平衡领域知识和泛化能力。此外，基于不确定性的选择机制和多模态上下文选择算法也是重要的创新点，能够进一步提升模型的性能。

**关键设计**：在训练阶段，领域感知的NER数据合成策略是关键。具体实现细节未知，但推测可能涉及使用LLM生成与目标领域相关的NER数据，并对生成的数据进行过滤和筛选，以避免引入噪声。在细化阶段，不确定性的度量方式以及阈值的选择是关键。在定位阶段，多模态上下文选择算法的具体实现细节未知，但推测可能涉及使用注意力机制或图神经网络来建模文本和图像之间的关系。

## 📊 实验亮点

ReFineG在CCKS2025 GMNER共享任务中取得了第二名的成绩，F1值为0.6461。该结果表明，在有限标注数据的情况下，ReFineG能够有效提升GMNER的性能。虽然论文中没有提供与具体基线的详细对比数据，但排名第二的结果足以证明该方法的有效性。

## 🎯 应用场景

ReFineG框架可应用于多种低资源场景下的多模态命名实体识别任务，例如特定领域的文档理解、医学影像报告分析、以及机器人视觉等。该方法能够有效降低对大规模标注数据的依赖，提高模型在实际应用中的可用性和泛化能力，具有重要的实际应用价值和潜力。

## 📄 摘要（原文）

> Grounded Multimodal Named Entity Recognition (GMNER) extends traditional NER by jointly detecting textual mentions and grounding them to visual regions. While existing supervised methods achieve strong performance, they rely on costly multimodal annotations and often underperform in low-resource domains. Multimodal Large Language Models (MLLMs) show strong generalization but suffer from Domain Knowledge Conflict, producing redundant or incorrect mentions for domain-specific entities. To address these challenges, we propose ReFineG, a three-stage collaborative framework that integrates small supervised models with frozen MLLMs for low-resource GMNER. In the Training Stage, a domain-aware NER data synthesis strategy transfers LLM knowledge to small models with supervised training while avoiding domain knowledge conflicts. In the Refinement Stage, an uncertainty-based mechanism retains confident predictions from supervised models and delegates uncertain ones to the MLLM. In the Grounding Stage, a multimodal context selection algorithm enhances visual grounding through analogical reasoning. In the CCKS2025 GMNER Shared Task, ReFineG ranked second with an F1 score of 0.6461 on the online leaderboard, demonstrating its effectiveness with limited annotations.

