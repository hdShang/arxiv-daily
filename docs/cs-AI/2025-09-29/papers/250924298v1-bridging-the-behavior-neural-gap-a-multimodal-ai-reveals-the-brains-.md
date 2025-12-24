---
layout: default
title: "Bridging the behavior-neural gap: A multimodal AI reveals the brain's geometry of emotion more accurately than human self-reports"
---

# Bridging the behavior-neural gap: A multimodal AI reveals the brain's geometry of emotion more accurately than human self-reports

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.24298" class="toolbar-btn" target="_blank">📄 arXiv: 2509.24298v1</a>
  <a href="https://arxiv.org/pdf/2509.24298.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.24298v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.24298v1', 'Bridging the behavior-neural gap: A multimodal AI reveals the brain\'s geometry of emotion more accurately than human self-reports')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Changde Du, Yizhuo Lu, Zhongyu Huang, Yi Sun, Zisen Zhou, Shaozheng Qin, Huiguang He

**分类**: cs.HC, cs.AI, cs.CL, cs.CY, cs.MM

**发布日期**: 2025-09-29

**🔗 代码/项目**: [PROJECT_PAGE](https://reedonepeck.github.io/ai-emotion.github.io/)

---

## 💡 一句话要点

**多模态AI超越人类自报告，更准确揭示大脑情感几何**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `情感表征` `多模态学习` `大语言模型` `神经活动预测` `行为-神经差距` `情感计算` `认知代理`

## 📋 核心要点

1. 现有情感研究依赖人类自报告，但其预测大脑活动的能力有限，存在“行为-神经差距”。
2. 利用多模态大语言模型（MLLM）和纯语言模型（LLM）进行大规模相似性判断，构建情感表征。
3. MLLM的情感表征能更准确地预测人类情感处理网络中的神经活动，优于LLM和人类自报告。

## 📝 摘要（中文）

情感表征在人类认知和社会互动中至关重要，但情感空间的高维几何结构及其神经基础仍存在争议。一个关键挑战是“行为-神经差距”，即人类自报告预测大脑活动的能力有限。本文验证了这一差距源于传统评级量表的约束，而大规模相似性判断能更真实地捕捉大脑的情感几何。研究使用AI模型作为“认知代理”，从多模态大型语言模型(MLLM)和纯语言模型(LLM)收集了数百万个三元组奇偶判断，以响应2180个情感视频。结果表明，这些模型产生的30维嵌入具有高度可解释性，并主要沿类别线组织情感，同时以融合的方式结合了维度属性。最重要的是，MLLM的表征以最高的准确度预测了人类情感处理网络中的神经活动，不仅优于LLM，而且出乎意料地优于直接从人类行为评级中获得的表征。该结果支持了主要假设，并表明感官基础——从丰富的视觉数据中学习——对于开发真正神经对齐的情感概念框架至关重要。研究结果提供了令人信服的证据，表明MLLM可以自主开发丰富的、神经对齐的情感表征，为弥合主观体验与其神经基质之间的差距提供了一个强大的范例。

## 🔬 方法详解

**问题定义**：现有情感研究主要依赖人类的自我报告，例如使用评级量表。然而，这种方法存在局限性，无法准确反映大脑中情感的真实表征，导致“行为-神经差距”。因此，需要一种新的方法来更有效地捕捉大脑的情感几何结构，并弥合主观体验和神经活动之间的差距。

**核心思路**：论文的核心思路是利用AI模型（特别是多模态大型语言模型MLLM）作为“认知代理”，通过大规模的三元组奇偶判断任务来学习情感表征。这种方法避免了传统评级量表的限制，能够更全面地捕捉情感的复杂性和细微差别。通过比较MLLM和LLM的表现，以及它们与人类神经活动的相关性，来验证感官基础对于构建神经对齐的情感表征的重要性。

**技术框架**：整体框架包括以下几个主要阶段：1) 收集情感视频数据集；2) 使用MLLM和LLM对视频进行三元组奇偶判断，生成情感相似性数据；3) 利用这些数据训练情感表征模型，得到情感嵌入；4) 将模型生成的情感表征与人类大脑的神经活动数据进行比较，评估其预测神经活动的能力。

**关键创新**：最重要的技术创新点在于使用多模态大型语言模型（MLLM）来学习情感表征，并证明其能够超越人类自报告，更准确地预测大脑的神经活动。这种方法突破了传统情感研究的局限性，为理解情感的神经基础提供了一种新的视角。

**关键设计**：论文使用了2180个情感视频作为输入，并设计了三元组奇偶判断任务，要求模型判断哪个视频与其他两个视频的情感差异最大。通过收集数百万个这样的判断，构建了大规模的情感相似性数据集。模型最终生成30维的情感嵌入，用于与人类大脑的神经活动数据进行比较。损失函数和网络结构等具体技术细节在论文中可能未详细描述，属于未知信息。

## 📊 实验亮点

实验结果表明，MLLM生成的情感表征能够以最高的准确度预测人类情感处理网络中的神经活动，优于纯语言模型（LLM）和人类自报告。这表明多模态信息对于构建神经对齐的情感表征至关重要，并验证了论文的主要假设。

## 🎯 应用场景

该研究成果可应用于情感计算、人机交互、心理健康评估等领域。通过更准确地理解和预测人类情感，可以开发更智能、更人性化的AI系统，例如情感识别助手、个性化推荐系统和心理健康干预工具。未来，该研究有望促进对情感障碍的诊断和治疗，并提升人与机器之间的情感交流。

## 📄 摘要（原文）

> The ability to represent emotion plays a significant role in human cognition and social interaction, yet the high-dimensional geometry of this affective space and its neural underpinnings remain debated. A key challenge, the `behavior-neural gap,' is the limited ability of human self-reports to predict brain activity. Here we test the hypothesis that this gap arises from the constraints of traditional rating scales and that large-scale similarity judgments can more faithfully capture the brain's affective geometry. Using AI models as `cognitive agents,' we collected millions of triplet odd-one-out judgments from a multimodal large language model (MLLM) and a language-only model (LLM) in response to 2,180 emotionally evocative videos. We found that the emergent 30-dimensional embeddings from these models are highly interpretable and organize emotion primarily along categorical lines, yet in a blended fashion that incorporates dimensional properties. Most remarkably, the MLLM's representation predicted neural activity in human emotion-processing networks with the highest accuracy, outperforming not only the LLM but also, counterintuitively, representations derived directly from human behavioral ratings. This result supports our primary hypothesis and suggests that sensory grounding--learning from rich visual data--is critical for developing a truly neurally-aligned conceptual framework for emotion. Our findings provide compelling evidence that MLLMs can autonomously develop rich, neurally-aligned affective representations, offering a powerful paradigm to bridge the gap between subjective experience and its neural substrates. Project page: https://reedonepeck.github.io/ai-emotion.github.io/.

